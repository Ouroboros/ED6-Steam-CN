import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3410_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3410   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '迪鲁队长'),
    TXT(0x02, '士兵维恩'),
    TXT(0x03, '多杰'),
    TXT(0x04, '拉德米拉'),
    TXT(0x05, '卡雷尔'),
    TXT(0x06, '士兵儒勒'),
    TXT(0x07, '士兵埃克托尔'),
    TXT(0x08, '士兵切斯利'),
    TXT(0x09, '阿鲁姆'),
    TXT(0x0A, '艾娅莉'),
    TXT(0x0B, '塔尔瓦托副长'),
    TXT(0x0C, '桑吉特'),
    TXT(0x0D, '黛米'),
    TXT(0x0E, '玛丽安'),
    TXT(0x0F, '诺琪'),
    TXT(0x10, '塔丽娅'),
    TXT(0x11, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3410.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x829B
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01520._CH', 'ED6_DT07/CH01520P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01233._CH', 'ED6_DT07/CH01233P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH02053._CH', 'ED6_DT07/CH02053P._CP'),
    ]

# id: 0x10002 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 6790,
            z                   = 0,
            y                   = 2810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
    )

# id: 0x10003 offset: 0x342
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x342
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x342
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 58180,
            triggerZ            = 5000,
            triggerY            = 51630,
            triggerRange        = 1000,
            actorX              = 58180,
            actorZ              = 6500,
            actorY              = 51630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 6760,
            triggerZ            = 0,
            triggerY            = 900,
            triggerRange        = 1000,
            actorX              = 6790,
            actorZ              = 1500,
            actorY              = 2810,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 109850,
            triggerZ            = 0,
            triggerY            = 21800,
            triggerRange        = 1000,
            actorX              = 111940,
            actorZ              = 1500,
            actorY              = 22150,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 91680,
            triggerZ            = 0,
            triggerY            = -22240,
            triggerRange        = 1000,
            actorX              = 89560,
            actorZ              = 1500,
            actorY              = -22370,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3D2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3DC',
    )

    Jump('loc_475')

    def _loc_3DC(): pass

    label('loc_3DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3FC',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 2760, 0, 2290, 87)

    Jump('loc_475')

    def _loc_3FC(): pass

    label('loc_3FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_406',
    )

    Jump('loc_475')

    def _loc_406(): pass

    label('loc_406')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_410',
    )

    Jump('loc_475')

    def _loc_410(): pass

    label('loc_410')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_41A',
    )

    Jump('loc_475')

    def _loc_41A(): pass

    label('loc_41A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_424',
    )

    Jump('loc_475')

    def _loc_424(): pass

    label('loc_424')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_42E',
    )

    Jump('loc_475')

    def _loc_42E(): pass

    label('loc_42E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_438',
    )

    Jump('loc_475')

    def _loc_438(): pass

    label('loc_438')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_442',
    )

    Jump('loc_475')

    def _loc_442(): pass

    label('loc_442')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_475',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 18880, 0, 2680, 270)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 17270, 0, 2680, 90)

    def _loc_475(): pass

    label('loc_475')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4FB',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 111940, 0, 22150, 283)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 11620, 0, -1350, 259)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 61040, 0, -24890, 265)
    CreateThread(0x0014, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)

    Jump('loc_BD5')

    def _loc_4FB(): pass

    label('loc_4FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_586',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 111940, 0, 22150, 283)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 11620, 0, -1350, 259)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 89690, 0, -24010, 0)
    CreateThread(0x0014, 0x00, 0x00, 0x0002)
    SetChrFlags(0x0014, 0x0010)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)

    Jump('loc_BD5')

    def _loc_586(): pass

    label('loc_586')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_611',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 111940, 0, 22150, 283)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 11620, 0, -1350, 259)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 89690, 0, -24010, 0)
    CreateThread(0x0014, 0x00, 0x00, 0x0002)
    SetChrFlags(0x0014, 0x0010)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)

    Jump('loc_BD5')

    def _loc_611(): pass

    label('loc_611')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_697',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 111940, 0, 22150, 283)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 11620, 0, -1350, 259)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 61040, 0, -24890, 265)
    CreateThread(0x0014, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)

    Jump('loc_BD5')

    def _loc_697(): pass

    label('loc_697')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_71D',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 111940, 0, 22150, 283)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 11620, 0, -1350, 259)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 61040, 0, -24890, 265)
    CreateThread(0x0014, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)

    Jump('loc_BD5')

    def _loc_71D(): pass

    label('loc_71D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_7A3',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 111940, 0, 22150, 283)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 11620, 0, -1350, 259)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 61040, 0, -24890, 265)
    CreateThread(0x0014, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)

    Jump('loc_BD5')

    def _loc_7A3(): pass

    label('loc_7A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_82C',
    )

    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 80890, 0, 23550, 110)
    SetChrFlags(0x0012, 0x0010)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 82450, 0, 23660, 271)
    SetChrFlags(0x0008, 0x0010)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 61040, 0, -24890, 265)
    CreateThread(0x0014, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)

    Jump('loc_BD5')

    def _loc_82C(): pass

    label('loc_82C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_8B5',
    )

    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 80890, 0, 23550, 110)
    SetChrFlags(0x0012, 0x0010)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 82450, 0, 23660, 271)
    SetChrFlags(0x0008, 0x0010)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 61040, 0, -24890, 265)
    CreateThread(0x0014, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)

    Jump('loc_BD5')

    def _loc_8B5(): pass

    label('loc_8B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_993',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 111940, 0, 22150, 283)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 11620, 0, -1350, 259)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 61040, 0, -24890, 265)
    CreateThread(0x0014, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, 58600, 150, -27620, 90)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, 60840, 150, -27720, 270)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 17220, 0, 2570, 103)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 18530, 0, 2570, 249)

    Jump('loc_BD5')

    def _loc_993(): pass

    label('loc_993')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_A71',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 111940, 0, 22150, 283)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 11620, 0, -1350, 259)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 61040, 0, -24890, 265)
    CreateThread(0x0014, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, 58600, 150, -27620, 90)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, 60840, 150, -27720, 270)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 22840, 0, -3730, 270)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 21050, 0, -3760, 90)

    Jump('loc_BD5')

    def _loc_A71(): pass

    label('loc_A71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_B26',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 111940, 0, 22150, 283)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 11620, 0, -1350, 259)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 89540, 0, -24220, 0)
    SetChrFlags(0x0014, 0x0010)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, 58600, 150, -27620, 90)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, 60840, 150, -27720, 270)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 180)
    SetChrFlags(0x0017, 0x0010)

    Jump('loc_BD5')

    def _loc_B26(): pass

    label('loc_B26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_BD5',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 111940, 0, 22150, 283)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 11620, 0, -1350, 259)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 54970, 0, -21440, 4)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 61040, 0, -24890, 265)
    CreateThread(0x0014, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, 58600, 150, -27620, 90)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, 60840, 150, -27720, 270)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 89560, 0, -22370, 98)

    def _loc_BD5(): pass

    label('loc_BD5')

    Return()

# id: 0x0001 offset: 0xBD6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_BE5',
    )

    OP_1B(0x00, 0x00, 0x0019)

    Jump('loc_BEA')

    def _loc_BE5(): pass

    label('loc_BE5')

    OP_1B(0x01, 0x00, 0x0018)

    def _loc_BEA(): pass

    label('loc_BEA')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x04)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0030, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C0A',
    )

    OP_65(0x00, 0x0001)

    def _loc_C0A(): pass

    label('loc_C0A')

    OP_65(0x02, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_C18',
    )

    Jump('loc_C8B')

    def _loc_C18(): pass

    label('loc_C18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_C22',
    )

    Jump('loc_C8B')

    def _loc_C22(): pass

    label('loc_C22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_C2C',
    )

    Jump('loc_C8B')

    def _loc_C2C(): pass

    label('loc_C2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_C36',
    )

    Jump('loc_C8B')

    def _loc_C36(): pass

    label('loc_C36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_C40',
    )

    Jump('loc_C8B')

    def _loc_C40(): pass

    label('loc_C40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_C4A',
    )

    Jump('loc_C8B')

    def _loc_C4A(): pass

    label('loc_C4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_C58',
    )

    OP_64(0x02, 0x0001)

    Jump('loc_C8B')

    def _loc_C58(): pass

    label('loc_C58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_C66',
    )

    OP_64(0x02, 0x0001)

    Jump('loc_C8B')

    def _loc_C66(): pass

    label('loc_C66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_C70',
    )

    Jump('loc_C8B')

    def _loc_C70(): pass

    label('loc_C70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_C7A',
    )

    Jump('loc_C8B')

    def _loc_C7A(): pass

    label('loc_C7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_C84',
    )

    Jump('loc_C8B')

    def _loc_C84(): pass

    label('loc_C84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_C8B',
    )

    def _loc_C8B(): pass

    label('loc_C8B')

    OP_1C(0x05, 0x00, 0x001B)

    Return()

# id: 0x0002 offset: 0xC91
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CA6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_CA6(): pass

    label('loc_CA6')

    Return()

# id: 0x0003 offset: 0xCA7
@scena.Code('func_03_CA7')
def func_03_CA7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CCA',
    )

    OP_8D(0x00FE, 5070, 820, 17900, -3880, 2000)

    Jump('func_03_CA7')

    def _loc_CCA(): pass

    label('loc_CCA')

    Return()

# id: 0x0004 offset: 0xCCB
@scena.Code('func_04_CCB')
def func_04_CCB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CEE',
    )

    OP_8D(0x00FE, 56600, -23980, 64040, -26210, 2000)

    Jump('func_04_CCB')

    def _loc_CEE(): pass

    label('loc_CEE')

    Return()

# id: 0x0005 offset: 0xCEF
@scena.Code('func_05_CEF')
def func_05_CEF():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0xCF4
@scena.Code('func_06_CF4')
def func_06_CF4():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_D74',
    )

    ChrTalk(
        0x0008,
        (
            '武术大会平安无事地结束了，\n',
            '但是恐怖分子会在诞辰庆典时\n',
            '发动袭击也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不要松懈，\n',
            '继续保持高度警戒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_174B')

    def _loc_D74(): pass

    label('loc_D74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_EBC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_DFF',
    )

    ChrTalk(
        0x0008,
        (
            '我听说情报部的特务部队\n',
            '似乎聚集了一批\n',
            '能力相当强的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '仔细想想的话，\n',
            '有调集那么多精英部队\n',
            '到情报部去的必要吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB9')

    def _loc_DFF(): pass

    label('loc_DFF')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x0008,
        (
            '我听说情报部的特务部队\n',
            '似乎聚集了一批\n',
            '能力相当强的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '仔细想想的话，\n',
            '有调集那么多精英部队\n',
            '到情报部去的必要吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然不是我应该深究的事，\n',
            '不过最近有很多现象让我在意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB9(): pass

    label('loc_EB9')

    Jump('loc_174B')

    def _loc_EBC(): pass

    label('loc_EBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_F1A',
    )

    ChrTalk(
        0x0008,
        (
            '上面下达了\n',
            '再次强化警备体制的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '情报部好像还没有\n',
            '确定恐怖分子的行踪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_174B')

    def _loc_F1A(): pass

    label('loc_F1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_FB8',
    )

    ChrTalk(
        0x0008,
        (
            '我们圣海姆的守备队\n',
            '也接到了不准接近\n',
            '艾尔贝离宫的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我觉得其实也不用特意强调嘛。\n',
            '那是我们管辖区之外的地方，\n',
            '根本就没想要去靠近那里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_174B')

    def _loc_FB8(): pass

    label('loc_FB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_103B',
    )

    ChrTalk(
        0x0008,
        (
            '关于蔡斯事件的调查，\n',
            '好像由情报部出马了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '交给理查德上校的话，\n',
            '肯定能像柏斯的空贼那样，\n',
            '把恐怖分子一网打尽吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_174B')

    def _loc_103B(): pass

    label('loc_103B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_10A0',
    )

    ChrTalk(
        0x0008,
        (
            '刚才误会你们了，\n',
            '实在是抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过，快到诞辰庆典了，\n',
            '盘查行动是\n',
            '绝对不能放松的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_174B')

    def _loc_10A0(): pass

    label('loc_10A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_11DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_1103',
    )

    ChrTalk(
        0x0008,
        (
            '绝对不能让\n',
            '犯人们入侵王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '紧张的日子还会再持续下去，\n',
            '请你们再加把劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11DB')

    def _loc_1103(): pass

    label('loc_1103')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    OP_4A(0x0012, 255)

    ChrTalk(
        0x0012,
        (
            '队长，\n',
            '先前的命令已经向士兵们传达了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '我向他们发出了\n',
            '在避免不必要的纠纷的同时\n',
            '严格盘查来往人员的指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '很好，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '紧张的日子还会再持续下去，\n',
            '现在是不能松懈的时期。\n',
            '请你们再加把劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0012, 255)

    def _loc_11DB(): pass

    label('loc_11DB')

    Jump('loc_174B')

    def _loc_11DE(): pass

    label('loc_11DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_131C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_1241',
    )

    ChrTalk(
        0x0008,
        (
            '绝对不能让\n',
            '罪犯们入侵王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '紧张的日子还会再持续下去，\n',
            '请你们再加把劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1319')

    def _loc_1241(): pass

    label('loc_1241')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    OP_4A(0x0012, 255)

    ChrTalk(
        0x0012,
        (
            '队长，\n',
            '先前的命令已经向士兵们传达了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '我向他们发出了\n',
            '在避免不必要的纠纷的同时\n',
            '严格盘查来往人员的指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '很好，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '紧张的日子还会再持续下去，\n',
            '现在是不能松懈的时期。\n',
            '请你们再加把劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0012, 255)

    def _loc_1319(): pass

    label('loc_1319')

    Jump('loc_174B')

    def _loc_131C(): pass

    label('loc_131C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_13E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_1387',
    )

    ChrTalk(
        0x0008,
        (
            '……对我来说，\n',
            '盘查解除的命令完全不能理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是命令就是命令。\n',
            '就是这么一回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13E3')

    def _loc_1387(): pass

    label('loc_1387')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x0008,
        (
            '……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我现在很忙。\n',
            '有问题的话去找其他士兵吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13E3(): pass

    label('loc_13E3')

    Jump('loc_174B')

    def _loc_13E6(): pass

    label('loc_13E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1526',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_147B',
    )

    ChrTalk(
        0x0008,
        (
            '只有这个是最重要的事。\n',
            '王国军正规的搜查\n',
            '不久就要开始了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '到那个时候\n',
            '犯人就会变成瓮中之鳖了。\n',
            '所以在这之前还是先忍耐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1523')

    def _loc_147B(): pass

    label('loc_147B')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x0008,
        (
            '现在，来往的旅行者\n',
            '在确认身份之前是不能通过的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '理由不用说你们也明白吧。\n',
            '就是因为蔡斯发生了恐怖事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为了不让犯人从蔡斯逃跑，\n',
            '王国军也是尽了全力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1523(): pass

    label('loc_1523')

    Jump('loc_174B')

    def _loc_1526(): pass

    label('loc_1526')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_15F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_1592',
    )

    ChrTalk(
        0x0008,
        (
            '唔……\n',
            '是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如何建立当情况紧急时\n',
            '能快速和王都取得联络的体制\n',
            '是关键所在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15F3')

    def _loc_1592(): pass

    label('loc_1592')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x0008,
        (
            '哦？你们有什么事？\n',
            '对不起，我现在正忙于公务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '除非有急事，\n',
            '否则还是去问别的士兵吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15F3(): pass

    label('loc_15F3')

    Jump('loc_174B')

    def _loc_15F6(): pass

    label('loc_15F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_174B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_1667',
    )

    ChrTalk(
        0x0008,
        (
            '现在随时都可能\n',
            '会向游击士协会请求帮助……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可是那边的人手也是有限的。\n',
            '不能抱太大希望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_174B')

    def _loc_1667(): pass

    label('loc_1667')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x0008,
        (
            '圣海姆门守备队的使命，\n',
            '首先就是城门的警备工作，\n',
            '但同时也必须确保街道的安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '马上就到女王的诞辰庆典了。\n',
            '那时候旅行者的人数也会激増吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个时候如果出现了凶暴的魔兽，\n',
            '该怎么对付才好呢……\n',
            '现在必须要好好想想了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_174B(): pass

    label('loc_174B')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x174F
@scena.Code('func_07_174F')
def func_07_174F():
    Return()

# id: 0x0008 offset: 0x1750
@scena.Code('func_08_1750')
def func_08_1750():
    Return()

# id: 0x0009 offset: 0x1751
@scena.Code('func_09_1751')
def func_09_1751():
    Return()

# id: 0x000A offset: 0x1752
@scena.Code('func_0A_1752')
def func_0A_1752():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_175F',
    )

    Jump('loc_1966')

    def _loc_175F(): pass

    label('loc_175F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1851',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_17CC',
    )

    ChrTalk(
        0x00FE,
        (
            '太好了，\n',
            '终于可以按照预定计划返回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为啊，\n',
            '想和她一起逛的地方还有很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184E')

    def _loc_17CC(): pass

    label('loc_17CC')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '呼，太好了。\n',
            '结束盘查的时间比我想象得还要早。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '现在已经没有危险了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样就可以\n',
            '按照预定计划返回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_184E(): pass

    label('loc_184E')

    Jump('loc_1966')

    def _loc_1851(): pass

    label('loc_1851')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1955',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1895',
    )

    ChrTalk(
        0x00FE,
        (
            '冷……冷静点！\n',
            '无论发生什么事也要临危不惧啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1952')

    def _loc_1895(): pass

    label('loc_1895')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '听说蔡斯那边\n',
            '发生了什么大事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为盘查，\n',
            '现在都不能回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但、但是，\n',
            '在这种时候我更要保持冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrDirection(0x0010, 270, 400)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '亲爱的……\n',
            '我、我一定会保护你的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1952(): pass

    label('loc_1952')

    Jump('loc_1966')

    def _loc_1955(): pass

    label('loc_1955')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_195F',
    )

    Jump('loc_1966')

    def _loc_195F(): pass

    label('loc_195F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1966',
    )

    def _loc_1966(): pass

    label('loc_1966')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x196A
@scena.Code('func_0B_196A')
def func_0B_196A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1977',
    )

    Jump('loc_1B15')

    def _loc_1977(): pass

    label('loc_1977')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1A52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_19CD',
    )

    ChrTalk(
        0x00FE,
        (
            '返回王都以后，\n',
            '就该到女王的诞辰庆典了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，真是期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A4F')

    def _loc_19CD(): pass

    label('loc_19CD')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '啊，太好了。\n',
            '好像又恢复正常了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '盘查的时候，\n',
            '士兵们给人的感觉好可怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这时我会比平时\n',
            '更加娇气地依靠着他哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A4F(): pass

    label('loc_1A4F')

    Jump('loc_1B15')

    def _loc_1A52(): pass

    label('loc_1A52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1B04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1AB5',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '阿鲁姆有些过于激动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，稍微有点不可靠\n',
            '也是他的魅力所在呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B01')

    def _loc_1AB5(): pass

    label('loc_1AB5')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '唉，又出事了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然都不是大事，\n',
            '可最近全都是这样的消息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B01(): pass

    label('loc_1B01')

    Jump('loc_1B15')

    def _loc_1B04(): pass

    label('loc_1B04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1B0E',
    )

    Jump('loc_1B15')

    def _loc_1B0E(): pass

    label('loc_1B0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1B15',
    )

    def _loc_1B15(): pass

    label('loc_1B15')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1B19
@scena.Code('func_0C_1B19')
def func_0C_1B19():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1B8F',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '关所接到的命令\n',
            '基本上都是由情报部发出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是因为理查德上校成为了\n',
            '公爵的辅佐的缘故吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_1B8F(): pass

    label('loc_1B8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1C02',
    )

    ChrTalk(
        0x00FE,
        (
            '有关女王陛下的病情，\n',
            '陛下自己没有发表任何声明，\n',
            '这一点让人在意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典\n',
            '到底会怎么样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_1C02(): pass

    label('loc_1C02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1C5E',
    )

    ChrTalk(
        0x00FE,
        (
            '正在举行的武术大会\n',
            '好像还平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能像这样\n',
            '一切顺利结束就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_1C5E(): pass

    label('loc_1C5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1CD2',
    )

    ChrTalk(
        0x00FE,
        (
            '如果和游击士协会合作的话，\n',
            '追查恐怖分子的行动\n',
            '应该会更加有把握吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但实现起来还是很困难啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_1CD2(): pass

    label('loc_1CD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1D4E',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才从格兰赛尔那边\n',
            '来了个身材非常高大的\n',
            '共和国人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说是要参加武术大会，\n',
            '来这里是为了\n',
            '做一下热身运动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_1D4E(): pass

    label('loc_1D4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_1DA0',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才真是\n',
            '对不住各位了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但这也是我的工作。\n',
            '希望你们能理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_1DA0(): pass

    label('loc_1DA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_1EE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_1E0B',
    )

    ChrTalk(
        0x00FE,
        (
            '逃亡中的犯人\n',
            '现在处境应该也很艰难吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在不能松懈这一点上，\n',
            '他们倒是和我们一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EE3')

    def _loc_1E0B(): pass

    label('loc_1E0B')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    OP_4A(0x0008, 255)

    ChrTalk(
        0x00FE,
        (
            '队长，\n',
            '先前的命令已经向士兵们传达了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我向他们发出了\n',
            '在避免不必要的纠纷的同时\n',
            '严格盘查来往人员的指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '很好，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '紧张的日子还会再持续下去，\n',
            '现在是不能松懈的时期。\n',
            '请你们再加把劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)

    def _loc_1EE3(): pass

    label('loc_1EE3')

    Jump('loc_24DF')

    def _loc_1EE6(): pass

    label('loc_1EE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_202C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_1F51',
    )

    ChrTalk(
        0x00FE,
        (
            '逃亡中的犯人\n',
            '现在处境应该也很艰难吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在不能松懈这一点上，\n',
            '他们倒是和我们一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2029')

    def _loc_1F51(): pass

    label('loc_1F51')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    OP_4A(0x0008, 255)

    ChrTalk(
        0x00FE,
        (
            '队长，\n',
            '先前的命令已经向士兵们传达了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我向他们发出了\n',
            '在避免不必要的纠纷的同时\n',
            '严格盘查来往人员的指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '很好，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '紧张的日子还会再持续下去，\n',
            '现在是不能松懈的时期。\n',
            '请你们再加把劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)

    def _loc_2029(): pass

    label('loc_2029')

    Jump('loc_24DF')

    def _loc_202C(): pass

    label('loc_202C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_216E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_20C2',
    )

    ChrTalk(
        0x00FE,
        (
            '一定是军队的上层\n',
            '得到了什么決定性的重要情报，\n',
            '所以才会认为盘查也没有用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么想的话，就能说明一切了。\n',
            '不管能不能理解……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_216B')

    def _loc_20C2(): pass

    label('loc_20C2')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '……解除盘查\n',
            '是军队总部的正式命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的责任就是服从命令，\n',
            '而不是去判断那个命令是否正确。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，今后仍然还是要\n',
            '继续保持警戒的方针。\n',
            '为了预防万一嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_216B(): pass

    label('loc_216B')

    Jump('loc_24DF')

    def _loc_216E(): pass

    label('loc_216E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2287',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_220D',
    )

    ChrTalk(
        0x00FE,
        (
            '游击士协会也有所行动，\n',
            '可还是没能抓住犯人的踪迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对手可是光天化日就敢\n',
            '明目张胆袭击中央工房的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不早一点抓到的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2284')

    def _loc_220D(): pass

    label('loc_220D')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '实在对不起，\n',
            '现在要对通行者进行盘查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是为了阻止\n',
            '恐怖分子逃亡而采取的措施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何请大家理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2284(): pass

    label('loc_2284')

    Jump('loc_24DF')

    def _loc_2287(): pass

    label('loc_2287')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_23D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_234B',
    )

    ChrTalk(
        0x00FE,
        (
            '『亚宁堡』长城\n',
            '一共设置了两个关所……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个圣海姆门和\n',
            '洛连特那边的格鲁纳门\n',
            '都是保护王都的绝对防线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我们守备队来说，\n',
            '无论是多么平静的一天，\n',
            '也不应该有懈怠的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D6')

    def _loc_234B(): pass

    label('loc_234B')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '唔，女王的诞辰庆典马上就到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有必要提前训练一下\n',
            '有大量旅客时的警备体制呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快向迪鲁队长\n',
            '请示一下训练的实施计划吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23D6(): pass

    label('loc_23D6')

    Jump('loc_24DF')

    def _loc_23D9(): pass

    label('loc_23D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_24DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_2478',
    )

    ChrTalk(
        0x00FE,
        (
            '从里面的楼梯上去，\n',
            '就可以到『亚宁堡』的\n',
            '城墙上面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为是利用了原来的遗迹建成的，\n',
            '所以里面的走廊稍微有些复杂。\n',
            '这也是没办法的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_2478(): pass

    label('loc_2478')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '啊，你们是来参观的吗？\n',
            '有问题的话请尽管提出来，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要在我的解答范围之内\n',
            '我都会尽力回答的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24DF(): pass

    label('loc_24DF')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x24E3
@scena.Code('func_0D_24E3')
def func_0D_24E3():
    TalkBegin(0x00FE)
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '欢迎品尝「终极肉火锅」700米拉\n'),
            TXT(0x03, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_255F',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x4A)
    OP_56(0x00)
    TalkEnd(0x0013)

    Return()

    def _loc_255F(): pass

    label('loc_255F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_265D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x2BC),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2628',
    )

    SubMira(700)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '终极肉火锅',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(0x0000, 0xFD, 700)
    SetChrStatus(0x0001, 0xFD, 700)
    SetChrStatus(0x0002, 0xFD, 700)
    SetChrStatus(0x0003, 0xFD, 700)
    SetChrStatus(0x0004, 0xFD, 700)
    SetChrStatus(0x0005, 0xFD, 700)
    SetChrStatus(0x0006, 0xFD, 700)
    SetChrStatus(0x0007, 0xFD, 700)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_261A',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0007)"),
            Expr.Return,
        ),
        'loc_25F2',
    )

    Jump('loc_261A')

    def _loc_25F2(): pass

    label('loc_25F2')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '终极肉火锅',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_261A(): pass

    label('loc_261A')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_264E')

    def _loc_2628(): pass

    label('loc_2628')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_264E(): pass

    label('loc_264E')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0013)

    Return()

    def _loc_265D(): pass

    label('loc_265D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2677',
    )

    FadeIn(300, 0)
    TalkEnd(0x0013)

    Return()

    def _loc_2677(): pass

    label('loc_2677')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_26E9',
    )

    ChrTalk(
        0x00FE,
        (
            '无论再忙，\n',
            '饭也是必须要好好吃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～为了士兵们，\n',
            '我要仔细制订\n',
            '确保营养的特别菜单！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF2')

    def _loc_26E9(): pass

    label('loc_26E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2739',
    )

    ChrTalk(
        0x00FE,
        (
            '黛米那家伙\n',
            '不知还在哪里偷懒呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，算了。\n',
            '现在客人也不多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF2')

    def _loc_2739(): pass

    label('loc_2739')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2791',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '这个时间还是休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又进了不少材料，\n',
            '考虑一下新的菜式吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF2')

    def _loc_2791(): pass

    label('loc_2791')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_280C',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会开始以后，\n',
            '基本上没有通行的旅客了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为有士兵在，\n',
            '倒不是完全没有客人来，\n',
            '不过还是有些寂寞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF2')

    def _loc_280C(): pass

    label('loc_280C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2946',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2890',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '刚才来用餐的那个巨汉\n',
            '也吃得好香呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看他吃的样子，都把我感动了。\n',
            '不由自主地就给他的餐费打了折。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2943')

    def _loc_2890(): pass

    label('loc_2890')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '如果客人觉得美味，\n',
            '我会很高兴哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也一直在\n',
            '钻研烹饪技术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才来用餐的那个巨汉\n',
            '也吃得好香呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看他吃的样子，都把我感动了。\n',
            '不由自主地就给他的餐费打了折。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2943(): pass

    label('loc_2943')

    Jump('loc_2FF2')

    def _loc_2946(): pass

    label('loc_2946')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_2A5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2983',
    )

    ChrTurnDirection(0x0013, 0x010E, 400)

    ChrTalk(
        0x00FE,
        (
            '学者先生，\n',
            '您的研究也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A58')

    def _loc_2983(): pass

    label('loc_2983')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    ChrTurnDirection(0x0013, 0x010E, 400)

    ChrTalk(
        0x00FE,
        (
            '咦，\n',
            '你不就是刚才的那个客人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0151850003V#130F哦，\n',
            '刚才真的是承蒙关照了，\n',
            '非常感谢您啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没什么没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的手艺不怎么样，\n',
            '你也能吃得那么香。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还要感谢你呢。\n',
            '您的研究也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A58(): pass

    label('loc_2A58')

    Jump('loc_2FF2')

    def _loc_2A5B(): pass

    label('loc_2A5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_2AFC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2AB4',
    )

    ChrTalk(
        0x00FE,
        (
            '请问客人们\n',
            '是要去格兰赛尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真好啊，\n',
            '我也想去诞辰庆典玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AF9')

    def _loc_2AB4(): pass

    label('loc_2AB4')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '这里是食堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也可以当作休息室，\n',
            '请随便坐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AF9(): pass

    label('loc_2AF9')

    Jump('loc_2FF2')

    def _loc_2AFC(): pass

    label('loc_2AFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2B48',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '这里是食堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也可以当作休息室，\n',
            '请随便坐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF2')

    def _loc_2B48(): pass

    label('loc_2B48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2C1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2BAC',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '说起来还没听说\n',
            '已经抓到犯人了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '盘查就这样解除了，\n',
            '这么做好吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C17')

    def _loc_2BAC(): pass

    label('loc_2BAC')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '啊～欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '盘查解除得比预想还要早……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，我是无所谓。\n',
            '但是捜査那边没问题吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C17(): pass

    label('loc_2C17')

    Jump('loc_2FF2')

    def _loc_2C1A(): pass

    label('loc_2C1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2D1D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2C67',
    )

    ChrTalk(
        0x00FE,
        (
            '但是，竟然敢袭击中央工房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些人也真是胆大包天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D1A')

    def _loc_2C67(): pass

    label('loc_2C67')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '事情好像变得很严重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在能做的事就是\n',
            '给不能外出的人们\n',
            '做出美味的食物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果就那么饿着肚子的话，\n',
            '人就会越发脆弱了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '填饱肚子的话，\n',
            '心情也会愉快的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D1A(): pass

    label('loc_2D1A')

    Jump('loc_2FF2')

    def _loc_2D1D(): pass

    label('loc_2D1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2EF5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2DBF',
    )

    ChrTalk(
        0x00FE,
        (
            '这里需要直接面对客人。\n',
            '所以任何时候都要全力以赴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～说起来，\n',
            '黛米那家伙到哪里去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '稍微偷懒一下倒没关系，\n',
            '但是也要看时候吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EF2')

    def _loc_2DBF(): pass

    label('loc_2DBF')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '我年轻的时候，目标是经营一流的餐厅。\n',
            '但是随着实际工作的展开，\n',
            '想法也开始改变了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就这样一直\n',
            '在这个食堂工作也很好啊。\n',
            '我现在就是这么想的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里能直接面对客人不是吗？\n',
            '从客人的反应马上就会知道\n',
            '饭菜是好吃还是难吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以任何时候都要全力以赴。\n',
            '想要提高烹饪水平的话，\n',
            '这里确实是最佳地点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EF2(): pass

    label('loc_2EF2')

    Jump('loc_2FF2')

    def _loc_2EF5(): pass

    label('loc_2EF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2FF2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2FC0',
    )

    ChrTalk(
        0x00FE,
        (
            '这里现有的材料也就这么多了，\n',
            '没办法作出丰富的菜式来……\n',
            '只好用烹饪技术来弥补这一不足了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有机会的话你们也来尝尝看吧。\n',
            '料理的好坏不是用价格衡量的。\n',
            '希望你们也能明白这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF2')

    def _loc_2FC0(): pass

    label('loc_2FC0')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '这里是食堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请随便坐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FF2(): pass

    label('loc_2FF2')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x2FF6
@scena.Code('func_0E_2FF6')
def func_0E_2FF6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_304F',
    )

    ChrTalk(
        0x00FE,
        (
            '最近士兵们\n',
            '好像都很忙哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，看不到我中意的人，\n',
            '真是好无聊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A17')

    def _loc_304F(): pass

    label('loc_304F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3141',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_30B3',
    )

    ChrTalk(
        0x00FE,
        (
            '有时我觉得\n',
            '严厉的人也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有真的关心对方\n',
            '才会如此严格要求，\n',
            '不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_313E')

    def _loc_30B3(): pass

    label('loc_30B3')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '这么考虑的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有温柔\n',
            '果然还是不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时我觉得\n',
            '严厉的人也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有真的关心对方\n',
            '才会如此严格要求，\n',
            '不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_313E(): pass

    label('loc_313E')

    Jump('loc_3A17')

    def _loc_3141(): pass

    label('loc_3141')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_31AB',
    )

    ChrTalk(
        0x00FE,
        (
            '是吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '桑吉特先生\n',
            '又随便给人打折了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他人确实挺不错的，\n',
            '不过没办法成为有钱人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A17')

    def _loc_31AB(): pass

    label('loc_31AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_328D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3213',
    )

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '这个时间比较无聊，\n',
            '要不要去找妈妈玩呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '在旅馆帮忙也很无聊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_328A')

    def _loc_3213(): pass

    label('loc_3213')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '现在这个时间， \n',
            '士兵们都在工作，无聊死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '要不要去找妈妈玩呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '在旅馆帮忙也很无聊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_328A(): pass

    label('loc_328A')

    Jump('loc_3A17')

    def _loc_328D(): pass

    label('loc_328D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_331D',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才有一个\n',
            '像熊一样的大哥哥来了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他的食量好惊人，\n',
            '看得我真是佩服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '桑吉特先生\n',
            '又给他打了折，\n',
            '这样下去会亏本的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A17')

    def _loc_331D(): pass

    label('loc_331D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_338F',
    )

    ChrTalk(
        0x00FE,
        (
            '桑吉特先生\n',
            '一看到客人吃得开心，\n',
            '马上就会给客人打折。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这家店，\n',
            '真的能赚钱吗……\n',
            '我真是担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A17')

    def _loc_338F(): pass

    label('loc_338F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_345C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_33EE',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才来的那个客人\n',
            '光点便宜的菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尽管如此，\n',
            '桑吉特先生也给他打折了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3459')

    def _loc_33EE(): pass

    label('loc_33EE')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '刚才来的那个客人\n',
            '光点便宜的菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尽管如此，\n',
            '桑吉特先生也给他打折了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他的心肠也太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3459(): pass

    label('loc_3459')

    Jump('loc_3A17')

    def _loc_345C(): pass

    label('loc_345C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_359A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3509',
    )

    ChrTalk(
        0x00FE,
        (
            '以前觉得\n',
            '欧鲁尼斯先生挺普通的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过不知道为什么，\n',
            '最近觉得他变帅了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道……\n',
            '是交了女朋友吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，如果是那样的话，\n',
            '真是可惜啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3597')

    def _loc_3509(): pass

    label('loc_3509')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '马上就到士兵们来吃饭的时间了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '守卫王都那一侧的欧鲁尼斯先生\n',
            '最近也很帅哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿……\n',
            '他们赶快来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3597(): pass

    label('loc_3597')

    Jump('loc_3A17')

    def _loc_359A(): pass

    label('loc_359A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_36EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3664',
    )

    ChrTalk(
        0x00FE,
        (
            '进行盘查时的士兵们\n',
            '比平时要帅多了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '儒勒先生和埃克托尔先生\n',
            '就算是被调到亲卫队\n',
            '我也不会觉得奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '穿上亲卫队制服的儒勒先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '光是想象我都要燃烧了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36E7')

    def _loc_3664(): pass

    label('loc_3664')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '太好了，\n',
            '又恢复平时的体制了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '儒勒先生他们在盘查时\n',
            '认真的样子也很帅哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '该怎么说呢，\n',
            '这就是男人的工作吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36E7(): pass

    label('loc_36E7')

    Jump('loc_3A17')

    def _loc_36EA(): pass

    label('loc_36EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_37DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3759',
    )

    ChrTalk(
        0x00FE,
        (
            '果然恋人就是要\n',
            '在任何时候都可以依靠的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么考虑的话，\n',
            '士兵就是我理想的恋人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37D8')

    def _loc_3759(): pass

    label('loc_3759')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '蔡斯发生的事件真是太可怕了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，这种非常时刻\n',
            '有强者在旁边的话就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿……\n',
            '士兵们果然很了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37D8(): pass

    label('loc_37D8')

    Jump('loc_3A17')

    def _loc_37DB(): pass

    label('loc_37DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_38F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3883',
    )

    ChrTalk(
        0x00FE,
        (
            '桑吉特先生是个好人，\n',
            '就是性格有点怪，不能当我恋爱对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不深入交往是不可能了解\n',
            '一个人原本的性格的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，\n',
            '一开始只能凭外表来选择了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38F0')

    def _loc_3883(): pass

    label('loc_3883')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '我说，\n',
            '妈妈觉得儒勒先生\n',
            '和埃克托尔先生哪个比较好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '儒勒先生\n',
            '虽然人长得帅，\n',
            '但是有些过于严厉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38F0(): pass

    label('loc_38F0')

    Jump('loc_3A17')

    def _loc_38F3(): pass

    label('loc_38F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3A17',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3998',
    )

    ChrTalk(
        0x00FE,
        (
            '男人就是要看外表呢。\n',
            '在所有士兵中，儒勒先生是最帅的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后就是埃克托尔先生……\n',
            '副长先生也还不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '剩下的就不在我考虑范围内了。  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A17')

    def _loc_3998(): pass

    label('loc_3998')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '马上就到士兵们来吃饭的时间了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0014, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿……\n',
            '儒勒先生，快点来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A17(): pass

    label('loc_3A17')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x3A1B
@scena.Code('func_0F_3A1B')
def func_0F_3A1B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3A28',
    )

    Jump('loc_3DC3')

    def _loc_3A28(): pass

    label('loc_3A28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3A9C',
    )

    ChrTalk(
        0x00FE,
        (
            '盘查好像解除了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是\n',
            '已经抓到犯人了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是如果是这样，\n',
            '《利贝尔通讯》又没有报道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DC3')

    def _loc_3A9C(): pass

    label('loc_3A9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3BC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3B10',
    )

    ChrTalk(
        0x00FE,
        (
            '在柏斯旅行的时候\n',
            '遇到了空贼团的事件，\n',
            '不能乘坐定期船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '女神爱德丝心情不太好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BC5')

    def _loc_3B10(): pass

    label('loc_3B10')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '刚才军队的人\n',
            '说明了盘查的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们两个本来就是格兰赛尔的市民，\n',
            '所以还好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是很多旅行者\n',
            '在确认身份之前都不能离开呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说到底就是因为\n',
            '发生了恐怖袭击事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BC5(): pass

    label('loc_3BC5')

    Jump('loc_3DC3')

    def _loc_3BC8(): pass

    label('loc_3BC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3D24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3C54',
    )

    ChrTalk(
        0x00FE,
        (
            '在像安特洛丝餐厅\n',
            '那样的一流饭店用餐，\n',
            '享受高级服务虽然很棒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过偶尔来这种有个性的地方\n',
            '体会一下新鲜感也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D21')

    def _loc_3C54(): pass

    label('loc_3C54')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '其实这个食堂\n',
            '也有着很好的风评呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里有其他地方\n',
            '品尝不到的特殊风味的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在像安特洛丝餐厅那样的一流饭店\n',
            '享受高级服务虽然很棒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过偶尔来这种有个性的地方\n',
            '体会一下新鲜感也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D21(): pass

    label('loc_3D21')

    Jump('loc_3DC3')

    def _loc_3D24(): pass

    label('loc_3D24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3DC3',
    )

    ChrTalk(
        0x00FE,
        (
            '我们是从王都那边\n',
            '来艾尔贝周游道散步的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾尔贝周游道\n',
            '气氛相当优雅恬静，\n',
            '简直像花园中的庭院小路呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '建议你们去王都的时候\n',
            '也到那里散散步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DC3(): pass

    label('loc_3DC3')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x3DC7
@scena.Code('func_10_3DC7')
def func_10_3DC7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3DD4',
    )

    Jump('loc_40B5')

    def _loc_3DD4(): pass

    label('loc_3DD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3E5C',
    )

    ChrTalk(
        0x00FE,
        (
            '太好了。\n',
            '看起来好像恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是这么早\n',
            '就停止了盘查，\n',
            '不会影响搜查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我是外行，\n',
            '不过还是有点担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40B5')

    def _loc_3E5C(): pass

    label('loc_3E5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3F3B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3EBB',
    )

    ChrTalk(
        0x00FE,
        (
            '最近一段时间\n',
            '连续发生了很多大事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '暂时还是不要到处旅行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F38')

    def _loc_3EBB(): pass

    label('loc_3EBB')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '真是很可怕啊。\n',
            '这次又是在蔡斯发生了恐怖活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近一段时间，\n',
            '连续发生了很多大事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望只是不幸的偶然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F38(): pass

    label('loc_3F38')

    Jump('loc_40B5')

    def _loc_3F3B(): pass

    label('loc_3F3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_4058',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3FB8',
    )

    ChrTalk(
        0x00FE,
        (
            '听说这是食堂独创的菜式，\n',
            '我本来没有报什么期待的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过吃过之后觉得还挺不错。\n',
            '想尝尝其他的菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4055')

    def _loc_3FB8(): pass

    label('loc_3FB8')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '这里的饭菜还真是好吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以利贝尔料理为基础，\n',
            '其中隐藏着的东方香料\n',
            '将味道提升至极致……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是食堂独创的菜式，\n',
            '但真的是美味的料理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4055(): pass

    label('loc_4055')

    Jump('loc_40B5')

    def _loc_4058(): pass

    label('loc_4058')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_40B5',
    )

    ChrTalk(
        0x00FE,
        (
            '我家先生啊，\n',
            '从来都不回家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在王都呆着除了无聊的事，\n',
            '也没有其他事可干了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40B5(): pass

    label('loc_40B5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x40B9
@scena.Code('func_11_40B9')
def func_11_40B9():
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x40BE
@scena.Code('func_12_40BE')
def func_12_40BE():
    TalkBegin(0x0017)
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_411A',
    )

    OP_0D()
    OP_A9(0x49)
    OP_56(0x00)
    TalkEnd(0x0017)

    Return()

    def _loc_411A(): pass

    label('loc_411A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_412B',
    )

    TalkEnd(0x0017)

    Return()

    def _loc_412B(): pass

    label('loc_412B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4193',
    )

    ChrTalk(
        0x0017,
        (
            '士兵们也一直都保持着紧张状态，\n',
            '难道他们不累吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '不过，那是他们的工作。\n',
            '累也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4917')

    def _loc_4193(): pass

    label('loc_4193')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_41F1',
    )

    ChrTalk(
        0x0017,
        (
            '这孩子也别絮絮叨叨了，\n',
            '早点交个男朋友，\n',
            '给我带来就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '她年纪也不小了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4917')

    def _loc_41F1(): pass

    label('loc_41F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4247',
    )

    ChrTalk(
        0x0017,
        (
            '这个孩子每天\n',
            '都要来说这些话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '这么明目张胆地偷懒\n',
            '很容易被开除的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4917')

    def _loc_4247(): pass

    label('loc_4247')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_429D',
    )

    ChrTalk(
        0x0017,
        (
            '用餐时间结束了，\n',
            '食堂那边\n',
            '也该闲下来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '我预感到那孩子该来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4917')

    def _loc_429D(): pass

    label('loc_429D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_431E',
    )

    ChrTalk(
        0x0017,
        (
            '今天天气不错。\n',
            '晒床单的话应该很快就能干吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '如果在『亚宁堡』上晒衣服\n',
            '会干得很快吧……\n',
            '但是队长肯定会生气的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4917')

    def _loc_431E(): pass

    label('loc_431E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_43B2',
    )

    ChrTalk(
        0x0017,
        (
            '在这里工作，\n',
            '就算自己不愿意，\n',
            '也不得不听士兵们谈话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '像什么恐怖分子啦，袭击什么的，\n',
            '那些讨厌的事情都会听到，\n',
            '弄得心情都很不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4917')

    def _loc_43B2(): pass

    label('loc_43B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_44AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_440F',
    )

    ChrTalk(
        0x0017,
        (
            '之前一段时间\n',
            '来这里的人很多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '不过现在大家\n',
            '都已经出发去王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44AB')

    def _loc_440F(): pass

    label('loc_440F')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0017,
        (
            '啊～欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '之前一段时间\n',
            '来这里的人很多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '不过现在大家\n',
            '都已经出发去王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '因为武术大会就要开始了嘛。\n',
            '他们急切的心情我很理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44AB(): pass

    label('loc_44AB')

    Jump('loc_4917')

    def _loc_44AE(): pass

    label('loc_44AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_4558',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_451B',
    )

    ChrTalk(
        0x0017,
        (
            '其他的客人\n',
            '都已经去王都了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '因为武术大会就要开始了嘛。\n',
            '他们急切的心情我很理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4555')

    def _loc_451B(): pass

    label('loc_451B')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0017,
        (
            '啊～欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '其他的客人\n',
            '都已经去王都了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4555(): pass

    label('loc_4555')

    Jump('loc_4917')

    def _loc_4558(): pass

    label('loc_4558')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_460F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_45A1',
    )

    ChrTalk(
        0x0017,
        (
            '虽然有些不能理解， \n',
            '不过一定是军队里发生了什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_460C')

    def _loc_45A1(): pass

    label('loc_45A1')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0017,
        (
            '虽然不太明白，\n',
            '但是盘查已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '队长先生好像\n',
            '也不能理解这件事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '他也不知道理由吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_460C(): pass

    label('loc_460C')

    Jump('loc_4917')

    def _loc_460F(): pass

    label('loc_460F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_4703',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_4674',
    )

    ChrTalk(
        0x0017,
        (
            '中央工房被袭击了，\n',
            '确实是不得了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '盘查也好怎么也好，\n',
            '赶快把犯人抓住吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4700')

    def _loc_4674(): pass

    label('loc_4674')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0017,
        (
            '不管怎么说，\n',
            '这可是非同一般的案件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '早点抓住犯人结束盘查虽然很好，\n',
            '但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '本来被禁止外出的客人\n',
            '已经做好住宿的准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4700(): pass

    label('loc_4700')

    Jump('loc_4917')

    def _loc_4703(): pass

    label('loc_4703')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_480F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_474F',
    )

    ChrTalk(
        0x0017,
        (
            '……话说回来，黛米。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '你在这种地方\n',
            '偷懒没关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_480C')

    def _loc_474F(): pass

    label('loc_474F')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0017,
        (
            '如果是我的话，\n',
            '就会盯住厨师桑吉特呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '他只会认真工作，\n',
            '对女人没兴趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '虽然他缺乏情趣，\n',
            '不过讲信用才是结婚的第一前提呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '抛开这个不说，\n',
            '他也是个很会听别人说话的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_480C(): pass

    label('loc_480C')

    Jump('loc_4917')

    def _loc_480F(): pass

    label('loc_480F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_4917',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_484E',
    )

    ChrTalk(
        0x0017,
        (
            '欢迎来到圣海姆门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '怎么？想休息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4917')

    def _loc_484E(): pass

    label('loc_484E')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0017,
        (
            '啊，\n',
            '欢迎来到圣海姆门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '这里是旅行者专用的住宿设施。\n',
            '任何人都可以放心使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '旁边有个食堂，\n',
            '我的女儿就在那里工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '如果方便的话，也到那边光顾一下吧。\n',
            '那里的饭菜有着不错的评价呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4917(): pass

    label('loc_4917')

    TalkEnd(0x0017)

    Return()

# id: 0x0013 offset: 0x491B
@scena.Code('func_13_491B')
def func_13_491B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4BF9',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B72',
    )

    SetScenaFlags(ScenaFlag(0x00B0, 3, 0x583))

    ChrTalk(
        0x00FE,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F啊，我还以为是谁呢……\n',
            '真的是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯？是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呵呵，就是在洛连特\n',
            '寻找结晶回路碎片的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找那碎片吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '接下来要去格兰赛尔了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '不，去蔡斯。\n',
            '因为在格兰赛尔卖了些东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老妈说要用那些米拉\n',
            '买些导力器回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿，老妈也开始知道\n',
            '什么东西才是有价值的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F怎么样都好啦。\n',
            '你还是老样子，那么自大傲慢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '是吗？我觉得自己 \n',
            '只不过是说了理所当然的话而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那再见吧。\n',
            '老这么乱逛的话，\n',
            '老妈又要唠叨了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BF9')

    def _loc_4B72(): pass

    label('loc_4B72')

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔这城市\n',
            '果然很厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家看起来都很有钱，\n',
            '我们带来的商品都很顺利地卖出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来要去蔡斯\n',
            '购入一些导力器制品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4BF9(): pass

    label('loc_4BF9')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x4BFD
@scena.Code('func_14_4BFD')
def func_14_4BFD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4D68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 2, 0x582)),
            Expr.Return,
        ),
        'loc_4C84',
    )

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔的确是个好地方。\n',
            '我们的民间手工艺品也很畅销哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赚够了本钱，\n',
            '就可以去进一些\n',
            '导力器制品了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D68')

    def _loc_4C84(): pass

    label('loc_4C84')

    SetScenaFlags(ScenaFlag(0x00B0, 2, 0x582))

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔的确是个好地方。\n',
            '不愧是被称为王都的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家的钱包都是鼓鼓的，\n',
            '我们的民间手工艺品也很畅销哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然已经赚够了本钱，\n',
            '就可以去进一些\n',
            '导力器制品了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果把导力器拿回共和国去卖，\n',
            '会赚一大笔钱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D68(): pass

    label('loc_4D68')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x4D6C
@scena.Code('func_15_4D6C')
def func_15_4D6C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_4E48',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4DB3',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀～去王都的飞艇坪\n',
            '就是接下来的期待所在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E48')

    def _loc_4DB3(): pass

    label('loc_4DB3')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '想到难得有这样的机会，\n',
            '回共和国的时候\n',
            '还是乘坐定期船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正准备去\n',
            '格兰赛尔的国际空港。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，旅费有限，\n',
            '到王都这段路还是走着去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E48(): pass

    label('loc_4E48')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x4E4C
@scena.Code('func_16_4E4C')
def func_16_4E4C():
    Call(0, 0x0017)

    Return()

# id: 0x0017 offset: 0x4E51
@scena.Code('func_17_4E51')
def func_17_4E51():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7069',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 7450, 0, 880, 0)
    SetChrPos(0x0102, 6480, 0, 880, 0)
    CameraMove(7630, 200, 2180, 0)
    SetChrDirection(0x0009, 180, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#2140100373V#5P你们好。\n',
            '欢迎来到圣海姆门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100374V#5P是来办理\n',
            '去王都的通行手续的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【办理通行手续】\n'),
            TXT(0x01, '【还是算了】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4F6B'),
        (0x00000001, 'loc_5011'),
        (-1, 'loc_504B'),
    )

    def _loc_4F6B(): pass

    label('loc_4F6B')

    OP_B7(0x000D, 0x01)
    FormationAddMember(0x0D, 0xFF)
    SetChrFlags(0x010E, 0x0080)
    ChrTurnDirection(0x0009, 0x0102, 0)
    SetChrPos(0x0101, 7450, 0, 880, 0)
    SetChrPos(0x0102, 6480, 0, 880, 0)

    ChrTalk(
        0x0101,
        (
            '#0010100376V#006F嗯，是的。\n',
            '请问现在可以办理吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100377V#5P可以，请过来吧。\n',
            '在这张单子上签个名就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_504B')

    def _loc_5011(): pass

    label('loc_5011')

    ChrTalk(
        0x0009,
        (
            '#2140100375V#5P我知道了。\n',
            '准备好的话请告诉我一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0009, 255)
    EventEnd(0x00)

    Return()

    def _loc_504B(): pass

    label('loc_504B')

    SetScenaFlags(ScenaFlag(0x00C0, 6, 0x606))
    OP_28(0x0054, 0x01, 0x0020)
    OP_28(0x002A, 0x04, 0x40)
    OP_28(0x002D, 0x04, 0x40)
    OP_28(0x002E, 0x04, 0x40)
    OP_28(0x002F, 0x04, 0x40)
    OP_28(0x0030, 0x04, 0x40)
    OP_28(0x0031, 0x04, 0x40)
    OP_28(0x0034, 0x04, 0x40)
    OP_1B(0x00, 0x00, 0x0019)
    OP_1B(0x01, 0x00, 0xFFFF)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚\n',
            '在手续单据上填写了必要的事项。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#2140100378V#5P不过话说回来，\n',
            '最近的孩子也真是的……\n',
            '该说你们前卫呢还是胆大什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100379V#5P特地沿着街道远足过来，\n',
            '你们两个是在约会吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100380V#004F哎！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100381V#503F约、约会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100382V#019F哈哈，不是这样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100383V别看我们这样，其实我们是兄妹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100384V#509F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100385V#5P哎～一点也不像，\n',
            '不过姓氏确实一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100386V#5P好了，这样通行手续就办完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010100387V#582F………呜………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100388V#014F艾丝蒂尔……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100389V从刚才开始你的样子就不对劲，\n',
            '是不是哪里不舒服了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100390V还是休息一下比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100391V#003F啊～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010100392V#007F没事没事，\n',
            '我真的没关系啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100393V加快脚步去王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100394V#012F那样的话就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100395V#5P不过，如果不是约会的话，\n',
            '是不是去参观武术大会呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5409')
    def lambda_5409():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5409)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100396V#004F哎，武术大会……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100397V#5P什么嘛，又没猜中吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100398V#5P武术大会就是\n',
            '在王都的『王立竞技场』举行的，\n',
            '每年一次的比武格斗盛会啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100399V#5P以王国军队的精锐为首，\n',
            '各地的武术强人齐聚一堂，\n',
            '在大会上以武术一较高下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100400V#5P今天下午\n',
            '就开始举行预选赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100401V#501F哎～真是有意思啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100402V#019F哈哈，\n',
            '是艾丝蒂尔你喜欢的事情嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100403V#5P按照女王陛下的意愿，\n',
            '今年的门票也打折了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100404V#5P啊啊，要不是为了值勤，\n',
            '我也想跑过去看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100405V#001F啊哈哈，真是不巧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100406V#006F不过，我们与其光去参观，\n',
            '倒不如直接参加还好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100407V还可以检验一下自己的修行成果。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100408V#010F确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100409V不过今天已经开始进行预选了，\n',
            '应该不能再参加了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100410V而且还要完成委托，\n',
            '有余闲的话去看看就算了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100411V#007F嘁，真可惜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100412V#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_577F')
    def lambda_577F():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_577F)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100413V#501F嗯？士兵先生？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100414V你怎么了？\n',
            '这样盯着我们看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100415V#5P你胸前那个徽章……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100416V#5P因为你们太年轻了，所以才没注意到。\n',
            '……你们难道是游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100417V#505F嗯，是又怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100418V#014F有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100419V#5P不，那个……\n',
            '该说是问题呢还是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100420V#5P算了……\n',
            '怎么想都不可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 13070, 0, 4800, 0)
    OP_70(0x0000, 20)
    OP_73(0x0000)

    @scena.Lambda('lambda_5901')
    def lambda_5901():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5901)

    @scena.Lambda('lambda_590F')
    def lambda_590F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_590F)

    @scena.Lambda('lambda_591D')
    def lambda_591D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_591D)

    @scena.Lambda('lambda_592B')
    def lambda_592B():
        CameraMove(8280, 0, 2380, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_592B)

    OP_4A(0x0008, 255)
    ChrWalkTo(0x0008, 12460, 0, 2910, 2000, 0x00)
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#2150100421V……喂。\n',
            '值勤的时候不要自言自语的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 9840, 0, 2130, 2000, 0x00)
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#2140100422V#1P啊，队长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100423V怎么，有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100424V#1P那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100425V#5P这两个人好像是……\n',
            '……游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2150100426V什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100427V#002F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 225, 400)

    ChrTalk(
        0x0008,
        (
            '#2150100428V啊，我说你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100429V不好意思，\n',
            '能不能稍微耽误你们一点时间？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100430V#004F哎～？\n',
            '可是我们现在要赶去王都啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100431V哦……是去王都啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100432V作为参考，\n',
            '我能问问你们去那里做什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100433V#580F哎、哎？\n',
            '那个是……被委托的工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100434V工作的内容呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100435V#505F嗯，博士的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100436V#003F……不对！\n',
            '唔，该怎么说呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100437V#015F这位队长，非常抱歉。\n',
            '游击士协会有明文规定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100438V委托人的隐私是不能随便透露出去的。\n',
            '希望您能够体谅我们工作的难处。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100439V嗯……这可真是可疑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100440V看起来，\n',
            '有必要问你们一些事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100441V#509F到底是怎么回事，\n',
            '我完全不明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2140100442V#1P那个，实际上……\n',
            '军队本部传达下来了命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5D41')
    def lambda_5D41():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5D41)

    @scena.Lambda('lambda_5D4F')
    def lambda_5D4F():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5D4F)

    ChrTalk(
        0x0009,
        (
            '#2140100443V#1P说王室亲卫队背叛了女王陛下，\n',
            '还在各地掀起恐怖事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100444V#1P而且，好像其中还有\n',
            '伪装成游击士进行活动的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100445V#1P正因如此，\n',
            '需要对自称游击士的人进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100446V#005F#3S你，你说什么！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#2150100447V喂，不要说多余的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2150100448V虽然很对不起，\n',
            '但这是军队上面的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5EAF')
    def lambda_5EAF():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5EAF)

    @scena.Lambda('lambda_5EBD')
    def lambda_5EBD():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5EBD)

    ChrTalk(
        0x0008,
        (
            '#2150100449V在证实身份之前，\n',
            '请你们暂时留在这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100450V#009F别、别开玩笑了。\n',
            '为什么我们非要听你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x010E, 0x0080)
    SetChrPos(0x010E, 21410, 0, -620, 0)

    NpcTalk(
        0x010E,
        '男性的声音',
        (
            '#0150100451V#3P啊啊！\n',
            '你们终于来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_5FB3')
    def lambda_5FB3():
        ChrTurnDirection(0x00FE, 0x010E, 400)
        Yield()

        Jump('lambda_5FB3')

    DispatchAsync2(0x0101, 0x0001, lambda_5FB3)

    @scena.Lambda('lambda_5FC4')
    def lambda_5FC4():
        ChrTurnDirection(0x00FE, 0x010E, 400)
        Yield()

        Jump('lambda_5FC4')

    DispatchAsync2(0x0008, 0x0001, lambda_5FC4)

    @scena.Lambda('lambda_5FD5')
    def lambda_5FD5():
        ChrTurnDirection(0x00FE, 0x010E, 400)
        Yield()

        Jump('lambda_5FD5')

    DispatchAsync2(0x0009, 0x0001, lambda_5FD5)

    @scena.Lambda('lambda_5FE6')
    def lambda_5FE6():
        ChrWalkTo(0x00FE, 9260, 0, 280, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_5FE6)

    CameraMove(8990, 0, 2340, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010100452V#004F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100453V#014F你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x010E, 0x0001)

    ChrTalk(
        0x010E,
        (
            '#0150100454V#130F#2P哎呀～真是让我等了很久啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100455V如果办完了通行手续，\n',
            '那就马上继续前往王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100456V#580F哎、哎、哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_60D3')
    def lambda_60D3():
        ChrWalkTo(0x00FE, 7860, 0, -380, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_60D3)

    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x010E, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100457V#010F真是抱歉，教授。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100458V签证的时候遇到点麻烦，\n',
            '所以可能要等一阵子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100459V等、等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100460V……那个，您是哪位……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010E, 0x0008, 400)

    ChrTalk(
        0x010E,
        (
            '#0150100461V#130F啊，抱歉，我忘了说。\n',
            '我是考古学家亚鲁瓦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100462V诺桑比亚自治州出身，　\n',
            '是来利贝尔王国进行研究调查的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0008, 0x0009, 400)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#2150100463V对了……\n',
            '这个人办完通行手续了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100464V#1P啊，是的，就在刚才……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2140100465V#1P护照是真的，\n',
            '而且王都的历史资料馆\n',
            '可以为这位先生做身份保证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100466V是吗……\n',
            '这样就没有问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x010E, 400)

    ChrTalk(
        0x0008,
        (
            '#2150100467V失敬了，亚鲁瓦先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010E, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#2150100468V请问一下，\n',
            '你是怎么认识这两位的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100469V#130F啊，他们是游击士嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100470V之前好几次从危险的地方把我救出来，\n',
            '是我的救命恩人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100471V正因为如此，\n',
            '这次就请了他们护送我去王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010E, 0x0101, 400)

    ChrTalk(
        0x010E,
        (
            '#0150100472V#130F#2P对吧？\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_641C')
    def lambda_641C():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_641C)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100473V#004F哎……啊，没错！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100474V#506F实、实际上就是这样～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100475V嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150100476V算了……\n',
            '这样的话就有身份保证了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2150100477V真是抱歉，\n',
            '刚才误会你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100478V#502F嗯、嗯，明白了就好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100479V#010F你们也是因职务所在才这样做，\n',
            '请不要放在心上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(59550, 200, -27280, 0)
    CameraSetDistance(2800, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x010E, 0x0004)
    SetChrChipByIndex(0x0101, 16)
    SetChrChipByIndex(0x0102, 17)
    SetChrChipByIndex(0x010E, 18)
    SetChrSubChip(0x0101, 2)
    SetChrSubChip(0x0102, 1)
    SetChrPos(0x010E, 59680, 200, -26270, 180)
    SetChrPos(0x0101, 58630, 200, -27770, 90)
    SetChrPos(0x0102, 59690, 200, -28910, 0)
    SetChrFlags(0x0014, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010100480V#009F真是的～\n',
            '不要吓我好不好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100481V教授就不说了，\n',
            '连约修亚也立刻就接上话了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100482V在那一刻我还以为自己\n',
            '真的是忘记了约定好的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100483V#017F哈哈，才不是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100484V#010F逢场作戏这种事情，\n',
            '应该立刻就要想到才行嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100485V#007F哼。\n',
            '理解力不好真是抱歉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100486V#003F自己都没察觉到一件很重要的事情，\n',
            '还说人家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100487V#014F哎……你刚才说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100488V#509F什么都没说～啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100489V#014F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100490V#130F#5P哈哈，真是不好意思。\n',
            '刚才好像让你吃惊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    Sleep(50)

    SetChrSubChip(0x0101, 1)

    ChrTalk(
        0x010E,
        (
            '#0150100491V#130F#5P看见你们好像遇到了点麻烦，\n',
            '就过去帮帮忙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100492V是不是让你感到为难了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100493V#506F啊，没关系。\n',
            '#006F确实遇到了点麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100494V谢谢，亚鲁瓦教授。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100495V#010F刚才真是多亏您出手相救。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100496V#130F#5P没什么没什么。\n',
            '就当作是以前帮助我的还礼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100497V#131F不过……\n',
            '怎么又和军队的人争执起来了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100498V我刚才听见什么恐怖活动之类的话。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100499V#015F最近，好像有一伙犯罪分子\n',
            '伪装成他人发动骚乱和袭击。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100500V看起来……\n',
            '我们大概是被误认为是那伙人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100501V#009F对对，肯定是这样。\n',
            '真是让人火冒三丈啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100502V果然军队里还是蛮横的人多啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100503V#131F#5P啊，还真是不走运呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100504V在『红莲之塔』发生的那件事是绑架事件，\n',
            '这我也听说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100505V对了，那件事情已经解决了吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100506V#006F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100507V虽然从根本上来说还留下不少问题，\n',
            '不过也可以说已经解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100508V#130F#5P啊，真是后生可畏啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100509V第一次见面的时候，\n',
            '我就觉得你们两个肯定能成为\n',
            '会闯出一番事业的游击士呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100510V嗯嗯……\n',
            '看来我没有看走眼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100511V#008F讨、讨厌啦～\n',
            '就算这么夸奖我们，也没有奖励给你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100512V#015F哈哈，我们还在修行中呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100513V#010F话说回来……\n',
            '教授为什么会来这种地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100514V#130F#5P当然是在去王都的途中了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100515V本来想乘坐定期船的，\n',
            '可是又心疼花这点无谓的钱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100516V反正，考古学家的体力就是生命，\n',
            '就当成是锻炼脚力吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100517V#131F……哈哈哈……呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100518V#506F没、没有必要\n',
            '把自己逼到这种地步吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100519V不过，你看起来还是老样子，\n',
            '依旧过着清贫的生活呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100520V#130F#5P文科系学者的钱包都是一样的呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100521V特别是考古学，\n',
            '一得到钱立刻就花在发掘上面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100522V#007F真是没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100523V#006F不过，先不说这个了……\n',
            '能在这里见面还真是有缘啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100524V难得再次相见，\n',
            '教授就和我们一起去王都吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100525V#014F等、等一下，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100526V还不知道亚鲁瓦教授的安排呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100527V#130F#5P我很赞成哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100528V街道上可能会有魔兽，\n',
            '和你们两个在一起能壮胆呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100529V而且从这里到王都距离也不是很远了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100530V#010F这样的话……\n',
            '就请您多多指教了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100531V#001F那么就决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100532V目标王都，我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0102, 0x0004)
    ClearChrFlags(0x010E, 0x0004)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x010E, 65535)
    SetChrPos(0x0101, 61550, 0, -21950, 0)
    SetChrPos(0x0102, 61550, 0, -21950, 0)
    SetChrPos(0x010E, 61550, 0, -21950, 0)
    ClearChrFlags(0x0014, 0x0080)
    CameraMove(61550, 0, -21950, 0)
    CameraSetDistance(2600, 0)
    OP_0D()
    EventEnd(0x00)

    Jump('loc_7817')

    def _loc_7069(): pass

    label('loc_7069')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_7192',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_70E0',
    )

    ChrTalk(
        0x0009,
        (
            '虽然通过这里的人数减少了，\n',
            '不过还有恐怖分子的隐患。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '还是老样子，\n',
            '非常警戒体制还要持续下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_718F')

    def _loc_70E0(): pass

    label('loc_70E0')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0009,
        (
            '观看完武术大会，\n',
            '然后在诞辰庆典之前\n',
            '一直留在王都里的人会有很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然通过这里的人数减少了，\n',
            '不过还有恐怖分子的隐患。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '还是老样子，\n',
            '非常警戒体制还要持续下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_718F(): pass

    label('loc_718F')

    Jump('loc_7817')

    def _loc_7192(): pass

    label('loc_7192')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_71FA',
    )

    ChrTalk(
        0x0009,
        (
            '大会的决赛好像是\n',
            '特务部队和游击士的对阵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '特务部队有那么多强人，\n',
            '应该会获得优胜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7817')

    def _loc_71FA(): pass

    label('loc_71FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_7253',
    )

    ChrTalk(
        0x0009,
        (
            '从今天开始， \n',
            '原定的训练全部停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '与此同时关所\n',
            '处在紧张警戒之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7817')

    def _loc_7253(): pass

    label('loc_7253')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_72AB',
    )

    ChrTalk(
        0x0009,
        (
            '从今天开始终于到了\n',
            '武术大会的正式赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '王国军的选手们\n',
            '也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7817')

    def _loc_72AB(): pass

    label('loc_72AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_73C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_7327',
    )

    ChrTalk(
        0x0009,
        (
            '虽然没有亲眼\n',
            '见到过理查德上校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过看过利贝尔通讯的\n',
            '采访报道之后，\n',
            '我就完全成为他的支持者了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_73C0')

    def _loc_7327(): pass

    label('loc_7327')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0009,
        (
            '虽然没有亲眼\n',
            '见到过理查德上校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过看过利贝尔通讯的\n',
            '采访报道之后，\n',
            '我就完全成为他的支持者了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '他的见解犀利，\n',
            '头脑又好，真是好帅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_73C0(): pass

    label('loc_73C0')

    Jump('loc_7817')

    def _loc_73C3(): pass

    label('loc_73C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_74A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_7434',
    )

    ChrTalk(
        0x0009,
        (
            '最近在艾尔贝周游道\n',
            '好像也有士兵在巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果诞辰庆典上发生恐怖活动，\n',
            '受害会相当大的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_749F')

    def _loc_7434(): pass

    label('loc_7434')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0009,
        (
            '啊，是你们。\n',
            '刚才很抱歉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '通行手续已经办好了，\n',
            '你们可以去王都了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么，祝旅行愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_749F(): pass

    label('loc_749F')

    Jump('loc_7817')

    def _loc_74A2(): pass

    label('loc_74A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_74AC',
    )

    Jump('loc_7817')

    def _loc_74AC(): pass

    label('loc_74AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_74B6',
    )

    Jump('loc_7817')

    def _loc_74B6(): pass

    label('loc_74B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_7556',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_74FE',
    )

    ChrTalk(
        0x0009,
        (
            '直到最后我们也不知道，\n',
            '到底是为了什么而盘查的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7553')

    def _loc_74FE(): pass

    label('loc_74FE')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0009,
        (
            '突然，\n',
            '盘查就下令被解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '犯人明明还没有抓到啊。\n',
            '这到底是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7553(): pass

    label('loc_7553')

    Jump('loc_7817')

    def _loc_7556(): pass

    label('loc_7556')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_7656',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_75C9',
    )

    ChrTalk(
        0x0009,
        (
            '为了抓住恐怖事件的犯人\n',
            '才开始实行盘查的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '对不起，\n',
            '现在不能这么轻易地就发行通行许可证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7653')

    def _loc_75C9(): pass

    label('loc_75C9')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0009,
        (
            '呼，\n',
            '本来今天预定有训练的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过因为发生了恐怖事件，\n',
            '所以进入了紧急状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '对不起，\n',
            '现在不能这么轻易地就发行通行许可证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7653(): pass

    label('loc_7653')

    Jump('loc_7817')

    def _loc_7656(): pass

    label('loc_7656')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_76AE',
    )

    ChrTalk(
        0x0009,
        (
            '哟，\n',
            '欢迎你们来到圣海姆门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '请各位好好体会一下\n',
            '『亚宁堡』的威严哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7817')

    def _loc_76AE(): pass

    label('loc_76AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_7817',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_7780',
    )

    ChrTalk(
        0x0009,
        (
            '这里虽然是负责办理通往王都手续的关所，\n',
            '但同时也是一座历史遗迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '就算在定期船开始运营之后，\n',
            '来参观的人也有很多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为马上就是女王的诞辰庆典了，\n',
            '我想通过这里的人也会变得更多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7817')

    def _loc_7780(): pass

    label('loc_7780')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0009,
        (
            '欢迎来到圣海姆门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里虽然是负责办理通往王都手续的关所，\n',
            '但同时也是一座历史遗迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '就算在定期船开始运营之后，\n',
            '来参观的人也有很多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7817(): pass

    label('loc_7817')

    TalkEnd(0x0009)

    Return()

# id: 0x0018 offset: 0x781B
@scena.Code('func_18_781B')
def func_18_781B():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7877',
    )

    ChrTalk(
        0x0106,
        (
            '#0050100371V#050F这边是格兰赛尔吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050100372V……现在没有去王都的必要呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_794C')

    def _loc_7877(): pass

    label('loc_7877')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_78E9',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100367V#010F前面就是格兰赛尔地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100368V没有通行许可证的话，\n',
            '是不能从这边出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_794C')

    def _loc_78E9(): pass

    label('loc_78E9')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100369V#010F前面就是格兰赛尔地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100368V没有通行许可证的话，\n',
            '是不能从这边出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_794C(): pass

    label('loc_794C')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0019 offset: 0x7968
@scena.Code('func_19_7968')
def func_19_7968():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_79DE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040100533V#030F唔，\n',
            '这边是往蔡斯的出口吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100534V可能什么时候会到那里探访，\n',
            '但现在还不是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7B1F')

    def _loc_79DE(): pass

    label('loc_79DE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A4E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080100535V#073F哦，\n',
            '这边是通往其他地区的出口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080100536V被士兵缠上就麻烦了。\n',
            '还是乖乖地回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7B1F')

    def _loc_7A4E(): pass

    label('loc_7A4E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A64',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_7A6B')

    def _loc_7A64(): pass

    label('loc_7A64')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_7A6B(): pass

    label('loc_7A6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_7ACB',
    )

    ChrTalk(
        0x0102,
        (
            '#0020100537V#012F现在关所被封锁了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100538V士兵们也在巡逻，\n',
            '我们还是早点回去比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7B1F')

    def _loc_7ACB(): pass

    label('loc_7ACB')

    ChrTalk(
        0x0102,
        (
            '#0020100539V#010F这边是蔡斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100540V我们还没取得许可证，\n',
            '是不能从这边出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7B1F(): pass

    label('loc_7B1F')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x001A offset: 0x7B3B
@scena.Code('func_1A_7B3B')
def func_1A_7B3B():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(57670, 5000, 52610, 0)
    SetChrPos(0x0101, 57160, 5000, 52610, 133)
    SetChrPos(0x0102, 58440, 5000, 53220, 189)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7B94',
    )

    SetChrPos(0x0107, 57140, 5000, 51520, 103)

    def _loc_7B94(): pass

    label('loc_7B94')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7BB3',
    )

    SetChrPos(0x0106, 57290, 5000, 53600, 134)

    def _loc_7BB3(): pass

    label('loc_7BB3')

    OP_0D()
    OP_64(0x00, 0x0001)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '发现了一个油纸包。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '里面放着',
            (TxtCtl.SetColor, 0x2),
            '３１棵丝柏树',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0345, 1)
    OP_28(0x0030, 0x01, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010181462V#508F好啊！\n',
            '找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181463V#010F这是最后一本了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181464V图书管理员的任务总算是完成了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181465V#007F是啊，好长的任务啊……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010181466V#004F……………………咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7D23',
    )

    @scena.Lambda('lambda_7D1B')
    def lambda_7D1B():
        ChrTurnDirection(0x0107, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_7D1B)

    def _loc_7D23(): pass

    label('loc_7D23')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181467V#014F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181468V#002F唔，\n',
            '书里面夹着一张卡片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181469V……啊，上面写了些什么东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            '#2130181470V',
            (TxtCtl.SetColor, 0x0),
            '　辛苦你了。\n',
            '　虽然不知道你是谁，\n',
            '　但总算是摸索到这里了。\n',
            '　\n',
            '　简单做一下自我介绍。\n',
            '　我是结晶回路的研究员，\n',
            '　也就是隐藏三本书的犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '#2130181471V',
            (TxtCtl.SetColor, 0x0),
            '　我希望把自己的作品\n',
            '　托付给那些聪明的人们，\n',
            '　这就是为何会出现谜语的原因……\n',
            '　对于你出色的表现，我会给予奖励。\n',
            '　\n',
            '　奖品结晶回路和这封信附在一起。\n',
            '　请注意查收包裹内部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '#2130181472V',
            (TxtCtl.SetColor, 0x0),
            '　那么，就多谢你们的配合了。\n',
            '　我制作的这个结晶回路\n',
            '　一定会对你很有用的。\n',
            '　\n',
            '　另：找到这本书的朋友，\n',
            '　　　还请把它归还到\n',
            '　　　中央工房二楼的资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010181473V#007F………………读完了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181474V#505F呼～\n',
            '这好像不是单纯的恶作剧呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_80C3',
    )

    ChrTurnDirection(0x0107, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_807A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070181475V#060F嗯，好像是～呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181476V#010F要调查一下这个包裹吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_80C0')

    def _loc_807A(): pass

    label('loc_807A')

    ChrTalk(
        0x0107,
        (
            '#0070181477V#060F好像是～呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181476V#010F要调查一下这个包裹吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_80C0(): pass

    label('loc_80C0')

    Jump('loc_80FE')

    def _loc_80C3(): pass

    label('loc_80C3')

    ChrTalk(
        0x0102,
        (
            '#0020181479V#010F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181480V……要调查一下这个包裹吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_80FE(): pass

    label('loc_80FE')

    ChrTalk(
        0x0101,
        (
            '#0010181481V#004F哦，对了，\n',
            '这里面会是……嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '妨碍３',
            (TxtCtl.SetColor, 0x0),
            '的结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010181482V#001F呵呵呵，真的有呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181483V#010F还是拿给委托人确认一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181484V#006F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x02C3, 1)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8223',
    )

    @scena.Lambda('lambda_8214')
    def lambda_8214():
        OP_92(0x0107, 0x0101, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_8214)

    def _loc_8223(): pass

    label('loc_8223')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8246',
    )

    @scena.Lambda('lambda_8237')
    def lambda_8237():
        OP_92(0x0106, 0x0101, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_8237)

    def _loc_8246(): pass

    label('loc_8246')

    OP_92(0x0102, 0x0101, 0, 3000, 0x00)
    EventEnd(0x00)

    Return()

# id: 0x001B offset: 0x8257
@scena.Code('func_1B_8257')
def func_1B_8257():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
