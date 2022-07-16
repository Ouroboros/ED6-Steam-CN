import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '尤莉亚中尉'),
    TXT(0x02, '奈尔'),
    TXT(0x03, '基库'),
    TXT(0x04, '理查德上校'),
    TXT(0x05, '凯诺娜上尉'),
    TXT(0x06, '西蒙'),
    TXT(0x07, '照相机'),
    TXT(0x08, '哈尔德'),
    TXT(0x09, '爱德望'),
    TXT(0x0A, '库莱泽'),
    TXT(0x0B, '萨马里奥'),
    TXT(0x0C, '豆豆'),
    TXT(0x0D, '亲卫队员'),
    TXT(0x0E, '亲卫队员'),
    TXT(0x0F, '亲卫队员'),
    TXT(0x10, '亲卫队员'),
    TXT(0x11, '亲卫队员'),
    TXT(0x12, '亲卫队员'),
    TXT(0x13, '亲卫队员'),
    TXT(0x14, '亲卫队员'),
    TXT(0x15, '亲卫队员'),
    TXT(0x16, '亲卫队员'),
    TXT(0x17, '亲卫队员'),
    TXT(0x18, '亲卫队员'),
    TXT(0x19, '亲卫队员'),
    TXT(0x1A, '亲卫队员'),
    TXT(0x1B, '亲卫队员'),
    TXT(0x1C, '亲卫队员'),
    TXT(0x1D, '　'),
    TXT(0x1E, '　'),
    TXT(0x1F, '卢安市·北街区'),
    TXT(0x20, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2102.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2102._SN', 'ED6_DT01/T2102_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3F0B
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00016F30,
            dword_04        = 0x00000000,
            dword_08        = 0x00013880,
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
        ('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT06/CH20127._CH', 'ED6_DT06/CH20127P._CP'),
        ('ED6_DT06/CH20128._CH', 'ED6_DT06/CH20128P._CP'),
        ('ED6_DT06/CH20129._CH', 'ED6_DT06/CH20129P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 800,
            z                   = 6130,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 47780,
            z                   = 0,
            y                   = 39390,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 47780,
            z                   = 0,
            y                   = 39390,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 111490,
            z                   = 4150,
            y                   = 81190,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 147300,
            z                   = 8200,
            y                   = 95200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 101700,
            z                   = 0,
            y                   = 83800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 134200,
            z                   = 8200,
            y                   = 93000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 140500,
            z                   = 6100,
            y                   = 100500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 126600,
            z                   = 8200,
            y                   = 95200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 134940,
            z                   = 8050,
            y                   = 85090,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 129360,
            z                   = 8050,
            y                   = 85070,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 130139,
            z                   = 8050,
            y                   = 85100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 134140,
            z                   = 8050,
            y                   = 85130,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 133300,
            z                   = 8050,
            y                   = 83500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 133300,
            z                   = 8050,
            y                   = 82200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 133300,
            z                   = 8050,
            y                   = 80900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 133300,
            z                   = 8050,
            y                   = 79600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 132100,
            z                   = 8050,
            y                   = 83500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 132100,
            z                   = 8050,
            y                   = 82200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 132100,
            z                   = 8050,
            y                   = 80900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 132100,
            z                   = 8050,
            y                   = 79600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 130900,
            z                   = 8050,
            y                   = 83500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 130900,
            z                   = 8050,
            y                   = 82200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 130900,
            z                   = 8050,
            y                   = 80900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 130900,
            z                   = 8050,
            y                   = 79600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 71170,
            z                   = 0,
            y                   = 80860,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x4FA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x4FA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x4FA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 114900,
            triggerZ            = 0,
            triggerY            = 101600,
            triggerRange        = 2000,
            actorX              = 114900,
            actorZ              = 1500,
            actorY              = 101600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 100400,
            triggerZ            = 0,
            triggerY            = 83700,
            triggerRange        = 1000,
            actorX              = 101700,
            actorZ              = 1500,
            actorY              = 83800,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 108610,
            triggerZ            = 6150,
            triggerY            = 96910,
            triggerRange        = 800,
            actorX              = 108610,
            actorZ              = 8350,
            actorY              = 96910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 127080,
            triggerZ            = 6150,
            triggerY            = 100740,
            triggerRange        = 800,
            actorX              = 127080,
            actorZ              = 8350,
            actorY              = 100740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 140870,
            triggerZ            = 1000,
            triggerY            = 108000,
            triggerRange        = 800,
            actorX              = 140870,
            actorZ              = 2000,
            actorY              = 108000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 149330,
            triggerZ            = 1000,
            triggerY            = 108000,
            triggerRange        = 800,
            actorX              = 149330,
            actorZ              = 2000,
            actorY              = 108000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 103030,
            triggerZ            = 1000,
            triggerY            = 108000,
            triggerRange        = 800,
            actorX              = 103030,
            actorZ              = 2000,
            actorY              = 108000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 96980,
            triggerZ            = 1000,
            triggerY            = 108000,
            triggerRange        = 800,
            actorX              = 96980,
            actorZ              = 2000,
            actorY              = 108000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x61A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_63A',
    )

    SetChrFlags(0x0013, 0x0010)
    SetChrPos(0x0013, 147500, 8150, 95630, 90)

    Jump('loc_7C9')

    def _loc_63A(): pass

    label('loc_63A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_65A',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0013, 147500, 8150, 95630, 90)

    Jump('loc_7C9')

    def _loc_65A(): pass

    label('loc_65A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_67F',
    )

    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0008)
    SetChrPos(0x0013, 135010, 8150, 94960, 0)

    Jump('loc_7C9')

    def _loc_67F(): pass

    label('loc_67F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_6C1',
    )

    SetChrFlags(0x0011, 0x0010)
    SetChrPos(0x0011, 136900, 6100, 101800, 135)
    SetChrPos(0x0013, 137600, 6100, 99400, 0)
    SetChrPos(0x0012, 139000, 6100, 101400, 270)

    Jump('loc_7C9')

    def _loc_6C1(): pass

    label('loc_6C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_70D',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 96700, 1000, 90100, 270)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 98600, 0, 81460, 45)
    SetChrFlags(0x0011, 0x0010)
    SetChrPos(0x0013, 159290, 0, 107030, 90)

    Jump('loc_7C9')

    def _loc_70D(): pass

    label('loc_70D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_73E',
    )

    SetChrFlags(0x0011, 0x0010)
    SetChrPos(0x0011, 132010, 8360, 93010, 90)
    SetChrPos(0x0013, 132950, 8150, 96370, 180)

    Jump('loc_7C9')

    def _loc_73E(): pass

    label('loc_73E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_76F',
    )

    SetChrFlags(0x0011, 0x0010)
    SetChrPos(0x0011, 129600, 8200, 94200, 0)
    SetChrPos(0x0013, 129600, 8200, 96800, 180)

    Jump('loc_7C9')

    def _loc_76F(): pass

    label('loc_76F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_78A',
    )

    SetChrPos(0x0013, 159290, 0, 107030, 90)

    Jump('loc_7C9')

    def _loc_78A(): pass

    label('loc_78A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_7C9',
    )

    SetChrFlags(0x0011, 0x0010)
    SetChrPos(0x0011, 131500, 8150, 97650, 180)
    SetChrPos(0x0013, 130539, 8150, 96030, 45)
    SetChrPos(0x0012, 132620, 8150, 95740, 315)

    def _loc_7C9(): pass

    label('loc_7C9')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0008)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0010)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7E8',
    )

    OP_64(0x00, 0x0001)

    def _loc_7E8(): pass

    label('loc_7E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_804',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x000A)
    OP_B1('t2102_1')
    OP_71(0x000A, 0x0004)

    def _loc_804(): pass

    label('loc_804')

    Return()

# id: 0x0001 offset: 0x805
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, 20000, -40000, 196681)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_838',
    )

    OP_B1('t2102_y')

    Jump('loc_89A')

    def _loc_838(): pass

    label('loc_838')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 2, 0x412)),
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_850',
    )

    OP_B1('t2102_0')

    Jump('loc_89A')

    def _loc_850(): pass

    label('loc_850')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 1, 0x429)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_868',
    )

    OP_B1('t2102_2')

    Jump('loc_89A')

    def _loc_868(): pass

    label('loc_868')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 2, 0x442)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_880',
    )

    OP_B1('t2102_0')

    Jump('loc_89A')

    def _loc_880(): pass

    label('loc_880')

    OP_B1('t2102_0')
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_6F(0x0007, 100)

    def _loc_89A(): pass

    label('loc_89A')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0008)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0010)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_8B9',
    )

    OP_64(0x00, 0x0001)

    def _loc_8B9(): pass

    label('loc_8B9')

    PlaySE(453, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x8BF
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0000,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_A26')

    def _loc_8E4(): pass

    label('loc_8E4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FD',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_A26')

    def _loc_8FD(): pass

    label('loc_8FD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_916',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_A26')

    def _loc_916(): pass

    label('loc_916')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_92F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_A26')

    def _loc_92F(): pass

    label('loc_92F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_948',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_A26')

    def _loc_948(): pass

    label('loc_948')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_961',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_A26')

    def _loc_961(): pass

    label('loc_961')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_97A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_A26')

    def _loc_97A(): pass

    label('loc_97A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_993',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_A26')

    def _loc_993(): pass

    label('loc_993')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9AC',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_A26')

    def _loc_9AC(): pass

    label('loc_9AC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9C5',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_A26')

    def _loc_9C5(): pass

    label('loc_9C5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9DE',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_A26')

    def _loc_9DE(): pass

    label('loc_9DE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9F7',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_A26')

    def _loc_9F7(): pass

    label('loc_9F7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A10',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_A26')

    def _loc_A10(): pass

    label('loc_A10')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A26',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_A26(): pass

    label('loc_A26')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A3B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_A26')

    def _loc_A3B(): pass

    label('loc_A3B')

    Return()

# id: 0x0003 offset: 0xA3C
@scena.Code('func_03_A3C')
def func_03_A3C():
    TalkBegin(0x0009)

    ChrTalk(
        0x00FE,
        (
            '#0270050979V#140F哟，\n',
            '我准备回格兰赛尔办点事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270050980V现在正在等着看看有没有人来退票。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270050981V等事情办完我会马上回卢安来的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0xACA
@scena.Code('func_04_ACA')
def func_04_ACA():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B69',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哎呀，回到柏斯之后\n',
            '还有一堆事情要等着我去处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '愉快的假期总是那么转瞬即逝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要把心思转回来，\n',
            '不然又要被米拉诺小姐骂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B9E')

    def _loc_B69(): pass

    label('loc_B69')

    ChrTalk(
        0x00FE,
        (
            '哎呀，回到柏斯之后\n',
            '还有一堆事情要等着我去处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B9E(): pass

    label('loc_B9E')

    TalkEnd(0x000D)

    Return()

# id: 0x0005 offset: 0xBA2
@scena.Code('func_05_BA2')
def func_05_BA2():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C09',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '好了……\n',
            '要去办理搭乘手续呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能准时在定期船起飞时上船，\n',
            '那真是万幸啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C2C')

    def _loc_C09(): pass

    label('loc_C09')

    ChrTalk(
        0x00FE,
        (
            '好了……\n',
            '要去办理搭乘手续呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C2C(): pass

    label('loc_C2C')

    TalkEnd(0x000F)

    Return()

# id: 0x0006 offset: 0xC30
@scena.Code('func_06_C30')
def func_06_C30():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_D5A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CF9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0010,
        (
            '市长干了那么多坏事，\n',
            '这我万万没有想到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不过既然已经被逮捕了，\n',
            '这样也就可以了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那样的人如果释放了的话，\n',
            '很可能又会去干坏事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这都是游击士协会的功劳啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D57')

    def _loc_CF9(): pass

    label('loc_CF9')

    ChrTalk(
        0x0010,
        (
            '市长已经被逮捕了，\n',
            '这样就可以了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那样的人如果释放了的话，\n',
            '很可能又会去干坏事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D57(): pass

    label('loc_D57')

    Jump('loc_11ED')

    def _loc_D5A(): pass

    label('loc_D5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_DBA',
    )

    ChrTalk(
        0x0010,
        (
            '飞艇公社的总部\n',
            '设立在王都格兰赛尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '嗯，\n',
            '记得我只在研修的时候去过那里一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11ED')

    def _loc_DBA(): pass

    label('loc_DBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_F02',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EA8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0010,
        (
            '这个空港在建造的时候，\n',
            '大家为了究竟建在城市的北边还是南边\n',
            '这个问题争执了很久呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '店铺和观光设施非常多的北街区\n',
            '从一开始就是最有利的场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '而且，南街区的仓库\n',
            '还聚集了一群不良青年，\n',
            '也不适合在那里兴建吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EFF')

    def _loc_EA8(): pass

    label('loc_EA8')

    ChrTalk(
        0x0010,
        (
            '这个空港在建造的时候，\n',
            '大家为了究竟建在城市的北边还是南边\n',
            '这个问题争执了很久呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()

    def _loc_EFF(): pass

    label('loc_EFF')

    Jump('loc_11ED')

    def _loc_F02(): pass

    label('loc_F02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_F57',
    )

    ChrTalk(
        0x0010,
        (
            '就在刚才，\n',
            '去柏斯的定期船已经飞走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '今天已经没有其他的航班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11ED')

    def _loc_F57(): pass

    label('loc_F57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_FCE',
    )

    ChrTalk(
        0x0010,
        (
            '当天取消的票\n',
            '会卖给先来的客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '如果有很紧急的事情，\n',
            '就算事先没有预约，\n',
            '也不要放弃，要赶快来询问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11ED')

    def _loc_FCE(): pass

    label('loc_FCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_106F',
    )

    ChrTalk(
        0x0010,
        (
            '在预定乘坐飞艇的那天，\n',
            '去南街区的时候要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '开合桥拉升了之后，\n',
            '来不及上飞艇的人可不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '因为这个时候\n',
            '拉桥与飞艇出发的时间重合了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11ED')

    def _loc_106F(): pass

    label('loc_106F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_10CA',
    )

    ChrTalk(
        0x0010,
        (
            '今天的天气真好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不过，不管天气好还是坏，\n',
            '我的干劲可永远都是满满的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11ED')

    def _loc_10CA(): pass

    label('loc_10CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_112C',
    )

    ChrTalk(
        0x0010,
        (
            '来卢安旅游的客人\n',
            '近几年来在急剧增加。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '特地来各个观光地\n',
            '度假休息的人也特别多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11ED')

    def _loc_112C(): pass

    label('loc_112C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_11ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11CA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0010,
        (
            '在定期船停航的时候，\n',
            '我可是忙个不停应付来问讯的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '通航恢复正常的话，\n',
            '我还是一样得忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '算了，\n',
            '反正我越忙就越有干劲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11ED')

    def _loc_11CA(): pass

    label('loc_11CA')

    ChrTalk(
        0x0010,
        (
            '算了，\n',
            '反正我越忙就越有干劲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11ED(): pass

    label('loc_11ED')

    TalkEnd(0x0010)

    Return()

# id: 0x0007 offset: 0x11F1
@scena.Code('func_07_11F1')
def func_07_11F1():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_12F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12B3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '蔡斯的中央工房\n',
            '邀请我去当客座技师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但我还是推辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我而言，\n',
            '技术人员的工作的确非常有吸引力，\n',
            '可我是豆豆的哥哥啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能只为了自己\n',
            '而离开卢安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F4')

    def _loc_12B3(): pass

    label('loc_12B3')

    ChrTalk(
        0x00FE,
        (
            '蔡斯的中央工房\n',
            '邀请我去当客座技师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但我还是推辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12F4(): pass

    label('loc_12F4')

    Jump('loc_1687')

    def _loc_12F7(): pass

    label('loc_12F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_134C',
    )

    ChrTalk(
        0x00FE,
        (
            '本部让我去\n',
            '蔡斯的研究所去上班。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这虽然是件非常值得庆祝的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1687')

    def _loc_134C(): pass

    label('loc_134C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1376',
    )

    ChrTalk(
        0x00FE,
        (
            '好～的，大家休息一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1687')

    def _loc_1376(): pass

    label('loc_1376')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_139E',
    )

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1687')

    def _loc_139E(): pass

    label('loc_139E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_142D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1401',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '这边的机器\n',
            '也差不多该换新的零件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去和总部的技术人员\n',
            '联系一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_142A')

    def _loc_1401(): pass

    label('loc_1401')

    ChrTalk(
        0x00FE,
        (
            '这边的机器\n',
            '也差不多该换新的零件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_142A(): pass

    label('loc_142A')

    Jump('loc_1687')

    def _loc_142D(): pass

    label('loc_142D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_150B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14CB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '听懂了吗？\n',
            '我再说明一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将导力流撞上动翼列，\n',
            '直线的运动能量\n',
            '将转变为回转运动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就是导力引擎的\n',
            '基本原理和构造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0011, 0x0010)

    Jump('loc_1508')

    def _loc_14CB(): pass

    label('loc_14CB')

    ChrTalk(
        0x00FE,
        (
            '豆豆是我唯一的亲人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会竭尽全力\n',
            '做好我能做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1508(): pass

    label('loc_1508')

    Jump('loc_1687')

    def _loc_150B(): pass

    label('loc_150B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_1588',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，桥好像被拉上去了。\n',
            '差不多可以开始整理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '伦格兰德大桥\n',
            '对我们卢安市民来说\n',
            '是具有跨时代意义的建筑物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1687')

    def _loc_1588(): pass

    label('loc_1588')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1687',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1664',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '虽然现在还没什么问题，\n',
            '以防万一，我还是把\n',
            '４号和７号的插座交换一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '与此同时，\n',
            '你也不要忘了检查一下导力压。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '好，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '豆豆去仓库\n',
            '把新的零件拿过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '知、知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0011, 0x0010)

    Jump('loc_1687')

    def _loc_1664(): pass

    label('loc_1664')

    ChrTalk(
        0x00FE,
        (
            '抱歉，\n',
            '现在我们正在讨论工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1687(): pass

    label('loc_1687')

    TalkEnd(0x0011)

    Return()

# id: 0x0008 offset: 0x168B
@scena.Code('func_08_168B')
def func_08_168B():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_16DD',
    )

    ChrTalk(
        0x00FE,
        (
            '如果能够达成一致意见\n',
            '就不会变成现在这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是难办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD6')

    def _loc_16DD(): pass

    label('loc_16DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_174F',
    )

    ChrTalk(
        0x00FE,
        (
            '糟了糟了，\n',
            '我最不擅长应付这种阴沉的气氛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算库莱泽的技术再强，\n',
            '遇到这种问题也很难决断……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD6')

    def _loc_174F(): pass

    label('loc_174F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_17B5',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然维修长不在，\n',
            '但是这个世上是不会允许失败的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要比平时更加严格地\n',
            '进行检查工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD6')

    def _loc_17B5(): pass

    label('loc_17B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_17EA',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～顺利地起飞了，\n',
            '真是松了一口气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD6')

    def _loc_17EA(): pass

    label('loc_17EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_186D',
    )

    ChrTalk(
        0x00FE,
        (
            '我以为刚才来的客人\n',
            '都与往常一样是来\n',
            '劝说库莱泽回本部工作的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是看库莱泽的样子，\n',
            '好像是一件更严重的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD6')

    def _loc_186D(): pass

    label('loc_186D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_18EF',
    )

    ChrTalk(
        0x00FE,
        (
            '我在库莱泽那边\n',
            '碰到了几个从总部来的客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……到底是什么事情\n',
            '我差不多也猜到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，这已是家常便饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD6')

    def _loc_18EF(): pass

    label('loc_18EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1967',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_193F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船过来之前，\n',
            '一定要把设备检查完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1964')

    def _loc_193F(): pass

    label('loc_193F')

    ChrTalk(
        0x00FE,
        (
            '现在要赶快\n',
            '把设备检查完毕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1964(): pass

    label('loc_1964')

    Jump('loc_1AD6')

    def _loc_1967(): pass

    label('loc_1967')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_1AAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A40',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '库莱泽是从蔡斯来的\n',
            '非常有经验的技师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他已经好几次收到调令，\n',
            '让他去总部工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他却以这里离家近的理由\n',
            '一直留在这里工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说这就是他的性格，\n',
            '但是我觉得这样有点不值得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA9')

    def _loc_1A40(): pass

    label('loc_1A40')

    ChrTalk(
        0x00FE,
        (
            '库莱泽他\n',
            '虽然已经好几次收到调令，\n',
            '让他去总部工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他却以这里离家近的理由\n',
            '一直留在这里工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AA9(): pass

    label('loc_1AA9')

    Jump('loc_1AD6')

    def _loc_1AAC(): pass

    label('loc_1AAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1AD6',
    )

    ChrTalk(
        0x00FE,
        (
            '现在我们\n',
            '正在讨论维修的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AD6(): pass

    label('loc_1AD6')

    TalkEnd(0x0012)

    Return()

# id: 0x0009 offset: 0x1ADA
@scena.Code('func_09_1ADA')
def func_09_1ADA():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1B43',
    )

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不是因为我的话，\n',
            '哥哥肯定已经成为\n',
            '新型引擎的研究者了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F68')

    def _loc_1B43(): pass

    label('loc_1B43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1C22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C00',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '虽然哥哥他\n',
            '什么都不跟我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我从爱德望叔叔那里听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有人向哥哥发出邀请，\n',
            '问他是不是愿意去蔡斯\n',
            '做导力引擎的开发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的哥哥\n',
            '果然很厉害呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1F')

    def _loc_1C00(): pass

    label('loc_1C00')

    ChrTalk(
        0x00FE,
        (
            '我的哥哥\n',
            '果然很厉害呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C1F(): pass

    label('loc_1C1F')

    Jump('loc_1F68')

    def _loc_1C22(): pass

    label('loc_1C22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1C4B',
    )

    ChrTalk(
        0x00FE,
        (
            '今天哥哥\n',
            '好像没有去出差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F68')

    def _loc_1C4B(): pass

    label('loc_1C4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1C7E',
    )

    ChrTalk(
        0x00FE,
        (
            '就在刚才，\n',
            '去蔡斯的定期船刚刚飞走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F68')

    def _loc_1C7E(): pass

    label('loc_1C7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1CD7',
    )

    ChrTalk(
        0x00FE,
        (
            '是我的错觉吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天哥哥不知为何\n',
            '有点提不起精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F68')

    def _loc_1CD7(): pass

    label('loc_1CD7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1DAB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D75',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '库莱泽哥哥\n',
            '果然是个很厉害的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '能够在哥哥手下实践学习真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总有一天，\n',
            '我也一定会成为像哥哥这样棒的技师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DA8')

    def _loc_1D75(): pass

    label('loc_1D75')

    ChrTalk(
        0x00FE,
        (
            '总有一天，\n',
            '我也一定会成为像哥哥这样棒的技师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DA8(): pass

    label('loc_1DA8')

    Jump('loc_1F68')

    def _loc_1DAB(): pass

    label('loc_1DAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1E60',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E3C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '库莱泽哥哥\n',
            '开始教我念书了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏了哥哥，\n',
            '我的功课也进步了很多，\n',
            '也变得有自信了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '哥哥就像爸爸一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E5D')

    def _loc_1E3C(): pass

    label('loc_1E3C')

    ChrTalk(
        0x00FE,
        (
            '库莱泽哥哥\n',
            '开始教我念书了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E5D(): pass

    label('loc_1E5D')

    Jump('loc_1F68')

    def _loc_1E60(): pass

    label('loc_1E60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_1F3C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EFC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '只要你的能力得到了\n',
            '蔡斯中央工房的认可，\n',
            '无论年龄大小都能在那里工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要努力磨练我的技术，\n',
            '总有一天在蔡斯工作是我的梦想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F39')

    def _loc_1EFC(): pass

    label('loc_1EFC')

    ChrTalk(
        0x00FE,
        (
            '我也要努力磨练我的技术，\n',
            '总有一天在蔡斯工作是我的梦想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F39(): pass

    label('loc_1F39')

    Jump('loc_1F68')

    def _loc_1F3C(): pass

    label('loc_1F3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1F68',
    )

    ChrTalk(
        0x00FE,
        (
            '我、我正在这里\n',
            '做维修师的实习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F68(): pass

    label('loc_1F68')

    TalkEnd(0x0013)

    Return()

# id: 0x000A offset: 0x1F6C
@scena.Code('func_0A_1F6C')
def func_0A_1F6C():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(132240, 8150, 95810, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    OP_4A(0x0009, 255)
    PlaySE(117, 0x00, 0x64)
    SetChrPos(0x0008, 133220, 8150, 96310, 270)
    SetChrPos(0x0101, 131000, 8150, 96980, 90)
    SetChrPos(0x0102, 130960, 8150, 95770, 90)
    SetChrPos(0x0105, 129930, 8150, 96550, 90)
    SetChrPos(0x0009, 131860, 8150, 98100, 135)
    SetChrPos(0x000A, 133250, 9200, 93100, 315)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0100061791V#178F#5P刚才我们审问了\n',
            '醒过来的戴尔蒙市长……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061792V不过奇怪的是，\n',
            '他好像突然失去了所有记忆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061793V就连纵火抢劫等事件，\n',
            '也似乎只有一点模糊的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061794V#505F这、这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061795V好像跟空贼的首领一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061796V#013F#2P突然失去记忆……\n',
            '这恐怕和那帮黑衣人有关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100061797V#176F#5P不过，就算记忆模糊，\n',
            '所犯下的罪行还是无可狡辩的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061798V当然，他的秘书基尔巴特\n',
            '也会一起受到严厉的审讯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061799V#171F有了调查结果之后，\n',
            '我们也会通知游击士协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061800V#010F#2P那太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061801V#147F对了，中尉大人。\n',
            '我这里有个不情之请。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_227C')
    def lambda_227C():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_227C)

    Sleep(300)

    @scena.Lambda('lambda_228F')
    def lambda_228F():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_228F)

    @scena.Lambda('lambda_229D')
    def lambda_229D():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_229D)

    @scena.Lambda('lambda_22AB')
    def lambda_22AB():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_22AB)

    ChrTalk(
        0x0008,
        (
            '#0100061802V#173F#5P什么事，记者先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061803V#141F如果不麻烦你们的话，\n',
            '能让我也搭乘一下那艘飞艇吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061804V毕竟是蔡斯中央工房研制的\n',
            '最新型飞艇啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061805V所以，恳请您让我上去做个采访。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100061806V#176F#5P非常抱歉，\n',
            '恕我不能答应你的请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061807V#170F这艘『埃尔赛尤号』\n',
            '前几天才刚完成了装配，\n',
            '现在还是处于非公开的试飞阶段之中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061808V在正式举行新闻发布会之前，\n',
            '还请贵社尽量不要做太多的报道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061809V#142F就、就通融一下吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061810V我还想和被逮捕的市长\n',
            '和秘书他们说两句……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100061811V#171F#5P这点你不用担心。调查完结之后，\n',
            '我们自然会把真相告之王都的通讯社。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061812V其他方面就恕我不能帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061813V#145F唉～没办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061814V#144F好吧，只有一条路了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061815V只能写完新闻之后，\n',
            '十万火急赶回王都了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0270061816V#147F那么各位，告辞了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_25B8')
    def lambda_25B8():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_25B8')

    DispatchAsync2(0x0008, 0x0001, lambda_25B8)

    @scena.Lambda('lambda_25C9')
    def lambda_25C9():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_25C9')

    DispatchAsync2(0x0101, 0x0001, lambda_25C9)

    @scena.Lambda('lambda_25DA')
    def lambda_25DA():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_25DA')

    DispatchAsync2(0x0102, 0x0001, lambda_25DA)

    @scena.Lambda('lambda_25EB')
    def lambda_25EB():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_25EB')

    DispatchAsync2(0x0105, 0x0001, lambda_25EB)

    SetChrDirection(0x0009, 90, 400)
    ChrWalkTo(0x0009, 134850, 8150, 99540, 5000, 0x00)
    ChrWalkTo(0x0009, 134900, 8150, 100980, 5000, 0x00)
    ChrWalkTo(0x0009, 126260, 6150, 101260, 5000, 0x00)
    SetChrFlags(0x0009, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010061817V#506F还是老样子，\n',
            '该说他干劲强呢，还是执念强呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061818V#019F#2P哈哈……\n',
            '不过这才是奈尔先生的风格啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100061819V#178F#5P听说《利贝尔通讯》的发行量\n',
            '最近在直线上升。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061820V我只是希望他能写出\n',
            '不被政治宣传所束缚的新闻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2735')
    def lambda_2735():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2735)

    @scena.Lambda('lambda_2743')
    def lambda_2743():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2743)

    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061821V#014F政治宣传……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0100061822V#175F#5P没什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000B, 0x0040)
    SetChrPos(0x000B, 126260, 6150, 101260, 90)
    SetChrPos(0x000C, 126260, 6150, 101260, 90)

    NpcTalk(
        0x000B,
        '男性的声音',
        (
            '#0130061823V#5P看来你立了一功啊。\n',
            '舒华兹中尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_2877')
    def lambda_2877():
        CameraMove(132920, 8150, 97630, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2877)

    @scena.Lambda('lambda_288F')
    def lambda_288F():
        OP_6C(45000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_288F)

    @scena.Lambda('lambda_289F')
    def lambda_289F():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_289F')

    DispatchAsync2(0x0008, 0x0001, lambda_289F)

    @scena.Lambda('lambda_28B0')
    def lambda_28B0():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_28B0')

    DispatchAsync2(0x0101, 0x0001, lambda_28B0)

    @scena.Lambda('lambda_28C1')
    def lambda_28C1():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_28C1')

    DispatchAsync2(0x0102, 0x0001, lambda_28C1)

    @scena.Lambda('lambda_28D2')
    def lambda_28D2():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_28D2')

    DispatchAsync2(0x0105, 0x0001, lambda_28D2)

    CreateThread(0x000B, 0x01, 0x00, 0x000B)
    Sleep(500)

    CreateThread(0x000C, 0x01, 0x00, 0x000C)
    WaitForThreadExit(0x000B, 0x0001)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0100061824V#173F这、这不是上校吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061825V#004F#6P啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061826V#014F理查德上校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0130061827V#113F哦，你们是上次的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130061828V#110F原来如此，协会发来的联络中\n',
            '所提到的游击士新人就是你们两位啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061829V#004F#6P咦……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061830V嘉恩哥哥联络的\n',
            '原来就是理查德上校啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0130061831V#110F嗯，王国军司令部所在的\n',
            '雷斯顿要塞收到了协会的联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130061832V我急急忙忙赶来一看，\n',
            '原来事情已经结束了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130061833V做得真漂亮，舒华兹中尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100061834V#176F不，您过奖了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610061835V#182F呵呵，不过还真不可思议啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610061836V想不到身在王都的亲卫队\n',
            '竟然会跑来这种地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610061837V看来，你们有着连我们情报部\n',
            '都还没掌握的独特情报网啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100061838V#175F您、您说笑了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061839V#047F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0130061840V#111F哈哈，凯诺娜上尉。\n',
            '这点我们也没必要深究了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130061841V#115F不过，负责守护陛下的亲卫队\n',
            '为其他琐事分神也并不是什么好事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130061842V#110F后面的调查由我们接手，\n',
            '而犯人就移交到雷斯顿要塞吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130061843V我们会代表王国军\n',
            '对市长他们进行严厉的审讯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100061844V#178F是……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0130061845V#111F那我们这就告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130061846V舒华兹中尉、各位游击士，\n',
            '还有那位穿校服的小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061847V#040F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0130061848V#115F……有机会再见吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130061849V#110F那么，告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610061850V#182F呵呵，多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    SetChrDirection(0x000B, 135, 400)
    CreateThread(0x000B, 0x01, 0x00, 0x000D)
    Sleep(600)

    SetChrDirection(0x000C, 135, 400)
    CreateThread(0x000C, 0x01, 0x00, 0x000D)
    WaitForThreadExit(0x000C, 0x0001)

    @scena.Lambda('lambda_2E0C')
    def lambda_2E0C():
        CameraMove(131910, 8150, 96570, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E0C)

    SetChrDirection(0x0101, 225, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010061851V#505F#1P可能是我多心了，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061852V刚才，理查德上校\n',
            '似乎一直在往科洛丝那边看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E91')
    def lambda_2E91():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2E91)

    @scena.Lambda('lambda_2E9F')
    def lambda_2E9F():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2E9F)

    ChrTurnDirection(0x0105, 0x0008, 400)

    ChrTalk(
        0x0105,
        (
            '#0060061853V#542F是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061854V#015F#2P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061855V#010F我也觉得是。\n',
            '像你这样的学生\n',
            '出现在这种场合并不寻常啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061856V他会觉得奇怪也是难免的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061857V#045F啊、啊哈哈……\n',
            '那也的确是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061858V我该反省一下了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061859V#007F#1P唔，不过我的感觉\n',
            '也不完全是你们说的那样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100061860V#176F……让我来说的话，\n',
            '你们的成绩也足够让人吃惊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3029')
    def lambda_3029():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3029)

    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0100061861V#171F就算是游击士，\n',
            '但这么年轻就能有如此的本领……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061862V可以的话，真想把你们招进亲卫队啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061863V#506F#1P没、没有啦～\n',
            '您就别这么抬举我们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061864V能解决这次的事件，\n',
            '也是因为多亏了很多人的帮助啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100061865V#170F不用这么谦虚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061866V你们似乎还是准游击士，\n',
            '打算进级成为正游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061867V#008F#1P嗯，是呢。\n',
            '现在正为了这目标而修行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061868V#010F我们打算在女王的诞辰庆典之前\n',
            '环游整个利贝尔王国一周。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100061869V#170F是吗……\n',
            '我支持你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#2690061870V#1P尤莉亚队长！\n',
            '出航准备完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0014, 400)

    ChrTalk(
        0x0008,
        (
            '#0100061871V#170F好，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0100061872V#170F艾丝蒂尔、约修亚。\n',
            '……还有科洛丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061873V我们这就要告辞了。\n',
            '有机会再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061874V#006F嗯，好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061875V#010F到时还请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061876V#048F……真的谢谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, 0x000E)

    @scena.Lambda('lambda_338E')
    def lambda_338E():
        OP_6C(224000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_338E)

    @scena.Lambda('lambda_339E')
    def lambda_339E():
        CameraMove(132040, 8960, 87760, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_339E)

    @scena.Lambda('lambda_33B6')
    def lambda_33B6():
        CameraSetDistance(3680, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_33B6)

    @scena.Lambda('lambda_33C6')
    def lambda_33C6():
        OP_67(0, 5440, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_33C6)

    Sleep(1000)

    @scena.Lambda('lambda_33E3')
    def lambda_33E3():
        ChrWalkTo(0x00FE, 132800, 8150, 94880, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_33E3)

    @scena.Lambda('lambda_33FE')
    def lambda_33FE():
        ChrWalkTo(0x00FE, 131540, 8150, 94710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_33FE)

    @scena.Lambda('lambda_3419')
    def lambda_3419():
        ChrWalkTo(0x00FE, 132180, 8150, 95760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3419)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrDirection(0x0101, 180, 400)
    WaitForThreadExit(0x0105, 0x0001)
    SetChrDirection(0x0105, 180, 400)
    WaitForThreadExit(0x0102, 0x0002)
    WaitForThreadExit(0x0008, 0x0000)
    SetChrChipByIndex(0x0008, 13)
    Sleep(100)

    OP_99(0x0008, 0x00, 0x01, 1200)

    ChrTalk(
        0x0008,
        (
            '#0100061877V#177F全体队员，敬礼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1F(0x50, 0x000001F4)
    PlaySE(152, 0x00, 0x64)

    @scena.Lambda('lambda_34A2')
    def lambda_34A2():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_34A2')

    DispatchAsync2(0x0014, 0x0000, lambda_34A2)

    @scena.Lambda('lambda_34B5')
    def lambda_34B5():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_34B5')

    DispatchAsync2(0x0015, 0x0000, lambda_34B5)

    @scena.Lambda('lambda_34C8')
    def lambda_34C8():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_34C8')

    DispatchAsync2(0x0016, 0x0000, lambda_34C8)

    @scena.Lambda('lambda_34DB')
    def lambda_34DB():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_34DB')

    DispatchAsync2(0x0017, 0x0000, lambda_34DB)

    SetChrChipByIndex(0x0018, 11)
    SetChrChipByIndex(0x001C, 11)
    SetChrChipByIndex(0x0020, 11)
    Sleep(100)

    SetChrChipByIndex(0x0019, 11)
    SetChrChipByIndex(0x001D, 11)
    SetChrChipByIndex(0x0021, 11)
    Sleep(100)

    SetChrChipByIndex(0x001A, 11)
    SetChrChipByIndex(0x001E, 11)
    SetChrChipByIndex(0x0022, 11)
    Sleep(100)

    SetChrChipByIndex(0x001B, 11)
    SetChrChipByIndex(0x001F, 11)
    SetChrChipByIndex(0x0023, 11)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010061878V#004F哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3556')
    def lambda_3556():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3556')

    DispatchAsync2(0x0102, 0x0001, lambda_3556)

    @scena.Lambda('lambda_3567')
    def lambda_3567():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3567')

    DispatchAsync2(0x0105, 0x0001, lambda_3567)

    @scena.Lambda('lambda_3578')
    def lambda_3578():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3578')

    DispatchAsync2(0x0101, 0x0001, lambda_3578)

    ChrTalk(
        0x0008,
        (
            '#0100061879V#172F王室亲卫队所属舰，\n',
            '『埃尔赛尤号』——起飞！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(3000)
    CameraMove(159890, 6490, 81650, 0)
    OP_67(0, 6210, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(388, 0)
    OP_6F(0x0007, 100)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    SetChrFlags(0x0020, 0x0080)
    SetChrFlags(0x0021, 0x0080)
    SetChrFlags(0x0022, 0x0080)
    SetChrFlags(0x0023, 0x0080)
    SetChrPos(0x0024, 138000, 6550, 81800, 90)
    SetChrPos(0x0025, 138000, 1200, 81800, 90)
    OP_A1(0x0024, 0x0008)
    OP_72(0x0008, 0x0004)
    OP_72(0x0008, 0x0020)
    SetChrFlags(0x0024, 0x0004)
    OP_A1(0x0025, 0x0009)
    OP_72(0x0009, 0x0004)
    SetChrFlags(0x0025, 0x0004)

    @scena.Lambda('lambda_36AE')
    def lambda_36AE():
        CameraMove(129389, 10000, 81550, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_36AE)

    Sleep(2000)

    PlaySE(119, 0x00, 0x64)
    OP_6F(0x0008, 1)
    OP_70(0x0008, 150)
    OP_73(0x0004)
    OP_6F(0x0008, 150)
    OP_70(0x0008, 330)
    CreateThread(0x0024, 0x03, 0x00, 0x000F)

    @scena.Lambda('lambda_36F6')
    def lambda_36F6():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_36F6)

    @scena.Lambda('lambda_3706')
    def lambda_3706():
        OP_67(0, 7850, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_3706)

    ChrMoveToRelativeAsync(0x0024, 0, 500, 0, 400, 0x00)
    ChrMoveToRelativeAsync(0x0024, 0, 1000, 0, 800, 0x00)
    ChrMoveToRelativeAsync(0x0024, 0, 2000, 0, 1600, 0x00)
    ChrMoveToRelativeAsync(0x0024, 0, 500, 0, 800, 0x00)
    ChrMoveToRelativeAsync(0x0024, 0, 400, 0, 400, 0x00)
    OP_73(0x0008)
    OP_71(0x0008, 0x0020)
    OP_6F(0x0008, 330)
    OP_70(0x0008, 430)

    @scena.Lambda('lambda_3798')
    def lambda_3798():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_3798)

    @scena.Lambda('lambda_37AE')
    def lambda_37AE():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_37AE)

    Sleep(200)

    @scena.Lambda('lambda_37C9')
    def lambda_37C9():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_37C9)

    @scena.Lambda('lambda_37DF')
    def lambda_37DF():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_37DF)

    Sleep(200)

    @scena.Lambda('lambda_37FA')
    def lambda_37FA():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_37FA)

    @scena.Lambda('lambda_3810')
    def lambda_3810():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_3810)

    Sleep(200)

    @scena.Lambda('lambda_382B')
    def lambda_382B():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_382B)

    @scena.Lambda('lambda_3841')
    def lambda_3841():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_3841)

    Sleep(200)

    @scena.Lambda('lambda_385C')
    def lambda_385C():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_385C)

    @scena.Lambda('lambda_3872')
    def lambda_3872():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_3872)

    Sleep(200)

    @scena.Lambda('lambda_388D')
    def lambda_388D():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_388D)

    @scena.Lambda('lambda_38A3')
    def lambda_38A3():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_38A3)

    Sleep(200)

    @scena.Lambda('lambda_38BE')
    def lambda_38BE():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_38BE)

    @scena.Lambda('lambda_38D4')
    def lambda_38D4():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_38D4)

    Sleep(200)

    @scena.Lambda('lambda_38EF')
    def lambda_38EF():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_38EF)

    @scena.Lambda('lambda_3905')
    def lambda_3905():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_3905)

    Sleep(200)

    @scena.Lambda('lambda_3920')
    def lambda_3920():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00002328, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_3920)

    @scena.Lambda('lambda_3936')
    def lambda_3936():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00002328, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_3936)

    Sleep(200)

    @scena.Lambda('lambda_3951')
    def lambda_3951():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_3951)

    @scena.Lambda('lambda_3967')
    def lambda_3967():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_3967)

    Sleep(200)

    @scena.Lambda('lambda_3982')
    def lambda_3982():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00002EE0, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_3982)

    @scena.Lambda('lambda_3998')
    def lambda_3998():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00002EE0, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_3998)

    Sleep(200)

    @scena.Lambda('lambda_39B3')
    def lambda_39B3():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000036B0, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_39B3)

    @scena.Lambda('lambda_39C9')
    def lambda_39C9():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000036B0, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_39C9)

    Sleep(2800)

    OP_24(0x0077, 0x5A)
    OP_24(0x0075, 0x5A)
    Sleep(100)

    OP_24(0x0077, 0x50)
    OP_24(0x0075, 0x50)
    Sleep(100)

    OP_24(0x0077, 0x46)
    OP_24(0x0075, 0x46)
    Sleep(100)

    OP_24(0x0077, 0x3C)
    OP_24(0x0075, 0x3C)
    Sleep(100)

    OP_24(0x0077, 0x32)
    OP_24(0x0075, 0x32)
    Sleep(100)

    OP_24(0x0077, 0x28)
    OP_24(0x0075, 0x28)
    Sleep(100)

    OP_24(0x0077, 0x1E)
    OP_24(0x0075, 0x1E)
    Sleep(100)

    OP_23(0x0077)
    OP_23(0x0075)
    OP_1F(0x64, 0x000001F4)
    Fade(1000)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0024, 0xFF)
    TerminateThread(0x0025, 0xFF)
    SetChrFlags(0x0024, 0x0080)
    SetChrFlags(0x0025, 0x0080)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    CameraMove(132060, 8150, 94520, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2840, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0105, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010061880V#506F哇～一边敬礼，\n',
            '一边吹起喇叭……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061881V简直是压倒性的震撼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061882V#019F是啊……\n',
            '飞艇也是最新型的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061883V不愧是保护女王陛下安全的\n',
            '精英部队啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061884V#041F呵呵，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010061885V#501F不过尤莉亚中尉\n',
            '不愧是一个巾帼英雄啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061886V#001F感觉就像科洛丝扮演的\n',
            '苍骑士奥斯卡那样帅气呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061887V#040F我也有这种感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061888V#041F呵呵，真是有趣的巧合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0440061889V#311F#1P啾～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2120._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x3C7A
@scena.Code('func_0B_3C7A')
def func_0B_3C7A():
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 134900, 8150, 100980, 3000, 0x00)
    ChrWalkTo(0x00FE, 134830, 8150, 99690, 3000, 0x00)
    ChrWalkTo(0x00FE, 133570, 8150, 98310, 3000, 0x00)
    SetChrDirection(0x00FE, 225, 400)

    Return()

# id: 0x000C offset: 0x3CC3
@scena.Code('func_0C_3CC3')
def func_0C_3CC3():
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 134900, 8150, 100980, 3000, 0x00)
    ChrWalkTo(0x00FE, 134500, 8150, 98250, 3000, 0x00)
    SetChrDirection(0x00FE, 225, 400)

    Return()

# id: 0x000D offset: 0x3CF8
@scena.Code('func_0D_3CF8')
def func_0D_3CF8():
    ChrWalkTo(0x00FE, 134830, 8150, 99690, 3000, 0x00)
    ChrWalkTo(0x00FE, 134900, 8150, 100980, 3000, 0x00)
    ChrWalkTo(0x00FE, 126260, 6150, 101260, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x000E offset: 0x3D3A
@scena.Code('func_0E_3D3A')
def func_0E_3D3A():
    ChrWalkTo(0x00FE, 132200, 8150, 94800, 3000, 0x00)
    ChrWalkTo(0x00FE, 132140, 8150, 85930, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 132070, 8050, 85140, 3000, 0x00)
    SetChrDirection(0x0008, 0, 400)

    Return()

# id: 0x000F offset: 0x3D83
@scena.Code('func_0F_3D83')
def func_0F_3D83():
    OP_6F(0x0008, 150)
    OP_70(0x0008, 250)
    OP_73(0x0008)
    PlaySE(221, 0x00, 0x64)
    OP_6F(0x0008, 251)
    OP_70(0x0008, 265)
    OP_73(0x0008)
    PlaySE(221, 0x00, 0x64)
    OP_6F(0x0008, 266)
    OP_70(0x0008, 287)
    OP_73(0x0008)
    PlaySE(221, 0x00, 0x64)
    OP_6F(0x0008, 288)
    OP_70(0x0008, 330)

    Return()

# id: 0x0010 offset: 0x3DD4
@scena.Code('func_10_3DD4')
def func_10_3DD4():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船起降坪\n',
            '≡　开往柏斯市\n',
            '≡　开往蔡斯市',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0011 offset: 0x3E31
@scena.Code('func_11_3E31')
def func_11_3E31():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　　利贝尔飞艇公社',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0012 offset: 0x3E95
@scena.Code('func_12_3E95')
def func_12_3E95():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
