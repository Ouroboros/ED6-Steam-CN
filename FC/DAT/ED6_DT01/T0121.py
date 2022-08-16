import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0121_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0121   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0121.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T0121._SN', 'ED6_DT01/T0121_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x0000109A,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFFF830,
            word_0C         = 0x0004,
            word_0E         = 0x005A,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 2,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x0000109A,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFFF830,
            word_0C         = 0x0004,
            word_0E         = 0x005A,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 315,
            word_34         = 315,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 2,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02560._CH', 'ED6_DT07/CH02560P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20133._CH', 'ED6_DT06/CH20133P._CP'),
    ]

# id: 0x10001 offset: 0x146
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '爱娜',
            x                   = 750,
            z                   = 0,
            y                   = 118600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 200,
            z                   = 0,
            y                   = 74200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '利吉',
            x                   = -355,
            z                   = 0,
            y                   = 71450,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '里农',
            x                   = 3800,
            z                   = 0,
            y                   = 2000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '布露姆老奶奶',
            x                   = 47500,
            z                   = 0,
            y                   = -1110,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '尤妮',
            x                   = -295,
            z                   = 0,
            y                   = 116400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '奥维德',
            x                   = 2000,
            z                   = 0,
            y                   = -3100,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            name                = '克劳斯市长',
            x                   = 82247,
            z                   = 0,
            y                   = 2548,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458761,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524297,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589833,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 655369,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 720905,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 786441,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x326
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x326
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -2700,
            y           = -500,
            z           = 109000,
            range       = -1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x0001B580,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = 2900,
            y           = -500,
            z           = 110700,
            range       = 5300,
            dword_10    = 0x00000BB8,
            dword_14    = 0x0001ABBC,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
    )

# id: 0x10004 offset: 0x366
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3810,
            triggerZ            = 0,
            triggerY            = 1080,
            triggerRange        = 800,
            actorX              = 3800,
            actorZ              = 1500,
            actorY              = 2000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1271,
            triggerZ            = 0,
            triggerY            = 116402,
            triggerRange        = 800,
            actorX              = 750,
            actorZ              = 1500,
            actorY              = 118600,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4900,
            triggerZ            = 0,
            triggerY            = 112600,
            triggerRange        = 1400,
            actorX              = 4900,
            actorZ              = 2000,
            actorY              = 112600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4900,
            triggerZ            = 0,
            triggerY            = 112600,
            triggerRange        = 1400,
            actorX              = 4900,
            actorZ              = 2000,
            actorY              = 112600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3F6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_41F',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 41, 0, 116398, 0)
    CreateThread(0x0009, 0x00, 0x00, func_02_660)

    def _loc_41F(): pass

    label('loc_41F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_43C',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 5649, 0, 114874, 0)

    def _loc_43C(): pass

    label('loc_43C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 7, 0x207)),
            Expr.Return,
        ),
        'loc_44D',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    def _loc_44D(): pass

    label('loc_44D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 4, 0x20C)),
            Expr.Return,
        ),
        'loc_459',
    )

    ChrClearFlags(0x000D, 0x0080)

    def _loc_459(): pass

    label('loc_459')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 7, 0x217)),
            Expr.Return,
        ),
        'loc_485',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0008)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000A, 0x0008)
    ChrSetPos(0x000A, -355, 0, 71450, 180)

    def _loc_485(): pass

    label('loc_485')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_496',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    def _loc_496(): pass

    label('loc_496')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_4A7',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000A, 0x0008)

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_4B8',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    def _loc_4B8(): pass

    label('loc_4B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_4C9',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000A, 0x0008)

    def _loc_4C9(): pass

    label('loc_4C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_4DC',
    )

    ChrSetFlags(0x0009, 0x0080)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_10_7941)

    def _loc_4DC(): pass

    label('loc_4DC')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_4F0'),
        (0x00000067, 'loc_54A'),
        (0x0000006A, 'loc_5D8'),
        (-1, 'loc_5EC'),
    )

    def _loc_4F0(): pass

    label('loc_4F0')

    MapClearFlags(0x00000001)
    ChrSetPos(0x0101, 1500, 0, 116000, 0)
    ChrSetPos(0x0102, 700, 0, 115200, 0)
    CameraMove(611, 0, 116942, 0)
    OP_6C(315000, 0)
    FadeIn(1000, 0)
    OP_B1('t0121_y')
    Event(0, func_1E_BCC7)

    Jump('loc_5EC')

    def _loc_54A(): pass

    label('loc_54A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 4, 0x204)),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58B',
    )

    MapClearFlags(0x00000001)
    ChrSetPos(0x0101, 2400, 0, 111120, 0)
    ChrSetPos(0x0102, 3790, 0, 110540, 0)
    FadeIn(500, 0)
    Event(0, func_12_9209)

    def _loc_58B(): pass

    label('loc_58B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 6, 0x266)),
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5AA',
    )

    SetScenaFlags(ScenaFlag(0x004D, 0, 0x268))
    EventBegin(0x00)
    MapSetFlags(0x00400000)
    MapClearFlags(0x00000001)
    Event(0, func_11_7EAB)

    def _loc_5AA(): pass

    label('loc_5AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 7, 0x22F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5D5',
    )

    @scena.Lambda('lambda_05BC')
    def lambda_05BC():
        ChrTurnDirection(0x0009, 0x0000, 0)
        Yield()

        Jump('lambda_05BC')

    DispatchAsync2(0x0009, 0x0001, lambda_05BC)

    MapSetFlags(0x00400000)
    MapClearFlags(0x00000001)
    Event(0, func_0E_7126)

    def _loc_5D5(): pass

    label('loc_5D5')

    Jump('loc_5EC')

    def _loc_5D8(): pass

    label('loc_5D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5E9',
    )

    Event(0, func_16_9479)

    def _loc_5E9(): pass

    label('loc_5E9')

    Jump('loc_5EC')

    def _loc_5EC(): pass

    label('loc_5EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_605',
    )

    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0008)

    Jump('loc_605')

    def _loc_605(): pass

    label('loc_605')

    Return()

# id: 0x0001 offset: 0x606
@scena.Code('func_01_606')
def func_01_606():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 1, 0x269)),
            (Expr.TestScenaFlags, ScenaFlag(0x0072, 0, 0x390)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_61B',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_61B(): pass

    label('loc_61B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_633',
    )

    OP_B1('t0121_y')

    Jump('loc_63C')

    def _loc_633(): pass

    label('loc_633')

    OP_B1('t0121_n')

    def _loc_63C(): pass

    label('loc_63C')

    OP_64(0x00, 0x0002)
    OP_64(0x01, 0x0002)
    OP_64(0x03, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_65F',
    )

    OP_64(0x02, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_65F',
    )

    OP_65(0x03, 0x0001)

    def _loc_65F(): pass

    label('loc_65F')

    Return()

# id: 0x0002 offset: 0x660
@scena.Code('func_02_660')
def func_02_660():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_675',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_660')

    def _loc_675(): pass

    label('loc_675')

    Return()

# id: 0x0003 offset: 0x676
@scena.Code('func_03_676')
def func_03_676():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_699',
    )

    OP_8D(0x00FE, 960, -4400, 2700, -2500, 3000)

    Jump('func_03_676')

    def _loc_699(): pass

    label('loc_699')

    Return()

# id: 0x0004 offset: 0x69A
@scena.Code('func_04_69A')
def func_04_69A():
    Call(0, 0x0006)

    Return()

# id: 0x0005 offset: 0x69F
@scena.Code('func_05_69F')
def func_05_69F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_6B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B2',
    )

    Call(0, 0x0006)

    def _loc_6B2(): pass

    label('loc_6B2')

    Jump('loc_7AA')

    def _loc_6B5(): pass

    label('loc_6B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 4, 0x20C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7AA',
    )

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 7, 0x22F)),
            Expr.Return,
        ),
        'loc_704',
    )

    ChrTalk(
        0x0009,
        (
            '#0030000631V#020F你们两个，\n',
            '快点到爱娜那儿报告去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7A7')

    def _loc_704(): pass

    label('loc_704')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_75E',
    )

    ChrTalk(
        0x0009,
        (
            '#0030000632V#020F你们两个不要随处乱跑了，\n',
            '快点到公告板那里确认工作内容吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7A7')

    def _loc_75E(): pass

    label('loc_75E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_7A7',
    )

    ChrTalk(
        0x0009,
        (
            '#0030000633V#020F你们两个不要随处乱跑了，\n',
            '赶快把东西接下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7A7(): pass

    label('loc_7A7')

    TalkEnd(0x0009)

    def _loc_7AA(): pass

    label('loc_7AA')

    Return()

# id: 0x0006 offset: 0x7AB
@scena.Code('func_06_7AB')
def func_06_7AB():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 0, 0x250)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 2, 0x23A)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 4, 0x22C)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 7, 0x22F)),
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_849',
    )

    FadeOut(300, 0, 70)

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
            TXT(0x01, '报告\n'),
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
        'loc_838',
    )

    OP_0D()
    Call(1, 0x0002)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_838(): pass

    label('loc_838')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_849',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_849(): pass

    label('loc_849')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_96C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_90D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '#0350020242V#740F啊，你们还没出发吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350020243V要去柏斯的话，\n',
            '沿米尔西街道往西走就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350020244V我已经和那边的\n',
            '协会支部取得联系了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350020245V你们一路小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_969')

    def _loc_90D(): pass

    label('loc_90D')

    ChrTalk(
        0x0008,
        (
            '#0350020246V#740F要去柏斯的话，\n',
            '沿米尔西街道往西走就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350020247V你们一路小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_969(): pass

    label('loc_969')

    Jump('loc_4125')

    def _loc_96C(): pass

    label('loc_96C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1F24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E12',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 1078, 0, 116398, 0)
    ChrTurnDirection(0x0101, 0x0009, 0)
    ChrSetPos(0x0102, 1078, 0, 115280, 0)
    ChrTurnDirection(0x0102, 0x0009, 0)
    TerminateThread(0x0009, 0xFF)
    ChrTurnDirection(0x0008, 0x0101, 0)
    ChrTurnDirection(0x0009, 0x0101, 0)
    CameraMove(270, 0, 117230, 0)
    CameraSetDistance(2800, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#0030010883V#020F#1P哎呀，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010884V#004F#4P啊，雪拉姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010885V#010F真少见啊，\n',
            '平时总是看到你在外面奔波的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010886V#020F#1P老师交待给我的工作\n',
            '终于都做完了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010887V#020F刚刚回来进行报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010888V#001F#4P啊，雪拉姐也完成了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010889V#027F#1P嗯，总算完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010890V#027F爱娜已经告诉我了。\n',
            '看来你们也很努力是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010891V#027F不过话说回来，能学到东西，\n',
            '即使辛苦点也是值得的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010892V#008F#4P嘿嘿，知道啦雪拉姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010893V#008F那么……\n',
            '我们也赶快报告吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0350010894V#740F好的，你们说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '两人报告了当记者护卫的经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_28(0x0019, 0x04, 0x10)
    OP_28(0x0019, 0x01, 0x0100)
    Sleep(100)

    OP_AF(0x04, 0x0019)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0350010895V#741F好的，真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010896V怎么样，雪拉扎德。\n',
            '不觉得他们成长了很多吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)
    ChrTurnDirection(0x0101, 0x0009, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x0019, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_E49',
    )

    ChrTalk(
        0x0009,
        (
            '#0030010897V#022F#1P还太嫩了点呢。\n',
            '在塔里的多余行动还是比较多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010898V#022F你们的任务不单是战斗，\n',
            '还要确保保护对象不受伤害才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010899V#022F记住以后工作需要更加谨慎，\n',
            '做好每一个细节是游击士应有的职责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010900V#007F#4P唔唔……雪拉姐好严呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F15')

    def _loc_E49(): pass

    label('loc_E49')

    ChrTalk(
        0x0009,
        (
            '#0030010901V#027F#1P作为新人来说干得还不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010902V#027F不过，可不能这样就满足哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010903V#027F特别是艾丝蒂尔，\n',
            '你啊，总是容易得意忘形。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010904V#502F#4P嗯……好啦。\n',
            '我知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F15(): pass

    label('loc_F15')

    ChrTalk(
        0x0008,
        (
            '#0350010905V#741F呵呵，艾丝蒂尔、约修亚，\n',
            '还有雪拉扎德，你们都辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0350010906V#740F卡西乌斯先生留下的空缺，\n',
            '没想到能这么快就填补上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010907V这么一来，\n',
            '可以暂时放松一段时间了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010908V#000F#4P那样的话，\n',
            '反倒觉得有点无聊呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010909V#010F还有巡视街道和消灭魔兽这样的琐碎工作嘛，\n',
            '没有关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010910V#027F#1P呵呵……\n',
            '好久没有这么悠闲了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010911V#021F好，今晚一定要喝个痛快～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010912V#021F艾丝蒂尔、约修亚，\n',
            '你们两人一定要来陪我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0009, 400)
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010913V#004F#4P啊～……\n',
            '要去陪喝醉的雪拉姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010914V#022F#1P哎呀，艾丝蒂尔，\n',
            '你想拒绝我的邀请吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010915V#022F哼哼，真是够胆量呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010916V#007F#4P因、因为雪拉姐的酒品\n',
            '实在差得一塌糊涂啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010917V#007F又大吵大闹，又跳舞，还脱衣服……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010918V#017F的确是……\n',
            '连我们都觉得不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350010919V#745F我说雪拉扎德，\n',
            '你对未成年人都做了些什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010920V#024F#1P什么呀，只是喝酒的助兴节目啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010921V#025F哼，既然这么不情愿的话，\n',
            '这次就先饶过艾丝蒂尔你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010922V#501F#4P啊，真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010923V#020F#1P嗯～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0009, 0x0102, 700, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0102, 400)
    OP_62(0x0009, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0030010924V#021F#1P不过作为补偿，\n',
            '就把你那份算到约修亚的头上吧㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0102, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020010925V#018F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010926V#018F那、那个，雪拉姐姐……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010927V#005F#4P慢、慢着！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010928V#027F#1P唔呼呼～\n',
            '谁叫你约修亚又正经又晚熟啊㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010929V#027F不管是喝酒，还是其他什么的，\n',
            '各种各样的事姐姐都会教你哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010930V#014F各、各种各样……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010931V#009F#4P喂，约修亚……\n',
            '你干嘛一脸色色的样子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010932V#012F你、你误会啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    ChrSetPos(0x000F, 4147, 0, 110113, 315)

    NpcTalk(
        0x000F,
        '老人的声音',
        (
            '#0340010933V不、不好啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0009, 0x000F, 0)
    ChrTurnDirection(0x0102, 0x000F, 0)
    ChrTurnDirection(0x0101, 0x000F, 0)
    ChrWalkTo(0x000F, 1708, 0, 111232, 4000, 0x00)
    ChrTurnDirection(0x0009, 0x000F, 0)
    ChrTurnDirection(0x0102, 0x000F, 0)
    ChrTurnDirection(0x0101, 0x000F, 0)
    ChrWalkTo(0x000F, 1190, 0, 113550, 4000, 0x00)
    CreateThread(0x0101, 0x01, 0x00, func_19_BBB0)
    CreateThread(0x0102, 0x01, 0x00, func_1A_BBD1)
    CreateThread(0x0009, 0x01, 0x00, func_1B_BBED)
    CameraMove(810, 0, 115660, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010010934V#004F#2P咦，市长爷爷？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0340010935V#603F呼呼……哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010936V#604F艾丝蒂尔、约修亚……\n',
            '哦哦，雪拉扎德也在啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010937V#014F（还好救兵来了……）\n',
            '发生什么事了，这么慌张？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0340010938V#604F不、不得了的大事啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010939V强盗不在家的时候，\n',
            '刚好有我闯进来啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010940V#008F#2P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010941V#025F我说市长，\n',
            '您先镇静一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010942V#020F深吸一口气，然后慢慢吐出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0009, 400)

    ChrTalk(
        0x000F,
        (
            '#0340010943V#604F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010944V#603F吸～～……呼～～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010945V#603F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010946V#602F……其实是这样的，\n',
            '我不在家的时候，刚好有强盗闯进来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010947V#004F#2P啊～～～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010948V#012F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010949V#022F那就不该镇静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0340010950V#602F因为我有些话要和教区长谈，\n',
            '所以刚才一直呆在教堂里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010951V回家的时候没有人出来迎接，\n',
            '觉得奇怪就在屋里到处查看了一下，\n',
            '才发现原来有强盗闯进来过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010952V#002F#2P等、等一下……\n',
            '米蕾奴婶婶她们呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0340010953V#600F还好，她们都平安无事。\n',
            '只是被关在阁楼里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010954V#007F#2P太、太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010955V#022F没有人受伤，\n',
            '总算是不幸中的万幸啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010956V#022F反正呆在这里也无济于事，\n',
            '市长，能让我们调查一下现场吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0340010957V#602F嗯，拜托你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010958V#002F#2P等一下，我们也要去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010959V#012F是啊。\n',
            '说不定能帮上什么忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030010960V#025F呼，真拿你们没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D03')
    def lambda_1D03():
        CameraMove(270, 0, 117230, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1D03)

    ChrTurnDirection(0x0009, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0030010961V#022F爱娜。\n',
            '我们去调查案件了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010962V#022F如果有什么事情，\n',
            '就全部交给利吉去办吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010963V#022F反正他肯定在酒馆闲着的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350010964V#742F嗯，我知道了，\n',
            '大家也要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    NewScene('ED6_DT01/T0210._SN', 1, 0, 0)
    IdleLoop()

    Jump('loc_1F21')

    def _loc_1E12(): pass

    label('loc_1E12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E9A',
    )

    ChrTalk(
        0x0008,
        (
            '#0350010965V#740F竟敢闯入市长官邸，\n',
            '这伙强盗胆子真不小啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010966V事件的调查就拜托你们了。\n',
            '你们三个都要小心行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F21')

    def _loc_1E9A(): pass

    label('loc_1E9A')

    ChrTalk(
        0x0008,
        (
            '#0350010967V#740F调查方面怎么样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010968V这里的工作就都交给利吉了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010969V你们就集中精力\n',
            '去调查这件失窃案件吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F21(): pass

    label('loc_1F21')

    Jump('loc_4125')

    def _loc_1F24(): pass

    label('loc_1F24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_20A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2025',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '#0350010450V#740F……对了， \n',
            '要是碰到里农的妈妈，\n',
            '麻烦帮我带下话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010451V#741F就说请她找城镇里的其他女性吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010452V不好意思， \n',
            '我还不打算结婚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010453V#740F呵呵，要是真的出现很棒的人，\n',
            '也许我会改变想法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_209E')

    def _loc_2025(): pass

    label('loc_2025')

    ChrTalk(
        0x0008,
        (
            '#0350010576V#740F哦，是去『翡翠之塔』啊，\n',
            '那要小心点了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010577V虽然你们去过那里，\n',
            '不过行动时也务必不要大意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_209E(): pass

    label('loc_209E')

    Jump('loc_4125')

    def _loc_20A1(): pass

    label('loc_20A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_2983',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 0, 0x250)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2809',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 1390, 0, 115970, 0)
    ChrSetPos(0x0102, 410, 0, 115820, 0)
    ChrSetDirection(0x0008, 180, 0)
    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0010, 1000)
    SetScenaFlags(ScenaFlag(0x004A, 0, 0x250))
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0350010391V#740F辛苦了。\n',
            '矿山似乎发生了不得了的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010392V#004F#4P啊，爱娜姐姐你也知道了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350010393V#740F矿山那边已经送来消息了。\n',
            '还对你们的帮忙感激不尽呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010394V好了，把那里发生的事情经过\n',
            '详细地报告给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010395V#010F好的，那么——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_AF(0x04, 0x0003)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0350010396V#740F呵呵……\n',
            '比预想的做得更好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010397V应对突发事件，\n',
            '也是游击士的使命之一哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010398V以后也拜托了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010399V#001F#4P嗯，尽管交给我们吧☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010400V#015F嗯，艾丝蒂尔她啊，\n',
            '就算没有人委托，也会自动去做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010401V#502F#4P对，对………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010402V#005F#4P喂！\n',
            '不要把人说得跟管家婆一样嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010403V#015F不管怎么说，事实就是如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010404V老好人心肠，好奇心旺盛，\n',
            '还有直率的性格就是你的特点嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010405V#009F#4P唔……约修亚，\n',
            '你这样打击人也太过分了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010406V#019F是你太敏感了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350010407V#740F哎呀，怎么又吵起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0350010408V#740F好了，我来介绍一下\n',
            '你们要做的最后一项任务吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010409V你们知道《利贝尔通讯》吗？\n',
            '这次要协助他们进行取材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010410V#004F#4P啊，那不是……\n',
            '之前帮老爸买的杂志吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010411V#004F嘿～还真是有趣的巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010412V#010F协助取材……\n',
            '具体要做些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350010413V#740F因为要去危险的场所取材，\n',
            '所以需要身手不凡的向导。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010414V详细的情况，直接向委托人询问吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010415V杂志社的记者和摄影师\n',
            '正暂住在『洛连特旅馆』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010416V啊，这个是协会的介绍信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '游击士协会的介绍信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x0019, 0x04, 0x04)
    OP_28(0x0019, 0x01, 0x0001)
    OP_28(0x0019, 0x01, 0x0002)
    AddItem(0x0324, 1)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010417V#000F#4P那好，\n',
            '我们现在就去旅馆看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010418V#010F是啊，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_2980')

    def _loc_2809(): pass

    label('loc_2809')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2903',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '#0350010578V#740F……对了， \n',
            '要是碰到里农的妈妈，\n',
            '麻烦帮我带下话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010579V#741F就说请她找城镇里的其他女性吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010580V不好意思， \n',
            '我还不打算结婚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010581V#740F呵呵，要是真的出现很棒的人，\n',
            '也许我会改变想法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2980')

    def _loc_2903(): pass

    label('loc_2903')

    ChrTalk(
        0x0008,
        (
            '#0350010419V#740F这次任务的委托人\n',
            '正暂住在『洛连特旅馆』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010420V给他看推荐信，\n',
            '并向他咨询详细的工作内容就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2980(): pass

    label('loc_2980')

    Jump('loc_4125')

    def _loc_2983(): pass

    label('loc_2983')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_3117',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 2, 0x23A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F9D',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 1390, 0, 115970, 0)
    ChrSetPos(0x0102, 410, 0, 115820, 0)
    ChrSetDirection(0x0008, 180, 0)
    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0010, 1000)
    SetScenaFlags(ScenaFlag(0x0047, 2, 0x23A))

    ChrTalk(
        0x0008,
        (
            '#0350010001V#740F辛苦了。\n',
            '农场的工作还顺利吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010002V#000F#4P嗯，虽然有点小波折……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010003V#010F总之先报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '两人报告了在农场执行任务的经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(100)

    OP_AF(0x04, 0x0002)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0350010004V#740F原来如此。\n',
            '最后还是把魔兽放走了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010005V虽然觉得这种做法有欠考虑……\n',
            '不过这次就不追究了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010006V#004F#4P啊？这可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350010007V#740F游击士的使命是保卫百姓、维护正义……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010008V然而保护的方式有很多种，\n',
            '正义的存在形式也多如繁星。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010009V所以，把握好做事的尺度\n',
            '也是你们的工作之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010010V#012F原来如此……\n',
            '还真是很深奥啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350010011V#744F因为我们不仅要打倒魔兽，\n',
            '有时还要调停国家间的争端。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010012V高级的游击士除了具备优秀战斗力，\n',
            '还要有纵观全局的判断力以及\n',
            '灵活处理问题的能力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010013V#012F判断力和处理问题的能力吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010014V#007F#4P唔唔～……\n',
            '成为一流游击士的道路还真艰辛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350010015V#741F呵呵，每天都要有进步才行哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010016V#740F接下来……\n',
            '该交给你们下一个任务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010017V#006F#4P我们正等着呢！\n',
            '快点告诉我们内容吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010018V#006F这次还是打倒魔兽之类的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350010019V#740F不，是运送物品的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010020V委托人是克劳斯市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010021V#004F#4P啊，是市长委托的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010022V#014F这样好吗？\n',
            '把这么重要的任务交给我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350010023V#740F据说是很简单的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010024V总之，\n',
            '详细情况可以先向市长询问一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0003, 0x01, 0x0001)
    OP_28(0x0003, 0x04, 0x04)
    EventEnd(0x00)

    Jump('loc_3114')

    def _loc_2F9D(): pass

    label('loc_2F9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_301E',
    )

    ChrTalk(
        0x0008,
        (
            '#0350010280V#744F呼呼，之前那次\n',
            '还没有和雪拉分胜负呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010281V#740F她回来之后，\n',
            '要再约她到酒馆去喝一回。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3114')

    def _loc_301E(): pass

    label('loc_301E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 3, 0x23B)),
            Expr.Return,
        ),
        'loc_307D',
    )

    ChrTalk(
        0x0008,
        (
            '#0350010028V#740F嗯，原来是去玛鲁加矿山啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010029V那你们路上要小心点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3114')

    def _loc_307D(): pass

    label('loc_307D')

    ChrTalk(
        0x0008,
        (
            '#0350010025V#740F这次任务的详细情况\n',
            '要直接向克劳斯市长咨询。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010026V克劳斯市长的官邸就在城镇的东面。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350010027V……你们应该知道的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3114(): pass

    label('loc_3114')

    Jump('loc_4125')

    def _loc_3117(): pass

    label('loc_3117')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_374C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 4, 0x22C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36A0',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 1390, 0, 115970, 0)
    ChrSetPos(0x0102, 410, 0, 115820, 0)
    ChrSetDirection(0x0008, 180, 0)
    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0010, 1000)
    SetScenaFlags(ScenaFlag(0x0045, 4, 0x22C))
    OP_28(0x0002, 0x04, 0x04)
    OP_28(0x0002, 0x01, 0x0001)
    OP_28(0x0002, 0x01, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0350001322V#740F哎呀，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001323V卡西乌斯先生已经出发了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001324V#000F#4P嗯，刚刚才走。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001325V#000F爱娜姐姐，\n',
            '还是快点把老爸\n',
            '留下来的工作介绍给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350001326V#740F我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001327V要拜托你们去做的任务一共有三个……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001328V首先，\n',
            '需要你们去西边的农场一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001329V#004F#4P西边的农场，不就是缇欧的家吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350001330V#743F缇欧？\n',
            '这名字我好像在哪听到过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001331V#010F她是和我们同级的同学，\n',
            '叫缇欧·帕赛尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001332V#010F帕赛尔农场家的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350001333V#740F哦，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001334V你们的任务就是\n',
            '打倒帕赛尔农场里的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010001335V#004F#4P啊……有魔兽出没吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350001336V#740F嗯，所幸的是没有人受伤，\n',
            '不过农田被破坏了也很伤脑筋呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001337V所以农场才向协会提出了请求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001338V#002F#4P有这种事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001339V#002F嗯，我知道了！\n',
            '我们马上就赶过去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350001340V#740F那么，把这个带上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '游击士协会的介绍信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0320, 1)

    ChrTalk(
        0x0008,
        (
            '#0350001341V#740F这封是介绍信。\n',
            '可以证明你们是协会派遣的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001342V把信交给农场的主人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001343V#501F#4P缇欧的爸爸认识我们，\n',
            '所以我觉得没这个必要……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001344V#501F不过还是拿着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_3749')

    def _loc_36A0(): pass

    label('loc_36A0')

    ChrTalk(
        0x0008,
        (
            '#0350001345V#740F你们第一个任务就是\n',
            '消灭帕赛尔农场里的魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001346V要去农场，沿着西面那条\n',
            '米尔西街道走到一半再向南拐就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001347V这件事拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3749(): pass

    label('loc_3749')

    Jump('loc_4125')

    def _loc_374C(): pass

    label('loc_374C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_388C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3826',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '#0350001054V#741F才刚当上游击士就已经那么忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001055V真是辛苦你们了。\n',
            '明天也要继续加油哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001056V#740F那可是寄给卡西乌斯的信件，\n',
            '我想应该是很重要的联络信吧。\n',
            '一定要记得交给他哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3889')

    def _loc_3826(): pass

    label('loc_3826')

    ChrTalk(
        0x0008,
        (
            '#0350001057V#740F那可是寄给卡西乌斯的信件，\n',
            '我想应该是很重要的联络信吧。\n',
            '一定要记得交给他哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3889(): pass

    label('loc_3889')

    Jump('loc_4125')

    def _loc_388C(): pass

    label('loc_388C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 4, 0x20C)),
            Expr.Return,
        ),
        'loc_3934',
    )

    ChrTalk(
        0x0008,
        (
            '#0350000920V#740F那两个孩子就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000921V翡翠之塔就在通往玛鲁加山道途中\n',
            '往西拐的那个方向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000922V玛鲁加山道从城镇的北边出去就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4125')

    def _loc_3934(): pass

    label('loc_3934')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_3A6F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A0C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '#0350000728V#740F恭喜！\n',
            '你们俩终于正式成为游击士了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000729V最近协会的工作比较多，\n',
            '你们也会开始忙起来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000730V#502F嘿嘿，这正是我期待的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000731V#010F请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A6C')

    def _loc_3A0C(): pass

    label('loc_3A0C')

    ChrTalk(
        0x0008,
        (
            '#0350000732V#740F最近协会的工作比较多，\n',
            '你们也会开始忙起来哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000733V请多多指教哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A6C(): pass

    label('loc_3A6C')

    Jump('loc_4125')

    def _loc_3A6F(): pass

    label('loc_3A6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 7, 0x22F)),
            Expr.Return,
        ),
        'loc_3B07',
    )

    ChrTalk(
        0x0008,
        (
            '#0350000366V#740F实地考试合格的话，\n',
            '你们就能正式成为游击士了。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000367V如果要报告已经完成的工作任务，\n',
            '在菜单上选择『报告』就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4125')

    def _loc_3B07(): pass

    label('loc_3B07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3B40',
    )

    ChrTalk(
        0x0008,
        (
            '#0350000362V#740F哎呀，公告板就在那边呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4125')

    def _loc_3B40(): pass

    label('loc_3B40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_4094',
    )

    EventBegin(0x00)
    OP_69(0x0008, 1000)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x0008,
        (
            '#0350000345V#740F这是很重要的东西，\n',
            '所以千万别弄丢哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '游击士手册',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    AddItem(0x0208, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrTurnDirection(0x0101, 0x0009, 400)
    ChrTurnDirection(0x0102, 0x0009, 400)

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x9, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x9, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x9, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0010, 800)

    ChrTalk(
        0x0009,
        (
            '#0030000346V#020F那是游击士手册，\n',
            '就是用来记录工作细节的正规手册。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000347V#020F无论从谁那里听到了什么情报，\n',
            '还是在哪里发现了什么东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000348V#020F这些细微的事件\n',
            '经常都会成为调查的线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000349V#020F工作中就算是再小的事，\n',
            '也一定要做记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F#2P#1K明白了。',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010000351V#509F#4P#1K嘁，真是麻烦……',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()

    ChrTalk(
        0x0009,
        (
            '#0030000352V#026F哎呀？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000353V不知道是不是我多心。\n',
            '怎么只听到一个回答的声音？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000354V#506F啊、啊哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000355V#020F记录工作过程中的详细内容是\n',
            '游击士重要的职责哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000356V开始的时候也许会觉得麻烦，\n',
            '不过你们无论如何都要好好去习惯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000357V#007F好～的，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000358V#020F呼，知道就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000359V#020F……那么，\n',
            '就用实际行动证明给我看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)
    ChrSetDirection(0x0009, 135, 400)

    ChrTalk(
        0x0009,
        (
            '#0030000360V#020F看门口那边。\n',
            '看到竖在那里的公告板吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 400)
    ChrSetDirection(0x0102, 135, 400)
    CameraMove(3915, 0, 113532, 1000)

    ChrTalk(
        0x0009,
        (
            '#0030000361V#020F你们去公告板那里，\n',
            '试试确认一下工作的内容吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※靠近公告板会出现『！』的标记，\n',
            '　点击右键可以浏览公告板的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※点击列出的各任务的名称，\n',
            '　就可以看见该任务的详细内容和信息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    EventEnd(0x01)

    @scena.Lambda('lambda_4082')
    def lambda_4082():
        ChrTurnDirection(0x0009, 0x0000, 0)
        Yield()

        Jump('lambda_4082')

    DispatchAsync2(0x0009, 0x0001, lambda_4082)

    OP_65(0x03, 0x0001)

    Jump('loc_4125')

    def _loc_4094(): pass

    label('loc_4094')

    ChrTalk(
        0x0008,
        (
            '#0350000363V#740F今天的研修结束之后，\n',
            '你们就会正式成为游击士的一员了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000364V雪拉扎德正在二楼等着你们呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000365V要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4125(): pass

    label('loc_4125')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x412B
@scena.Code('func_07_412B')
def func_07_412B():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_42B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_426A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '雪、雪拉前辈。\n',
            '我听说您要带他们两个\n',
            '到柏斯那里去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯先生也不在，\n',
            '这里只有我一个人不要紧吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#024F你说什么呀。\n',
            '你要知道自己是个男人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#020F虽说工作可能比较多，\n',
            '而且有些也比较难做，\n',
            '不过大家就看你的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#020F这里就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '知、知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42B0')

    def _loc_426A(): pass

    label('loc_426A')

    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '雪拉前辈，\n',
            '我会好好努力工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也请你们路上要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42B0(): pass

    label('loc_42B0')

    Jump('loc_4B50')

    def _loc_42B3(): pass

    label('loc_42B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_437B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4348',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和约修亚啊。\n',
            '市长官邸的事情我听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼逃到天上，\n',
            '这样也拿他们没办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，大家都辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4378')

    def _loc_4348(): pass

    label('loc_4348')

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '你们背着旅行包，\n',
            '打算要去做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4378(): pass

    label('loc_4378')

    Jump('loc_4B50')

    def _loc_437B(): pass

    label('loc_437B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_4469',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4426',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，雪拉前辈……\n',
            '难道你们三人在一起工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '也许我的那部分工作会交给你，\n',
            '到时候就麻烦你了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是！\n',
            '我会尽力加油的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4466')

    def _loc_4426(): pass

    label('loc_4426')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '烦琐的工作都交给我吧，\n',
            '你们就专心去做这件工作好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4466(): pass

    label('loc_4466')

    Jump('loc_4B50')

    def _loc_4469(): pass

    label('loc_4469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_456A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4536',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '说起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有个和雪拉前辈同辈的人，\n',
            '是柏斯出身的很厉害的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且听说\n',
            '他最近也很活跃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '大家都很厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我进协会也有三年了……\n',
            '必须要继续努力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4567')

    def _loc_4536(): pass

    label('loc_4536')

    ChrTalk(
        0x00FE,
        (
            '我进协会也有三年了……\n',
            '必须要继续努力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4567(): pass

    label('loc_4567')

    Jump('loc_4B50')

    def _loc_456A(): pass

    label('loc_456A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_474F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_470A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，\n',
            '你们也是由雪拉前辈带着训练的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那和我一样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实被雪拉前辈训练\n',
            '可是我的骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为她也是王国里\n',
            '首屈一指的游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一起工作的话，你就会知道\n',
            '『银闪』的称号可不是浪得虚名的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯先生也是，\n',
            '洛连特支部多亏了前辈们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F雪拉姐果然是很厉害的人啊……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F一听别人说，\n',
            '感觉马上就不一样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_474C')

    def _loc_470A(): pass

    label('loc_470A')

    ChrTalk(
        0x00FE,
        (
            '雪拉前辈也是，\n',
            '卡西乌斯先生也是，\n',
            '洛连特支部多亏了前辈们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_474C(): pass

    label('loc_474C')

    Jump('loc_4B50')

    def _loc_474F(): pass

    label('loc_474F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_49AA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4966',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '啊，卡西乌斯先生\n',
            '要出差一段时间了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F我的老爸真是一点也不考虑到家里，\n',
            '老是随随便便就出差了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这样也能好好工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯先生可是\n',
            '我们洛连特支部的脸面人物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前所有重要的\n',
            '委托全部都是拜托\n',
            '卡西乌斯先生去完成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，最近开始\n',
            '也有些拜托雪拉前辈的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过好像大多是从\n',
            '其他支部过来的直接委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此他们才会\n',
            '经常到外地出差呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F是这样啊，我都不知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……嗯，\n',
            '因为我们都还是新人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F嗯，在家里的时候\n',
            '他只是个不良中年。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49A7')

    def _loc_4966(): pass

    label('loc_4966')

    ChrTalk(
        0x00FE,
        (
            '敬仰卡西乌斯先生的\n',
            '游击士可是很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也是其中之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49A7(): pass

    label('loc_49A7')

    Jump('loc_4B50')

    def _loc_49AA(): pass

    label('loc_49AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_4B2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4AE4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000A,
        (
            '呀，是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，利吉哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '研修好像结束了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们两个可是游击士行列里年纪最小的，\n',
            '真是后生可畏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '同为游击士的我\n',
            '以后要请你们多多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F彼此彼此，\n',
            '请您多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我马上就要去工作了。\n',
            '如果有什么事情不明白，\n',
            '不用客气尽管来问我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B2C')

    def _loc_4AE4(): pass

    label('loc_4AE4')

    ChrTalk(
        0x000A,
        (
            '我马上就要去工作了。\n',
            '如果有什么事情不明白，\n',
            '不用客气尽管来问我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B2C(): pass

    label('loc_4B2C')

    Jump('loc_4B50')

    def _loc_4B2F(): pass

    label('loc_4B2F')

    ChrTalk(
        0x000A,
        (
            '这个时候\n',
            '我没有出现在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4B50(): pass

    label('loc_4B50')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x4B54
@scena.Code('func_08_4B54')
def func_08_4B54():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0x4B59
@scena.Code('func_09_4B59')
def func_09_4B59():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 7, 0x207)),
            Expr.Return,
        ),
        'loc_4BE7',
    )

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
        'loc_4BD6',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_4BC2',
    )

    OP_A9(0x08)

    Jump('loc_4BD0')

    def _loc_4BC2(): pass

    label('loc_4BC2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 7, 0x217)),
            Expr.Return,
        ),
        'loc_4BCE',
    )

    OP_A9(0x07)

    Jump('loc_4BD0')

    def _loc_4BCE(): pass

    label('loc_4BCE')

    OP_A9(0x02)

    def _loc_4BD0(): pass

    label('loc_4BD0')

    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_4BD6(): pass

    label('loc_4BD6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4BE7',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_4BE7(): pass

    label('loc_4BE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_4DD2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D5D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '哟，你们都拿着行李，\n',
            '难道说你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '要到哪里去工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，\n',
            '我们要到柏斯那里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '柏、柏斯？\n',
            '可是，现在定期船停航了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……难道你们\n',
            '打算走路过去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F没错，其实我听说\n',
            '这段路程也不算非常远。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '虽说不是很远，\n',
            '不过我想也不会很近吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '就算是游击士也应该很辛苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你们带的东西准备充足了吗？\n',
            '路上一定要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DCF')

    def _loc_4D5D(): pass

    label('loc_4D5D')

    ChrTalk(
        0x000B,
        (
            '说起柏斯，那是个商人的城市吧。\n',
            '我最近也没去过那里呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '以前为了学习店铺的经营方法，\n',
            '曾去过那里好几次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DCF(): pass

    label('loc_4DCF')

    Jump('loc_6638')

    def _loc_4DD2(): pass

    label('loc_4DD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_4F3D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F0D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '哎呀，三个游击士聚在一块儿，\n',
            '是发生了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，有点工作要做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你们要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '说起来，\n',
            '雪拉扎德小姐\n',
            '你订的附件终于到了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '因为是通过共和国那边弄来的，\n',
            '所以花了点时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F啊，真的？\n',
            '多谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过现在正忙着，\n',
            '等下次有空了再来拿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那好，我等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F3A')

    def _loc_4F0D(): pass

    label('loc_4F0D')

    ChrTalk(
        0x000B,
        (
            '三位工作结束之后，\n',
            '还请常来小店逛逛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F3A(): pass

    label('loc_4F3A')

    Jump('loc_6638')

    def _loc_4F3D(): pass

    label('loc_4F3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_505D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5003',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '最近街上的人\n',
            '总是朝我看上看下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '大概是\n',
            '老妈到处去\n',
            '替我说亲的缘故。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '知道这事的时候\n',
            '真是羞得我脸上火辣辣的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我劝她别这么做了，\n',
            '但怎么说她也听不进，真头疼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_505A')

    def _loc_5003(): pass

    label('loc_5003')

    ChrTalk(
        0x000B,
        (
            '大概是\n',
            '老妈到处去\n',
            '替我说亲的缘故。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '知道这事的时候\n',
            '真是羞得我脸上火辣辣的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_505A(): pass

    label('loc_505A')

    Jump('loc_6638')

    def _loc_505D(): pass

    label('loc_505D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_5107',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50E1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '老妈真是的，\n',
            '忽然要我去相亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我都跟她说了\n',
            '暂时不想结婚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '可她完全当作耳旁风。\n',
            '真是怕了她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5104')

    def _loc_50E1(): pass

    label('loc_50E1')

    ChrTalk(
        0x000B,
        (
            '我还没打算\n',
            '要这么早成家啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5104(): pass

    label('loc_5104')

    Jump('loc_6638')

    def _loc_5107(): pass

    label('loc_5107')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_52D5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5270',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '哟，是艾丝蒂尔啊。\n',
            '最近很忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '都没见你来买零食吃，\n',
            '真有点寂寞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F哦……\n',
            '说起来以前研修回来的路上，\n',
            '经常走着走着你就不见了，原来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#009F什、什么嘛……\n',
            '这有什么关系啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '买零食吃\n',
            '是花季女孩的特权嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 500)

    ChrTalk(
        0x000B,
        (
            '哈哈，你们休息日有空的话，\n',
            '还请多多光顾小店啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '艾丝蒂尔喜欢的运动鞋\n',
            '我也会多多留意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52D2')

    def _loc_5270(): pass

    label('loc_5270')

    ChrTalk(
        0x000B,
        (
            '哈哈，你们休息日有空的话，\n',
            '还请多多光顾小店啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '艾丝蒂尔喜欢的运动鞋\n',
            '我也会多多留意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_52D2(): pass

    label('loc_52D2')

    Jump('loc_6638')

    def _loc_52D5(): pass

    label('loc_52D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_534A',
    )

    ChrTalk(
        0x000B,
        (
            '刚才飞行船『林德号』\n',
            '好像已经到达停机坪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '从柏斯采购来的商品\n',
            '应该也已经到了，\n',
            '得过去取回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6638')

    def _loc_534A(): pass

    label('loc_534A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_53CC',
    )

    ChrTalk(
        0x000B,
        (
            '呀，是二位游击士新人啊。\n',
            '我为你们的活跃表现感到很高兴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过小店马上就要打佯了，\n',
            '要买东西就请快点挑选好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6638')

    def _loc_53CC(): pass

    label('loc_53CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5943',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 0, 0x208)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5634',
    )

    SetScenaFlags(ScenaFlag(0x0041, 0, 0x208))
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0101,
        (
            '#001F早上好，里农叔叔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哟，这不是艾丝蒂尔和约修亚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这么大清早就来这儿还真是少见哦。\n',
            '是来买新鞋子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F啊～进了新货吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F难道是『斯托雷加』的新产品？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#018F一转眼就把来这里的目的忘掉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '父亲的吩咐已经忘了吗？ \n',
            '我们是来买《利贝尔通讯》啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F啊，对对对☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呵呵，艾丝蒂尔\n',
            '还是那么热衷于收集运动鞋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过真是很遗憾啊，\n',
            '『斯托雷加』的新产品还没有出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '《利贝尔通讯》最新号的话，\n',
            '我想今天中午才可以到货哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_61(0x0101)

    ChrTalk(
        0x0101,
        (
            '#505F中午啊……\n',
            '那时我们正在进行研修呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000B, 500)

    ChrTalk(
        0x0102,
        (
            '#010F那研修结束后我们再过来买吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那好，我给你们留着哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5940')

    def _loc_5634(): pass

    label('loc_5634')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 1, 0x209)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_585B',
    )

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
        'loc_56AF',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_569B',
    )

    OP_A9(0x08)

    Jump('loc_56A9')

    def _loc_569B(): pass

    label('loc_569B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 7, 0x217)),
            Expr.Return,
        ),
        'loc_56A7',
    )

    OP_A9(0x07)

    Jump('loc_56A9')

    def _loc_56A7(): pass

    label('loc_56A7')

    OP_A9(0x02)

    def _loc_56A9(): pass

    label('loc_56A9')

    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_56AF(): pass

    label('loc_56AF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56C0',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_56C0(): pass

    label('loc_56C0')

    SetScenaFlags(ScenaFlag(0x0041, 1, 0x209))

    ChrTalk(
        0x000B,
        (
            '这样啊……\n',
            '你们也要成为游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '真令人羡慕啊，\n',
            '我小时候也好想成为一名游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_61(0x0102)

    ChrTalk(
        0x0102,
        (
            '#011F可以说利贝尔的男孩子\n',
            '都拥有这一美好的憧憬呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……不过这里有一位女孩也是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#009F真是的～这算什么话啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '雪拉姐不也是\n',
            '一名女游击士吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#010F我没有说当女游击士有什么不好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '好啦，你们两个可要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '待会儿新的《利贝尔通讯》到货的时候\n',
            '你们可要记得来买哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5940')

    def _loc_585B(): pass

    label('loc_585B')

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
        'loc_58CE',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_58BA',
    )

    OP_A9(0x08)

    Jump('loc_58C8')

    def _loc_58BA(): pass

    label('loc_58BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 7, 0x217)),
            Expr.Return,
        ),
        'loc_58C6',
    )

    OP_A9(0x07)

    Jump('loc_58C8')

    def _loc_58C6(): pass

    label('loc_58C6')

    OP_A9(0x02)

    def _loc_58C8(): pass

    label('loc_58C8')

    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_58CE(): pass

    label('loc_58CE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_58DF',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_58DF(): pass

    label('loc_58DF')

    ChrTalk(
        0x000B,
        (
            '好啦，你们两个可要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '待会儿新的《利贝尔通讯》到货的时候\n',
            '你们可要记得来买哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5940(): pass

    label('loc_5940')

    Jump('loc_6638')

    def _loc_5943(): pass

    label('loc_5943')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 0, 0x208)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6027',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 2, 0x20A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5FB3',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0041, 2, 0x20A))
    Fade(1000)
    CameraMove(3870, 0, 1030, 0)
    ChrSetPos(0x0101, 3420, 0, 50, 0)
    ChrSetPos(0x0102, 4360, 0, 40, 0)
    ChrSetDirection(0x000B, 180, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0870000807V哟，这不是艾丝蒂尔和约修亚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000808V欢迎。\n',
            '是来买新鞋子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000809V#004F啊～进了新货吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000810V#001F难道是『斯托雷加』的新产品？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000811V#018F一转眼就把来这里的目的忘掉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000812V父亲的吩咐已经忘了吗？ \n',
            '我们是来买《利贝尔通讯》啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000813V#008F啊，对对对☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000814V呵呵，艾丝蒂尔\n',
            '还是那么热衷于收集运动鞋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000815V不过真是很遗憾啊，\n',
            '『斯托雷加』的新产品还没有出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000816V《利贝尔通讯》已经到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000817V#006F那么，我们就要一本吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000818V多谢，盛惠１００米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x64),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_5BF0',
    )

    RemoveMira(100)

    Jump('loc_5CC9')

    def _loc_5BF0(): pass

    label('loc_5BF0')

    ChrTalk(
        0x0101,
        (
            '#0010000819V#004F糟糕！\n',
            '钱不够了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000820V#017F真是的，刚才又乱花钱了。\n',
            '你又想被父亲说一顿吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000821V#018F真拿你没办法。\n',
            '算了，我先垫付着这点钱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000822V#007F哎呀，真没面子啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5CC9(): pass

    label('loc_5CC9')

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '购入',
            (TxtCtl.SetColor, 0x2),
            '利贝尔通讯 第１号',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0040, 7, 0x207))
    AddItem(0x0347, 1)

    ChrTalk(
        0x0101,
        (
            '#0010000823V#000F我家的老爸，\n',
            '很喜欢看这本杂志……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000824V#000F对了，这本杂志卖得很好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000825V对啊，还经常报道独家新闻呢。\n',
            '这杂志社有很精干的记者和摄影师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000826V杂志最近还在连载\n',
            '女王诞辰庆典等相关的报道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0041, 3, 0x20B))

    ChrTalk(
        0x000B,
        (
            '#0870000827V对了，\n',
            '你们顺利成为游击士了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000828V最后的研修怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000829V#502F嘿嘿，当然了⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000830V#004F对了，里农叔叔。\n',
            '你是怎么知道的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000831V哈哈，你们现在已经成为\n',
            '洛连特的风云人物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000832V我从顾客那里听到了许多关于你们的事情哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000833V#509F小城镇就是小城镇……\n',
            '消息传的比广播还快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000834V#019F这也是没办法的事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x001F)
    EventEnd(0x00)

    Jump('loc_6024')

    def _loc_5FB3(): pass

    label('loc_5FB3')

    TalkSetChrName('里农')

    ChrTalk(
        0x000B,
        (
            '恭喜你们游击士考试合格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '为了这值得庆祝的一刻，\n',
            '买点东西作为纪念如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我会给你们打折的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_6024(): pass

    label('loc_6024')

    Jump('loc_6638')

    def _loc_6027(): pass

    label('loc_6027')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 2, 0x20A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_64BE',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0041, 2, 0x20A))
    Fade(1000)
    CameraMove(3870, 0, 1030, 0)
    ChrSetPos(0x0101, 3420, 0, 50, 0)
    ChrSetPos(0x0102, 4360, 0, 40, 0)
    ChrSetDirection(0x000B, 180, 0)
    OP_0D()
    TalkSetChrName('里农')

    ChrTalk(
        0x000B,
        (
            '#0870000835V哟，这不是艾丝蒂尔和约修亚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000836V欢迎。\n',
            '顺利成为游击士了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_61(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010000837V#502F嘿嘿，当然了⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000838V#502F现在的我可是正牌游击士哦。\n',
            '里农叔叔，从今天起叫我\n',
            '『超级游击士·艾丝蒂尔』就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000839V#010F对了，里农先生。\n',
            '《利贝尔通讯》到货了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000840V嗯，刚过中午就到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000841V#009F喂，没看到我正在高兴吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000842V#007F……算了，就买一本吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('里农')

    ChrTalk(
        0x000B,
        (
            '#0870000843V多谢，盛惠１００米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x64),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_6292',
    )

    RemoveMira(100)

    Jump('loc_636B')

    def _loc_6292(): pass

    label('loc_6292')

    ChrTalk(
        0x0101,
        (
            '#0010000844V#004F糟糕！\n',
            '钱不够了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000845V#017F真是的，刚才又乱花钱了。\n',
            '你又想被父亲说一顿吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000846V#018F真拿你没办法。\n',
            '算了，我先垫付着这点钱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000847V#007F哎呀，真没面子啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_636B(): pass

    label('loc_636B')

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '购入',
            (TxtCtl.SetColor, 0x2),
            '利贝尔通讯 第１号',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0040, 7, 0x207))
    AddItem(0x0347, 1)

    ChrTalk(
        0x0101,
        (
            '#0010000848V#000F我家的老爸，\n',
            '很喜欢看这本杂志……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000849V#000F对了，这本杂志卖得很好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000850V对啊，还经常报道独家新闻呢。\n',
            '这杂志社有很精干的记者和摄影师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000851V杂志最近还在连载\n',
            '女王诞辰庆典等相关的报道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x001F)
    EventEnd(0x00)

    Jump('loc_6638')

    def _loc_64BE(): pass

    label('loc_64BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 3, 0x20B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_65C7',
    )

    SetScenaFlags(ScenaFlag(0x0041, 3, 0x20B))

    ChrTalk(
        0x0101,
        (
            '#505F对了，里农老板。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#505F你怎么知道我们的研修\n',
            '是今天结业的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哈哈，你们现在已经成为\n',
            '洛连特的风云人物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我从顾客那里听到了许多关于你们的事情哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#509F小城镇就是小城镇……\n',
            '消息传的比广播还快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F这也是没办法的事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6638')

    def _loc_65C7(): pass

    label('loc_65C7')

    TalkSetChrName('里农')

    ChrTalk(
        0x000B,
        (
            '恭喜你们游击士考试合格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '为了这值得庆祝的一刻，\n',
            '买点东西作为纪念如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我会给你们打折的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6638(): pass

    label('loc_6638')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x663C
@scena.Code('func_0A_663C')
def func_0A_663C():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_674D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66DC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '拿着这么多的行李，\n',
            '难道说你们要去旅行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅行时要是遇到适合做我家媳妇的人选，\n',
            '记得回来和我说说哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会立刻飞奔而去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_674A')

    def _loc_66DC(): pass

    label('loc_66DC')

    ChrTalk(
        0x00FE,
        (
            '拿着这么多的行李，\n',
            '难道说你们要去旅行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅行时要是遇到适合做我家媳妇的人选，\n',
            '记得回来和我说说哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_674A(): pass

    label('loc_674A')

    Jump('loc_6F5F')

    def _loc_674D(): pass

    label('loc_674D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_6903',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68DF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x000C, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '……哎呀，你的头发是银色的呢，\n',
            '难道你是外国人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F您说我吗？\n',
            '嗯，也可以这样说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，年龄倒是正合适，\n',
            '不过作为新娘好像太惹眼了些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F啊？新娘？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F（雪拉姐作新娘啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F（首先对方酒量不过关\n',
            '　就没办法当她老公啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F（哇，这可不是闹着玩的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F喂，你们两个，\n',
            '在那儿嘀嘀咕咕说些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6900')

    def _loc_68DF(): pass

    label('loc_68DF')

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '找媳妇可真不容易啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6900(): pass

    label('loc_6900')

    Jump('loc_6F5F')

    def _loc_6903(): pass

    label('loc_6903')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_6B69',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B26',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '你是卡西乌斯家的那个……\n',
            '叫艾丝蒂尔的孩子是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，看起来\n',
            '又健康又开朗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么样，\n',
            '愿意嫁到我们家来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#501F我、我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然太年轻了点，不过反正最近\n',
            '大家都不大在意年龄差距的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F等、等一下。\n',
            '我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唔，果然不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家的儿子倒\n',
            '的确是没有你身边\n',
            '那位黑发小哥长得帅……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '你可要让\n',
            '艾丝蒂尔幸福哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F哦、哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F（好像被老婆婆误会了呢……）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（哈哈……\n',
            '　就先顺着她说吧，\n',
            '　否则恐怕脱不了身了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B66')

    def _loc_6B26(): pass

    label('loc_6B26')

    ChrTalk(
        0x00FE,
        (
            '最近女孩子\n',
            '也都出去工作了，\n',
            '要找媳妇还真不是那么容易呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B66(): pass

    label('loc_6B66')

    Jump('loc_6F5F')

    def _loc_6B69(): pass

    label('loc_6B69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_6BD8',
    )

    ChrTalk(
        0x00FE,
        (
            '我决定要悄悄地替儿子\n',
            '物色媳妇的人选。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我去了城里所有年龄合适\n',
            '又贤淑端庄的姑娘家帮他说媒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F5F')

    def _loc_6BD8(): pass

    label('loc_6BD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_6CCB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6C6E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '儿子好像满脑子\n',
            '都是店里的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但人要成家立业、\n',
            '生儿育女后才算是真正的成熟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这当老妈的\n',
            '是不是该推他一把呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CC8')

    def _loc_6C6E(): pass

    label('loc_6C6E')

    ChrTalk(
        0x00FE,
        (
            '人要成家立业、\n',
            '生儿育女后才算是真正的成熟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这当老妈的\n',
            '是不是该推他一把呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CC8(): pass

    label('loc_6CC8')

    Jump('loc_6F5F')

    def _loc_6CCB(): pass

    label('loc_6CCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_6D30',
    )

    ChrTalk(
        0x00FE,
        (
            '里农很勤快，\n',
            '是个好孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但作父母的还是\n',
            '希望他快点讨个老婆，\n',
            '好让我们放心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F5F')

    def _loc_6D30(): pass

    label('loc_6D30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_6DDF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6DAA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '已经到傍晚时分了啊，\n',
            '我也该准备去吃饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '……里农那孩子\n',
            '能够早点讨个\n',
            '会做饭的老婆就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6DDC')

    def _loc_6DAA(): pass

    label('loc_6DAA')

    ChrTalk(
        0x000C,
        (
            '里农那孩子\n',
            '能够早点讨个\n',
            '会做饭的老婆就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6DDC(): pass

    label('loc_6DDC')

    Jump('loc_6F5F')

    def _loc_6DDF(): pass

    label('loc_6DDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_6EDE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6EA2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '里农开的店已经走上正轨了，\n',
            '这可比什么都好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '看着各种新商品\n',
            '从飞艇上运送下来，\n',
            '人们购物也增添几分乐趣呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '自从导力器发明以来，\n',
            '人们的生活就变得方便了许多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6EDB')

    def _loc_6EA2(): pass

    label('loc_6EA2')

    ChrTalk(
        0x000C,
        (
            '自从导力器发明以来，\n',
            '人们的生活就变得方便了许多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6EDB(): pass

    label('loc_6EDB')

    Jump('loc_6F5F')

    def _loc_6EDE(): pass

    label('loc_6EDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F3A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '呼～～果然还是\n',
            '清晨的空气最新鲜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '接下来要给可爱的\n',
            '花朵们浇水了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F5F')

    def _loc_6F3A(): pass

    label('loc_6F3A')

    ChrTalk(
        0x000C,
        (
            '接下来要给可爱的\n',
            '花朵们浇水了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F5F(): pass

    label('loc_6F5F')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x6F63
@scena.Code('func_0B_6F63')
def func_0B_6F63():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6FC4',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000D,
        (
            '鲁克和帕特他们\n',
            '不会有事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我都已经\n',
            '那样拼命阻止了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '呜呜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7002')

    def _loc_6FC4(): pass

    label('loc_6FC4')

    ChrTalk(
        0x000D,
        (
            '艾丝蒂尔姐姐，\n',
            '约修亚哥哥，\n',
            '那两个人就拜托你们了，呜呜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7002(): pass

    label('loc_7002')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x7006
@scena.Code('func_0C_7006')
def func_0C_7006():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 7, 0x22F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7095',
    )

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    OP_69(0x0009, 800)

    @scena.Lambda('lambda_702A')
    def lambda_702A():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_702A)

    @scena.Lambda('lambda_7038')
    def lambda_7038():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_7038)

    ChrTalk(
        0x0009,
        (
            '#0030000498V#024F怎么了，想出去吗？\n',
            '研修还没结束呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1000, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_7095(): pass

    label('loc_7095')

    Return()

# id: 0x000D offset: 0x7096
@scena.Code('func_0D_7096')
def func_0D_7096():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 7, 0x22F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7125',
    )

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    OP_69(0x0009, 800)

    @scena.Lambda('lambda_70BA')
    def lambda_70BA():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_70BA)

    @scena.Lambda('lambda_70C8')
    def lambda_70C8():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_70C8)

    ChrTalk(
        0x0009,
        (
            '#0030000499V#024F怎么了，想出去吗？\n',
            '研修还没结束呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_7125(): pass

    label('loc_7125')

    Return()

# id: 0x000E offset: 0x7126
@scena.Code('func_0E_7126')
def func_0E_7126():
    EventBegin(0x00)
    OP_4A(0x0008, 0)
    ChrClearFlags(0x0009, 0x0080)
    MapClearFlags(0x00000001)
    ChrSetPos(0x0009, -764, 0, 114882, 90)
    ChrSetPos(0x0101, 811, 0, 115528, 270)
    ChrSetPos(0x0102, 811, 0, 114132, 270)
    CameraMove(342, 0, 115532, 0)
    CameraSetDistance(3000, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x0009,
        (
            '#0030000624V#020F最后的研修就是\n',
            '完成工作之后的报告方法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000625V#020F不管是什么工作，\n',
            '完成之后一定要到协会报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000626V#020F解决了什么样的事情、解决事情的经过，\n',
            '这些都需要一一汇报，\n',
            '因为工作报告也是游击士应履行的职责。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000627V#020F受理报告的地点是各个协会的接待处。\n',
            '洛连特这里的负责人\n',
            '就是你们两人都很熟悉的爱娜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000628V#020F啊，还要记得的是\n',
            '工作报酬也是在协会里获得的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000629V#740F今后就请多多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000630V#020F好了，你们两人\n',
            '就试试向爱娜报告一下工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※站在柜台附近时会出现『TALK』的标记，\n',
            '　用右键点击会出现选择菜单。\n',
            '　在前台报告工作的时候在菜单上选择『报告』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_4B(0x0008, 0)
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x741C
@scena.Code('func_0F_741C')
def func_0F_741C():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    Sleep(500)

    OP_2A(0x000A, 0xFFFF)

    If(
        (
            (Expr.Eval, "OP_29(0x000A, 0x00, 0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_743B',
    )

    EventEnd(0x01)

    Return()

    def _loc_743B(): pass

    label('loc_743B')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※已在公告板上确认的\n',
            '　工作详情和工作中的要点\n',
            '　都会自动记录在游击士手册上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※手册在Camp内［Item］栏的［书籍］中。\n',
            ' 或者点击画面右下角显示的手册图标\n',
            ' 也可以查看到所有工作任务及其相关的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    Fade(1000)
    CameraMove(-91, 0, 115143, 0)
    TerminateThread(0x0009, 0xFF)
    ChrSetPos(0x0009, -764, 0, 114882, 90)
    ChrSetPos(0x0101, 811, 0, 115528, 270)
    ChrSetPos(0x0102, 811, 0, 114132, 270)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0030000368V#020F嗯，可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000369V#020F你们两人都仔细确认过\n',
            '公告板上的内容了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000370V#020F对游击士来说，\n',
            '时常留意公告板是基本中的基本。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000371V#020F经常确认是不是有紧急的工作，\n',
            '对游击士来说，也是一个重要的职责哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000372V#007F呼……这么多的职责，\n',
            '光是听就已经觉得快窒息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000373V#010F的确有很多规则，\n',
            '因为游击士要做的都是需要负责任的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000374V#010F如果抱着敷衍了事的态度，\n',
            '是无法胜任游击士这种职业的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000375V#006F……嗯，也对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000376V得更加努力去适应才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000377V#020F呵呵，\n',
            '是不是已经有所觉悟了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000378V#001F是的。\n',
            '完全没问题了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000379V#020F那么……\n',
            '趁热情还没有消退，\n',
            '马上进行下一项研修吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000380V#010F这次是什么内容呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000381V#020F要去对面梅尔达斯先生的工房。\n',
            '我希望你们学习一下\n',
            '工房的主要用途和具体操作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000382V#020F因为我们占用了\n',
            '工房的营业时间去请教人家，\n',
            '所以你们不要做出失礼的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000383V#501F好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    NewScene('ED6_DT01/T0120._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x7941
@scena.Code('func_10_7941')
def func_10_7941():
    EventBegin(0x00)
    CameraMove(740, 0, 117300, 0)
    CameraSetDistance(3000, 0)
    ChrSetPos(0x0101, 780, 0, 115570, 0)
    ChrSetPos(0x0103, -440, 0, 116340, 45)
    ChrSetPos(0x0102, 1860, 0, 116020, 0)
    TerminateThread(0x0008, 0xFF)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0350020087V#740F——事情我已经了解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350020088V说实话，继卡西乌斯先生之后，\n',
            '雪拉扎德也离开的话，\n',
            '这里的人手会相当紧张……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350020089V不过，毕竟事关卡西乌斯先生的安危。\n',
            '请不要挂念太多，放心地出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020090V#020F多谢你，爱娜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020091V#021F呵呵，利吉那小子，\n',
            '你就使劲地使唤他吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020092V以平常的工作量来算，\n',
            '就算再加三倍我想也没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020093V#506F真、真是可怜呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350020094V#741F呵呵，万一不行的话，\n',
            '还可以向王都支部请求支援，\n',
            '所以你们不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350020095V#740F对了，雪拉扎德。\n',
            '能耽误你一些时间吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350020096V关于你刚接手的那个工作\n',
            '有点事情要说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020097V#020F嗯，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030020098V#020F艾丝蒂尔、约修亚。\n',
            '你们在二楼等我一会儿好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020099V马上就会说完的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020100V#010F#4P好的，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020101V#505F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020102V#501F那个，雪拉姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020103V如果要等的话，\n',
            '我想去钟楼那里可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020104V有点……\n',
            '有点话想和一个人说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020105V#014F#4P……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020106V#026F是吗……\n',
            '嗯，那好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020107V#020F那么，\n',
            '一会儿就在钟楼的前面会合吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020108V等办完事情，\n',
            '我马上就过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020109V#000F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020110V#501F约修亚，走吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020111V#014F#4P啊，好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    FormationDelMember(0x02, 0xFF)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T0100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x7EAB
@scena.Code('func_11_7EAB')
def func_11_7EAB():
    EventBegin(0x00)
    CameraMove(590, 0, 117600, 0)
    OP_67(0, 8010, -10000, 0)
    CameraSetDistance(2560, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 780, 0, 115570, 0)
    ChrSetPos(0x0103, -440, 0, 116340, 45)
    ChrSetPos(0x0102, 1860, 0, 116020, 0)
    TerminateThread(0x0008, 0xFF)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0350011326V#742F真是不得了呢。\n',
            '没想到犯人竟然是空贼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011327V#742F被他们逃掉也是没办法的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011328V#025F不，这次是我的失误。\n',
            '都是因为我一时大意才会这样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011329V果然，离老师的境界还远着呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011330V#003F哎呀，不是雪拉姐的责任啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011331V#003F要怪就怪我一时冲动，\n',
            '才会让他们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011332V#015F#4P……我也疏忽大意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0102, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x001A, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_8106',
    )

    ChrTalk(
        0x0103,
        (
            '#0030011333V#020F不，你们已经做得很好了。\n',
            '在市长家的现场调查十分完美。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81BB')

    def _loc_8106(): pass

    label('loc_8106')

    If(
        (
            (Expr.Eval, "OP_29(0x001A, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_8160',
    )

    ChrTalk(
        0x0103,
        (
            '#0030011334V#020F不，你们已经做得很好了。\n',
            '在市长家的现场调查也算可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81BB')

    def _loc_8160(): pass

    label('loc_8160')

    If(
        (
            (Expr.Eval, "OP_29(0x001A, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_81BB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030011335V#020F不，你们已经做得很好了。\n',
            '虽然在市长家的现场调查不怎么样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_81BB(): pass

    label('loc_81BB')

    ChrTurnDirection(0x0103, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030011336V#027F爱娜……\n',
            '他们可以获得推荐的资格吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350011337V#741F嗯，当然可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 0)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010011338V#004F推荐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011339V#014F#4P这是什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350011340V#740F在这之前，\n',
            '先把这次调查的报酬支付给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_28(0x001A, 0x04, 0x10)
    OP_AF(0x04, 0x001A)
    OP_28(0x001B, 0x04, 0x10)
    OP_28(0x001B, 0x04, 0x20)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0350011341V#740F然后……\n',
            '你们收下这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0330, 1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '正游击士资格的推荐信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010011342V#004F这、这个是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350011343V#740F现在你们是准游击士。\n',
            '也就是说还是在见习阶段。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011344V要成为正游击士的话，\n',
            '还必须取得王国所有地区支部的\n',
            '推荐信才可以哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011345V而这就是洛连特支部的推荐信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011346V#008F可、可以吗？\n',
            '给我们这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011347V#014F#4P而且我听说，\n',
            '要成为正游击士，\n',
            '必须要做出很优秀的成绩才……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350011348V#741F你们完成的三个任务和这次的活跃表现，\n',
            '作为成绩来说已经完全足够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011349V#740F……不过，\n',
            '这也只是洛连特地区的成绩而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0102, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011350V#027F你们还要在其他地区作出像样的成绩，\n',
            '这样才能取得所有支部的推荐资格。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011351V#027F柏斯、卢安、蔡斯，\n',
            '还有王都格兰赛尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011352V#021F要走的路还很长呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010011353V#001F可是可是，我真的很开心！\n',
            '努力工作得到回报了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010011354V#006F约修亚，这样的话，\n',
            '我们不去其他地方不行呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020011355V#019F#4P哈哈，就知道你会这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011356V#010F虽然我也赞成这样……\n',
            '不过我们也不能擅自决定啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011357V#010F等父亲回来之后再商量一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011358V#006F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(195, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    @scena.Lambda('lambda_8806')
    def lambda_8806():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8806)

    @scena.Lambda('lambda_8814')
    def lambda_8814():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8814)

    @scena.Lambda('lambda_8822')
    def lambda_8822():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_8822)

    Sleep(1000)

    ChrSetDirection(0x0008, 315, 400)

    ChrTalk(
        0x0008,
        (
            '#0350011359V#743F哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011360V#501F啊，那个是通信器吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8886')
    def lambda_8886():
        CameraMove(-660, 0, 118480, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8886)

    ChrWalkTo(0x0008, -430, 0, 118990, 2000, 0x00)
    ChrSetDirection(0x0008, 0, 400)
    Sleep(500)

    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x01, 0x00, 0x00FF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_23(0x00C3)
    PlaySE(131, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0350011361V#740F#5P你好，这里是游击士协会，\n',
            '利贝尔王国·洛连特支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011362V#743F啊，很久没有联系了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0350011363V#742F#5P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011364V#742F……………是真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011365V#744F那、那真是……\n',
            '不得了的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010011366V#505F发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011367V#012F#4P嗯……看来好像是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350011368V#743F#5P嗯，没错。\n',
            '确实是前几天出发的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_21()
    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0350011369V#742F#3S#5P什么！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)
    PlayBGM(81)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0350011370V#745F#5P不、不好意思。\n',
            '事出突然，实在不敢相信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011371V好，我明白了。\n',
            '家属方面我会通知的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011372V#742F……没关系。\n',
            '他们本身也是游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011373V好……\n',
            '如果有什么消息请赶快联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010011374V#505F爱娜姐姐，发生什么事情了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011375V#020F真是少见啊。\n',
            '让你吃惊到那种程度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011376V对了，是哪里来的联络？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0008)

    @scena.Lambda('lambda_8CD9')
    def lambda_8CD9():
        CameraMove(590, 0, 117600, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8CD9)

    ChrSetDirection(0x0008, 90, 400)
    ChrWalkTo(0x0008, 750, 0, 118600, 2000, 0x00)
    ChrSetDirection(0x0008, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0350011377V#742F是柏斯支部的。\n',
            '……发生了很严重的事情啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011378V定期船『林德号』\n',
            '在柏斯地区失去了音讯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010011379V#004F啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011380V#012F#4P到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350011381V#744F详细情况还不清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011382V据说王国军已经出动了，\n',
            '在附近进行着大规模的搜索行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011383V也因为这件事，\n',
            '其他航线的定期船也要暂时停航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011384V#022F原来如此……\n',
            '难怪飞艇坪会聚集那么多人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350011385V#745F而、而且……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011386V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011387V#505F爱娜姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350011388V#742F艾丝蒂尔、约修亚。\n',
            '你们一定要保持镇定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011389V#742F失踪的定期船似乎正是……\n',
            '卡西乌斯先生所乘坐的那一艘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010011390V#580F#3S…………啊。',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011391V#016F#4P怎么会……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011392V#023F开、开玩笑吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350011393V#742F乘客名单上似乎有他的名字。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011394V利贝尔游击士协会，\n',
            '洛连特支部所属，正游击士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350011395V卡西乌斯·布莱特，４５岁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000009C4)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS045._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    WaitEffect(0x11, 0x00)
    SetScenaFlags(ScenaFlag(0x004D, 1, 0x269))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xF0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-87490, 0, 61990, 0)
    FadeIn(0, 0)

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
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_91BA',
    )

    ShowSaveMenu()

    def _loc_91BA(): pass

    label('loc_91BA')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    Sleep(2000)

    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    NewScene('ED6_DT01/T0301._SN', 3, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x9209
@scena.Code('func_12_9209')
def func_12_9209():
    EventBegin(0x00)
    OP_0D()
    CreateThread(0x0101, 0x00, 0x00, func_13_93E7)
    CreateThread(0x0102, 0x00, 0x00, func_14_9416)
    CreateThread(0x0101, 0x01, 0x00, func_15_944A)
    OP_4A(0x0008, 0)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_A5(0x0003)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0350000255V#740F哎呀，早啊。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000256V#001F爱娜姐姐，早上好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000257V#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_A5(0x0000)
    OP_A5(0x0001)
    OP_A5(0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010000258V#000F#4P雪拉姐已经来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000259V#740F嗯，在二楼等着呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000260V今天的研修结束之后，\n',
            '就可以正式成为游击士的一员了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000261V你们俩要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000262V#006F#4P嗯，谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000263V#010F我们会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_4B(0x0008, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    SetScenaFlags(ScenaFlag(0x0040, 4, 0x204))
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x93E7
@scena.Code('func_13_93E7')
def func_13_93E7():
    OP_A6(0x0000)
    ChrWalkTo(0x00FE, 2200, 0, 113000, 3000, 0x00)
    ChrWalkTo(0x00FE, 1500, 0, 116000, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0014 offset: 0x9416
@scena.Code('func_14_9416')
def func_14_9416():
    OP_A6(0x0001)
    Sleep(200)

    ChrWalkTo(0x00FE, 2000, 0, 112000, 3000, 0x00)
    ChrWalkTo(0x00FE, 700, 0, 115200, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0015 offset: 0x944A
@scena.Code('func_15_944A')
def func_15_944A():
    OP_A6(0x0003)
    CameraMove(1500, 0, 116000, 1200)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_A6(0x0003)
    CameraMove(740, 0, 117400, 1500)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x0016 offset: 0x9479
@scena.Code('func_16_9479')
def func_16_9479():
    FadeIn(1000, 0)
    CameraMove(-90, 0, 72340, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetPos(0x0012, -400, 700, 73300, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0013, -100, 700, 73300, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0014, 200, 700, 73300, 0)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0015, 500, 700, 73300, 0)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0016, 800, 700, 73300, 0)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetPos(0x0009, 200, 200, 74100, 180)
    ChrSetFlags(0x0101, 0x0008)
    ChrSetFlags(0x0102, 0x0008)
    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0009, 0xFF)
    CreateThread(0x0101, 0x00, 0x00, func_18_BB65)
    CreateThread(0x0102, 0x00, 0x00, func_1C_BC0E)
    CreateThread(0x0009, 0x00, 0x00, func_1D_BC74)
    ChrSetSubChip(0x0012, 8)
    ChrSetSubChip(0x0013, 9)
    ChrSetSubChip(0x0014, 10)
    ChrSetSubChip(0x0015, 11)
    ChrSetSubChip(0x0016, 7)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetSubChip(0x0009, 1)
    ChrSetFlags(0x0009, 0x0002)
    OP_0D()
    Sleep(1000)

    ChrSetSubChip(0x0009, 0)
    Sleep(200)

    Fade(1000)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetSubChip(0x0009, 1)
    ChrSetSubChip(0x0016, 12)
    Sleep(1000)

    OP_99(0x0009, 0x01, 0x03, 1000)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0030000264V#026F#2P………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000265V『星星』和『倒吊男』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000266V『隐者』和『魔术师』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000267V最后是逆位置的『命运之轮』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000268V#025F这可难办了。\n',
            '该怎么解读好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, -4850, -2000, 66000, 0)
    ChrClearFlags(0x0101, 0x0008)

    ChrTalk(
        0x0101,
        (
            '#0010000269V#2P雪拉姐，早啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_99(0x0009, 0x03, 0x01, 1200)
    Sleep(100)

    Fade(1000)
    ChrSetSubChip(0x0016, 12)
    ChrClearFlags(0x0016, 0x0080)
    Sleep(400)

    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 8)
    ChrSetSubChip(0x0009, 0)
    Sleep(1000)

    @scena.Lambda('lambda_9737')
    def lambda_9737():
        CameraMove(-2250, 0, 73500, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_9737)

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A5(0x0000)
    OP_A5(0x0001)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0030000270V#023F#2P噢，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000271V#023F真是少见啊。\n',
            '你们这么早就来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000272V#006F嘿嘿，因为是最后的研修嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000273V而且通过考试之后\n',
            '我们就可以成为游击士啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000274V#025F#2P唉……\n',
            '难得你这么有干劲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000275V#020F好吧！为了回应你的气势，\n',
            '今天的训练也会格外严格。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000276V你们做好心理准备吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000277V#009F啊～怎么会呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000278V#022F#2P多·说·无·用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000279V每次教你的东西\n',
            '总是左耳进右耳出的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000280V这样做也是为了\n',
            '让你这个漏勺一样的脑子牢牢记住啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010000281V#504F哎～约修亚！\n',
            '雪拉姐欺负我啦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000282V#010F没问题的，雪拉姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000283V艾丝蒂尔虽然讨厌学习，\n',
            '平时也不怎么预习和复习……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000284V而且做事不假思索，\n',
            '经常做老好人又喜欢多管闲事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000285V不过敏锐的第六感却是首屈一指的，\n',
            '导力器的运用也在实战中得到过锻炼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000286V#025F#2P呵呵，既然如此，\n',
            '也只好期待她的表现了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010000287V#509F我说约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000288V怎么听起来你说的\n',
            '全是些胳膊肘向外拐的话啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020000289V#019F你想太多了。\n',
            '我只是坦白说出你的优点而已嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000290V#007F真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000291V#501F啊，对了雪拉姐。\n',
            '你用塔罗牌在占卜什么啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000292V看你一脸心事重重的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000293V#522F#2P啊，这个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000294V我本来想试试占卜一下\n',
            '最近身边可能会发生的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000295V可似乎状态不太好，\n',
            '怎么也解读不出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000296V#505F解读不出来？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000297V#014F咦……\n',
            '会有这样的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000298V#020F#2P隐藏于形态的涵义越深，\n',
            '相应地也就越难让人解读呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000299V#020F算了，先不管这个了。\n',
            '开始最后的研修吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(500, 0, -1)
    Sleep(1000)

    ChrSetPos(0x0101, 500, 0, 72250, 0)
    ChrSetPos(0x0102, -500, 0, 72250, 0)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetSubChip(0x0009, 0)
    CameraMove(-440, 0, 73390, 0)
    FadeIn(500, 0)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0030000300V#020F#2P先把至今为止所学习的内容\n',
            '从头到尾复习一遍吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000301V#020F因为这些都是作为游击士\n',
            '所必须具备的最低限度的常识。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000302V#020F特别是艾丝蒂尔，\n',
            '好好听着哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000303V#006F是～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -56)
    OP_0D()
    Sleep(500)

    def _loc_9F2E(): pass

    label('loc_9F2E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A8B0',
    )

    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030000304V',
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '#020F想知道关于哪方面的内容？',
            TxtCtl.Enter,
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

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_A02B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_9FDD',
    )

    Menu(
        0,
        200,
        100,
        0,
        (
            TXT(0x00, '【导力器是什么？】\n'),
            TXT(0x01, '【游击士协会是什么？】\n'),
            TXT(0x02, '【关于利贝尔王国】\n'),
            TXT(0x03, '【放弃】\n'),
        ),
    )

    Jump('loc_A028')

    def _loc_9FDD(): pass

    label('loc_9FDD')

    Menu(
        0,
        200,
        100,
        0,
        (
            TXT(0x00, '【导力器是什么？】\n'),
            TXT(0x01, '【游击士是什么？】\n'),
            TXT(0x02, '【关于利贝尔王国】\n'),
            TXT(0x03, '【放弃】\n'),
        ),
    )

    def _loc_A028(): pass

    label('loc_A028')

    Jump('loc_A06D')

    def _loc_A02B(): pass

    label('loc_A02B')

    Menu(
        0,
        200,
        100,
        0,
        (
            TXT(0x00, '【导力器是什么？】\n'),
            TXT(0x01, '【游击士是什么？】\n'),
            TXT(0x02, '【关于利贝尔王国】\n'),
        ),
    )

    def _loc_A06D(): pass

    label('loc_A06D')

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
        (0x00000000, 'loc_A097'),
        (0x00000001, 'loc_A09A'),
        (0x00000002, 'loc_A0AE'),
        (0x00000003, 'loc_A0C2'),
        (-1, 'loc_A0CF'),
    )

    def _loc_A097(): pass

    label('loc_A097')

    Jump('loc_A0CF')

    def _loc_A09A(): pass

    label('loc_A09A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_A0AB',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A0AB(): pass

    label('loc_A0AB')

    Jump('loc_A0CF')

    def _loc_A0AE(): pass

    label('loc_A0AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_A0BF',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A0BF(): pass

    label('loc_A0BF')

    Jump('loc_A0CF')

    def _loc_A0C2(): pass

    label('loc_A0C2')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A0CF')

    def _loc_A0CF(): pass

    label('loc_A0CF')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_A0EF'),
        (0x00000001, 'loc_A2E2'),
        (0x00000002, 'loc_A42A'),
        (0x00000004, 'loc_A6DC'),
        (0x00000003, 'loc_A89B'),
        (-1, 'loc_A8AB'),
    )

    def _loc_A0EF(): pass

    label('loc_A0EF')

    OP_AD('ED6_DT04/C_VIS000._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030000305V#020F使用一种被称为『导力』的能源来驱动的\n',
            '机械装置单元就叫做导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000306V#020F导力器内部装有用\n',
            '七耀石加工而成的结晶回路，\n',
            '根据其不同结构能够引起各种各样的现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000307V#020F从发明至今\n',
            '虽只经历了５０年左右的时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000308V#020F但现今无论是照明、取暖等日用品，\n',
            '还是兵器、魔法、飞艇等高科技工具，\n',
            '各个领域内，导力器的力量都已得到广泛应用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000309V#020F顺带一提，\n',
            '实用导力器的技术革新一般通称为『导力革命』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(500)

    Jump('loc_A8AB')

    def _loc_A2E2(): pass

    label('loc_A2E2')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    OP_AD('ED6_DT04/C_VIS002._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030000310V#020F游击士是一种\n',
            '为保护地区和平及百姓安全，\n',
            '而进行调查与战斗活动的专家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000311V#020F不只是消灭魔兽、制止犯罪，\n',
            '还有像护送货物、寻找失物等\n',
            '对地区有贡献的工作都是游击士所理应承担的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000312V#020F管理各地游击士的机构，\n',
            '就是分布在大陆各地的游击士协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(500)

    Jump('loc_A8AB')

    def _loc_A42A(): pass

    label('loc_A42A')

    OP_AD('ED6_DT04/C_VIS001._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030000313V#020F我们所居住的这个利贝尔王国，\n',
            '位于塞姆里亚大陆西部，\n',
            '是一个拥有悠久历史传统和丰富自然资源的国家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000314V#020F身为整个大陆内为数不多的七耀石产地之一，\n',
            '利贝尔利用这个优势进行各种高端的导力器开发，\n',
            '因此王国也以拥有最尖端的导力技术而闻名整个大陆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000315V#020F对于利贝尔王国来说，\n',
            '导力技术是其能与周边的大国进行抗衡，\n',
            '保持国家独立性的重要支柱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000316V#020F１０年前遭到埃雷波尼亚帝国侵略之时，\n',
            '在最后关头拯救了王国的，\n',
            '正是使用以导力引擎驱动的飞艇所进行的反攻作战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000317V#020F嗯，虽说现在王国和帝国的关系仍很微妙，\n',
            '不过依靠艾莉茜雅女王陛下英明的政治手腕，\n',
            '现在的利贝尔，大致上可说是和平安定的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(500)

    Jump('loc_A8AB')

    def _loc_A6DC(): pass

    label('loc_A6DC')

    OP_AD('ED6_DT04/C_VIS002._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030000318V#020F游击士协会，\n',
            '是５０年前设立的一个世界范围的游击士联合组织。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000319V#020F在利贝尔王国以外的\n',
            '国家和地区都设有其支部，\n',
            '协会对各地的和平作出了很大贡献。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000320V#020F而且因为协会具有国际性和中立性，\n',
            '所以也曾经承担过仲裁国家间纠纷的工作。\n',
            '在终止１０年前的战争一事中也发挥了重要作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0030000321V#025F不过，经常被委托做各种各样的工作，\n',
            '协会也一直为人手不足的问题所困扰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(500)

    Jump('loc_A8AB')

    def _loc_A89B(): pass

    label('loc_A89B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_A8AB')

    def _loc_A8AB(): pass

    label('loc_A8AB')

    OP_56(0x00)

    Jump('loc_9F2E')

    def _loc_A8B0(): pass

    label('loc_A8B0')

    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0030000322V#020F#2P那么……\n',
            '复习就到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000323V#020F今天要做的事情堆积如山，\n',
            '我们还是赶快进行实地研修吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000324V#505F我说雪拉姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000325V那个实地研修，\n',
            '和我们之前做的研修有什么不一样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000326V#020F#2P所谓实地，\n',
            '就是要亲自去现场体验啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000327V#020F从现在开始，\n',
            '我要你们两个亲身去体会一下\n',
            '身为游击士必须要做的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000328V#501F也就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000329V不是坐在桌子前面\n',
            '傻乎乎地埋头学习啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000330V#027F#2P嗯，当然不是啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000331V#027F其实我希望你们到各种地方去，\n',
            '让自己的身体真正活动起来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000332V#027F尽情挥洒汗水，\n',
            '好好体会当中的乐趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000333V#001F嘿嘿嘿，得救了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000334V#001F如果是运动之类的话，\n',
            '那可比之前的研修要轻松多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000335V#001F真是……之前还害我担心得要死。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000336V#010F#3P怎么好像突然精神起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000337V#026F#2P看你这么开心，\n',
            '我希望你能笑到最后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000338V#020F……那么，\n',
            '我们去第一个实地研修地点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000339V#508F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-91, 0, 115143, 0)
    OP_4A(0x0008, 0)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 1)
    ChrClearFlags(0x0009, 0x0004)
    ChrClearFlags(0x0009, 0x0010)
    ChrSetPos(0x0009, -764, 0, 114882, 90)
    ChrSetPos(0x0101, 811, 0, 115528, 270)
    ChrSetPos(0x0102, 811, 0, 114132, 270)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0030000340V#020F第一项研修，\n',
            '是确认工作内容。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000341V#020F……在此之前，\n',
            '我有样东西要交给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0030000342V#020F爱娜。\n',
            '准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000343V#740F嗯，准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 90, 400)

    ChrTalk(
        0x0009,
        (
            '#0030000344V#020F可以了，\n',
            '你们两个到爱娜那里去拿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    OP_4B(0x0008, 0)
    EventEnd(0x00)

    @scena.Lambda('lambda_AE08')
    def lambda_AE08():
        ChrTurnDirection(0x0009, 0x0001, 0)
        Yield()

        Jump('lambda_AE08')

    DispatchAsync2(0x0009, 0x0001, lambda_AE08)

    Return()

# id: 0x0017 offset: 0xAE14
@scena.Code('func_17_AE14')
def func_17_AE14():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetPos(0x0101, 500, 0, 72250, 0)
    ChrSetPos(0x0102, -500, 0, 72250, 0)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetChipByIndex(0x0009, 8)
    ChrSetPos(0x0009, 200, 200, 74100, 180)
    CameraMove(-440, 0, 73390, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(500, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0030000677V#020F#2P你们两人都辛苦了。\n',
            '这样所有的研修课程都结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000678V#020F之后要做的就是\n',
            '亲自在实践中总结经验。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000679V#026F那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德取出两个小箱子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010000680V#004F#6P啊，那个箱子是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000681V#027F#2P对啊，\n',
            '就是刚才考试收回的小箱子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000682V#027F看来你们也很在意\n',
            '里面究竟装了些什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000683V#501F#6P难道说……\n',
            '现在可以让我们打开了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000684V#020F#2P嗯，可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000685V#020F你们两人\n',
            '都打开看看里面的东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000686V#001F#6P嘿嘿，太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000687V#010F#3P那我就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '两人把小箱子打开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT04/C_VIS015._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 280, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '准游击士的徽章',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    AddItem(0x035C, 1)

    ChrTalk(
        0x0101,
        (
            '#0010000688V#004F#6P这个徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000689V#010F#3P这么说，现在我们就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000690V#026F#2P……咳咳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000691V#022F艾丝蒂尔·布莱特。\n',
            '约修亚·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000692V#022F以上两人于本日１５：００\n',
            '正式被任命为『准游击士』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000693V#022F今后，作为游击士协会的一员，\n',
            '你们要谨记为守护人民的和平生活\n',
            '以及维护正义而贡献力量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000694V#021F……恭喜你们两人，\n',
            '从现在开始我们就是同事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000695V#001F#4P成功啦，约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000696V#001F这么一来我们也\n',
            '堂堂正正地成为协会的一员啦☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 300)

    ChrTalk(
        0x0102,
        (
            '#0020000697V#015F#3P是吗，我也成为游击士了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000698V#015F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000699V#011F哈哈，感觉有点不可思议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000700V#006F#4P真是的，约修亚～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000701V#006F你别这么心平气和嘛，\n',
            '应该表现得更加兴高采烈才对啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010000702V#001F#2P#5S呀嗬～太棒啦～⊙',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020000703V#018F#3P兴高采烈过头了吧，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000704V#021F#2P呵呵，那么……\n',
            '我差不多该告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000705V#021F外面还有一大堆的工作\n',
            '在等着我去处理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 0)
    ChrTurnDirection(0x0102, 0x0009, 0)

    ChrTalk(
        0x0101,
        (
            '#0010000706V#501F#6P是吗，工作那么忙，\n',
            '每天还要抽空陪我们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000707V#501F雪拉姐，真是太感谢你啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000708V#010F#3P真是给你添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000709V#027F#2P呵呵，别这么说。\n',
            '培养新人也是游击士的义务啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000710V#027F我以前研修的时候，\n',
            '也曾受到卡西乌斯老师很多照顾呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000711V#501F#6P啊，因为这样\n',
            '你就称呼老爸为『老师』是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000712V#020F#2P不仅仅是因为这个理由。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000713V#020F我希望你们也能早日独当一面，\n',
            '这样就拥有指导后辈的能力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000714V#020F然后，\n',
            '逐渐成为像老师那样伟大的游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000715V#021F好了，以后再聊吧，再见哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetPos(0x0009, 200, 0, 74100, 180)
    ChrClearFlags(0x0009, 0x0010)
    Sleep(500)

    @scena.Lambda('lambda_B847')
    def lambda_B847():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_B847')

    DispatchAsync2(0x0101, 0x0003, lambda_B847)

    @scena.Lambda('lambda_B858')
    def lambda_B858():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_B858')

    DispatchAsync2(0x0102, 0x0003, lambda_B858)

    CreateThread(0x0009, 0x00, 0x00, func_1D_BC74)
    Sleep(200)

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    Sleep(500)

    ChrClearFlags(0x0009, 0x0004)
    OP_A5(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    Sleep(200)

    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0102, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010000716V#505F#4P嗯……真是想不明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020000717V#014F#3P什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000718V#505F#4P说起『银闪雪拉扎德』，\n',
            '大家都知道她是游击士当中\n',
            '数一数二的厉害人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000719V#505F可是为什么\n',
            '她会给老爸那么高的评价呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000720V#007F要是让作为女儿的我来评价的话，\n',
            '他只不过是个经常外出不归的不良中年罢了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000721V#015F#3P不良中年……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000722V#015F不过，站在艾丝蒂尔的角度，\n',
            '做这种评价也不是没有道理的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000723V#004F#4P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000724V#010F#3P……啊，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000725V#010F那么，今天早点回家吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000726V#010F我们还要把成为游击士的事告诉父亲呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000727V#006F#4P嗯，好啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    SetScenaFlags(ScenaFlag(0x0040, 5, 0x205))
    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0xBB65
@scena.Code('func_18_BB65')
def func_18_BB65():
    OP_A6(0x0000)
    ChrWalkTo(0x00FE, -4850, 0, 71000, 3000, 0x00)
    ChrWalkTo(0x00FE, -2310, 0, 71900, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0009, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    def _loc_BB9D(): pass

    label('loc_BB9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_BBAF',
    )

    ChrTurnDirection(0x00FE, 0x0009, 0)
    Yield()

    Jump('loc_BB9D')

    def _loc_BBAF(): pass

    label('loc_BBAF')

    Return()

# id: 0x0019 offset: 0xBBB0
@scena.Code('func_19_BBB0')
def func_19_BBB0():
    Sleep(600)

    ChrWalkTo(0x0101, 810, 0, 115890, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x000F, 400)

    Return()

# id: 0x001A offset: 0xBBD1
@scena.Code('func_1A_BBD1')
def func_1A_BBD1():
    ChrWalkTo(0x0102, 1890, 0, 115660, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x000F, 400)

    Return()

# id: 0x001B offset: 0xBBED
@scena.Code('func_1B_BBED')
def func_1B_BBED():
    Sleep(300)

    ChrWalkTo(0x0009, -90, 0, 115270, 2000, 0x00)
    ChrTurnDirection(0x0009, 0x000F, 400)

    Return()

# id: 0x001C offset: 0xBC0E
@scena.Code('func_1C_BC0E')
def func_1C_BC0E():
    OP_A6(0x0001)
    ChrSetPos(0x00FE, -4850, -2000, 66000, 0)
    ChrClearFlags(0x00FE, 0x0008)
    Sleep(500)

    ChrWalkTo(0x00FE, -4850, 0, 71000, 3000, 0x00)
    ChrWalkTo(0x00FE, -3510, 0, 72200, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0009, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    def _loc_BC61(): pass

    label('loc_BC61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_BC73',
    )

    ChrTurnDirection(0x00FE, 0x0009, 0)
    Yield()

    Jump('loc_BC61')

    def _loc_BC73(): pass

    label('loc_BC73')

    Return()

# id: 0x001D offset: 0xBC74
@scena.Code('func_1D_BC74')
def func_1D_BC74():
    OP_A6(0x0002)
    ChrWalkTo(0x00FE, -2980, 0, 74100, 3000, 0x00)
    ChrClearFlags(0x0009, 0x0004)
    ChrWalkTo(0x00FE, -5050, 0, 70690, 3000, 0x00)
    ChrWalkTo(0x00FE, -5050, -2000, 66170, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x001E offset: 0xBCC7
@scena.Code('func_1E_BCC7')
def func_1E_BCC7():
    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_4A(0x0008, 0)
    CameraSetDistance(2800, 0)
    ChrSetPos(0x0101, 1500, 0, 116000, 0)
    ChrSetPos(0x0102, 700, 0, 115200, 0)
    FadeIn(2000, 0)
    OP_0D()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)

    ChrTalk(
        0x0008,
        (
            '#0350001029V#740F呵呵，真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001030V#007F老爸真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001031V#007F刚到镇上就扔下一句\n',
            '『报告的事就拜托了』，\n',
            '然后就一溜烟地跑回家了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001032V#007F真不知道该怎么形容他这种性格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001033V#010F算了，也无所谓吧。\n',
            '反正孩子们平安无事就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001034V#010F……以上就是这次任务的报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0001, 0x04, 0x10)
    Sleep(100)

    OP_AF(0x04, 0x0001)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0350001035V#740F初次任务，你们辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001036V从工作报告看来，\n',
            '你们都已经很努力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001037V我觉得足够引以为荣哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001038V#008F是、是吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350001039V#741F没问题，下次会做得更好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001040V再有什么事的话，还要靠你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001041V#003F……嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001042V#010F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001043V#010F那么艾丝蒂尔，我们回去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001044V#000F好吧～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001045V#000F得回去做晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350001046V#743F啊，稍等一下。\n',
            '刚好有一封信是寄给卡西乌斯先生的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0350001047V#740F刚才没有机会交给他，\n',
            '帮我转交一下好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '致卡西乌斯的信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0336, 1)

    ChrTalk(
        0x0101,
        (
            '#0010001048V#000F……是和工作有关的联络吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350001049V#740F我想应该是。\n',
            '好像是从国外的支部寄来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001050V#014F国外的支部……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350001051V#740F拥有游击士协会的国家\n',
            '并不只局限于利贝尔王国。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001052V卡西乌斯先生的交际很广，\n',
            '所以经常会收到这样的信件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350001053V那么，就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0042, 2, 0x212))
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_4B(0x0008, 0)
    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x001F offset: 0xC2A9
@scena.Code('func_1F_C2A9')
def func_1F_C2A9():
    ChrTalk(
        0x000B,
        (
            '#0870000858V啊，对了对了。\n',
            '这是我给你们的贺礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000859V不过说起来，\n',
            '这其实是刚进货的试销品而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '料理手册',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    AddItem(0x020D, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010000860V#004F啊，这是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000861V#014F手册里面的食谱，是做料理用的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000862V和魔兽战斗受伤的时候，\n',
            '总是使用药的话不是太花钱了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0870000863V用料理代替的话可以节省很多钱呢，\n',
            '有材料就可以做出多种有回复效果的料理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0870000864V只要尝过新的料理，\n',
            '就可以把食谱写到那个手册里面，\n',
            '慢慢地就会掌握越来越多的料理做法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0870000865V那么，你们来试试看吧。\n',
            '艾丝蒂尔，尝尝这块曲奇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '枫糖曲奇',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010000866V#001F嘿嘿嘿⊙\n',
            '那我就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '枫糖曲奇',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetStatus(0x0000, 0xFD, 80)
    OP_AC(0x0014)
    Sleep(500)

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '枫糖曲奇',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000B,
        (
            '#0870000867V……就是这样子了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0870000868V',
            (TxtCtl.SetColor, 0x4),
            '尝过料理并且记住它的做法',
            (TxtCtl.SetColor, 0x0),
            '是基本的要领。\n',
            '没见过的料理更要去尝尝看，\n',
            '反正看到什么吃什么就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000869V#010F原来如此，真是方便啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000870V#505F嗯～虽然我不讨厌做饭，\n',
            '但是做出来的东西都不太好吃……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000871V#006F不过我也想多学些菜式，\n',
            '让老爸对我另眼相看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0870000872V对对，有这种志气已经很不错了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0870000873V你们要买食物材料时，\n',
            '记得到我的店子里挑挑看哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000874V#001F#4P啊哈哈。\n',
            '不愧是里农叔叔，真会做生意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000875V#019F真是谢谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※在酒吧食用『推荐料理』，\n',
            '　或使用『便携食物』时，\n',
            '　其烹饪方法便会自动记录到料理手册上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※使用料理手册会显示已记录的料理，\n',
            '　如果具备必要的材料便可以将其烹调出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※料理分为当场食用的『大盘料理』和\n',
            '　可作为道具而随身携带的『便携料理』。\n',
            '　即使做出『大盘料理』，也没办法变成道具带走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※料理所使用的『食物材料』\n',
            '　可以在杂货铺等店铺购买。\n',
            '　此外，部分材料也可以通过击败魔兽获得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_0D()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
