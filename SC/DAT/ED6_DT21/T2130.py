import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2130_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2130   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2130.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T2130._SN', 'ED6_DT21/T2130_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01670._CH', 'ED6_DT07/CH01670P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT26/CH20237._CH', 'ED6_DT26/CH20237P._CP'),
        ('ED6_DT07/CH01390._CH', 'ED6_DT07/CH01390P._CP'),
        ('ED6_DT07/CH01393._CH', 'ED6_DT07/CH01393P._CP'),
        ('ED6_DT07/CH00450._CH', 'ED6_DT07/CH00450P._CP'),
        ('ED6_DT07/CH00460._CH', 'ED6_DT07/CH00460P._CP'),
        ('ED6_DT07/CH00470._CH', 'ED6_DT07/CH00470P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00454._CH', 'ED6_DT07/CH00454P._CP'),
        ('ED6_DT07/CH00464._CH', 'ED6_DT07/CH00464P._CP'),
        ('ED6_DT07/CH00474._CH', 'ED6_DT07/CH00474P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
    ]

# id: 0x10001 offset: 0x182
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '迪恩',
            x                   = -4150,
            z                   = 0,
            y                   = 9070,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '雷斯',
            x                   = -1590,
            z                   = 0,
            y                   = 7520,
            direction           = 322,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '洛克',
            x                   = -2970,
            z                   = 0,
            y                   = 7390,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '托尼奥',
            x                   = 56350,
            z                   = 80,
            y                   = 44530,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '迪奥德罗教区长',
            x                   = 58970,
            z                   = 1000,
            y                   = 52150,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '修女芙丽达',
            x                   = 54460,
            z                   = 0,
            y                   = 50690,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            name                = '凯文神父',
            x                   = 60540,
            z                   = 1000,
            y                   = 52350,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '爱蕾塔',
            x                   = 59120,
            z                   = 0,
            y                   = 47050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '豆豆',
            x                   = 57540,
            z                   = 0,
            y                   = 47300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '阿杰',
            x                   = 59980,
            z                   = 0,
            y                   = 47260,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '路易',
            x                   = 61430,
            z                   = 0,
            y                   = 47360,
            direction           = 303,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '布鲁托',
            x                   = -10050,
            z                   = 0,
            y                   = 3740,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '巴克',
            x                   = -12730,
            z                   = 0,
            y                   = 4160,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '多姆斯',
            x                   = -9930,
            z                   = 0,
            y                   = 7470,
            direction           = 280,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '加布',
            x                   = -13330,
            z                   = 600,
            y                   = 6230,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '皮卡罗',
            x                   = -11600,
            z                   = 250,
            y                   = 1950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '布拉奥',
            x                   = 59140,
            z                   = 0,
            y                   = 46600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 52250,
            z                   = 5000,
            y                   = 51330,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用照相机',
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
            name                = '托尼奥',
            x                   = 56350,
            z                   = -600,
            y                   = 44730,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x402
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x402
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x402
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 59140,
            triggerZ            = 1000,
            triggerY            = 50250,
            triggerRange        = 400,
            actorX              = 58970,
            actorZ              = 2700,
            actorY              = 52150,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x426
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_45F',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_45C',
    )

    ChrSetFlags(0x0018, 0x0010)

    def _loc_45C(): pass

    label('loc_45C')

    Jump('loc_4D7')

    def _loc_45F(): pass

    label('loc_45F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4D7',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetFlags(0x000C, 0x0010)

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_49E',
    )

    Jump('loc_4D7')

    def _loc_49E(): pass

    label('loc_49E')

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_4C1',
    )

    ChrSetFlags(0x000D, 0x0010)
    ChrSetPos(0x000D, 53390, 0, 52130, 180)

    Jump('loc_4D7')

    def _loc_4C1(): pass

    label('loc_4C1')

    ChrSetFlags(0x000D, 0x0010)
    ChrSetPos(0x000D, -16840, 0, 42910, 270)

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_521',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 1, 0x1231)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F5',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_4F5(): pass

    label('loc_4F5')

    Jump('loc_502')

    def _loc_4F8(): pass

    label('loc_4F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_502',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_502(): pass

    label('loc_502')

    ChrSetFlags(0x000A, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_515',
    )

    Jump('loc_521')

    def _loc_515(): pass

    label('loc_515')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_521',
    )

    ChrClearFlags(0x000A, 0x0010)

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_52D',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_52D(): pass

    label('loc_52D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_556',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrTurnDirection(0x000C, 0x000E, 0)
    ChrTurnDirection(0x000E, 0x000C, 0)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetFlags(0x000E, 0x0010)

    def _loc_556(): pass

    label('loc_556')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_562'),
        (-1, 'loc_57F'),
    )

    def _loc_562(): pass

    label('loc_562')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 6, 0x120E)),
            Expr.Return,
        ),
        'loc_56C',
    )

    Jump('loc_57C')

    def _loc_56C(): pass

    label('loc_56C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_57C',
    )

    MapSetFlags(0x10000000)
    Event(0, func_14_23BC)

    def _loc_57C(): pass

    label('loc_57C')

    Jump('loc_57F')

    def _loc_57F(): pass

    label('loc_57F')

    Return()

# id: 0x0001 offset: 0x580
@scena.Code('func_01_580')
def func_01_580():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_590',
    )

    OP_64(0x00, 0x0001)

    def _loc_590(): pass

    label('loc_590')

    Return()

# id: 0x0002 offset: 0x591
@scena.Code('func_02_591')
def func_02_591():
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
        'loc_5B6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_6F8')

    def _loc_5B6(): pass

    label('loc_5B6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5CF',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_6F8')

    def _loc_5CF(): pass

    label('loc_5CF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5E8',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_6F8')

    def _loc_5E8(): pass

    label('loc_5E8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_601',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_6F8')

    def _loc_601(): pass

    label('loc_601')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_61A',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_6F8')

    def _loc_61A(): pass

    label('loc_61A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_633',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_6F8')

    def _loc_633(): pass

    label('loc_633')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_64C',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_6F8')

    def _loc_64C(): pass

    label('loc_64C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_665',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_6F8')

    def _loc_665(): pass

    label('loc_665')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_67E',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_6F8')

    def _loc_67E(): pass

    label('loc_67E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_697',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_6F8')

    def _loc_697(): pass

    label('loc_697')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B0',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_6F8')

    def _loc_6B0(): pass

    label('loc_6B0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C9',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_6F8')

    def _loc_6C9(): pass

    label('loc_6C9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E2',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_6F8')

    def _loc_6E2(): pass

    label('loc_6E2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F8',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_6F8(): pass

    label('loc_6F8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_70D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_6F8')

    def _loc_70D(): pass

    label('loc_70D')

    Return()

# id: 0x0003 offset: 0x70E
@scena.Code('func_03_70E')
def func_03_70E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_757',
    )

    ChrTalk(
        0x00FE,
        (
            '贝尔夫那家伙\n',
            '在帮忙选举呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛克他们\n',
            '不会生气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89F')

    def _loc_757(): pass

    label('loc_757')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_809',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_798',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，孩提时代多好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想回到那时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_806')

    def _loc_798(): pass

    label('loc_798')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '今天是主日学校的日子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别看我这样，我以前因为努力学习\n',
            '经常被修女称赞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，那时候多好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_806(): pass

    label('loc_806')

    Jump('loc_89F')

    def _loc_809(): pass

    label('loc_809')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_850',
    )

    ChrTalk(
        0x00FE,
        (
            '全城都是选举气氛呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正闲着\n',
            '就偷偷去投票吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89F')

    def _loc_850(): pass

    label('loc_850')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_89F',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～好久没有\n',
            '这么紧张的场面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总，总而言之\n',
            '还好没被卷进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_89F(): pass

    label('loc_89F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x8A3
@scena.Code('func_04_8A3')
def func_04_8A3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_8F6',
    )

    ChrTalk(
        0x00FE,
        (
            '选举那么麻烦，\n',
            '真是受不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能给米拉\n',
            '那倒还能考虑考虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D8')

    def _loc_8F6(): pass

    label('loc_8F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_944',
    )

    ChrTalk(
        0x00FE,
        (
            '娱乐场是挺有趣的，\n',
            '就是稍微远了点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '桥又出问题了\n',
            '过不去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D8')

    def _loc_944(): pass

    label('loc_944')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_996',
    )

    ChrTalk(
        0x00FE,
        (
            '参加了武术大会\n',
            '一点好处也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我说麻烦\n',
            '不要去了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D8')

    def _loc_996(): pass

    label('loc_996')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_9D8',
    )

    ChrTalk(
        0x00FE,
        (
            '洛克大哥他们\n',
            '也真是爱打架呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明知道会被打败的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9D8(): pass

    label('loc_9D8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x9DC
@scena.Code('func_05_9DC')
def func_05_9DC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_A92',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A46',
    )

    ChrTalk(
        0x00FE,
        (
            '洛克那家伙好像想把\n',
            '渡鸦帮变成自卫团呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，要是惹上麻烦\n',
            '我就闪人好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_A8F')

    def _loc_A46(): pass

    label('loc_A46')

    ChrTalk(
        0x00FE,
        (
            '洛克那家伙好像想把\n',
            '渡鸦帮变成自卫团呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，反正和我没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A8F(): pass

    label('loc_A8F')

    Jump('loc_CCC')

    def _loc_A92(): pass

    label('loc_A92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B20',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯？什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的成员\n',
            '全都出去了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '渡口在这边～这样\n',
            '叫喊着，没看见？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛克那家伙真是的，\n',
            '想什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_B62')

    def _loc_B20(): pass

    label('loc_B20')

    ChrTalk(
        0x00FE,
        (
            '我们的成员\n',
            '全都出去了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛克那家伙真是的，\n',
            '想什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B62(): pass

    label('loc_B62')

    Jump('loc_CCC')

    def _loc_B65(): pass

    label('loc_B65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_BAB',
    )

    ChrTalk(
        0x00FE,
        (
            '洛克的样子\n',
            '好像挺奇怪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定准备\n',
            '逃跑比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCC')

    def _loc_BAB(): pass

    label('loc_BAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_C2B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_BD5',
    )

    ChrTalk(
        0x00FE,
        (
            '卷进纠纷\n',
            '就麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C28')

    def _loc_BD5(): pass

    label('loc_BD5')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '卷进纠纷\n',
            '就麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关于这个我总是\n',
            '不疏防范的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出问题之前就撤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C28(): pass

    label('loc_C28')

    Jump('loc_CCC')

    def _loc_C2B(): pass

    label('loc_C2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C81',
    )

    ChrTalk(
        0x00FE,
        (
            '正商量着要干什么呢，\n',
            '不知不觉天就黑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '浪费人生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCC')

    def _loc_C81(): pass

    label('loc_C81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_CCC',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，这次\n',
            '也没被卷进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可不想惹麻烦。\n',
            '人生就得圆滑点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CCC(): pass

    label('loc_CCC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xCD0
@scena.Code('func_06_CD0')
def func_06_CD0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_D27',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，欧尼尔老爷子\n',
            '多找钱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然要保持沉默啦。\n',
            '我可真是坏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E91')

    def _loc_D27(): pass

    label('loc_D27')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_D6F',
    )

    ChrTalk(
        0x00FE,
        (
            '巧克力香烟\n',
            '没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要是没有这个\n',
            '就镇定不下来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E91')

    def _loc_D6F(): pass

    label('loc_D6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_DF6',
    )

    ChrTalk(
        0x00FE,
        (
            '在娱乐场拣到的游戏币\n',
            '变卖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿，嘿嘿……\n',
            '白拿１００啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，不知道店员有没有发现。\n',
            '……哆嗦，哆哆嗦嗦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E91')

    def _loc_DF6(): pass

    label('loc_DF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_E91',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_E4D',
    )

    ChrTalk(
        0x00FE,
        (
            '洛克大哥他们\n',
            '虽然强了很多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '终究还是敌不过\n',
            '那些游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E91')

    def _loc_E4D(): pass

    label('loc_E4D')

    ChrTalk(
        0x00FE,
        (
            '洛克大哥他们\n',
            '虽然强了很多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '终究还不是\n',
            '阿加特的对手啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E91(): pass

    label('loc_E91')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xE95
@scena.Code('func_07_E95')
def func_07_E95():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_EDD',
    )

    ChrTalk(
        0x00FE,
        (
            '贝尔夫那家伙好像在他老爸的\n',
            '事务所里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FD1')

    def _loc_EDD(): pass

    label('loc_EDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_F1E',
    )

    ChrTalk(
        0x00FE,
        (
            '居然在城市中心吵架。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '选举的人\n',
            '一定也很闲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FD1')

    def _loc_F1E(): pass

    label('loc_F1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_F88',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_F49',
    )

    ChrTalk(
        0x00FE,
        (
            '呼啊～好无聊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F85')

    def _loc_F49(): pass

    label('loc_F49')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '呼啊～好无聊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想去娱乐场，\n',
            '没米拉也不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F85(): pass

    label('loc_F85')

    Jump('loc_FD1')

    def _loc_F88(): pass

    label('loc_F88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_FD1',
    )

    ChrTalk(
        0x00FE,
        (
            '贝尔夫那家伙\n',
            '和老爸关系不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，就加入\n',
            '我们这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FD1(): pass

    label('loc_FD1')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xFD5
@scena.Code('func_08_FD5')
def func_08_FD5():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1026',
    )

    ChrTalk(
        0x00FE,
        (
            '#1742F洛克到底\n',
            '怎么了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '说要『活动一下身体』\n',
            '一去就不回了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1268')

    def _loc_1026(): pass

    label('loc_1026')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_10C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_107D',
    )

    ChrTalk(
        0x00FE,
        (
            '#1740F想当市长的家伙\n',
            '让他们当不就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '谁来\n',
            '都比那个戴尔蒙强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C0')

    def _loc_107D(): pass

    label('loc_107D')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '#1744F这么说来\n',
            '正在选举呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1740F当然我是\n',
            '不能去投票的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10C0(): pass

    label('loc_10C0')

    Jump('loc_1268')

    def _loc_10C3(): pass

    label('loc_10C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_113B',
    )

    ChrTalk(
        0x00FE,
        (
            '#1742F我们应该也\n',
            '变强了许多……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是最近，魔兽\n',
            '变得更强了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1744F弄得我们一点也没有变强的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1268')

    def _loc_113B(): pass

    label('loc_113B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1268',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 0, 0x1210)),
            Expr.Return,
        ),
        'loc_11B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1181',
    )

    ChrTalk(
        0x00FE,
        (
            '#1740F哟，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '贝尔夫那家伙怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11B5')

    def _loc_1181(): pass

    label('loc_1181')

    ChrTalk(
        0x00FE,
        (
            '#1740FA啊，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '贝尔夫那家伙，\n',
            '说什么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11B5(): pass

    label('loc_11B5')

    Jump('loc_1268')

    def _loc_11B8(): pass

    label('loc_11B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1212',
    )

    ChrTalk(
        0x00FE,
        (
            '#1740F贝尔夫的家\n',
            '在市长官邸的右边。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '一个叫诺曼的大叔家，\n',
            '他是家里的长子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1268')

    def _loc_1212(): pass

    label('loc_1212')

    ChrTalk(
        0x00FE,
        (
            '#1740F贝尔夫的家是\n',
            '市长官邸右边的房子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '一个叫诺曼的大叔家，\n',
            '他是家里的长子哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1268(): pass

    label('loc_1268')

    TalkEnd(0x0008)

    Return()

# id: 0x0009 offset: 0x126C
@scena.Code('func_09_126C')
def func_09_126C():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1367',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_12DA',
    )

    ChrTalk(
        0x00FE,
        (
            '#1754F刚才出去了一趟，\n',
            '洛克在仓库的后面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那家伙一个人不声不响的\n',
            '在努力练习挥刀呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1364')

    def _loc_12DA(): pass

    label('loc_12DA')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '#1752F刚才出去了一趟，\n',
            '洛克在仓库的后面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那家伙一个人不声不响的\n',
            '在努力练习挥刀呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1754F洛克一旦开始锻炼身体\n',
            '就没什么好事啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1364(): pass

    label('loc_1364')

    Jump('loc_1574')

    def _loc_1367(): pass

    label('loc_1367')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_143B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_13C4',
    )

    ChrTalk(
        0x00FE,
        (
            '#1756F嘿嘿，支持者们\n',
            '发生了争执呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '装得品格高尚，\n',
            '骨子里还不是一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1438')

    def _loc_13C4(): pass

    label('loc_13C4')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '#1756F嘿嘿，支持者们\n',
            '发生了争执呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '装得品格高尚，\n',
            '骨子里还不是一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1750F戴尔蒙那家伙\n',
            '就是最好的例子～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1438(): pass

    label('loc_1438')

    Jump('loc_1574')

    def _loc_143B(): pass

    label('loc_143B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_14D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_147B',
    )

    ChrTalk(
        0x00FE,
        (
            '#1754F最近洛克那家伙\n',
            '好像在想些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D6')

    def _loc_147B(): pass

    label('loc_147B')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '#1755F洛克那家伙\n',
            '好像在想些什么呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1754F那家伙变成那样的时候\n',
            '最好还是不要靠近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14D6(): pass

    label('loc_14D6')

    Jump('loc_1574')

    def _loc_14D9(): pass

    label('loc_14D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1574',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1516',
    )

    ChrTalk(
        0x00FE,
        (
            '#1751F嘿嘿，艾丝蒂尔。\n',
            '要再来哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1574')

    def _loc_1516(): pass

    label('loc_1516')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_154C',
    )

    ChrTalk(
        0x00FE,
        (
            '#1750F辛、辛苦了。\n',
            '再等你们来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1574')

    def _loc_154C(): pass

    label('loc_154C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1574',
    )

    ChrTalk(
        0x00FE,
        (
            '#1751F要再来哦～大姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1574(): pass

    label('loc_1574')

    TalkEnd(0x0009)

    Return()

# id: 0x000A offset: 0x1578
@scena.Code('func_0A_1578')
def func_0A_1578():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_15B3',
    )

    ChrTalk(
        0x00FE,
        (
            '#1765F市长选举啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1763F哼，无聊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B8')

    def _loc_15B3(): pass

    label('loc_15B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_161F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_15EA',
    )

    ChrTalk(
        0x00FE,
        (
            '#1764F…………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可恶…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_161C')

    def _loc_15EA(): pass

    label('loc_15EA')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '#1764F可恶…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这样下去不行\n',
            '我们也明白啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_161C(): pass

    label('loc_161C')

    Jump('loc_16B8')

    def _loc_161F(): pass

    label('loc_161F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_16B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_165C',
    )

    ChrTalk(
        0x00FE,
        (
            '#1764F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '…………可恶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B8')

    def _loc_165C(): pass

    label('loc_165C')

    ChrTalk(
        0x00FE,
        (
            '#1765F看到那影子之后\n',
            '贝尔夫就把自己关在家里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '本来就是好人家的小孩嘛，\n',
            '胆小的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16B8(): pass

    label('loc_16B8')

    TalkEnd(0x000A)

    Return()

# id: 0x000B offset: 0x16BC
@scena.Code('func_0B_16BC')
def func_0B_16BC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_170B',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，果然还是\n',
            '游击士有型啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也想当当看啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_172C')

    def _loc_170B(): pass

    label('loc_170B')

    ChrTalk(
        0x00FE,
        (
            '今天教区长的\n',
            '授课真有趣啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_172C(): pass

    label('loc_172C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1730
@scena.Code('func_0C_1730')
def func_0C_1730():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1779',
    )

    ChrTalk(
        0x00FE,
        (
            '游击士\n',
            '还当学校的老师啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真吃了一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1794')

    def _loc_1779(): pass

    label('loc_1779')

    ChrTalk(
        0x00FE,
        (
            '和爱蕾塔\n',
            '一起学习哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1794(): pass

    label('loc_1794')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1798
@scena.Code('func_0D_1798')
def func_0D_1798():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_17F6',
    )

    ChrTalk(
        0x00FE,
        (
            '上课差、差不多\n',
            '该结束了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再不赶快\n',
            '下一艘定期船就要到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_183C')

    def _loc_17F6(): pass

    label('loc_17F6')

    ChrTalk(
        0x00FE,
        (
            '我在飞船坪\n',
            '经常看见游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总是很忙的样子，\n',
            '工作很辛苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_183C(): pass

    label('loc_183C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1840
@scena.Code('func_0E_1840')
def func_0E_1840():
    OP_4A(0x000C, 255)
    OP_4A(0x000E, 255)

    ChrTalk(
        0x000C,
        (
            '哟，辛苦了。\n',
            '孤儿院的孩子们怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1060F很有精神呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '好像已经\n',
            '完全恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '唔，就像幼苗一样\n',
            '茁壮成长吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这下，我们\n',
            '都不得不向他们学习了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1060F呀，真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000C, 255)
    OP_4B(0x000E, 255)

    Return()

# id: 0x000F offset: 0x190B
@scena.Code('func_0F_190B')
def func_0F_190B():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_19AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1980',
    )

    ChrTalk(
        0x000C,
        (
            '渡鸦帮那些年轻人\n',
            '也相当有用的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '经历挫折的人\n',
            '复苏后会更努力，\n',
            '感觉就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_19A9')

    def _loc_1980(): pass

    label('loc_1980')

    ChrTalk(
        0x000C,
        (
            '渡鸦帮那些年轻人\n',
            '也相当有用的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19A9(): pass

    label('loc_19A9')

    Jump('loc_1F41')

    def _loc_19AC(): pass

    label('loc_19AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1AA2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A4D',
    )

    ChrTalk(
        0x000C,
        (
            '这个现象发生的时候\n',
            '市内一片骚乱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '现在总算镇定下来了，\n',
            '但那时还真是着急啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '完全可以看出来\n',
            '平时我们是多么\n',
            '依赖导力器啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1A9F')

    def _loc_1A4D(): pass

    label('loc_1A4D')

    ChrTalk(
        0x000C,
        (
            '现象发生之初，\n',
            '市内一片骚乱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯，说明我们已经\n',
            '这么的依赖导力器了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A9F(): pass

    label('loc_1A9F')

    Jump('loc_1F41')

    def _loc_1AA2(): pass

    label('loc_1AA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1B00',
    )

    ChrTalk(
        0x000C,
        (
            '无论哪边胜出，\n',
            '还是赶快做个了结吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '选举结束的话\n',
            '卢安市民就会团结努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F41')

    def _loc_1B00(): pass

    label('loc_1B00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1D44',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C7F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1BBA',
    )

    ChrTalk(
        0x000C,
        (
            '多亏这样的特质,\n',
            '协会才会超越国家间的框架\n',
            '成为整体的组织啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '此外协会和国家之间\n',
            '也有一些规定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '其中最有名的约定\n',
            '就是不干涉国家权力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C7C')

    def _loc_1BBA(): pass

    label('loc_1BBA')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000C,
        (
            '……在这时候\n',
            '登场的组织就是游击士协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '大家都知道\n',
            '游击士协会是统率\n',
            '全境游击士的巨大组织……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '但其最大的特征\n',
            '是非政府性的组织。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊～『非政府性』\n',
            '就是和国家没有关系的意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C7C(): pass

    label('loc_1C7C')

    Jump('loc_1D41')

    def _loc_1C7F(): pass

    label('loc_1C7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1CDC',
    )

    ChrTalk(
        0x000C,
        (
            '那么，授课最后再次\n',
            '复习一下今天学的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '首先是关于游击士协会的成立……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D41')

    def _loc_1CDC(): pass

    label('loc_1CDC')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrClearFlags(0x000C, 0x0010)
    ChrTurnDirection(0x000C, 0x0000, 0)
    ChrSetFlags(0x000C, 0x0010)

    ChrTalk(
        0x000C,
        (
            '哦，是你们啊。\n',
            '今天辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '还在授课中，\n',
            '不好意思，我先失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000C, 180, 0)

    def _loc_1D41(): pass

    label('loc_1D41')

    Jump('loc_1F41')

    def _loc_1D44(): pass

    label('loc_1D44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_1D99',
    )

    ChrTalk(
        0x000C,
        (
            '哦。那么着急，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那位巡回神父哥哥\n',
            '已经出发去下一个任地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F41')

    def _loc_1D99(): pass

    label('loc_1D99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_1E16',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1E0C',
    )

    OP_4A(0x000E, 255)

    ChrTalk(
        0x000C,
        (
            '对了，凯文神父。\n',
            '准备出发去下一个任地了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '机会难得，\n',
            '再稍微在卢安享受一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000E, 255)

    Jump('loc_1E13')

    def _loc_1E0C(): pass

    label('loc_1E0C')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    Call(0, 0x000E)

    def _loc_1E13(): pass

    label('loc_1E13')

    Jump('loc_1F41')

    def _loc_1E16(): pass

    label('loc_1E16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1E5D',
    )

    ChrTalk(
        0x000C,
        (
            '好，今天有主日学校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '鼓足干劲\n',
            '去教导小鬼们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F41')

    def _loc_1E5D(): pass

    label('loc_1E5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1F41',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1EC4',
    )

    ChrTalk(
        0x000C,
        (
            '选举热闹倒是很好，\n',
            '但希望别出现骚乱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '别看卢安这样，\n',
            '当地人性情可火暴啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F41')

    def _loc_1EC4(): pass

    label('loc_1EC4')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000C,
        (
            '选举热闹倒是很好，\n',
            '但希望别出现骚乱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '别看卢安这样，\n',
            '毕竟是海的男人们建立的城市嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '当地人性情可火暴啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F41(): pass

    label('loc_1F41')

    TalkEnd(0x000C)

    Return()

# id: 0x0010 offset: 0x1F45
@scena.Code('func_10_1F45')
def func_10_1F45():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1FA0',
    )

    OP_4A(0x000C, 255)

    ChrTalk(
        0x000E,
        (
            '#1060F稍微休息一下\n',
            '就打算马上出发了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '调查了很多\n',
            '但还是不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000C, 255)

    Jump('loc_1FA7')

    def _loc_1FA0(): pass

    label('loc_1FA0')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    Call(0, 0x000E)

    def _loc_1FA7(): pass

    label('loc_1FA7')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1FAB
@scena.Code('func_11_1FAB')
def func_11_1FAB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1FB8',
    )

    Jump('loc_21BE')

    def _loc_1FB8(): pass

    label('loc_1FB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_21BE',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_20B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_202D',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～１１８７年吗。\n',
            '好，这次记住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤迪斯是１１８７年。\n',
            '是１１８７年。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20B4')

    def _loc_202D(): pass

    label('loc_202D')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '艾莉茜雅Ⅱ世即位是１１６２年。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～此后\n',
            '尤迪斯皇太子逝世是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……啊～又忘记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20B4(): pass

    label('loc_20B4')

    Jump('loc_21BE')

    def _loc_20B7(): pass

    label('loc_20B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2132',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，刚设立的时候不叫中央工房，\n',
            '是叫《技术工房》啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些地方\n',
            '入学考试很可能会考到，\n',
            '要注意才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21BE')

    def _loc_2132(): pass

    label('loc_2132')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '中央工房的设立是１１５７年。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『卡特兰帕号』\n',
            '试飞是１１６８年，\n',
            '定期船开航是１１７５年……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……好，到这里都记住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21BE(): pass

    label('loc_21BE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x21C2
@scena.Code('func_12_21C2')
def func_12_21C2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_21CF',
    )

    Jump('loc_2270')

    def _loc_21CF(): pass

    label('loc_21CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2270',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2217',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～是刚才的老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又来教课了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2270')

    def _loc_2217(): pass

    label('loc_2217')

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，爱蕾塔\n',
            '也能上主日学校了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要好好学习，\n',
            '和基诺奇奥哥哥\n',
            '上同一所学校哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2270(): pass

    label('loc_2270')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x2274
@scena.Code('func_13_2274')
def func_13_2274():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_22F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22CE',
    )

    ChrTalk(
        0x00FE,
        (
            '女神啊……\n',
            '请宽恕我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '失去信仰的人们\n',
            '一定也会悔改吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_22EF')

    def _loc_22CE(): pass

    label('loc_22CE')

    ChrTalk(
        0x00FE,
        (
            '啊啊，女神……\n',
            '请宽恕我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22EF(): pass

    label('loc_22EF')

    Jump('loc_23B8')

    def _loc_22F2(): pass

    label('loc_22F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_23B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_237C',
    )

    ChrTalk(
        0x00FE,
        (
            '到卢安\n',
            '是来找熟人的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到运气不好变成这样\n',
            '想回也回不去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，不管怎样现在只能\n',
            '祈求女神保佑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_23B8')

    def _loc_237C(): pass

    label('loc_237C')

    ChrTalk(
        0x00FE,
        (
            '来，你们也来\n',
            '向女神祈祷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '变成这样\n',
            '只能祈祷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23B8(): pass

    label('loc_23B8')

    TalkEnd(0x0018)

    Return()

# id: 0x0014 offset: 0x23BC
@scena.Code('func_14_23BC')
def func_14_23BC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23CD',
    )

    Call(0, 0x0017)

    def _loc_23CD(): pass

    label('loc_23CD')

    EventBegin(0x00)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0101, 110, 0, 450, 348)
    ChrSetPos(0x00F7, -790, 0, -230, 347)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    ChrSetDirection(0x0008, 135, 0)
    ChrSetDirection(0x0009, 270, 0)
    CameraMove(-3640, 0, 9320, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(2850, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0450200978V#1749F#5P唉，感觉最近懒洋洋的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450200979V#5P进行了各种锻炼\n',
            '却没觉得有什么长进……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460200980V#1764F#3P哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460200981V#3P没想到现在还会和\n',
            '街道出没的魔兽苦战啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470200982V#1753F#4P啊～感觉最近\n',
            '魔兽好像比以前更凶残了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470200983V#1750F#4P据说变得有以前的\n',
            '2～3倍那么强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0009, 400)

    ChrTalk(
        0x000A,
        (
            '#0460200984V#1765F#5P原来如此，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460200985V#1763F#5P……没办法了。\n',
            '好久没去了，再去街上转转吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460200986V#1761F#5P如何，去北区的\n',
            '拉旺塔尔游戏吧转转吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470200987V#1756F#4P啊～２楼的娱乐场\n',
            '重新装修开放了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470200988V#1751F#4P好呀，听说还有\n',
            '漂亮的服务小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470200989V#4P嘿嘿，运气好的话\n',
            '说不定还可以亲近一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0450200990V#1743F#5P就是这个！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450200991V#1741F#5P卡露娜大姐似乎也不在，\n',
            '稍微放松下也无所谓吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3F2A',
    )

    NpcTalk(
        0x0106,
        '青年的声音',
        (
            '#0050200992V#2P……什么无所谓？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, 410, 0, -450, 348)
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_282F')
    def lambda_282F():
        CameraMove(-2500, 0, 4470, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_282F)

    @scena.Lambda('lambda_2847')
    def lambda_2847():
        OP_67(0, 6500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2847)

    @scena.Lambda('lambda_285F')
    def lambda_285F():
        CameraSetDistance(2670, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_285F)

    @scena.Lambda('lambda_286F')
    def lambda_286F():
        OP_6E(280, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_286F)

    @scena.Lambda('lambda_287F')
    def lambda_287F():
        ChrTurnDirection(0x0008, 0x0106, 400)
        Yield()

        Jump('lambda_287F')

    DispatchAsync2(0x0008, 0x0001, lambda_287F)

    @scena.Lambda('lambda_2890')
    def lambda_2890():
        ChrTurnDirection(0x0009, 0x0106, 400)
        Yield()

        Jump('lambda_2890')

    DispatchAsync2(0x0009, 0x0001, lambda_2890)

    @scena.Lambda('lambda_28A1')
    def lambda_28A1():
        ChrTurnDirection(0x000A, 0x0106, 400)
        Yield()

        Jump('lambda_28A1')

    DispatchAsync2(0x000A, 0x0001, lambda_28A1)

    ChrTurnDirection(0x0013, 0x0106, 800)
    ChrTurnDirection(0x0014, 0x0106, 800)
    ChrTurnDirection(0x0015, 0x0106, 800)
    Sleep(300)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0450200993V#1743F#4P阿、阿加特！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460200994V#1762F#5P……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2929')
    def lambda_2929():
        ChrTurnDirection(0x0101, 0x0009, 0)
        Yield()

        Jump('lambda_2929')

    DispatchAsync2(0x0106, 0x0001, lambda_2929)

    @scena.Lambda('lambda_293A')
    def lambda_293A():
        ChrTurnDirection(0x0106, 0x000A, 0)
        Yield()

        Jump('lambda_293A')

    DispatchAsync2(0x0106, 0x0002, lambda_293A)

    @scena.Lambda('lambda_294B')
    def lambda_294B():
        ChrTurnDirection(0x0013, 0x0106, 0)
        Yield()

        Jump('lambda_294B')

    DispatchAsync2(0x0013, 0x0000, lambda_294B)

    @scena.Lambda('lambda_295C')
    def lambda_295C():
        ChrTurnDirection(0x0014, 0x0106, 0)
        Yield()

        Jump('lambda_295C')

    DispatchAsync2(0x0014, 0x0000, lambda_295C)

    @scena.Lambda('lambda_296D')
    def lambda_296D():
        ChrMoveTo(0x00FE, -3000, 0, 4790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_296D)

    Sleep(300)

    @scena.Lambda('lambda_298D')
    def lambda_298D():
        ChrMoveTo(0x00FE, -1800, 0, 4900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_298D)

    Sleep(500)

    @scena.Lambda('lambda_29AD')
    def lambda_29AD():
        CameraMove(-3350, 0, 7460, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_29AD)

    @scena.Lambda('lambda_29C5')
    def lambda_29C5():
        OP_67(0, 8350, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_29C5)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0106, 0x0000)
    TerminateThread(0x0106, 0x01)
    TerminateThread(0x0106, 0x02)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0014, 0x01)

    ChrTalk(
        0x0106,
        (
            '#0050200995V#057F真是的，你们这些人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200996V稍微对你们改观了点\n',
            '马上就偷懒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450200997V#1749F#5P讨、讨厌啦～\n',
            '只不过是开玩笑啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0450200998V#1743F#5P对了，那边的是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0470200999V#1753F#2P这不是新人游击士\n',
            '艾丝蒂尔吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201000V#6P#1006F你们好，好久不见呢。\n',
            '武术大会对战之后就没见过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201001V#1760F#5P啊～对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201002V#1756F#2P呀～我们在那之后\n',
            '一直观战到决胜战了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470201003V#1751F#2P真是厉害啊。\n',
            '我重新开始仰慕你了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201004V#6P#1016F啊哈哈……谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201005V#1002F对了，今天来访\n',
            '是为了协会的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201006V嗯，你们之中\n',
            '是不是有人看到了『白影』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0450201007V#1742F#5P那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0470201008V#1752F#4P……是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201009V#6P#1011F啊，你们果然知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201010V#053F那就赶快\n',
            '把你们知道的说出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201011V别浪费我们的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0460201012V#1763F#5P……稍等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201013V#1765F#5P你啊，是不是\n',
            '稍微得意忘形过头了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201014V#052F……啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201015V#1764F#5P烦死了，你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201016V#5P随意离开组织\n',
            '当了游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201017V#1760F#5P只在需要我们的时候\n',
            '跑回来问话？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201018V#5P真是受不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000A, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0450201019V#1743F#5P喂、喂洛克！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201020V#051F哼，还是那么\n',
            '逞强啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201021V那么，要怎样\n',
            '你才会满足？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201022V跪下求饶吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201023V#1765F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x000A, 15)
    ChrSetSubChip(0x000A, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0460201024V#1760F#5P就在这里……\n',
            '跟我们决一胜负吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(800)

    ChrTalk(
        0x0008,
        (
            '#0450201025V#1742F#5P为、为什么会是这样啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#0470201026V#1753F#2P喂喂，干嘛头脑发热啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201027V#1767F#5P别吵，怎么也要有一个结果。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201028V#1763F#5P你们赢了\n',
            '我们就说出知道的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201029V#1760F#5P要是我们赢了……\n',
            '就别再摆那么大架子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201030V#051F哼，好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0106, 18)
    ChrSetSubChip(0x0106, 0)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050201031V#053F就用我这重剑\n',
            '确认一下你们强了多少吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201032V#054F你们三个，鼓足劲来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_3282')
    def lambda_3282():
        ChrWalkTo(0x00FE, -4380, 0, 7750, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3282)

    WaitForThreadExit(0x0008, 0x0000)
    ChrClearFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_32A7')
    def lambda_32A7():
        ChrTurnDirection(0x0008, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_32A7)

    @scena.Lambda('lambda_32B5')
    def lambda_32B5():
        ChrTurnDirection(0x0009, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_32B5)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 13)
    ChrSetSubChip(0x0008, 0)
    Sleep(200)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 14)
    ChrSetSubChip(0x0009, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0450201033V#1749F#5P唉哟哟……\n',
            '怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201034V#1751F#2P不过、能再和艾丝蒂尔\n',
            '战斗真是幸运㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201035V#6P#1016F是、是这样吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201036V#1018F算了。\n',
            '我们也不会手软的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 16)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    Battle(0x0000079A, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_33F0'),
        (-1, 'loc_33F5'),
    )

    def _loc_33F0(): pass

    label('loc_33F0')

    OP_B4(0x00)

    Jump('loc_33F5')

    def _loc_33F5(): pass

    label('loc_33F5')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Sleep(1000)

    MapClearFlags(0x00000001)
    ChrSetPos(0x0101, -1240, 0, 3520, 357)
    ChrSetPos(0x0106, -2620, 0, 3570, 359)
    ChrSetPos(0x000A, -2360, 0, 6360, 182)
    ChrSetPos(0x0009, -1110, 0, 7050, 195)
    ChrSetPos(0x0008, -3870, 0, 6790, 123)
    ChrSetChipByIndex(0x0008, 19)
    ChrSetSubChip(0x0008, 3)
    ChrSetChipByIndex(0x0009, 20)
    ChrSetSubChip(0x0009, 3)
    ChrSetChipByIndex(0x000A, 21)
    ChrSetSubChip(0x000A, 3)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0106, 65535)
    CameraMove(-2650, 0, 5850, 0)
    OP_67(0, 8350, -10000, 0)
    CameraSetDistance(2670, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0450201037V#1748F哇～果然是强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201038V#1755F白旗白旗，投降啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201039V#1767F……可恶………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201040V#051F哼，能出席武术大会\n',
            '看来不完全是骗人的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201041V不过，本事还差得远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201042V#1006F#6P但身为普通人来说\n',
            '应该算是相当强了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201043V别窝在这种地方了\n',
            '不如也试着当游击士看看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_99(0x000A, 0x03, 0x01, 1000)
    ChrSetChipByIndex(0x000A, 2)
    ChrSetSubChip(0x000A, 0)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0460201044V#1762F什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x03, 0x01, 1000)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetSubChip(0x0009, 0)
    OP_99(0x0008, 0x03, 0x01, 1000)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0450201045V#1743F我、我们当游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201046V#1753F不、不可能啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201047V#1011F#6P看，像我这样的小女孩\n',
            '也能当上游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201048V你们也一样，只要有心\n',
            '就一定能成功的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000A, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0008)
    OP_63(0x0009)
    OP_63(0x000A)
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050201049V#050F#5P喂，别说得那么简单。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201050V游击士又不是佣兵。\n',
            '要做的事又不只是打架。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201051V你不是也经历了很多事吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201052V#1015F#4P嗯……\n',
            '那倒是啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450201053V#1742F就、就是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450201054V#1749F我们几个，除了打架\n',
            '又没别的本事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201055V#1754F那么好的事，\n',
            '怎么可能嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201056V#1764F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201057V#1763F总之，约定就是约定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201058V#1760F你们想知道的事\n',
            '我就说出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x000A, 400)
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0106,
        (
            '#0050201059V#051F哦，那就开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201060V#1002F#6P刚才也说了，\n',
            '我们在找目击了\n',
            '『白影』的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201061V听说\n',
            '有你们的伙伴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201062V#1761F啊啊，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201063V但是今天他没来，\n',
            '是个叫贝尔夫的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450201064V#1740F１年前加入的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450201065V阿加特也应该\n',
            '记得有这个人的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201066V#552F啊啊，那家伙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201067V调查之前的事件时\n',
            '稍微说过几句话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201068V#1752F贝尔夫那家伙，这几天\n',
            '都没来这个仓库呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470201069V#1754F可能因为看到幽灵\n',
            '太过受惊关在家里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010201070V#1020F#6P咦咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201071V那、那难不成是\n',
            '中了诅咒什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201072V#1764F这就不知道了……\n',
            '不过确实被吓得够呛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201073V#1760F原本就是好人家的小孩，\n',
            '胆小的家伙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201074V#053F哼，生在正经的家庭\n',
            '却还来当不良少年啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201075V#050F算了，详细情况\n',
            '就去问本人吧，把他家地址告诉我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450201076V#1740F嗯～\n',
            '在市长官邸右边的房子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450201077V住在那里的是诺曼大叔一家，\n',
            '贝尔夫是他的长子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201078V#1011F#6P市长官邸右邻的房子，对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201079V#1001F多谢你们提供情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201080V#1006F#6P既然知道了地方\n',
            '就去拜访贝尔夫看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050201081V#051F#5P啊啊，就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x000A, 400)
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0106,
        (
            '#0050201082V#051F那我们走了。\n',
            '别闲着就去做坏事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201083V#1760F哼，多管闲事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450201084V#1741F辛苦了。\n',
            '有空请再来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201085V#1751F加油哦～艾丝蒂尔㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B0B')

    def _loc_3F2A(): pass

    label('loc_3F2A')

    ChrTalk(
        0x0101,
        (
            '#0010201086V#2P唉……\n',
            '才刚刚有点改观……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3FBC')
    def lambda_3FBC():
        CameraMove(-2500, 0, 4470, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3FBC)

    @scena.Lambda('lambda_3FD4')
    def lambda_3FD4():
        OP_67(0, 6500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3FD4)

    @scena.Lambda('lambda_3FEC')
    def lambda_3FEC():
        CameraSetDistance(2670, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3FEC)

    @scena.Lambda('lambda_3FFC')
    def lambda_3FFC():
        OP_6E(280, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3FFC)

    @scena.Lambda('lambda_400C')
    def lambda_400C():
        ChrTurnDirection(0x0008, 0x0103, 400)
        Yield()

        Jump('lambda_400C')

    DispatchAsync2(0x0008, 0x0001, lambda_400C)

    @scena.Lambda('lambda_401D')
    def lambda_401D():
        ChrTurnDirection(0x0009, 0x0101, 400)
        Yield()

        Jump('lambda_401D')

    DispatchAsync2(0x0009, 0x0001, lambda_401D)

    @scena.Lambda('lambda_402E')
    def lambda_402E():
        ChrTurnDirection(0x000A, 0x0103, 400)
        Yield()

        Jump('lambda_402E')

    DispatchAsync2(0x000A, 0x0001, lambda_402E)

    ChrTurnDirection(0x0013, 0x0103, 800)
    ChrTurnDirection(0x0014, 0x0103, 800)
    ChrTurnDirection(0x0015, 0x0103, 800)
    Sleep(300)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0450201087V#1743F#4P你、你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201088V#1753F#6P哇！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470201089V#1751F#6P这不是新人游击士\n',
            '艾丝蒂尔吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_40E6')
    def lambda_40E6():
        ChrTurnDirection(0x0101, 0x0009, 0)
        Yield()

        Jump('lambda_40E6')

    DispatchAsync2(0x0103, 0x0001, lambda_40E6)

    @scena.Lambda('lambda_40F7')
    def lambda_40F7():
        ChrTurnDirection(0x0103, 0x000A, 0)
        Yield()

        Jump('lambda_40F7')

    DispatchAsync2(0x0103, 0x0002, lambda_40F7)

    @scena.Lambda('lambda_4108')
    def lambda_4108():
        ChrTurnDirection(0x0013, 0x0103, 0)
        Yield()

        Jump('lambda_4108')

    DispatchAsync2(0x0013, 0x0000, lambda_4108)

    @scena.Lambda('lambda_4119')
    def lambda_4119():
        ChrTurnDirection(0x0014, 0x0103, 0)
        Yield()

        Jump('lambda_4119')

    DispatchAsync2(0x0014, 0x0000, lambda_4119)

    @scena.Lambda('lambda_412A')
    def lambda_412A():
        ChrMoveTo(0x00FE, -1800, 0, 4900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_412A)

    Sleep(300)

    @scena.Lambda('lambda_414A')
    def lambda_414A():
        ChrMoveTo(0x00FE, -3000, 0, 4790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_414A)

    Sleep(500)

    @scena.Lambda('lambda_416A')
    def lambda_416A():
        CameraMove(-3350, 0, 7460, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_416A)

    @scena.Lambda('lambda_4182')
    def lambda_4182():
        OP_67(0, 8350, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4182)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0103, 0x0000)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0103, 0x02)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0014, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010201000V#6P#1006F你们好，好久不见呢。\n',
            '武术大会对战之后就没见过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201001V#1760F#5P啊～对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201002V#1756F#2P呀～我们在那之后\n',
            '一直观战到决胜战了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470201003V#1751F#2P真是厉害啊。\n',
            '我重新开始仰慕你了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201094V#6P#1008F啊哈哈……谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201095V#1007F话说回来……\n',
            '卡露娜姐姐一不在\n',
            '你们就想偷懒啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201096V#1019F被阿加特知道了\n',
            '可有你们好受的哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450201097V#1749F#5P只、只不过是开玩笑嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450201098V#1742F#5P可千万别\n',
            '跟那家伙说哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201099V#1765F#5P切……那种家伙，\n',
            '有什么好怕的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201100V#1753F#2P嗯，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470201101V#1750F#2P这位\n',
            '妩媚的姐姐是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201102V#6P#1011F这是雪拉姐。\n',
            '和我同为游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201103V#021F幸会。\n',
            '我是雪拉扎德·哈维。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201104V和你们的阿加特前辈\n',
            '关系很好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201105V#027F呵呵……\n',
            '多多关照哦，不良少年们㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0450201106V#1743F#5P吞口水……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201107V#1762F#5P这真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201108V#1753F#2P好、好迷人～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201109V#4P#1019F我说，雪拉姐。\n',
            '干嘛这么的散发魅力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201110V这些人本来就\n',
            '很少接触女性，很危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201111V#021F#5P好了，\n',
            '知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201112V#027F先不说这些了，那件事\n',
            '不问问他们看吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201113V#1004F#4P啊，是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)
    ChrTurnDirection(0x0103, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201114V#1002F#6P那个，这次来找你们\n',
            '是为了协会的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201006V嗯，你们之中\n',
            '是不是有人看到了『白影』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0450201007V#1742F#5P那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0470201008V#1752F#4P……是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201118V#1011F#6P啊，你们果然知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201119V#020F不介意的话\n',
            '能不能告诉我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000A, 400)
    ChrTurnDirection(0x0009, 0x000A, 400)
    ChrSetDirection(0x000A, 0, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000A, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0450201120V#1741F#5P果然这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201121V#1761F#3P是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201122V#1751F#4P……呜哦～太棒了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010201123V#1015F#6P（在说什么呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0008)
    OP_63(0x0009)
    OP_63(0x000A)
    Sleep(1000)

    ChrTurnDirection(0x0009, 0x0101, 400)
    ChrTurnDirection(0x000A, 0x0103, 400)
    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '#0450201124V#1740F#5P告诉你们是可以，不过有条件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201125V#1756F#2P只要你们答应的话\n',
            '就告诉你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201126V#1019F#6P什、什么啦。\n',
            '什么条件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201127V#025F（嗯～是不是\n',
            '有点挑拨过头了呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201128V#1761F#5P哼，这还用说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201129V#5P说到那时候\n',
            '的约定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_4AA6')
    def lambda_4AA6():
        ChrWalkTo(0x00FE, -4380, 0, 7750, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_4AA6)

    WaitForThreadExit(0x0008, 0x0000)
    ChrClearFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_4ACB')
    def lambda_4ACB():
        ChrTurnDirection(0x0008, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4ACB)

    @scena.Lambda('lambda_4AD9')
    def lambda_4AD9():
        ChrTurnDirection(0x0009, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4AD9)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x000A, 15)
    ChrSetSubChip(0x000A, 0)
    Sleep(200)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 13)
    ChrSetSubChip(0x0008, 0)
    Sleep(200)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 14)
    ChrSetSubChip(0x0009, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0450201130V#1741F#5P那就是，一决胜负！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450201131V#5P武术大会时的仇\n',
            '就在这里讨回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201132V#6P#023F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201133V#1751F#2P从那以后，我们\n',
            '可是强多～了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470201134V#1756F#2P而且现在是３对２，\n',
            '绝对不会输哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201135V#6P#1006F怎么，原来是这种事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 16)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010201136V#1018F#6P求之不得！\n',
            '雪拉姐也没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201137V#023F嗯、嗯，倒是无所谓……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201138V#027F算了。\n',
            '那就不客气了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0103, 17)
    ChrSetSubChip(0x0103, 0)
    OP_0D()
    Sleep(500)

    ChrSetChipByIndex(0x0103, 23)
    PlaySE(502, 0x00, 0x64)

    @scena.Lambda('lambda_4D1E')
    def lambda_4D1E():
        OP_99(0x0103, 0x00, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_4D1E)

    Sleep(100)

    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_4D45')
    def lambda_4D45():
        ChrJumpTo(0x000A, -2970, 0, 7500, 300, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4D45)

    WaitForThreadExit(0x0103, 0x0000)

    @scena.Lambda('lambda_4D68')
    def lambda_4D68():
        OP_99(0x0103, 0x07, 0x09, 2000)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_4D68)

    WaitForThreadExit(0x0103, 0x0000)
    ChrSetChipByIndex(0x0103, 17)
    ChrSetSubChip(0x0103, 0)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#1743F#2P#1K呜哦！？',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000A,
        (
            '#1762F#3P#1K呜哎！？',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0009,
        (
            '#0470201141V#1753F#4P#1K呜啊！？',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()

    ChrTalk(
        0x0103,
        (
            '#0030201142V#021F欢迎，小男孩们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201143V姐姐会\n',
            '好好疼爱你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0450201144V#1749F#5P呀，啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201145V#1762F#5P果然跟女人打\n',
            '实在是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201146V#1755F#2P感觉没有男人风度啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201147V#021F呵呵，不用客气哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201148V#027F机会难得，\n',
            '我会让你们酥软到骨子里的！㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x000A, 0xFF)
    Battle(0x0000079A, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_4F95'),
        (-1, 'loc_4F9A'),
    )

    def _loc_4F95(): pass

    label('loc_4F95')

    OP_B4(0x00)

    Jump('loc_4F9A')

    def _loc_4F9A(): pass

    label('loc_4F9A')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Sleep(1000)

    MapClearFlags(0x00000001)
    ChrSetPos(0x0101, -1240, 0, 3520, 357)
    ChrSetPos(0x0103, -2620, 0, 3570, 359)
    ChrSetPos(0x000A, -2360, 0, 6360, 182)
    ChrSetPos(0x0009, -1110, 0, 7050, 195)
    ChrSetPos(0x0008, -3870, 0, 6790, 123)
    ChrSetChipByIndex(0x0008, 19)
    ChrSetSubChip(0x0008, 3)
    ChrSetChipByIndex(0x0009, 20)
    ChrSetSubChip(0x0009, 3)
    ChrSetChipByIndex(0x000A, 21)
    ChrSetSubChip(0x000A, 3)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    CameraMove(-2650, 0, 5850, 0)
    OP_67(0, 8350, -10000, 0)
    CameraSetDistance(2670, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0450201149V#1749F啊呜啊呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201150V#1755F麻、麻掉了～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201151V#1764F败、败了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201152V#023F哎呀，这么快就结束了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201153V#021F最近的孩子真柔弱啊。\n',
            '再多来点也没关系嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201154V#1007F#6P唉，面对雪拉姐\n',
            '来多少都不够啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201155V#1006F不过，大会结束后\n',
            '你们好像也有认真锻炼呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201043V别窝在这种地方了，\n',
            '不如也试着当游击士看看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_99(0x000A, 0x03, 0x01, 1000)
    ChrSetChipByIndex(0x000A, 2)
    ChrSetSubChip(0x000A, 0)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0460201044V#1762F什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x03, 0x01, 1000)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetSubChip(0x0009, 0)
    OP_99(0x0008, 0x03, 0x01, 1000)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0450201045V#1743F我、我们当游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201046V#1753F不、不可能啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201047V#1011F#6P看，像我这样的小女孩\n',
            '也能当上游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201048V你们也一样，只要有心\n',
            '就一定能成功的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000A, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0008)
    OP_63(0x0009)
    OP_63(0x000A)
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201162V#020F#5P嗯，单说打斗的话\n',
            '应该跟准游击士差不多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201163V不过，游击士要做的\n',
            '并不只是战斗的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201164V不要以为嘴上说说\n',
            '就能轻易当上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201165V#1015F#4P嗯……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450201053V#1742F就、就是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450201054V#1749F我们几个，除了打架\n',
            '又没别的本事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201055V#1754F那么好的事，\n',
            '怎么可能嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201056V#1764F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201057V#1763F总之，约定就是约定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201058V#1760F你们想知道的事\n',
            '我就说出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x000A, 400)
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201172V#021F呵呵，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201060V#1002F#6P刚才也说了，\n',
            '我们在找目击了\n',
            '『白影』的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201061V听说\n',
            '有你们的伙伴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201062V#1761F啊啊，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201063V但是今天他没来，\n',
            '是个叫贝尔夫的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450201064V#1740F１年前加入帮里的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450201178V你应该\n',
            '也见过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201179V#1015F#6P嗯～你们以外的人\n',
            '就没什么印象了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201180V不过感觉好像是有这么个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201181V#1752F贝尔夫那家伙，差不多一周\n',
            '都没来这个仓库呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470201069V#1754F可能因为看到幽灵太过受惊，\n',
            '就把自己关在家里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010201070V#1020F#6P咦咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201071V那、那难不成是\n',
            '中了诅咒什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201072V#1764F这就不知道了……\n',
            '不过确实被吓得够呛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460201073V#1760F原本就是好人家的小孩，\n',
            '胆小的家伙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201187V#026F好像有各种原因呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201188V#020F详细情况去问本人好了，\n',
            '能告诉我们他住的地方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450201189V#1740F嗯～\n',
            '在市长官邸右边的房子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450201190V住在那里的是诺曼大叔一家，\n',
            '贝尔夫是他的长子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201078V#1011F#6P市长官邸右边的房子，对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201079V#1001F多谢你们提供情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201080V#1006F#6P既然知道了地方\n',
            '就去拜访贝尔夫看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201194V#020F#5P是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x000A, 400)
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201195V#021F谢谢了，不良少年们。\n',
            '我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460201196V#1760F哦，哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450201197V#1741F辛苦了！\n',
            '再来哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470201198V#1751F加油哦～㈱\n',
            '大姐姐还有艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5B0B(): pass

    label('loc_5B0B')

    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0008, -4150, 0, 9070, 90)
    ChrSetPos(0x0009, -1590, 0, 7520, 322)
    ChrSetPos(0x000A, -2970, 0, 7390, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, func_02_591)
    CreateThread(0x0009, 0x00, 0x00, func_02_591)
    CreateThread(0x000A, 0x00, 0x00, func_02_591)
    CreateThread(0x0013, 0x00, 0x00, func_02_591)
    CreateThread(0x0014, 0x00, 0x00, func_02_591)
    CreateThread(0x0015, 0x00, 0x00, func_02_591)
    ChrSetDirection(0x0013, 280, 0)
    ChrSetDirection(0x0014, 80, 0)
    ChrSetDirection(0x0015, 303, 0)
    ChrSetDirection(0x0016, 90, 0)
    ChrSetDirection(0x0017, 0, 0)
    CameraMove(-3460, 0, 3720, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -3460, 0, 3720, 0)
    ChrSetPos(0x00F7, -3460, 0, 3720, 0)
    OP_6A(0x0000)
    SetScenaFlags(ScenaFlag(0x0241, 6, 0x120E))
    OP_28(0x0082, 0x02, 0x0010)
    OP_28(0x0082, 0x01, 0x0020)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x5C31
@scena.Code('func_15_5C31')
def func_15_5C31():
    ChrClearFlags(0x00FE, 0x0008)
    ChrWalkTo(0x00FE, -6570, 0, 3800, 6000, 0x00)

    Return()

# id: 0x0016 offset: 0x5C4B
@scena.Code('func_16_5C4B')
def func_16_5C4B():
    ChrWalkTo(0x00FE, -7920, 0, 2850, 6000, 0x00)

    Return()

# id: 0x0017 offset: 0x5C60
@scena.Code('func_17_5C60')
def func_17_5C60():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        (0x00000000, 'loc_5CDA'),
        (0x00000001, 'loc_5CE0'),
        (-1, 'loc_5CE6'),
    )

    def _loc_5CDA(): pass

    label('loc_5CDA')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5CE6')

    def _loc_5CE0(): pass

    label('loc_5CE0')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5CE6')

    def _loc_5CE6(): pass

    label('loc_5CE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5CF4',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_5CF8')

    def _loc_5CF4(): pass

    label('loc_5CF4')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_5CF8(): pass

    label('loc_5CF8')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
