import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0700_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0700   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0700.x'
    header.mapIndex       = 9
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01440._CH', 'ED6_DT07/CH01440P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿兰',
            x                   = 36100,
            z                   = 0,
            y                   = 35620,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '凯文神父',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '赛希莉亚号',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '赛希莉亚号影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '赛希莉亚号',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '桥',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '斯库拉特',
            x                   = 44350,
            z                   = 4000,
            y                   = 39550,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '法布利',
            x                   = 31840,
            z                   = 0,
            y                   = 51530,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '提克',
            x                   = 39680,
            z                   = 4000,
            y                   = 35470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '莫莉',
            x                   = 39680,
            z                   = 4000,
            y                   = 36730,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 36520,
            z                   = 0,
            y                   = 33790,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 37790,
            z                   = 0,
            y                   = 32820,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 35870,
            z                   = 0,
            y                   = 32330,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '戴恩副队长',
            x                   = 34280,
            z                   = 0,
            y                   = 30400,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '古兰托机长',
            x                   = 43580,
            z                   = 4000,
            y                   = 30220,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '乘务员卡拉莉丝',
            x                   = 44340,
            z                   = 4000,
            y                   = 35280,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '乘务员迪蒙',
            x                   = 42290,
            z                   = 4000,
            y                   = 31720,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 45360,
            z                   = 4000,
            y                   = 54040,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '利库斯',
            x                   = 45360,
            z                   = 4000,
            y                   = 55190,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '林德号的乘客',
            x                   = 36820,
            z                   = 0,
            y                   = 27490,
            direction           = 360,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '林德号的乘客',
            x                   = 33120,
            z                   = 0,
            y                   = 30640,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '洛连特市街区',
            x                   = 35320,
            z                   = 0,
            y                   = -13920,
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

# id: 0x10002 offset: 0x56A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x56A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x56A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 36142,
            triggerZ            = 0,
            triggerY            = 34342,
            triggerRange        = 1000,
            actorX              = 36095,
            actorZ              = 1500,
            actorY              = 35619,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 38000,
            triggerZ            = 0,
            triggerY            = 30000,
            triggerRange        = 800,
            actorX              = 38000,
            actorZ              = 2200,
            actorY              = 30000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0026,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 40000,
            triggerZ            = 4000,
            triggerY            = 41300,
            triggerRange        = 800,
            actorX              = 40000,
            actorZ              = 5500,
            actorY              = 41800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0027,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 34500,
            triggerZ            = 0,
            triggerY            = 46570,
            triggerRange        = 800,
            actorX              = 35000,
            actorZ              = 1500,
            actorY              = 46570,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0028,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x5FA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_618',
    )

    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0028, 0x0080)

    Jump('loc_6C7')

    def _loc_618(): pass

    label('loc_618')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_622',
    )

    Jump('loc_6C7')

    def _loc_622(): pass

    label('loc_622')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_66B',
    )

    ChrSetPos(0x001B, 42670, 4000, 39780, 90)
    CreateThread(0x001B, 0x00, 0x00, func_02_7FA)
    ChrSetPos(0x0014, 43140, 4000, 38650, 45)
    ChrSetPos(0x001A, 44350, 4000, 39550, 270)
    ChrClearFlags(0x0021, 0x0080)

    Jump('loc_6C7')

    def _loc_66B(): pass

    label('loc_66B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_69F',
    )

    ChrClearFlags(0x001C, 0x0080)
    ChrSetPos(0x001C, 36940, 0, 31150, 0)
    ChrSetFlags(0x0014, 0x0010)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)

    Jump('loc_6C7')

    def _loc_69F(): pass

    label('loc_69F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_6C7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 2, 0x189A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B3',
    )

    ChrSetFlags(0x0014, 0x0010)

    def _loc_6B3(): pass

    label('loc_6B3')

    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)

    def _loc_6C7(): pass

    label('loc_6C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_6E6',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_18_3798)

    Jump('loc_6F7')

    def _loc_6E6(): pass

    label('loc_6E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F7',
    )

    MapSetFlags(0x10000000)
    Event(0, func_15_2F47)

    def _loc_6F7(): pass

    label('loc_6F7')

    Return()

# id: 0x0001 offset: 0x6F8
@scena.Code('func_01_6F8')
def func_01_6F8():
    OP_16(0x02, 4000, -92000, -97000, 2293767)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_74C',
    )

    OP_B5(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_737',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)

    Jump('loc_74C')

    def _loc_737(): pass

    label('loc_737')

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 80000, 0)

    def _loc_74C(): pass

    label('loc_74C')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_77B',
    )

    OP_A1(0x0018, 0x000B)
    ChrSetPos(0x0018, 56000, -3075, 35200, 0)
    OP_72(0x000B, 0x0004)
    OP_71(0x000D, 0x0004)

    Jump('loc_7E4')

    def _loc_77B(): pass

    label('loc_77B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_794',
    )

    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)

    Jump('loc_7E4')

    def _loc_794(): pass

    label('loc_794')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_7E4',
    )

    OP_71(0x000B, 0x0004)
    OP_72(0x000F, 0x0004)
    OP_A1(0x0018, 0x000F)
    ChrSetPos(0x0018, 56000, -3075, 35200, 0)
    OP_72(0x000C, 0x0004)
    OP_A1(0x0017, 0x000C)
    ChrSetPos(0x0017, 55800, -3070, 35000, 0)
    OP_6F(0x000F, 1)
    OP_70(0x000F, 1)

    def _loc_7E4(): pass

    label('loc_7E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_7EE',
    )

    Jump('loc_7F9')

    def _loc_7EE(): pass

    label('loc_7EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_7F9',
    )

    OP_64(0x00, 0x0001)

    def _loc_7F9(): pass

    label('loc_7F9')

    Return()

# id: 0x0002 offset: 0x7FA
@scena.Code('func_02_7FA')
def func_02_7FA():
    ExecExpressionWithReg(
        0x0001,
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
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_81F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_961')

    def _loc_81F(): pass

    label('loc_81F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_838',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_961')

    def _loc_838(): pass

    label('loc_838')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_851',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_961')

    def _loc_851(): pass

    label('loc_851')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_86A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_961')

    def _loc_86A(): pass

    label('loc_86A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_883',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_961')

    def _loc_883(): pass

    label('loc_883')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_89C',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_961')

    def _loc_89C(): pass

    label('loc_89C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B5',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_961')

    def _loc_8B5(): pass

    label('loc_8B5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8CE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_961')

    def _loc_8CE(): pass

    label('loc_8CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E7',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_961')

    def _loc_8E7(): pass

    label('loc_8E7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_900',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_961')

    def _loc_900(): pass

    label('loc_900')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_919',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_961')

    def _loc_919(): pass

    label('loc_919')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_932',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_961')

    def _loc_932(): pass

    label('loc_932')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_94B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_961')

    def _loc_94B(): pass

    label('loc_94B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_961',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_961(): pass

    label('loc_961')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_976',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_961')

    def _loc_976(): pass

    label('loc_976')

    Return()

# id: 0x0003 offset: 0x977
@scena.Code('func_03_977')
def func_03_977():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_99A',
    )

    OP_8D(0x00FE, 29021, 54795, 33637, 48557, 2000)

    Jump('func_03_977')

    def _loc_99A(): pass

    label('loc_99A')

    Return()

# id: 0x0004 offset: 0x99B
@scena.Code('func_04_99B')
def func_04_99B():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x9A0
@scena.Code('func_05_9A0')
def func_05_9A0():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_E58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 7, 0x20A7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B99',
    )

    ChrTalk(
        0x0014,
        (
            '呀，艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '怎么，回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F阿兰也\n',
            '还和以前一样，没什么变化啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0102, 400)

    ChrTalk(
        0x0014,
        (
            '很有精神嘛！\n',
            '本来是想这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '但定期船再这么停航下去的话，\n',
            '实在让人受不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对客人解释原因\n',
            '也是阿兰的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1035F确实是个麻烦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '嗯，确实\n',
            '很棘手…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '世界上最痛苦的事情\n',
            '就是没有女孩子可以欣赏！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '啊啊！！那可是我\n',
            '唯一的乐趣啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#1048F完、完全没变啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0414, 7, 0x20A7))

    Jump('loc_E55')

    def _loc_B99(): pass

    label('loc_B99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_BFD',
    )

    ChrTalk(
        0x0014,
        (
            '虽然向客人解释很累，\n',
            '但要是没有客人就更累。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '欣赏漂亮女孩\n',
            '是我在这里的唯一乐趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E55')

    def _loc_BFD(): pass

    label('loc_BFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_D4D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CF0',
    )

    ChrTalk(
        0x0014,
        (
            '虽然维修员做过检查，\n',
            '但却没有发现任何异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '这种时候唯一的精神安慰\n',
            '就是看漂亮女孩了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F（阿兰还是和平时一样……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '啊、那里的女孩…\n',
            '还蛮可爱的啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '……嗯，不过只能给７８分。\n',
            '毕竟不是很完美。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_D4A')

    def _loc_CF0(): pass

    label('loc_CF0')

    ChrTalk(
        0x0014,
        (
            '那边的女孩……\n',
            '还算可爱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '……嗯，不过只能给７８分。\n',
            '这种程度还是不能满足我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D4A(): pass

    label('loc_D4A')

    Jump('loc_E55')

    def _loc_D4D(): pass

    label('loc_D4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E05',
    )

    ChrTalk(
        0x0014,
        (
            '现在停在飞船坪的是\n',
            '『林德号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '在起飞前往王都之前\n',
            '发生了那种现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '确保客人们的住宿，\n',
            '也费了不少力气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '最近总发生意外事件，\n',
            '公社这边快忙不过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_E55')

    def _loc_E05(): pass

    label('loc_E05')

    ChrTalk(
        0x0014,
        (
            '现在停在飞船坪的是\n',
            '『林德号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '因为异变无法出航，\n',
            '大家都要挤在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E55(): pass

    label('loc_E55')

    Jump('loc_19C6')

    def _loc_E58(): pass

    label('loc_E58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E6B',
    )

    Call(0, 0x0020)

    Jump('loc_19C6')

    def _loc_E6B(): pass

    label('loc_E6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_F2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_EC2',
    )

    ChrTalk(
        0x0014,
        (
            '我也打算过一阵子\n',
            '就回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '在这种大雾之下\n',
            '根本没法工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F2C')

    def _loc_EC2(): pass

    label('loc_EC2')

    ChrTalk(
        0x0014,
        (
            '上午来的客人\n',
            '总算是回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '我也打算过一阵子\n',
            '就回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '在这种大雾之下\n',
            '根本没法工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_F2C(): pass

    label('loc_F2C')

    Jump('loc_19C6')

    def _loc_F2F(): pass

    label('loc_F2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_FF2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_F7B',
    )

    ChrTalk(
        0x0014,
        (
            '恢复航行的时间\n',
            '还是没有决定下来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '十、十分抱歉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FEF')

    def _loc_F7B(): pass

    label('loc_F7B')

    ChrTalk(
        0x0014,
        (
            '十、十分抱歉！\n',
            '定期船还没有恢复正常！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '请、请各位\n',
            '再耐心等等！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '我代表飞船公社\n',
            '向大家诚恳道歉！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_FEF(): pass

    label('loc_FEF')

    Jump('loc_19C6')

    def _loc_FF2(): pass

    label('loc_FF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_17F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 2, 0x189A)),
            Expr.Return,
        ),
        'loc_10B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1060',
    )

    ChrTalk(
        0x0014,
        (
            '王立学院的制服\n',
            '果然看多少次也不腻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '呀～～不能输给大雾，\n',
            '我也要努力工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B6')

    def _loc_1060(): pass

    label('loc_1060')

    ChrTalk(
        0x0014,
        (
            '定期船停运的话，\n',
            '也就没有女孩子可以欣赏了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '……嗯～讨厌。\n',
            '这可是大问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10B6(): pass

    label('loc_10B6')

    Jump('loc_17F5')

    def _loc_10B9(): pass

    label('loc_10B9')

    ChrTalk(
        0x0014,
        (
            '……７２分、８０分、７５分……\n',
            '呼～今天的质量很一般嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_127A',
    )

    OP_62(0x0014, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0014, 0x0105, 400)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '嗯嗯、那长袜还有',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '清纯的白色裙子…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '噢噢！！这、这不就是\n',
            '杰尼丝王立学院的制服吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '还有完全配得上制服\n',
            '的出众气质！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '太、太完美了！！！\n',
            '绝对可以给１００分！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#542F那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F好啦，科洛丝都被你吓到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1019F……你还是一点也没变啊，阿兰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1685')

    def _loc_127A(): pass

    label('loc_127A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1293',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1358')

    def _loc_1293(): pass

    label('loc_1293')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12AC',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1358')

    def _loc_12AC(): pass

    label('loc_12AC')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12C5',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1358')

    def _loc_12C5(): pass

    label('loc_12C5')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12DE',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1358')

    def _loc_12DE(): pass

    label('loc_12DE')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12F7',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1358')

    def _loc_12F7(): pass

    label('loc_12F7')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1310',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1358')

    def _loc_1310(): pass

    label('loc_1310')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1329',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1358')

    def _loc_1329(): pass

    label('loc_1329')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1342',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1358')

    def _loc_1342(): pass

    label('loc_1342')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1358',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1358(): pass

    label('loc_1358')

    Switch(
        (
            (Expr.PushReg, 0x4),
            Expr.Return,
        ),
        (0x00000002, 'loc_136D'),
        (0x00000006, 'loc_1466'),
        (0x00000000, 'loc_1599'),
        (-1, 'loc_1685'),
    )

    def _loc_136D(): pass

    label('loc_136D')

    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0014, 0x0103, 400)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '噢噢！这种大胆的装扮……\n',
            '充满魔性吸引力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '还有魅惑力十足\n',
            '却不低俗的气质。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '可以给９７分！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#526F哎呀，不是１００分吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '哈哈，哪有那么简单就给满分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F你还是一点也没变啊，阿兰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1685')

    def _loc_1466(): pass

    label('loc_1466')

    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0014, 0x0107, 400)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '嗯，那金色的头发，\n',
            '还有让人可以联想到夏日海洋的眼睛…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '虽然还没有发育完全，\n',
            '不过确实有种说不出的魅力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '嗯，现在可以打８０分，\n',
            '不过将来还是很有发展前途的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#065F啊、啊啊啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F好啦！提妲都\n',
            '被你吓到了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1019F你还是一点也没变啊，阿兰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1685')

    def _loc_1599(): pass

    label('loc_1599')

    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0014, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '啊、这修长的美腿……\n',
            '清纯的服装……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '虽然欠缺女人的魅力，\n',
            '但这也正是年轻女孩的健康美啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '嗯，这样的话，可以给９０分！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1019F你还是一点也没变啊，阿兰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1685')

    def _loc_1685(): pass

    label('loc_1685')

    ChrTurnDirection(0x0014, 0x0101, 400)

    ChrTalk(
        0x0014,
        (
            '呀，欢迎回家，艾丝蒂尔。\n',
            '很有潜力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '嗯，成长下去的话，\n',
            '将来一定会更完美的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F你还有力气说这种轻浮的话吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '定期船停运了，\n',
            '现在的状况可是很紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '哈哈哈～\n',
            '别这么说嘛，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '这也是保持工作\n',
            '精力的秘诀之一呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '不过，这雾\n',
            '还真是讨厌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '拜它所赐，\n',
            '一个女孩也看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F……最后总算是安定下来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0313, 2, 0x189A))
    ChrClearFlags(0x0014, 0x0010)
    def _loc_17F5(): pass

    label('loc_17F5')

    Jump('loc_19C6')

    def _loc_17F8(): pass

    label('loc_17F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_19C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 7, 0x1027)),
            Expr.Return,
        ),
        'loc_1861',
    )

    ChrTalk(
        0x0014,
        (
            '参加女王诞辰庆典的人们\n',
            '也终于都安顿下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '洛连特又回到\n',
            '平时的正常生活了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C6')

    def _loc_1861(): pass

    label('loc_1861')

    ChrTalk(
        0x0014,
        (
            '……９０分、７０分、８４分……\n',
            '呼呼～今天还算不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0014, 0x0101, 400)
    Sleep(600)

    ChrTalk(
        0x0014,
        (
            '啊、栗色头发……\n',
            '还有那清澈的眼神……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '虽然充满活力，\n',
            '但还是缺少女性的魅力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '嗯，给８２分好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#509F……谁是８２分啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '……什么啊，仔细一看，\n',
            '这不是艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '好久不见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F你在说什么啊，\n',
            '还真是一点都没变呢，阿兰……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0204, 7, 0x1027))

    def _loc_19C6(): pass

    label('loc_19C6')

    TalkEnd(0x0014)

    Return()

# id: 0x0006 offset: 0x19CA
@scena.Code('func_06_19CA')
def func_06_19CA():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1A27',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然已经检查过好几次，\n',
            '但哪里也没发现异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然原因还是\n',
            '因为异变吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF2')

    def _loc_1A27(): pass

    label('loc_1A27')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1A76',
    )

    ChrTalk(
        0x00FE,
        (
            '引擎没问题，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也没有发现其他什么异常……\n',
            '究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF2')

    def _loc_1A76(): pass

    label('loc_1A76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1AC9',
    )

    ChrTalk(
        0x00FE,
        (
            '乘船手续已经办好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要想乘坐定期船的话，\n',
            '就来这里办手续吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF2')

    def _loc_1AC9(): pass

    label('loc_1AC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1B24',
    )

    ChrTalk(
        0x00FE,
        (
            '本以为今天雾就会散去了，\n',
            '都打算准备开始工作了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，看来还是不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF2')

    def _loc_1B24(): pass

    label('loc_1B24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1B93',
    )

    ChrTalk(
        0x00FE,
        (
            '林德号\n',
            '在洛连特之外的４座城市\n',
            '往返飞行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的飞行方式，\n',
            '自之前的空贼事件之后可是首次啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF2')

    def _loc_1B93(): pass

    label('loc_1B93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_1CA1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1BFC',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才的着陆\n',
            '真是吓了我一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能在那种状况下成功着陆，\n',
            '佩特洛夫船长真了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C9E')

    def _loc_1BFC(): pass

    label('loc_1BFC')

    ChrTalk(
        0x00FE,
        (
            '呼～定期船的着陆\n',
            '真是吓了我一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然进行了引导，\n',
            '但毕竟视线实在太差了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能在那种状况下成功着陆，\n',
            '佩特洛夫船长真了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是很危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1C9E(): pass

    label('loc_1C9E')

    Jump('loc_1CF2')

    def _loc_1CA1(): pass

    label('loc_1CA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_1CF2',
    )

    ChrTalk(
        0x00FE,
        (
            '王都来的林德号\n',
            '就要到达了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了避免发生事故，\n',
            '要好好准备一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CF2(): pass

    label('loc_1CF2')

    TalkEnd(0x001A)

    Return()

# id: 0x0007 offset: 0x1CF6
@scena.Code('func_07_1CF6')
def func_07_1CF6():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1DF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D9A',
    )

    ChrTalk(
        0x00FE,
        (
            '听说军队的警备艇\n',
            '也在附近迫降了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力停止现象\n',
            '发生在整个王国…\n',
            '看来传闻果然是真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个怎么办才好，\n',
            '难道我们要失业了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_1DF0')

    def _loc_1D9A(): pass

    label('loc_1D9A')

    ChrTalk(
        0x00FE,
        (
            '听说军队的警备艇\n',
            '也在附近迫降了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种现象似乎真的\n',
            '已经覆盖到整个王国了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DF0(): pass

    label('loc_1DF0')

    Jump('loc_218B')

    def _loc_1DF3(): pass

    label('loc_1DF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1EBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E69',
    )

    ChrTalk(
        0x00FE,
        (
            '可恶…\n',
            '到底是哪里出了问题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『林德号』的装置部分\n',
            '很正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其他零件也\n',
            '没有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_1EB7')

    def _loc_1E69(): pass

    label('loc_1E69')

    ChrTalk(
        0x00FE,
        (
            '可恶…\n',
            '究竟是哪里出了问题呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么『林德号』\n',
            '的引擎无法运转了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EB7(): pass

    label('loc_1EB7')

    Jump('loc_218B')

    def _loc_1EBA(): pass

    label('loc_1EBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1F7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1F0B',
    )

    ChrTalk(
        0x00FE,
        (
            '赛希莉亚号\n',
            '似乎也是一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是因为\n',
            '引擎过热了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F79')

    def _loc_1F0B(): pass

    label('loc_1F0B')

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，航行终于再开始了，\n',
            '接下来又要忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赛希莉亚号\n',
            '似乎也是一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也要努力\n',
            '起飞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1F79(): pass

    label('loc_1F79')

    Jump('loc_218B')

    def _loc_1F7C(): pass

    label('loc_1F7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1FE0',
    )

    ChrTalk(
        0x00FE,
        (
            '赛希莉亚号\n',
            '已经准备完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雾如果还是那么厉害的话，\n',
            '今天也准备撤销出航计划了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_218B')

    def _loc_1FE0(): pass

    label('loc_1FE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2021',
    )

    ChrTalk(
        0x00FE,
        (
            '阿兰那里也很忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一直要向乘客们\n',
            '拼命解释啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_218B')

    def _loc_2021(): pass

    label('loc_2021')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2134',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2084',
    )

    ChrTalk(
        0x00FE,
        (
            '管制塔、我们整备屋、\n',
            '还有定期船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有三者协力\n',
            '才能让飞船坪正常运营。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2131')

    def _loc_2084(): pass

    label('loc_2084')

    ChrTalk(
        0x00FE,
        (
            '定期船的着陆\n',
            '需要大家齐心协力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '管制塔、我们整备屋、\n',
            '还有定期船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样的话，\n',
            '工作就可以顺利完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有我们完美配合的话，\n',
            '很难在这种恶劣条件下着陆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_2131(): pass

    label('loc_2131')

    Jump('loc_218B')

    def _loc_2134(): pass

    label('loc_2134')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_218B',
    )

    ChrTalk(
        0x00FE,
        (
            '想看一看传闻中\n',
            '王室的埃尔赛尤号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，它一般也不会\n',
            '在洛连特着陆的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_218B(): pass

    label('loc_218B')

    TalkEnd(0x001B)

    Return()

# id: 0x0008 offset: 0x218F
@scena.Code('func_08_218F')
def func_08_218F():
    TalkBegin(0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_21E5',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船今天还是不行吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天的雾那么大，\n',
            '这也是没办法的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2248')

    def _loc_21E5(): pass

    label('loc_21E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2248',
    )

    ChrTalk(
        0x00FE,
        (
            '真是让人没办法啊……\n',
            '即使降落在洛连特也很麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～本来还要去哈肯大门\n',
            '参观呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2248(): pass

    label('loc_2248')

    TalkEnd(0x001C)

    Return()

# id: 0x0009 offset: 0x224C
@scena.Code('func_09_224C')
def func_09_224C():
    TalkBegin(0x001D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_234C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_22B0',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然在洛连特\n',
            '也有想去的地方…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但雾这么大，摄影旅行的话\n',
            '根本不可能啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234C')

    def _loc_22B0(): pass

    label('loc_22B0')

    ChrTalk(
        0x00FE,
        (
            '虽然在洛连特\n',
            '也有想去的地方…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但雾这么大，摄影旅行的话\n',
            '根本不可能啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但要一直只在旅馆休息的话，\n',
            '未免太让人不爽了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯、真头疼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_234C(): pass

    label('loc_234C')

    TalkEnd(0x001D)

    Return()

# id: 0x000A offset: 0x2350
@scena.Code('func_0A_2350')
def func_0A_2350():
    UnlockAchievement(0x01, 0x0009, 0x00)
    TalkBegin(0x0025)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_23AB',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，本来是想\n',
            '要去柏斯的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连、连自然现象\n',
            '都要妨碍我的人生吗？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23AB(): pass

    label('loc_23AB')

    TalkEnd(0x0025)

    Return()

# id: 0x000B offset: 0x23AF
@scena.Code('func_0B_23AF')
def func_0B_23AF():
    TalkBegin(0x0026)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_248B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_240F',
    )

    ChrTalk(
        0x00FE,
        (
            '安敦…\n',
            '怨天尤人是没有用的喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，先去协会\n',
            '试着商谈一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_248B')

    def _loc_240F(): pass

    label('loc_240F')

    ChrTalk(
        0x00FE,
        (
            '安敦…\n',
            '怨天尤人是没有用的喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，先去协会\n',
            '试着商谈一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果可能的话，\n',
            '也许可以走陆路去柏斯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_248B(): pass

    label('loc_248B')

    TalkEnd(0x0026)

    Return()

# id: 0x000C offset: 0x248F
@scena.Code('func_0C_248F')
def func_0C_248F():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_24C6',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，真麻烦啊。\n',
            '定期船还没有恢复正常吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24C6(): pass

    label('loc_24C6')

    TalkEnd(0x001E)

    Return()

# id: 0x000D offset: 0x24CA
@scena.Code('func_0D_24CA')
def func_0D_24CA():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_25BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_252B',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船看起来还是不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，在城里随便看看，\n',
            '然后再回旅馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25BB')

    def _loc_252B(): pass

    label('loc_252B')

    ChrTalk(
        0x00FE,
        (
            '定期船看起来还是不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，死心了、\n',
            '回旅馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，不过在那之前\n',
            '还是想在城里逛逛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许会找到不错\n',
            '的店也说不定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_25BB(): pass

    label('loc_25BB')

    TalkEnd(0x001F)

    Return()

# id: 0x000E offset: 0x25BF
@scena.Code('func_0E_25BF')
def func_0E_25BF():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_263B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_25F4',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，死心了，\n',
            '今天也不行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_263B')

    def _loc_25F4(): pass

    label('loc_25F4')

    ChrTalk(
        0x00FE,
        (
            '唉，死心了，\n',
            '今天也不行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～还要再和妻子\n',
            '联络一次啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_263B(): pass

    label('loc_263B')

    TalkEnd(0x0020)

    Return()

# id: 0x000F offset: 0x263F
@scena.Code('func_0F_263F')
def func_0F_263F():
    TalkBegin(0x0021)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_272B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_26A7',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，飞船的乘客\n',
            '也增多了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然明白您的心情，\n',
            '不过现在还是先待在旅馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_272B')

    def _loc_26A7(): pass

    label('loc_26A7')

    ChrTalk(
        0x00FE,
        (
            '嗯，飞船的乘客\n',
            '也增多了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然明白您的心情，\n',
            '不过现在还是先待在旅馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '轻易外出的话，\n',
            '警备工作的负担会加重的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_272B(): pass

    label('loc_272B')

    TalkEnd(0x0021)

    Return()

# id: 0x0010 offset: 0x272F
@scena.Code('func_10_272F')
def func_10_272F():
    TalkBegin(0x0022)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_2890',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2802',
    )

    ChrTalk(
        0x00FE,
        (
            '对引擎进行了检查，\n',
            '没发现任何毛病。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是全国性质\n',
            '的大异变啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '失去导力的话，\n',
            '我们就不能再次飞行了，\n',
            '只能在陆地上行走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知从何时开始，\n',
            '我们似乎就忘记了自身的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_288D')

    def _loc_2802(): pass

    label('loc_2802')

    ChrTalk(
        0x00FE,
        (
            '失去导力之后\n',
            '我们就变得不知所措。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…不但无法在天空飞行，\n',
            '连在陆地上行走都有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我们自身的能力\n',
            '本来不就是如此的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_288D(): pass

    label('loc_288D')

    Jump('loc_29B3')

    def _loc_2890(): pass

    label('loc_2890')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_29B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2951',
    )

    ChrTalk(
        0x00FE,
        (
            '导力引擎为什么无法发动，\n',
            '原因还在调查中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有家人的成员很着急地\n',
            '回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力突然消失，\n',
            '对我们来说完全是未知现象啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '解决这些异变\n',
            '大概还要花些时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_29B3')

    def _loc_2951(): pass

    label('loc_2951')

    ChrTalk(
        0x00FE,
        (
            '导力引擎为什么无法发动，\n',
            '原因还在调查中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算原因解明了，\n',
            '重新恢复航运也需要一些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29B3(): pass

    label('loc_29B3')

    TalkEnd(0x0022)

    Return()

# id: 0x0011 offset: 0x29B7
@scena.Code('func_11_29B7')
def func_11_29B7():
    TalkBegin(0x0023)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_2A45',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船的恢复工作\n',
            '现在还没有头绪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很遗憾，\n',
            '但也是没有办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '引擎为什么停止运转，\n',
            '其原因现在还不得而知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B47')

    def _loc_2A45(): pass

    label('loc_2A45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2B47',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AEA',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然航行停止\n',
            '给客人们带来不少麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但至少没有人员伤亡，\n',
            '就算是幸运的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是在起飞后\n',
            '引擎才停止运转…\n',
            '那后果就不堪设想了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_2B47')

    def _loc_2AEA(): pass

    label('loc_2AEA')

    ChrTalk(
        0x00FE,
        (
            '总之，客人们\n',
            '就算是幸运的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是在起飞后\n',
            '引擎才停止运转…\n',
            '那后果就不堪设想了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B47(): pass

    label('loc_2B47')

    TalkEnd(0x0023)

    Return()

# id: 0x0012 offset: 0x2B4B
@scena.Code('func_12_2B4B')
def func_12_2B4B():
    TalkBegin(0x0024)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_2BB4',
    )

    ChrTalk(
        0x00FE,
        (
            '船上也没有\n',
            '发现什么异常啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '整备屋的人真可怜，\n',
            '……大家全都一筹莫展，抱头呻吟着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D09')

    def _loc_2BB4(): pass

    label('loc_2BB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2D09',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CA4',
    )

    ChrTalk(
        0x00FE,
        (
            '真奇怪…\n',
            '这样的情况还是第一次见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一般情况下，出现故障\n',
            '之前都会有相应的反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比如装置部分异常加热、\n',
            '船体振动之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但这次却没有发生\n',
            '任何不正常的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是太突然了。\n',
            '突然之间，引擎就停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_2D09')

    def _loc_2CA4(): pass

    label('loc_2CA4')

    ChrTalk(
        0x00FE,
        (
            '这次的故障完全\n',
            '没有任何前兆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我当时也是\n',
            '完全不敢相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出力针的指数\n',
            '瞬间就滑到了０。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D09(): pass

    label('loc_2D09')

    TalkEnd(0x0024)

    Return()

# id: 0x0013 offset: 0x2D0D
@scena.Code('func_13_2D0D')
def func_13_2D0D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_2E09',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D8D',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，可也不能\n',
            '一直待在洛连特呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然也想过走陆路\n',
            '回去，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～果然还是太麻烦了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_2E06')

    def _loc_2D8D(): pass

    label('loc_2D8D')

    ChrTalk(
        0x00FE,
        (
            '啊，可是走陆路回去的话\n',
            '还是太危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是遇到魔兽的话…\n',
            '后悔也来不及了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以还是老老实实\n',
            '等飞船恢复吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E06(): pass

    label('loc_2E06')

    Jump('loc_2E47')

    def _loc_2E09(): pass

    label('loc_2E09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2E47',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～今天\n',
            '飞船还是不行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，早已经想到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E47(): pass

    label('loc_2E47')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x2E4B
@scena.Code('func_14_2E4B')
def func_14_2E4B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_2EC5',
    )

    ChrTalk(
        0x00FE,
        (
            '恢复时间还不知道。\n',
            '故障的原因也不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种话\n',
            '我也会说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些工作人员\n',
            '真的在认真工作吗？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F43')

    def _loc_2EC5(): pass

    label('loc_2EC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2F43',
    )

    ChrTalk(
        0x00FE,
        (
            '那种不负责任的话\n',
            '真是听够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪怕是说谎也好，\n',
            '我也希望听到一些明确的答复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那？明白了吧？\n',
            '我想说的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F43(): pass

    label('loc_2F43')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x2F47
@scena.Code('func_15_2F47')
def func_15_2F47():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    MapClearFlags(0x00000001)
    OP_11(0xA4, 0xB7, 0xFF, 43000, 300000, 0)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_72(0x000F, 0x0004)
    OP_72(0x000C, 0x0004)
    OP_A1(0x0018, 0x000F)
    ChrSetPos(0x0018, 55700, -300, 35000, 0)
    OP_A1(0x0017, 0x000C)
    ChrSetPos(0x0017, 55800, -1000, 35000, 0)
    ChrSetFlags(0x0018, 0x0004)
    ChrSetFlags(0x0017, 0x0004)
    MapClearFlags(0x02000000)
    CameraMove(47960, 26950, 30490, 0)
    OP_67(0, 27020, -10000, 0)
    CameraSetDistance(2480, 0)
    OP_6C(62000, 0)
    OP_6E(262, 0)
    PlaySE(121, 0x00, 0x64)
    OP_C8(0x0200, 0x0046, 'C_PLAC00._CH', 0x01, 0x0BB8)
    ShowPlaceName('洛连特')
    FadeIn(3000, 0)
    OP_6F(0x000D, 200)
    OP_70(0x000D, 200)
    OP_12(0x0000A7F8, 0x0003D090, 0x00002710)

    @scena.Lambda('lambda_3040')
    def lambda_3040():
        CameraMove(53380, 4050, 31110, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3040)

    @scena.Lambda('lambda_3058')
    def lambda_3058():
        OP_67(0, 9500, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3058)

    @scena.Lambda('lambda_3070')
    def lambda_3070():
        CameraSetDistance(3300, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3070)

    @scena.Lambda('lambda_3080')
    def lambda_3080():
        OP_6C(65000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3080)

    @scena.Lambda('lambda_3090')
    def lambda_3090():
        ChrMoveToRelativeAsync(0x00FE, 0, -3007, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0000, lambda_3090)

    @scena.Lambda('lambda_30AB')
    def lambda_30AB():
        ChrMoveToRelativeAsync(0x00FE, 0, -2007, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_30AB)

    OP_6F(0x000F, 130)
    WaitForThreadExit(0x0018, 0x0000)
    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 200, 3000, 300)
    Sleep(1000)

    OP_B0(0x000F, 0x32)
    OP_6F(0x000F, 130)
    OP_70(0x000F, 1)
    Sleep(900)

    PlaySE(118, 0x00, 0x46)
    OP_73(0x000F)
    Sleep(400)

    PlaySE(120, 0x00, 0x64)
    OP_B0(0x000D, 0x64)
    OP_6F(0x000D, 200)
    OP_70(0x000D, 0)
    OP_73(0x000D)
    Sleep(1000)

    PlaySE(6, 0x00, 0x64)
    OP_6F(0x000F, 411)
    OP_70(0x000F, 450)
    PlaySE(6, 0x00, 0x64)
    OP_73(0x000F)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, func_16_36E6)
    CreateThread(0x0009, 0x01, 0x00, func_17_3745)
    Sleep(1000)

    CreateThread(0x000A, 0x01, 0x00, func_16_36E6)
    Sleep(1000)

    CreateThread(0x000B, 0x01, 0x00, func_16_36E6)
    CreateThread(0x000C, 0x01, 0x00, func_17_3745)
    Sleep(500)

    CreateThread(0x000D, 0x01, 0x00, func_16_36E6)
    Sleep(1000)

    CreateThread(0x000E, 0x01, 0x00, func_17_3745)
    Sleep(500)

    Sleep(1000)

    CreateThread(0x000F, 0x01, 0x00, func_16_36E6)
    Sleep(3000)

    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0015, 0x0040)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0015, 0x0004)
    ChrSetBattleFlags(0x0101, 0x0020)
    ChrSetBattleFlags(0x0015, 0x0020)
    Yield()
    OP_89(0x0101, 55990, 4230, 34970, 6)
    OP_89(0x0015, 55990, 4230, 34970, 6)

    @scena.Lambda('lambda_31F9')
    def lambda_31F9():
        ChrWalkTo(0x0101, 55520, 4130, 31980, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_31F9)

    Sleep(1000)

    @scena.Lambda('lambda_3219')
    def lambda_3219():
        ChrWalkTo(0x0015, 55730, 4130, 33030, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0000, lambda_3219)

    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_3239')
    def lambda_3239():
        ChrWalkTo(0x0101, 52520, 4130, 30950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3239)

    WaitForThreadExit(0x0015, 0x0000)

    @scena.Lambda('lambda_3259')
    def lambda_3259():
        ChrWalkTo(0x0015, 52520, 4130, 30950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0000, lambda_3259)

    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_3279')
    def lambda_3279():
        ChrWalkTo(0x0101, 42070, 4000, 31310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3279)

    WaitForThreadExit(0x0015, 0x0000)

    @scena.Lambda('lambda_3299')
    def lambda_3299():
        ChrWalkTo(0x0015, 43430, 4000, 30970, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0000, lambda_3299)

    ChrClearFlags(0x0101, 0x0004)
    Sleep(1000)

    ChrClearFlags(0x0015, 0x0004)
    Sleep(1000)

    Fade(500)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    CameraMove(42990, 4000, 31290, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(57000, 0)
    OP_6E(200, 0)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0015, 0x0000)
    OP_0D()
    Sleep(500)

    ChrSetDirection(0x0015, 225, 500)
    Sleep(500)

    ChrTalk(
        0x0015,
        (
            '#0180190265V#1061F哈～这里就是洛连特吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190266V呵呵，老实说，\n',
            '飞船坪之外的地方简直就像是乡村啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 120, 500)

    ChrTalk(
        0x0101,
        (
            '#0010190267V#007F#3P不好意思啊，本来就是乡村城镇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190268V#509F不过事先告诉你，\n',
            '这里也是有礼拜堂的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0015, 270, 500)

    ChrTalk(
        0x0015,
        (
            '#0180190269V#1062F那、那过一会儿我去和\n',
            '教区长打个招呼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190270V对了，艾丝蒂尔的家\n',
            '在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190271V#505F#3P都说了嘛……\n',
            '没必要送我回家了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190272V出城之后走一会儿就可以到。\n',
            '而且，毕竟我也是个游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0180190273V#1061F哈哈～～不用客气啊，\n',
            '送女士回家也是男人的义务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190274V#1060F而且我也好想见见\n',
            '你那位引以为傲的男朋友呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190275V#503F#3P男朋友……\n',
            '也不能说是男朋友啦…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190276V#008F呼！不管了！！\n',
            '那就先到我家喝杯茶吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0180190277V#1061FＴｈａｎｋ　ｙｏｕ！\n',
            '那就请带路吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    OP_72(0x000A, 0x0004)
    CameraMove(42190, 4000, 31180, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FormationAddMember(ChrTable['凯文神父2'], 0xFF, 0xFF)
    ChrSetPos(0x0101, 42190, 4000, 31180, 0)
    ChrSetPos(0x0142, 42190, 4000, 31180, 0)
    SetScenaFlags(ScenaFlag(0x0200, 3, 0x1003))
    ChrClearFlags(0x0101, 0x0002)
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0101, 0x0004)
    ChrSetFlags(0x0015, 0x0080)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x36E6
@scena.Code('func_16_36E6')
def func_16_36E6():
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 55680, 3890, 35740, 0)
    ChrWalkTo(0x00FE, 55750, 4190, 31070, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)
    ChrMoveTo(0x00FE, 43530, 3930, 30320, 2000, 0x00)
    Sleep(2000)

    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0017 offset: 0x3745
@scena.Code('func_17_3745')
def func_17_3745():
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 52970, 4293, 42260, 357)
    ChrWalkTo(0x00FE, 52990, 4130, 31490, 2000, 0x00)
    ChrWalkTo(0x00FE, 43040, 4000, 31350, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0018 offset: 0x3798
@scena.Code('func_18_3798')
def func_18_3798():
    EventBegin(0x00)
    OP_DB()
    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 80000, 0)
    CameraMove(51650, -3070, 39040, 0)
    OP_67(0, 16810, -10000, 0)
    CameraSetDistance(3130, 0)
    OP_6C(135000, 0)
    OP_6E(540, 0)
    ChrSetFlags(0x0000, 0x0080)
    OP_72(0x000F, 0x0020)
    OP_72(0x000C, 0x0004)
    OP_6F(0x000F, 60)
    OP_70(0x000F, 60)
    OP_6F(0x000E, 0)
    OP_6F(0x000D, 200)
    ChrSetFlags(0x0018, 0x0004)
    ChrSetFlags(0x0017, 0x0004)
    OP_A1(0x0018, 0x000F)
    ChrSetPos(0x0018, 55800, 15000, 35000, 0)
    OP_A1(0x0017, 0x000C)
    ChrSetPos(0x0017, 55800, 10000, 35000, 0)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['阿加特'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xF9, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFC, 0xFF)
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0000, 0x0020)
    OP_71(0x0001, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_71(0x0003, 0x0020)
    OP_71(0x0004, 0x0020)
    OP_71(0x0005, 0x0020)
    OP_71(0x0007, 0x0020)
    OP_71(0x0008, 0x0020)
    OP_71(0x0009, 0x0020)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 720)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 720)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 720)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 720)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 720)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 720)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 720)
    OP_6F(0x0008, 0)
    OP_70(0x0008, 720)
    OP_6F(0x0009, 0)
    OP_70(0x0009, 720)

    @scena.Lambda('lambda_391C')
    def lambda_391C():
        CameraMove(51760, -3070, 40830, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_391C)

    @scena.Lambda('lambda_3934')
    def lambda_3934():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3934)

    @scena.Lambda('lambda_3944')
    def lambda_3944():
        ChrMoveTo(0x00FE, 55800, -3000, 35000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_3944)

    @scena.Lambda('lambda_395F')
    def lambda_395F():
        ChrMoveTo(0x00FE, 55800, 0, 35000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_395F)

    OP_C8(0x0200, 0x0046, 'C_PLAC00._CH', 0x01, 0x03E8)
    ShowPlaceName('洛连特')
    FadeIn(1000, 0)
    PlaySE(226, 0x00, 0x64)
    WaitForThreadExit(0x0018, 0x0001)

    @scena.Lambda('lambda_39AA')
    def lambda_39AA():
        ChrMoveTo(0x00FE, 55800, -1000, 35000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_39AA)

    WaitForThreadExit(0x0018, 0x0001)

    @scena.Lambda('lambda_39CA')
    def lambda_39CA():
        ChrMoveTo(0x00FE, 55800, -3000, 35000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_39CA)

    WaitForThreadExit(0x0018, 0x0001)
    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 200, 3000, 300)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(118, 0x00, 0x46)
    OP_B0(0x000F, 0x3C)
    OP_6F(0x000F, 60)
    OP_70(0x000F, 1)
    OP_73(0x000F)
    PlaySE(120, 0x00, 0x64)
    OP_B0(0x000D, 0x64)
    OP_6F(0x000D, 200)
    OP_70(0x000D, 0)
    OP_73(0x000D)
    Sleep(1000)

    OP_23(0x0079)
    Fade(1000)
    CameraMove(55840, 4200, 32009, 0)
    OP_67(0, 7250, -10000, 0)
    CameraSetDistance(2940, 0)
    OP_6C(29000, 0)
    OP_6E(262, 0)
    OP_0D()
    PlaySE(6, 0x00, 0x64)
    OP_6F(0x000F, 411)
    OP_70(0x000F, 450)
    OP_73(0x000F)
    CreateThread(0x0101, 0x00, 0x00, func_19_3E1A)
    Sleep(500)

    CreateThread(0x0107, 0x00, 0x00, func_1C_3F43)
    Sleep(300)

    CreateThread(0x0106, 0x00, 0x00, func_1B_3EE0)
    Sleep(500)

    CreateThread(0x0103, 0x00, 0x00, func_1A_3E7D)
    Sleep(500)

    CreateThread(0x0104, 0x00, 0x00, func_1D_3F9F)
    Sleep(500)

    CreateThread(0x0105, 0x00, 0x00, func_1E_4002)
    Sleep(500)

    CreateThread(0x0108, 0x00, 0x00, func_1F_4065)
    Sleep(500)

    WaitForThreadExit(0x0108, 0x0000)
    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010280700V#1020F哇……一片白啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070280701V#065F#6P啊……\n',
            '什么都看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060280702V#043F#1P雾散去之前，\n',
            '定期船是无法出航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030231269V#026F#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030280704V#020F#2P那么我们就在这里下船，\n',
            '然后去协会一趟吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C06')
    def lambda_3C06():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_3C06)

    Sleep(50)

    @scena.Lambda('lambda_3C19')
    def lambda_3C19():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0000, lambda_3C19)

    Sleep(50)

    @scena.Lambda('lambda_3C2C')
    def lambda_3C2C():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0000, lambda_3C2C)

    Sleep(400)

    ChrTalk(
        0x0106,
        (
            '#0050280705V#051F#2P啊啊，说的对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C67')
    def lambda_3C67():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3C67)

    Sleep(50)

    @scena.Lambda('lambda_3C7A')
    def lambda_3C7A():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_3C7A)

    Sleep(50)

    @scena.Lambda('lambda_3C8D')
    def lambda_3C8D():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0000, lambda_3C8D)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010280706V#1004F唉……为、为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280707V#074F#2P连你们这些当地人\n',
            '都这么惊讶的浓雾…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280708V#072F很可能又是『结社』\n',
            '搞出来的勾当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210161V#1026F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040280710V#035F#2P呼……\n',
            '剩下的地区只有柏斯和洛连特了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280711V#030F看来他们下一个目标不是柏斯，\n',
            '而是洛连特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_AD('ED6_DT24/C_VIS144._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    FadeOut(0, 0, -1)
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0121._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x3E1A
@scena.Code('func_19_3E1A')
def func_19_3E1A():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 55890, 4230, 35050, 0)

    @scena.Lambda('lambda_3E41')
    def lambda_3E41():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3E41)

    ChrWalkTo(0x00FE, 56010, 4230, 33450, 2000, 0x00)
    ChrWalkTo(0x00FE, 53480, 4130, 31320, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x001A offset: 0x3E7D
@scena.Code('func_1A_3E7D')
def func_1A_3E7D():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 55890, 4230, 35050, 0)

    @scena.Lambda('lambda_3EA4')
    def lambda_3EA4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3EA4)

    ChrWalkTo(0x00FE, 56010, 4230, 33450, 2000, 0x00)
    ChrWalkTo(0x00FE, 55610, 4130, 31730, 2000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x001B offset: 0x3EE0
@scena.Code('func_1B_3EE0')
def func_1B_3EE0():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 55890, 4230, 35050, 0)

    @scena.Lambda('lambda_3F07')
    def lambda_3F07():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3F07)

    ChrWalkTo(0x00FE, 56010, 4230, 33450, 2000, 0x00)
    ChrWalkTo(0x00FE, 55780, 4130, 30240, 2000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x001C offset: 0x3F43
@scena.Code('func_1C_3F43')
def func_1C_3F43():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 55890, 4230, 35050, 0)

    @scena.Lambda('lambda_3F6A')
    def lambda_3F6A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3F6A)

    ChrWalkTo(0x00FE, 56010, 4230, 33450, 2000, 0x00)
    ChrWalkTo(0x00FE, 54190, 4130, 30060, 2000, 0x00)

    Return()

# id: 0x001D offset: 0x3F9F
@scena.Code('func_1D_3F9F')
def func_1D_3F9F():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 55890, 4230, 35050, 0)

    @scena.Lambda('lambda_3FC6')
    def lambda_3FC6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3FC6)

    ChrWalkTo(0x00FE, 56010, 4230, 33450, 2000, 0x00)
    ChrWalkTo(0x00FE, 56950, 4130, 30840, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x001E offset: 0x4002
@scena.Code('func_1E_4002')
def func_1E_4002():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 55890, 4230, 35050, 0)

    @scena.Lambda('lambda_4029')
    def lambda_4029():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4029)

    ChrWalkTo(0x00FE, 56010, 4230, 33450, 2000, 0x00)
    ChrWalkTo(0x00FE, 54600, 4200, 32380, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x001F offset: 0x4065
@scena.Code('func_1F_4065')
def func_1F_4065():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 55890, 4230, 35050, 0)

    @scena.Lambda('lambda_408C')
    def lambda_408C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_408C)

    ChrWalkTo(0x00FE, 56010, 4230, 33450, 2000, 0x00)
    ChrWalkTo(0x00FE, 56960, 4130, 32810, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0020 offset: 0x40C8
@scena.Code('func_20_40C8')
def func_20_40C8():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_40E9',
    )

    Call(0, 0x0025)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_40E9(): pass

    label('loc_40E9')

    Fade(1000)
    CameraMove(36120, 0, 34420, 0)
    OP_67(0, 7200, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(38000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 36570, 0, 33800, 0)
    ChrSetPos(0x0103, 35550, 0, 33750, 0)
    ChrSetPos(0x00F8, 35590, 0, 32350, 0)
    ChrSetPos(0x00F9, 36650, 0, 32439, 0)
    ChrTurnDirection(0x0014, 0x0101, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 1, 0x1A01)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_43BA',
    )

    SetScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))

    ChrTalk(
        0x0014,
        (
            '#1030300146V#5P啊，艾丝蒂尔。\n',
            '这就要出发了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1030300147V#5P难得回来一次，\n',
            '为什么不多留一阵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300148V#1016F#4P嗯……还有很多事要忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300149V#1006F等这次的工作结束之后，\n',
            '我会好好休息一阵的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1030300150V#5P嗯，那最好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1030300151V#5P好了，爱娜已经\n',
            '付过乘船费用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1030300152V#5P要马上办理乘船手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 90, 400)

    ChrTalk(
        0x0103,
        (
            '#0030271209V#020F#6P要办手续的话，在飞船起飞\n',
            '之前来这里办理就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300154V在洛连特还有\n',
            '其他事情要做吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        0,
        (
            TXT(0x00, '【还有点事】\n'),
            TXT(0x01, '【办理乘船手续】\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_443A')

    def _loc_43BA(): pass

    label('loc_43BA')

    ChrTalk(
        0x0014,
        (
            '#1030300155V#5P噢。\n',
            '要办理乘船手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        0,
        (
            TXT(0x00, '【还有点事】\n'),
            TXT(0x01, '【办理乘船手续】\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_443A(): pass

    label('loc_443A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_447A',
    )

    ChrTalk(
        0x0014,
        (
            '#1030300156V#5P那么，有需要的时候\n',
            '再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_447A(): pass

    label('loc_447A')

    ChrTalk(
        0x0014,
        (
            '#1030300157V#5P好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 0, 400)

    ChrTalk(
        0x0014,
        (
            '#1030300158V#5P那么我就去和协会联络，\n',
            '把其他人叫来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    TalkSetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行人办理完乘船手续之后\n',
            '就在原地等待飞船起飞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Call(0, 0x0024)
    CameraMove(44610, 4000, 35220, 0)
    OP_67(0, 8220, -10000, 0)
    CameraSetDistance(3660, 0)
    OP_6C(50000, 0)
    OP_6E(331, 0)
    ChrSetPos(0x0101, 40690, 4000, 36460, 180)
    ChrSetPos(0x0103, 41780, 4000, 37050, 180)
    ChrSetPos(0x00F8, 39750, 4000, 37200, 180)
    ChrSetPos(0x00F9, 40930, 4000, 38420, 180)
    ChrSetPos(0x00FA, 39260, 4000, 38230, 180)
    ChrSetPos(0x00FB, 40230, 4000, 39230, 180)
    ChrSetPos(0x00FC, 39020, 4000, 39620, 180)
    ChrSetPos(0x0008, 42970, 4000, 31060, 90)
    ChrSetPos(0x0009, 42660, 4000, 31950, 180)
    ChrSetPos(0x000A, 42690, 4000, 33090, 180)
    ChrSetPos(0x000B, 42120, 4000, 34240, 114)
    ChrSetPos(0x000C, 41690, 4000, 35590, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    OP_71(0x000A, 0x0004)
    OP_71(0x000A, 0x0002)
    OP_72(0x000F, 0x0004)
    OP_72(0x000C, 0x0004)
    OP_72(0x000D, 0x0004)
    OP_6F(0x000F, 450)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    ChrSetFlags(0x001A, 0x0080)
    OP_A1(0x0018, 0x000F)
    ChrSetPos(0x0018, 55000, -3040, 35000, 0)
    OP_A1(0x0017, 0x000C)
    ChrSetPos(0x0017, 55000, -3040, 35000, 0)
    Yield()
    PlaySE(226, 0x00, 0x64)
    PlaySE(117, 0x00, 0x64)
    Sleep(3000)

    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    Sleep(1000)

    PlaySE(118, 0x00, 0x64)
    Sleep(1000)

    PlaySE(120, 0x00, 0x64)
    Sleep(1000)

    FadeIn(2000, 0)
    CreateThread(0x0008, 0x01, 0x00, func_21_4E21)
    Sleep(500)

    CreateThread(0x0009, 0x01, 0x00, func_22_4E68)
    Sleep(580)

    CreateThread(0x000A, 0x01, 0x00, func_22_4E68)
    Sleep(550)

    CreateThread(0x000B, 0x01, 0x00, func_22_4E68)
    Sleep(680)

    CreateThread(0x000C, 0x01, 0x00, func_22_4E68)
    Sleep(650)

    CreateThread(0x0101, 0x01, 0x00, func_23_4EC3)
    Sleep(500)

    CreateThread(0x0103, 0x01, 0x00, func_23_4EC3)
    Sleep(480)

    CreateThread(0x00F8, 0x01, 0x00, func_23_4EC3)
    Sleep(470)

    CreateThread(0x00F9, 0x01, 0x00, func_23_4EC3)
    Sleep(490)

    CreateThread(0x00FA, 0x01, 0x00, func_23_4EC3)
    Sleep(500)

    CreateThread(0x00FB, 0x01, 0x00, func_23_4EC3)
    Sleep(480)

    CreateThread(0x00FC, 0x01, 0x00, func_23_4EC3)
    Sleep(4800)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    CameraMove(48470, 3930, 38060, 0)
    OP_67(0, 40540, -45000, 0)
    CameraSetDistance(740, 0)
    OP_6C(159000, 0)
    OP_6E(510, 0)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x00FA, 0x01)
    TerminateThread(0x00FB, 0x01)
    TerminateThread(0x00FC, 0x01)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0103, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    ChrSetFlags(0x00FA, 0x0080)
    ChrSetFlags(0x00FB, 0x0080)
    ChrSetFlags(0x00FC, 0x0080)
    OP_6F(0x000F, 1)
    FadeIn(1000, 0)
    PlaySE(226, 0x00, 0x64)
    Sleep(2000)

    PlaySE(120, 0x00, 0x64)
    OP_B0(0x000D, 0x64)
    OP_6F(0x000D, 0)
    OP_70(0x000D, 300)
    Sleep(1800)

    PlaySE(118, 0x00, 0x64)
    OP_B0(0x000F, 0x32)
    OP_6F(0x000F, 1)
    OP_70(0x000F, 60)
    OP_73(0x000F)
    Sleep(1000)

    OP_23(0x0075)
    PlaySE(119, 0x01, 0x64)

    @scena.Lambda('lambda_48D2')
    def lambda_48D2():
        CameraMove(59300, 3930, 70000, 18000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_48D2)

    @scena.Lambda('lambda_48EA')
    def lambda_48EA():
        OP_6C(215000, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_48EA)

    @scena.Lambda('lambda_48FA')
    def lambda_48FA():
        CameraSetDistance(850, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_48FA)

    @scena.Lambda('lambda_490A')
    def lambda_490A():
        OP_6E(580, 20000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_490A)

    LoadEffect(0x00, 'map\\\\mp028_00.eff')
    Play3DEffect(0x00, 0x00, 0x0B, 'Frame1_E0000_ground_Layer1', 0xFFFFE7C8, 0x000008FC, 0x00002567, 0x0000, 0x0000, 0x0000, 0x000005DC, 0x000005DC, 0x000005DC, 0x00000000)
    Play3DEffect(0x00, 0x01, 0x0B, 'Frame1_E0000_ground_Layer1', 0x00001838, 0x000008FC, 0x00002567, 0x0000, 0x0000, 0x0000, 0x000005DC, 0x000005DC, 0x000005DC, 0x00000000)

    @scena.Lambda('lambda_49B0')
    def lambda_49B0():
        ChrWalkTo(0x00FE, 55000, -2040, 35000, 300, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0000, lambda_49B0)

    PlaySE(119, 0x00, 0x64)
    OP_6F(0x000F, 61)
    OP_70(0x000F, 160)
    OP_73(0x000F)
    OP_71(0x000F, 0x0020)
    OP_6F(0x000F, 161)
    OP_70(0x000F, 260)
    WaitForThreadExit(0x0018, 0x0000)

    @scena.Lambda('lambda_49F9')
    def lambda_49F9():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 100, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_49F9)

    @scena.Lambda('lambda_4A14')
    def lambda_4A14():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 100, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4A14)

    Sleep(200)

    @scena.Lambda('lambda_4A34')
    def lambda_4A34():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4A34)

    @scena.Lambda('lambda_4A4F')
    def lambda_4A4F():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4A4F)

    Sleep(200)

    @scena.Lambda('lambda_4A6F')
    def lambda_4A6F():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4A6F)

    @scena.Lambda('lambda_4A8A')
    def lambda_4A8A():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4A8A)

    Sleep(200)

    @scena.Lambda('lambda_4AAA')
    def lambda_4AAA():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4AAA)

    @scena.Lambda('lambda_4AC5')
    def lambda_4AC5():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4AC5)

    Sleep(200)

    @scena.Lambda('lambda_4AE5')
    def lambda_4AE5():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4AE5)

    @scena.Lambda('lambda_4B00')
    def lambda_4B00():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4B00)

    Sleep(200)

    @scena.Lambda('lambda_4B20')
    def lambda_4B20():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4B20)

    @scena.Lambda('lambda_4B3B')
    def lambda_4B3B():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4B3B)

    Sleep(200)

    @scena.Lambda('lambda_4B5B')
    def lambda_4B5B():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4B5B)

    @scena.Lambda('lambda_4B76')
    def lambda_4B76():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4B76)

    Sleep(200)

    @scena.Lambda('lambda_4B96')
    def lambda_4B96():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4B96)

    @scena.Lambda('lambda_4BB1')
    def lambda_4BB1():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4BB1)

    Sleep(200)

    @scena.Lambda('lambda_4BD1')
    def lambda_4BD1():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4BD1)

    @scena.Lambda('lambda_4BEC')
    def lambda_4BEC():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4BEC)

    Sleep(200)

    @scena.Lambda('lambda_4C0C')
    def lambda_4C0C():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4C0C)

    @scena.Lambda('lambda_4C27')
    def lambda_4C27():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4C27)

    Sleep(200)

    @scena.Lambda('lambda_4C47')
    def lambda_4C47():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4C47)

    @scena.Lambda('lambda_4C62')
    def lambda_4C62():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4C62)

    Sleep(200)

    @scena.Lambda('lambda_4C82')
    def lambda_4C82():
        ChrWalkTo(0x00FE, 55000, 2040, 1075000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4C82)

    @scena.Lambda('lambda_4C9D')
    def lambda_4C9D():
        ChrWalkTo(0x00FE, 55000, -40, 1075000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4C9D)

    Sleep(200)

    @scena.Lambda('lambda_4CBD')
    def lambda_4CBD():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4CBD)

    @scena.Lambda('lambda_4CD8')
    def lambda_4CD8():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4CD8)

    Sleep(200)

    @scena.Lambda('lambda_4CF8')
    def lambda_4CF8():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4CF8)

    @scena.Lambda('lambda_4D13')
    def lambda_4D13():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4D13)

    Sleep(200)

    @scena.Lambda('lambda_4D33')
    def lambda_4D33():
        ChrWalkTo(0x00FE, 55000, 2040, 105000, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4D33)

    @scena.Lambda('lambda_4D4E')
    def lambda_4D4E():
        ChrWalkTo(0x00FE, 55000, -40, 105000, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4D4E)

    Sleep(2800)

    OP_24(0x0077, 0x5A)
    Sleep(300)

    OP_24(0x0077, 0x50)
    Sleep(300)

    OP_24(0x0077, 0x46)
    Sleep(100)

    FadeOut(2000, 0, -1)
    Sleep(200)

    OP_24(0x0077, 0x3C)
    Sleep(300)

    OP_24(0x0077, 0x32)
    Sleep(300)

    OP_24(0x0077, 0x28)
    Sleep(300)

    OP_24(0x0077, 0x1E)
    Sleep(300)

    OP_23(0x0077)
    OP_0D()
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    OP_28(0x0072, 0x04, 0x40)
    OP_28(0x0073, 0x04, 0x40)
    OP_28(0x0074, 0x04, 0x40)
    OP_28(0x0075, 0x04, 0x40)
    OP_28(0x0076, 0x04, 0x40)
    OP_28(0x0077, 0x04, 0x40)
    OP_28(0x00AD, 0x04, 0x40)
    OP_28(0x00AE, 0x04, 0x40)
    OP_28(0x00AF, 0x04, 0x40)
    OP_28(0x00B0, 0x04, 0x40)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T3133._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0021 offset: 0x4E21
@scena.Code('func_21_4E21')
def func_21_4E21():
    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrWalkTo(0x00FE, 48250, 3130, 30990, 2000, 0x00)
    ChrWalkTo(0x00FE, 55300, 3130, 30990, 2000, 0x00)
    ChrWalkTo(0x00FE, 55300, 3130, 34700, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0022 offset: 0x4E68
@scena.Code('func_22_4E68')
def func_22_4E68():
    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrWalkTo(0x00FE, 42700, 4000, 30910, 2000, 0x00)
    ChrWalkTo(0x00FE, 48250, 3130, 30990, 2000, 0x00)
    ChrWalkTo(0x00FE, 55300, 3930, 30990, 2000, 0x00)
    ChrWalkTo(0x00FE, 55300, 3130, 34700, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0023 offset: 0x4EC3
@scena.Code('func_23_4EC3')
def func_23_4EC3():
    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrWalkTo(0x00FE, 41770, 4000, 34840, 2000, 0x00)
    ChrWalkTo(0x00FE, 42700, 4000, 30910, 2000, 0x00)
    ChrWalkTo(0x00FE, 48250, 3130, 30990, 2000, 0x00)
    ChrWalkTo(0x00FE, 55300, 3130, 30990, 2000, 0x00)
    ChrWalkTo(0x00FE, 55300, 3130, 34700, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0024 offset: 0x4F32
@scena.Code('func_24_4F32')
def func_24_4F32():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4F6B',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_4F6B(): pass

    label('loc_4F6B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4FB8',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FA0',
    )

    FormationAddMember(ChrTable['提妲'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_4FB8')

    def _loc_4FA0(): pass

    label('loc_4FA0')

    FormationAddMember(ChrTable['提妲'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_4FB8(): pass

    label('loc_4FB8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_502D',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FED',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_502D')

    def _loc_4FED(): pass

    label('loc_4FED')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5015',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_502D')

    def _loc_5015(): pass

    label('loc_5015')

    FormationAddMember(ChrTable['奥利维尔'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_502D(): pass

    label('loc_502D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_507A',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5062',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_507A')

    def _loc_5062(): pass

    label('loc_5062')

    FormationAddMember(ChrTable['科洛丝'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_507A(): pass

    label('loc_507A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_509F',
    )

    FormationAddMember(ChrTable['金'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_509F(): pass

    label('loc_509F')

    Return()

# id: 0x0025 offset: 0x50A0
@scena.Code('func_25_50A0')
def func_25_50A0():
    FadeOut(0, 0, -1)
    CameraMove(90, 0, 24870, 0)
    Sleep(100)

    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

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
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_512A'),
        (0x00000001, 'loc_5130'),
        (-1, 'loc_5136'),
    )

    def _loc_512A(): pass

    label('loc_512A')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5136')

    def _loc_5130(): pass

    label('loc_5130')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5136')

    def _loc_5136(): pass

    label('loc_5136')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x0026 offset: 0x5172
@scena.Code('func_26_5172')
def func_26_5172():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船飞船坪\n',
            '≡　开往王都格兰赛尔\n',
            '≡　开往柏斯市',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　『利贝尔飞船公社』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0027 offset: 0x520E
@scena.Code('func_27_520E')
def func_27_520E():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞船坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            '   『利贝尔飞船公社』　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0028 offset: 0x528A
@scena.Code('func_28_528A')
def func_28_528A():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　※无关人员禁止入内　　\n',
            '   『利贝尔飞船公社』　',
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
