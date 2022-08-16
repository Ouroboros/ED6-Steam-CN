import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1510_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1510   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1510.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20109._CH', 'ED6_DT06/CH20109P._CP'),
        ('ED6_DT26/CH20225._CH', 'ED6_DT26/CH20225P._CP'),
        ('ED6_DT26/CH20226._CH', 'ED6_DT26/CH20226P._CP'),
        ('ED6_DT26/CH20231._CH', 'ED6_DT26/CH20231P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01233._CH', 'ED6_DT07/CH01233P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT26/CH20315._CH', 'ED6_DT26/CH20315P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT27/CH03840._CH', 'ED6_DT27/CH03840P._CP'),
    ]

# id: 0x10001 offset: 0x18A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雪拉扎德',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '阿加特',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '科洛丝',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '提妲',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '金',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '凯文神父',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '索菲娜',
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '雷纳德',
            x                   = 26500,
            z                   = 0,
            y                   = 12600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '库瓦诺老人',
            x                   = 17240,
            z                   = 0,
            y                   = 13470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '诺琪',
            x                   = 16219,
            z                   = 200,
            y                   = 6370,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '赫穆特',
            x                   = 15130,
            z                   = 0,
            y                   = 7430,
            direction           = 196,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '测量师艾柯',
            x                   = 23990,
            z                   = 0,
            y                   = 8790,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '水壶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703952,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638416,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638416,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638416,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638416,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '水壶',
            x                   = 14900,
            z                   = 800,
            y                   = 6350,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703952,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 15300,
            z                   = 800,
            y                   = 6200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638416,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x40A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x40A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x40A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 23100,
            triggerZ            = 0,
            triggerY            = 6000,
            triggerRange        = 700,
            actorX              = 24500,
            actorZ              = 1500,
            actorY              = 6100,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x42E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 2, 0x1C02)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_860',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_477',
    )

    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0008, 0x0080)

    def _loc_477(): pass

    label('loc_477')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DF',
    )

    ChrSetFlags(0x0009, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B5',
    )

    ChrSetPos(0x0009, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4D0')

    def _loc_4B5(): pass

    label('loc_4B5')

    ChrSetPos(0x0009, 18100, 200, 10270, 270)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4D0(): pass

    label('loc_4D0')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0009, 0x0080)

    def _loc_4DF(): pass

    label('loc_4DF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_572',
    )

    ChrSetFlags(0x000A, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51D',
    )

    ChrSetPos(0x000A, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_563')

    def _loc_51D(): pass

    label('loc_51D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_548',
    )

    ChrSetPos(0x000A, 18100, 200, 10270, 270)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_563')

    def _loc_548(): pass

    label('loc_548')

    ChrSetPos(0x000A, 15510, 200, 10470, 90)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_563(): pass

    label('loc_563')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000A, 0x0080)

    def _loc_572(): pass

    label('loc_572')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_630',
    )

    ChrSetFlags(0x000B, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B0',
    )

    ChrSetPos(0x000B, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_621')

    def _loc_5B0(): pass

    label('loc_5B0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5DB',
    )

    ChrSetPos(0x000B, 18100, 200, 10270, 270)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_621')

    def _loc_5DB(): pass

    label('loc_5DB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_606',
    )

    ChrSetPos(0x000B, 15510, 200, 10470, 90)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_621')

    def _loc_606(): pass

    label('loc_606')

    ChrSetPos(0x000B, 15510, 200, 9020, 90)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_621(): pass

    label('loc_621')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000B, 0x0080)

    def _loc_630(): pass

    label('loc_630')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6EE',
    )

    ChrSetFlags(0x000C, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_66E',
    )

    ChrSetPos(0x000C, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6DF')

    def _loc_66E(): pass

    label('loc_66E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_699',
    )

    ChrSetPos(0x000C, 18100, 200, 10270, 270)

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6DF')

    def _loc_699(): pass

    label('loc_699')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C4',
    )

    ChrSetPos(0x000C, 15510, 200, 10470, 90)

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6DF')

    def _loc_6C4(): pass

    label('loc_6C4')

    ChrSetPos(0x000C, 15510, 200, 9020, 90)

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6DF(): pass

    label('loc_6DF')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000C, 0x0080)

    def _loc_6EE(): pass

    label('loc_6EE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7AC',
    )

    ChrSetFlags(0x000D, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_72C',
    )

    ChrSetPos(0x000D, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_79D')

    def _loc_72C(): pass

    label('loc_72C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_757',
    )

    ChrSetPos(0x000D, 18100, 200, 10270, 270)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_79D')

    def _loc_757(): pass

    label('loc_757')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_782',
    )

    ChrSetPos(0x000D, 15510, 200, 10470, 90)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_79D')

    def _loc_782(): pass

    label('loc_782')

    ChrSetPos(0x000D, 15510, 200, 9020, 90)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_79D(): pass

    label('loc_79D')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000D, 0x0080)

    def _loc_7AC(): pass

    label('loc_7AC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_860',
    )

    ChrSetFlags(0x000E, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7EA',
    )

    ChrSetPos(0x000E, 18100, 200, 8820, 0)

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_85B')

    def _loc_7EA(): pass

    label('loc_7EA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_815',
    )

    ChrSetPos(0x000E, 18100, 200, 10270, 0)

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_85B')

    def _loc_815(): pass

    label('loc_815')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_840',
    )

    ChrSetPos(0x000E, 15510, 200, 10470, 0)

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_85B')

    def _loc_840(): pass

    label('loc_840')

    ChrSetPos(0x000E, 15510, 200, 9020, 90)

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_85B(): pass

    label('loc_85B')

    ChrClearFlags(0x000E, 0x0080)

    def _loc_860(): pass

    label('loc_860')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_87A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_877',
    )

    ChrClearFlags(0x0014, 0x0080)

    Jump('loc_877')

    def _loc_877(): pass

    label('loc_877')

    Jump('loc_9FE')

    def _loc_87A(): pass

    label('loc_87A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Return,
        ),
        'loc_9AA',
    )

    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetPos(0x0008, 109270, 200, 12030, 270)
    ChrSetPos(0x000B, 106990, 200, 13150, 90)
    ChrSetPos(0x000C, 106980, 200, 12170, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0015, 108420, 800, 12550, 0)
    ChrSetPos(0x0016, 108690, 800, 12880, 90)
    ChrSetPos(0x0017, 108620, 800, 11860, 90)
    ChrSetPos(0x0018, 107530, 800, 11920, 270)
    ChrSetPos(0x0019, 107550, 800, 12940, 270)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetPos(0x0009, 18100, 200, 8820, 270)
    ChrSetPos(0x000A, 18100, 200, 10270, 270)
    ChrSetPos(0x000D, 15510, 200, 10470, 90)
    ChrSetPos(0x000E, 15510, 200, 9020, 90)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_9FE')

    def _loc_9AA(): pass

    label('loc_9AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_9CA',
    )

    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 24700, 0, 8790, 0)

    Jump('loc_9FE')

    def _loc_9CA(): pass

    label('loc_9CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_9E8',
    )

    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)

    Jump('loc_9FE')

    def _loc_9E8(): pass

    label('loc_9E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_9F2',
    )

    Jump('loc_9FE')

    def _loc_9F2(): pass

    label('loc_9F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_9FE',
    )

    ChrClearFlags(0x0011, 0x0080)

    def _loc_9FE(): pass

    label('loc_9FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_A18',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    OP_B1('t1510_y')
    Event(0, func_20_537F)

    Jump('loc_A85')

    def _loc_A18(): pass

    label('loc_A18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_A32',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x19),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_32_6399)

    Jump('loc_A85')

    def _loc_A32(): pass

    label('loc_A32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_A55',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x19),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    OP_B1('t1510_y')
    Event(0, func_36_67B4)

    Jump('loc_A85')

    def _loc_A55(): pass

    label('loc_A55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_A75',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x46),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1F(0x5A, 0x00000064)
    Event(0, func_37_7412)

    Jump('loc_A85')

    def _loc_A75(): pass

    label('loc_A75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 2, 0x1C02)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A85',
    )

    Event(0, func_11_2FFC)

    def _loc_A85(): pass

    label('loc_A85')

    Return()

# id: 0x0001 offset: 0xA86
@scena.Code('func_01_A86')
def func_01_A86():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B20',
    )

    OP_B1('t1510_n')
    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0020)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0020)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0020)
    OP_72(0x0007, 0x0008)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_71(0x0011, 0x0004)

    Jump('loc_B41')

    def _loc_B20(): pass

    label('loc_B20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Return,
        ),
        'loc_B38',
    )

    OP_B1('t1510_y')
    OP_71(0x001D, 0x0004)

    Jump('loc_B41')

    def _loc_B38(): pass

    label('loc_B38')

    OP_B1('t1510_n')

    def _loc_B41(): pass

    label('loc_B41')

    Return()

# id: 0x0002 offset: 0xB42
@scena.Code('func_02_B42')
def func_02_B42():
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
        'loc_B67',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_CA9')

    def _loc_B67(): pass

    label('loc_B67')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B80',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_CA9')

    def _loc_B80(): pass

    label('loc_B80')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B99',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_CA9')

    def _loc_B99(): pass

    label('loc_B99')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB2',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_CA9')

    def _loc_BB2(): pass

    label('loc_BB2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BCB',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_CA9')

    def _loc_BCB(): pass

    label('loc_BCB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BE4',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_CA9')

    def _loc_BE4(): pass

    label('loc_BE4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BFD',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_CA9')

    def _loc_BFD(): pass

    label('loc_BFD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C16',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_CA9')

    def _loc_C16(): pass

    label('loc_C16')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C2F',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_CA9')

    def _loc_C2F(): pass

    label('loc_C2F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C48',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_CA9')

    def _loc_C48(): pass

    label('loc_C48')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C61',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_CA9')

    def _loc_C61(): pass

    label('loc_C61')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C7A',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_CA9')

    def _loc_C7A(): pass

    label('loc_C7A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C93',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_CA9')

    def _loc_C93(): pass

    label('loc_C93')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CA9',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_CA9(): pass

    label('loc_CA9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CBE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_CA9')

    def _loc_CBE(): pass

    label('loc_CBE')

    Return()

# id: 0x0003 offset: 0xCBF
@scena.Code('func_03_CBF')
def func_03_CBF():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0xCC4
@scena.Code('func_04_CC4')
def func_04_CC4():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 4, 0x1C04)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D47',
    )

    ChrTalk(
        0x000F,
        (
            '哎呀，你去散步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '离吃晚饭\n',
            '还有些时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '请就随便在四周走走，\n',
            '享受一下散步的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_D9B')

    def _loc_D47(): pass

    label('loc_D47')

    ChrTalk(
        0x000F,
        (
            '这个时间，夕阳照射到湖面\n',
            '折射出非常美丽的光辉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我想正是散步\n',
            '最好的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D9B(): pass

    label('loc_D9B')

    TalkEnd(0x000F)

    Return()

    def _loc_D9F(): pass

    label('loc_D9F')

    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DB6',
    )

    OP_A9(0x49)
    TalkEnd(0x000F)

    Return()

    def _loc_DB6(): pass

    label('loc_DB6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DC7',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_DC7(): pass

    label('loc_DC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_EB8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E5D',
    )

    ChrTalk(
        0x000F,
        (
            '罗伊德和平时一样\n',
            '在开心地钓鱼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '明明空中出现了奇怪的岛，\n',
            '还能这样静下心来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这样的专业…\n',
            '还真是个厉害的家伙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_EB5')

    def _loc_E5D(): pass

    label('loc_E5D')

    ChrTalk(
        0x000F,
        (
            '在空中浮着岛的时候\n',
            '竟然还很开心地钓鱼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '要是我在这里的话\n',
            '只会感到不安呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB5(): pass

    label('loc_EB5')

    Jump('loc_10A2')

    def _loc_EB8(): pass

    label('loc_EB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_FA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F4C',
    )

    ChrTalk(
        0x000F,
        (
            '王室的船停靠在湖上，\n',
            '空中又出现岛屿…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '尽是些难以置信的事，\n',
            '我也不由地感到不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因此昨天就\n',
            '没怎么睡……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_FA4')

    def _loc_F4C(): pass

    label('loc_F4C')

    ChrTalk(
        0x000F,
        (
            '王室的船停靠在湖上，\n',
            '空中又出现岛屿…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '呼，最近尽是些\n',
            '难以置信的事呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FA4(): pass

    label('loc_FA4')

    Jump('loc_10A2')

    def _loc_FA7(): pass

    label('loc_FA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_FF1',
    )

    ChrTalk(
        0x000F,
        (
            '非常感谢各位\n',
            '预约本旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '如果有任何指示\n',
            '请尽管吩咐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A2')

    def _loc_FF1(): pass

    label('loc_FF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_105B',
    )

    ChrTalk(
        0x000F,
        (
            '不安心情在住宿的客人们中间\n',
            '也散播开来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '王国军好像有什么计划，\n',
            '真想快点解决骚乱呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A2')

    def _loc_105B(): pass

    label('loc_105B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_10A2',
    )

    ChrTalk(
        0x000F,
        (
            '欢迎光临。\n',
            '欢迎来到川蝉亭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '想要住宿的话\n',
            '请和我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10A2(): pass

    label('loc_10A2')

    TalkEnd(0x000F)

    Return()

# id: 0x0005 offset: 0x10A6
@scena.Code('func_05_10A6')
def func_05_10A6():
    TalkBegin(0x0010)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10C0',
    )

    OP_A9(0x4A)
    TalkEnd(0x0010)

    Return()

    def _loc_10C0(): pass

    label('loc_10C0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10D1',
    )

    TalkEnd(0x0010)

    Return()

    def _loc_10D1(): pass

    label('loc_10D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_11E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1194',
    )

    ChrTalk(
        0x0010,
        (
            '不过，湖上『埃尔赛尤』\n',
            '今后怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这样的异常延续下去，\n',
            '导力引擎肯定也飞不起来吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '但是，也不可能\n',
            '整艘拖回王都去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '暂时可能会这样，\n',
            '浮在湖面上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_11E4')

    def _loc_1194(): pass

    label('loc_1194')

    ChrTalk(
        0x0010,
        (
            '不过，湖上『埃尔赛尤』\n',
            '今后怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '暂时可能会这样，\n',
            '浮在湖面上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11E4(): pass

    label('loc_11E4')

    Jump('loc_15A6')

    def _loc_11E7(): pass

    label('loc_11E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_12DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1284',
    )

    ChrTalk(
        0x0010,
        (
            '停泊在湖面上的飞船\n',
            '是王室的船呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '亲卫队的人经常到我们这里\n',
            '来买些东西回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那次异常\n',
            '幸好发生在水面上，\n',
            '没事实在太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_12DA')

    def _loc_1284(): pass

    label('loc_1284')

    ChrTalk(
        0x0010,
        (
            '停泊在湖面上的飞船\n',
            '是王室的船呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '亲卫队的人经常到我们这里\n',
            '来买些东西回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12DA(): pass

    label('loc_12DA')

    Jump('loc_15A6')

    def _loc_12DD(): pass

    label('loc_12DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Return,
        ),
        'loc_1322',
    )

    ChrTalk(
        0x0010,
        (
            '今天进了很多\n',
            '新鲜的鱼贝类食物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '好好期待晚饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A6')

    def _loc_1322(): pass

    label('loc_1322')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1440',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1392',
    )

    ChrTalk(
        0x0010,
        (
            '慢慢消遣\n',
            '等待晚饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '没事做的话\n',
            '试着钓鱼怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '在筏桥的附近\n',
            '有很好钓鱼点哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_143D')

    def _loc_1392(): pass

    label('loc_1392')

    ChrTalk(
        0x0010,
        (
            '喔，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '非常感谢各位预订\n',
            '我们兄妹的旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '离晚饭还有段时间，\n',
            '慢慢消遣等待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '没事做的话\n',
            '试着钓鱼怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '在筏桥的附近\n',
            '有很好钓鱼点哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_143D(): pass

    label('loc_143D')

    Jump('loc_15A6')

    def _loc_1440(): pass

    label('loc_1440')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_14D6',
    )

    ChrTalk(
        0x0010,
        (
            '据说有到拉文努村\n',
            '好像被龙破坏了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '虽说离这里有些距离，\n',
            '但能飞在空中的话就没什么距离可言了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这可不能当成别人家的事不管啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A6')

    def _loc_14D6(): pass

    label('loc_14D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_15A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_153B',
    )

    ChrTalk(
        0x0010,
        (
            '最近来钓鱼的\n',
            '客人特别多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '还有年轻的女性，\n',
            '现在钓鱼爱好者的层面还真广呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A6')

    def _loc_153B(): pass

    label('loc_153B')

    ChrTalk(
        0x0010,
        (
            '噢，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '最近来钓鱼的\n',
            '客人特别多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '还有对夫妇一起来的，\n',
            '现在钓鱼爱好者的层面还真广呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_15A6(): pass

    label('loc_15A6')

    TalkEnd(0x0010)

    Return()

# id: 0x0006 offset: 0x15AA
@scena.Code('func_06_15AA')
def func_06_15AA():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1696',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1616',
    )

    ChrTalk(
        0x00FE,
        (
            '听说龙出现了……\n',
            '真是件难以置信的事呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为经常去城里，\n',
            '没想到有这么大的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1696')

    def _loc_1616(): pass

    label('loc_1616')

    ChrTalk(
        0x00FE,
        (
            '听说龙出现了……\n',
            '真是件难以置信的事呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为经常去城里，\n',
            '没想到有这么大的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『安特洛丝』的各位\n',
            '没有事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1696(): pass

    label('loc_1696')

    TalkEnd(0x0012)

    Return()

# id: 0x0007 offset: 0x169A
@scena.Code('func_07_169A')
def func_07_169A():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1788',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_16EC',
    )

    ChrTalk(
        0x00FE,
        (
            '在钓鱼比赛中\n',
            '输给了妻子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，是才能\n',
            '的差距吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1785')

    def _loc_16EC(): pass

    label('loc_16EC')

    ChrTalk(
        0x00FE,
        (
            '呼，向妻子挑战\n',
            '比赛钓鱼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……又输掉了。\n',
            '已经，无话可说的惨败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '搞不懂为什么总是\n',
            '她的鱼竿有鱼上钩呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，是才能\n',
            '的差距吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1785(): pass

    label('loc_1785')

    Jump('loc_17E9')

    def _loc_1788(): pass

    label('loc_1788')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_17E9',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到龙之类的生物\n',
            '真的存在的呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像受到了相当严重的损害，\n',
            '这里不要紧吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17E9(): pass

    label('loc_17E9')

    TalkEnd(0x0013)

    Return()

# id: 0x0008 offset: 0x17ED
@scena.Code('func_08_17ED')
def func_08_17ED():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_17FA',
    )

    Jump('loc_18A8')

    def _loc_17FA(): pass

    label('loc_17FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_18A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_185F',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来，休息休息，\n',
            '那就试着钓钓鱼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里的湖里\n',
            '有很多处非常好的钓鱼点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A8')

    def _loc_185F(): pass

    label('loc_185F')

    ChrTalk(
        0x00FE,
        (
            '呼，到了宿舍后\n',
            '果然放松下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在家里的婆婆\n',
            '实在太烦人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_18A8(): pass

    label('loc_18A8')

    TalkEnd(0x0011)

    Return()

# id: 0x0009 offset: 0x18AC
@scena.Code('func_09_18AC')
def func_09_18AC():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 5, 0x2095)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B8C',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，是你们呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 6, 0x2096)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19C3',
    )

    ChrTalk(
        0x0101,
        (
            '#1001F啊，你好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1004F……嗯，咦！？\n',
            '怎么会有亲卫队的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '我们划小船来的……\n',
            '为了筹措食物的任务……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F是，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '想想好象『埃尔赛尤』\n',
            '还停靠在湖面上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1043F就连拉赛尔博士也\n',
            '好象陷入苦战了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A66')

    def _loc_19C3(): pass

    label('loc_19C3')

    ChrTalk(
        0x0101,
        (
            '#1001F嘿嘿，你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F你是来购物的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，准备持久战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '修复军舰的日期还未确定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1043F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就连拉赛尔博士也\n',
            '好象陷入苦战了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A66(): pass

    label('loc_1A66')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A91',
    )

    ChrTalk(
        0x0107,
        (
            '#561F嗯，好象是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A91(): pass

    label('loc_1A91')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AE6',
    )

    ChrTalk(
        0x0106,
        (
            '#051F那是老爷子的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '交给他吧，最后一定会\n',
            '想办法解决好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B19')

    def _loc_1AE6(): pass

    label('loc_1AE6')

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，既然是博士，\n',
            '交给他一定能解决好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B19(): pass

    label('loc_1B19')

    ChrTalk(
        0x00FE,
        (
            '希望是吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再见，我还有任务……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1041F那么，请代我们\n',
            '向尤莉亚上尉问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0412, 5, 0x2095))

    Jump('loc_1BC2')

    def _loc_1B8C(): pass

    label('loc_1B8C')

    ChrTalk(
        0x00FE,
        (
            '我回去进行自己的任务了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们也保重呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1BC2(): pass

    label('loc_1BC2')

    TalkEnd(0x0014)

    Return()

# id: 0x000A offset: 0x1BC6
@scena.Code('func_0A_1BC6')
def func_0A_1BC6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 2, 0x1C02)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CD6',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0008)
    ChrClearFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1C62',
    )

    Jump('loc_1CA4')

    def _loc_1C62(): pass

    label('loc_1C62')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1C7E',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CA4')

    def _loc_1C7E(): pass

    label('loc_1C7E')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1C9A',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CA4')

    def _loc_1C9A(): pass

    label('loc_1C9A')

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1CA4(): pass

    label('loc_1CA4')

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0008, 0x0010)
    Call(0, 0x001A)
    ChrSetSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Return()

    def _loc_1CD6(): pass

    label('loc_1CD6')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0008)
    ChrClearFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1D66',
    )

    Jump('loc_1DA8')

    def _loc_1D66(): pass

    label('loc_1D66')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1D82',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1DA8')

    def _loc_1D82(): pass

    label('loc_1D82')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1D9E',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1DA8')

    def _loc_1D9E(): pass

    label('loc_1D9E')

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1DA8(): pass

    label('loc_1DA8')

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0008, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0030320705V#026F今天的夕阳也很美呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320706V#027F离晚饭还有些时间，\n',
            '去散散步吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x000B offset: 0x1E35
@scena.Code('func_0B_1E35')
def func_0B_1E35():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 2, 0x1C02)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F45',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0009)
    ChrClearFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1ED1',
    )

    Jump('loc_1F13')

    def _loc_1ED1(): pass

    label('loc_1ED1')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1EED',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F13')

    def _loc_1EED(): pass

    label('loc_1EED')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1F09',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F13')

    def _loc_1F09(): pass

    label('loc_1F09')

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1F13(): pass

    label('loc_1F13')

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0009, 0x0010)
    Call(0, 0x0018)
    ChrSetSubChip(0x0009, 0)
    TalkEnd(0x0009)

    Return()

    def _loc_1F45(): pass

    label('loc_1F45')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0009)
    ChrClearFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1FD5',
    )

    Jump('loc_2017')

    def _loc_1FD5(): pass

    label('loc_1FD5')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1FF1',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2017')

    def _loc_1FF1(): pass

    label('loc_1FF1')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_200D',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2017')

    def _loc_200D(): pass

    label('loc_200D')

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2017(): pass

    label('loc_2017')

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0009, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0386, 0, 0x1C30)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21FC',
    )

    ChrTalk(
        0x0009,
        (
            '#0050320692V#051F哟，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320693V怎么，还在散步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320694V#1011F嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320695V阿加特你们在干吗呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320696V#050F一边喝酒，\n',
            '一边闲聊呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320697V总之就是在\n',
            '悠闲的享受啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320698V反正这次就是为了休息\n',
            '才来这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320699V#1001F对对……\n',
            '必须好好休养身心一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320700V偶尔把工作抛开\n',
            '也没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320701V#051F啊啊，可不是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320702V那么，待会儿见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0386, 0, 0x1C30))

    Jump('loc_225F')

    def _loc_21FC(): pass

    label('loc_21FC')

    ChrTalk(
        0x0009,
        (
            '#0050320703V#051F偶尔这样\n',
            '深入交流也很好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320704V嗯，到晚饭前就在这里\n',
            '悠闲地度过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_225F(): pass

    label('loc_225F')

    ChrSetSubChip(0x0009, 0)
    TalkEnd(0x0009)

    Return()

# id: 0x000C offset: 0x2268
@scena.Code('func_0C_2268')
def func_0C_2268():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 2, 0x1C02)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2378',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000A)
    ChrClearFlags(0x000A, 0x0010)
    ChrTurnDirection(0x000A, 0x0000, 0)

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2304',
    )

    Jump('loc_2346')

    def _loc_2304(): pass

    label('loc_2304')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2320',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2346')

    def _loc_2320(): pass

    label('loc_2320')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_233C',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2346')

    def _loc_233C(): pass

    label('loc_233C')

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2346(): pass

    label('loc_2346')

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000A, 0x0010)
    Call(0, 0x001B)
    ChrSetSubChip(0x000A, 0)
    TalkEnd(0x000A)

    Return()

    def _loc_2378(): pass

    label('loc_2378')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000A)
    ChrClearFlags(0x000A, 0x0010)
    ChrTurnDirection(0x000A, 0x0000, 0)

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2408',
    )

    Jump('loc_244A')

    def _loc_2408(): pass

    label('loc_2408')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2424',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_244A')

    def _loc_2424(): pass

    label('loc_2424')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2440',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_244A')

    def _loc_2440(): pass

    label('loc_2440')

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_244A(): pass

    label('loc_244A')

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000A, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2551',
    )

    ChrTalk(
        0x000A,
        (
            '#0040320707V#031F哎呀，你好啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320708V这里有上等的美酒、新鲜的下酒菜……\n',
            '哎呀真是优雅的黄昏呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320709V再有美人来斟酒的话\n',
            '就没有什么可说的啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320710V嗯，好好期待\n',
            '晚饭之后吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_260F')

    def _loc_2551(): pass

    label('loc_2551')

    ChrTalk(
        0x000A,
        (
            '#0040320711V#031F这里有上等的美酒、新鲜的下酒菜……\n',
            '哎呀真是优雅的黄昏呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320712V唯一遗憾的是，没有如花似玉的美人相伴\n',
            '空添了一丝寂寞……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320713V嗯，真期待晚餐后\n',
            '的时间呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_260F(): pass

    label('loc_260F')

    ChrSetSubChip(0x000A, 0)
    TalkEnd(0x000A)

    Return()

# id: 0x000D offset: 0x2618
@scena.Code('func_0D_2618')
def func_0D_2618():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 2, 0x1C02)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2728',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000B)
    ChrClearFlags(0x000B, 0x0010)
    ChrTurnDirection(0x000B, 0x0000, 0)

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_26B4',
    )

    Jump('loc_26F6')

    def _loc_26B4(): pass

    label('loc_26B4')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_26D0',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_26F6')

    def _loc_26D0(): pass

    label('loc_26D0')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_26EC',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_26F6')

    def _loc_26EC(): pass

    label('loc_26EC')

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_26F6(): pass

    label('loc_26F6')

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000B, 0x0010)
    Call(0, 0x001C)
    ChrSetSubChip(0x000B, 0)
    TalkEnd(0x000B)

    Return()

    def _loc_2728(): pass

    label('loc_2728')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000B)
    ChrClearFlags(0x000B, 0x0010)
    ChrTurnDirection(0x000B, 0x0000, 0)

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_27B8',
    )

    Jump('loc_27FA')

    def _loc_27B8(): pass

    label('loc_27B8')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_27D4',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_27FA')

    def _loc_27D4(): pass

    label('loc_27D4')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27F0',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_27FA')

    def _loc_27F0(): pass

    label('loc_27F0')

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_27FA(): pass

    label('loc_27FA')

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000B, 0x0010)

    ChrTalk(
        0x000B,
        (
            '#0060320714V#040F晚霞照映下的瓦雷利亚湖\n',
            '十分的美丽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320715V#40F我们接下来也\n',
            '去阳台看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000B, 0)
    TalkEnd(0x000B)

    Return()

# id: 0x000E offset: 0x288F
@scena.Code('func_0E_288F')
def func_0E_288F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 2, 0x1C02)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_299F',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000C)
    ChrClearFlags(0x000C, 0x0010)
    ChrTurnDirection(0x000C, 0x0000, 0)

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_292B',
    )

    Jump('loc_296D')

    def _loc_292B(): pass

    label('loc_292B')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2947',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_296D')

    def _loc_2947(): pass

    label('loc_2947')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2963',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_296D')

    def _loc_2963(): pass

    label('loc_2963')

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_296D(): pass

    label('loc_296D')

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000C, 0x0010)
    Call(0, 0x0019)
    ChrSetSubChip(0x000C, 0)
    TalkEnd(0x000C)

    Return()

    def _loc_299F(): pass

    label('loc_299F')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000C)
    ChrClearFlags(0x000C, 0x0010)
    ChrTurnDirection(0x000C, 0x0000, 0)

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2A2F',
    )

    Jump('loc_2A71')

    def _loc_2A2F(): pass

    label('loc_2A2F')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2A4B',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2A71')

    def _loc_2A4B(): pass

    label('loc_2A4B')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2A67',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2A71')

    def _loc_2A67(): pass

    label('loc_2A67')

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A71(): pass

    label('loc_2A71')

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000C, 0x0010)

    ChrTalk(
        0x000C,
        (
            '#0070320716V#060F我们再留在这里\n',
            '喝一会儿茶。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070320717V再见，姐姐。\n',
            '吃晚饭时再见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000C, 0)
    TalkEnd(0x000C)

    Return()

# id: 0x000F offset: 0x2AFC
@scena.Code('func_0F_2AFC')
def func_0F_2AFC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 2, 0x1C02)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C0C',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000D)
    ChrClearFlags(0x000D, 0x0010)
    ChrTurnDirection(0x000D, 0x0000, 0)

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xD, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2B98',
    )

    Jump('loc_2BDA')

    def _loc_2B98(): pass

    label('loc_2B98')

    If(
        (
            (Expr.GetChrWork, 0xD, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2BB4',
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2BDA')

    def _loc_2BB4(): pass

    label('loc_2BB4')

    If(
        (
            (Expr.GetChrWork, 0xD, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2BD0',
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2BDA')

    def _loc_2BD0(): pass

    label('loc_2BD0')

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.GetChrWork, 0xD, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2BDA(): pass

    label('loc_2BDA')

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000D, 0x0010)
    Call(0, 0x001D)
    ChrSetSubChip(0x000D, 0)
    TalkEnd(0x000D)

    Return()

    def _loc_2C0C(): pass

    label('loc_2C0C')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000D)
    ChrClearFlags(0x000D, 0x0010)
    ChrTurnDirection(0x000D, 0x0000, 0)

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xD, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2C9C',
    )

    Jump('loc_2CDE')

    def _loc_2C9C(): pass

    label('loc_2C9C')

    If(
        (
            (Expr.GetChrWork, 0xD, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2CB8',
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2CDE')

    def _loc_2CB8(): pass

    label('loc_2CB8')

    If(
        (
            (Expr.GetChrWork, 0xD, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2CD4',
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2CDE')

    def _loc_2CD4(): pass

    label('loc_2CD4')

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.GetChrWork, 0xD, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2CDE(): pass

    label('loc_2CDE')

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000D, 0x0010)

    ChrTalk(
        0x000D,
        (
            '#0080320718V#070F又去钓鱼吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320719V#071F哈哈，不要太投入，\n',
            '不然赶不上吃晚饭的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000D, 0)
    TalkEnd(0x000D)

    Return()

# id: 0x0010 offset: 0x2D6F
@scena.Code('func_10_2D6F')
def func_10_2D6F():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000E)
    ChrClearFlags(0x000E, 0x0010)
    ChrTurnDirection(0x000E, 0x0000, 0)

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2DFF',
    )

    Jump('loc_2E41')

    def _loc_2DFF(): pass

    label('loc_2DFF')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2E1B',
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2E41')

    def _loc_2E1B(): pass

    label('loc_2E1B')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2E37',
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2E41')

    def _loc_2E37(): pass

    label('loc_2E37')

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2E41(): pass

    label('loc_2E41')

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000E, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 2, 0x1C02)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E79',
    )

    Call(0, 0x001E)

    Jump('loc_2FF3')

    def _loc_2E79(): pass

    label('loc_2E79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0386, 1, 0x1C31)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F8C',
    )

    ChrTalk(
        0x000E,
        (
            '#0180320720V#1064F噢，艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320721V喝茶的时间已经结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320722V#1025F不，雪拉姐他们\n',
            '还在房间里休息……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320723V我稍微想来\n',
            '看看湖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320724V#1060F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320725V是吗，嗯……\n',
            '天黑之前要回来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0386, 1, 0x1C31))

    Jump('loc_2FF3')

    def _loc_2F8C(): pass

    label('loc_2F8C')

    ChrTalk(
        0x000E,
        (
            '#0180320726V#1062F如果想欣赏美景的话\n',
            '现在的确是最好的时机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320727V不过，天黑之前要回来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FF3(): pass

    label('loc_2FF3')

    ChrSetSubChip(0x000E, 0)
    TalkEnd(0x000E)

    Return()

# id: 0x0011 offset: 0x2FFC
@scena.Code('func_11_2FFC')
def func_11_2FFC():
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
        'loc_3013',
    )

    Call(0, 0x0038)
    Call(0, 0x0039)

    def _loc_3013(): pass

    label('loc_3013')

    Call(0, 0x0016)
    ChrSetFlags(0x00FA, 0x0004)
    ChrSetFlags(0x00FB, 0x0004)
    ChrSetFlags(0x00FC, 0x0004)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetPos(0x0101, 18570, 0, 3140, 0)
    ChrSetPos(0x00F7, 17490, -250, 2650, 0)
    ChrSetPos(0x00F8, 18440, -250, 2200, 0)
    ChrSetPos(0x00F9, 19610, -250, 2530, 0)
    ChrSetPos(0x00FA, 15510, 200, 9020, 90)
    ChrSetPos(0x00FB, 18100, 200, 10270, 270)
    ChrSetPos(0x00FC, 15510, 200, 10470, 90)
    ChrSetPos(0x000E, 18100, 200, 8820, 270)
    ChrClearFlags(0x000E, 0x0080)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xFA)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_30D9'),
        (0x00000005, 'loc_30E1'),
        (0x00000003, 'loc_30E9'),
        (0x00000004, 'loc_30F1'),
        (0x00000006, 'loc_30F9'),
        (0x00000007, 'loc_3101'),
        (-1, 'loc_3109'),
    )

    def _loc_30D9(): pass

    label('loc_30D9')

    ChrSetChipByIndex(0x00FA, 0)

    Jump('loc_3109')

    def _loc_30E1(): pass

    label('loc_30E1')

    ChrSetChipByIndex(0x00FA, 1)

    Jump('loc_3109')

    def _loc_30E9(): pass

    label('loc_30E9')

    ChrSetChipByIndex(0x00FA, 2)

    Jump('loc_3109')

    def _loc_30F1(): pass

    label('loc_30F1')

    ChrSetChipByIndex(0x00FA, 3)

    Jump('loc_3109')

    def _loc_30F9(): pass

    label('loc_30F9')

    ChrSetChipByIndex(0x00FA, 4)

    Jump('loc_3109')

    def _loc_3101(): pass

    label('loc_3101')

    ChrSetChipByIndex(0x00FA, 5)

    Jump('loc_3109')

    def _loc_3109(): pass

    label('loc_3109')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xFB)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_312A'),
        (0x00000005, 'loc_3132'),
        (0x00000003, 'loc_313A'),
        (0x00000004, 'loc_3142'),
        (0x00000006, 'loc_314A'),
        (0x00000007, 'loc_3152'),
        (-1, 'loc_315A'),
    )

    def _loc_312A(): pass

    label('loc_312A')

    ChrSetChipByIndex(0x00FB, 0)

    Jump('loc_315A')

    def _loc_3132(): pass

    label('loc_3132')

    ChrSetChipByIndex(0x00FB, 1)

    Jump('loc_315A')

    def _loc_313A(): pass

    label('loc_313A')

    ChrSetChipByIndex(0x00FB, 2)

    Jump('loc_315A')

    def _loc_3142(): pass

    label('loc_3142')

    ChrSetChipByIndex(0x00FB, 3)

    Jump('loc_315A')

    def _loc_314A(): pass

    label('loc_314A')

    ChrSetChipByIndex(0x00FB, 4)

    Jump('loc_315A')

    def _loc_3152(): pass

    label('loc_3152')

    ChrSetChipByIndex(0x00FB, 5)

    Jump('loc_315A')

    def _loc_315A(): pass

    label('loc_315A')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xFC)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_317B'),
        (0x00000005, 'loc_3183'),
        (0x00000003, 'loc_318B'),
        (0x00000004, 'loc_3193'),
        (0x00000006, 'loc_319B'),
        (0x00000007, 'loc_31A3'),
        (-1, 'loc_31AB'),
    )

    def _loc_317B(): pass

    label('loc_317B')

    ChrSetChipByIndex(0x00FC, 0)

    Jump('loc_31AB')

    def _loc_3183(): pass

    label('loc_3183')

    ChrSetChipByIndex(0x00FC, 1)

    Jump('loc_31AB')

    def _loc_318B(): pass

    label('loc_318B')

    ChrSetChipByIndex(0x00FC, 2)

    Jump('loc_31AB')

    def _loc_3193(): pass

    label('loc_3193')

    ChrSetChipByIndex(0x00FC, 3)

    Jump('loc_31AB')

    def _loc_319B(): pass

    label('loc_319B')

    ChrSetChipByIndex(0x00FC, 4)

    Jump('loc_31AB')

    def _loc_31A3(): pass

    label('loc_31A3')

    ChrSetChipByIndex(0x00FC, 5)

    Jump('loc_31AB')

    def _loc_31AB(): pass

    label('loc_31AB')

    CameraMove(18890, 0, 7310, 0)
    OP_67(0, 6370, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(297, 0)
    ChrSetStatus(ChrTable['凯文神父'], 0x00, 65)
    ChrSetStatus(ChrTable['凯文神父'], 0xFE, 0)
    OP_37(0x08, 0x80, 0x02)
    OP_37(0x08, 0x81, 0x02)
    OP_37(0x08, 0x82, 0x02)
    EquipCmd(ChrTable['凯文神父'], ItemTable['石弩'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['真空防护服'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['高级皮靴'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['行动力３'], 0x00)
    EquipCmd(ChrTable['凯文神父'], ItemTable['ＥＰ３'], 0x01)
    EquipCmd(ChrTable['凯文神父'], ItemTable['ＨＰ３'], 0x02)
    EquipCmd(ChrTable['凯文神父'], ItemTable['精神２'], 0x03)
    EquipCmd(ChrTable['凯文神父'], ItemTable['防御２'], 0x04)
    AddCraft(ChrTable['凯文神父'], 0x0000)
    FadeIn(1000, 0)
    OP_0D()
    ChrSetSubChip(0x000E, 1)
    ChrSetSubChip(0x00FA, 2)
    Sleep(100)

    ChrSetSubChip(0x00FB, 1)
    ChrSetSubChip(0x00FC, 2)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0180320401V#1062F#5P噢，好像\n',
            '来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320402V#1004F#2P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_32A9')
    def lambda_32A9():
        CameraMove(18360, 0, 9200, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_32A9)

    @scena.Lambda('lambda_32C1')
    def lambda_32C1():
        OP_67(0, 5410, -10000, 4000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_32C1)

    @scena.Lambda('lambda_32D9')
    def lambda_32D9():
        CameraSetDistance(2600, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_32D9)

    CreateThread(0x0101, 0x01, 0x00, func_12_3F3E)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_13_3F82)
    Sleep(300)

    CreateThread(0x00F8, 0x01, 0x00, func_14_3FC6)
    Sleep(300)

    CreateThread(0x00F9, 0x01, 0x00, func_15_400A)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010320403V#1008F为，为什么凯文先生\n',
            '会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320404V#1061F哎呀～要问我为什么会在这里，\n',
            '这话说起来可就长了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_340B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320405V#027F到这里来的途中，\n',
            '正好在街道碰上的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320406V接着呢\n',
            '就跟着来到旅馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355A')

    def _loc_340B(): pass

    label('loc_340B')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_347C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080320407V#070F到这里来的途中，\n',
            '正好在街道碰上的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320408V接着呢\n',
            '就跟着来到旅馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355A')

    def _loc_347C(): pass

    label('loc_347C')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_34EB',
    )

    ChrTalk(
        0x0107,
        (
            '#0070320409V#061F来这里的时候，\n',
            '在街道的路上碰到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070320410V接着就一起\n',
            '到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355A')

    def _loc_34EB(): pass

    label('loc_34EB')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_355A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320411V#035F来这里的路上，\n',
            '在街道碰上的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320412V#030F交流后\n',
            '就跟着来到旅馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_355A(): pass

    label('loc_355A')

    ChrTalk(
        0x0101,
        (
            '#0010320413V#1015F街道的路上……\n',
            '为什么会在那里遇到？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320414V#1060F坦白说吧，\n',
            '我是来调查『琥珀之塔』的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320415V其实，自从在洛连特\n',
            '和艾丝蒂尔分别后\n',
            '正在调查所有的『四轮之塔』。',
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
            '#0010320416V#1004F四轮之塔……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36AF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050320417V#052F也就是说……\n',
            '其它的三个塔也调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_378D')

    def _loc_36AF(): pass

    label('loc_36AF')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36FA',
    )

    ChrTalk(
        0x0105,
        (
            '#0060320418V#044F也就是说……\n',
            '其它的三个塔也调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_378D')

    def _loc_36FA(): pass

    label('loc_36FA')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3745',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320419V#032F唔，这么说来\n',
            '其它的三个塔也调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_378D')

    def _loc_3745(): pass

    label('loc_3745')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_378D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320420V#023F就是说……\n',
            '其它的三个塔也要调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_378D(): pass

    label('loc_378D')

    ChrTalk(
        0x000E,
        (
            '#0180320421V#1068F嗯，是这样呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320422V由于这里龙的骚乱，\n',
            '我调查完全没有进展。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320423V#1066F所以想来这里交换下情报，\n',
            '所以才跟着来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320424V#1011F这倒没关系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320425V#1006F那么，这就开始\n',
            '在这里交换情报吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320426V#1060F啊啊，可能的话\n',
            '晚饭后比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320427V那样的话大家都能\n',
            '放心地谈话了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320428V#1001F啊，也是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320429V#1004F……啊，凯文先生也\n',
            '打算住在这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320430V#1061F哈哈，我听说这\n',
            '旅馆十分有名呀？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320431V#1062F既然如此，正好我也\n',
            '想陪伴艾丝蒂尔\n',
            '一起休假呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320432V#1016F太，太突然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320433V#1006F不过，受到过凯文先生\n',
            '好多次的关照了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320434V各位，你们的意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050320435V#051F啊，蛮不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030320436V#021F唔，的确是个\n',
            '回报的好机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070320437V#061F嘿嘿，我也赞成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040320438V#035F呵，我也没有异议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060320439V#048F呵呵……\n',
            '这也是种缘分吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080320440V#071F嗯，难得有机会\n',
            '就尽情放松吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180261097V#1061F谢谢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320442V#1062F真的感谢你们。\n',
            '如果有什么需要',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320443V就尽管吩咐吧。',
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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【已经没有事了】\n'),
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
    SetScenaFlags(ScenaFlag(0x0380, 2, 0x1C02))

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E5A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010320444V#1025F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320445V好不容易的一次机会，那我们就\n',
            '先去把行李放好，然后好好地休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320446V#1064F什么，那好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320447V#1068F真可惜～难得\n',
            '我想用身体为你们效劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320448V#1019F真是的。\n',
            '有点太过得意了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070320449V#067F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0097, 0x01, 0x0010)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D78',
    )

    ChrTalk(
        0x0106,
        (
            '#0050320450V#051F好吧，那就\n',
            '带我们去房间吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E3C')

    def _loc_3D78(): pass

    label('loc_3D78')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DBB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320451V#021F呵呵，接下来\n',
            '带我们去房间吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E3C')

    def _loc_3DBB(): pass

    label('loc_3DBB')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DFE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080320452V#071F那好，接下来\n',
            '带我们去房间吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E3C')

    def _loc_3DFE(): pass

    label('loc_3DFE')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E3C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320453V#031F呵，接下来\n',
            '带我们去房间吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E3C(): pass

    label('loc_3E3C')

    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0017)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1510._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_3F3D')

    def _loc_3E5A(): pass

    label('loc_3E5A')

    ChrTalk(
        0x0101,
        (
            '#0010320454V#1016F啊哈哈，那就\n',
            '不客气的麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0097, 0x01, 0x0004)
    OP_28(0x0097, 0x01, 0x0008)
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x001F)
    CameraMove(17250, 0, 5960, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 17250, 0, 5960, 180)
    ChrSetPos(0x0001, 17250, 0, 5960, 180)
    ChrSetPos(0x0002, 17250, 0, 5960, 180)
    ChrSetPos(0x0003, 17250, 0, 5960, 180)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    def _loc_3F3D(): pass

    label('loc_3F3D')

    Return()

# id: 0x0012 offset: 0x3F3E
@scena.Code('func_12_3F3E')
def func_12_3F3E():
    ChrWalkTo(0x00FE, 17030, 0, 3640, 2000, 0x00)
    ChrWalkTo(0x00FE, 17240, 0, 5040, 2000, 0x00)
    ChrWalkTo(0x00FE, 17970, 0, 7400, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0013 offset: 0x3F82
@scena.Code('func_13_3F82')
def func_13_3F82():
    ChrWalkTo(0x00FE, 17030, 0, 3640, 2000, 0x00)
    ChrWalkTo(0x00FE, 17240, 0, 5040, 2000, 0x00)
    ChrWalkTo(0x00FE, 18750, 0, 6460, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0014 offset: 0x3FC6
@scena.Code('func_14_3FC6')
def func_14_3FC6():
    ChrWalkTo(0x00FE, 17030, 0, 3640, 2000, 0x00)
    ChrWalkTo(0x00FE, 17240, 0, 5040, 2000, 0x00)
    ChrWalkTo(0x00FE, 17360, 0, 6110, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0015 offset: 0x400A
@scena.Code('func_15_400A')
def func_15_400A():
    ChrWalkTo(0x00FE, 17030, 0, 3640, 2000, 0x00)
    ChrWalkTo(0x00FE, 17240, 0, 5040, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0016 offset: 0x403A
@scena.Code('func_16_403A')
def func_16_403A():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4073',
    )

    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_4073(): pass

    label('loc_4073')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_40AC',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4094',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFA, 0xFF)

    Jump('loc_4098')

    def _loc_4094(): pass

    label('loc_4094')

    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)

    def _loc_4098(): pass

    label('loc_4098')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_40AC(): pass

    label('loc_40AC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_40F9',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40CD',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    Jump('loc_40E5')

    def _loc_40CD(): pass

    label('loc_40CD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40E1',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFB, 0xFF)

    Jump('loc_40E5')

    def _loc_40E1(): pass

    label('loc_40E1')

    FormationAddMember(ChrTable['奥利维尔'], 0xFC, 0xFF)

    def _loc_40E5(): pass

    label('loc_40E5')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_40F9(): pass

    label('loc_40F9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4146',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_411A',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFA, 0xFF)

    Jump('loc_4132')

    def _loc_411A(): pass

    label('loc_411A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_412E',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFB, 0xFF)

    Jump('loc_4132')

    def _loc_412E(): pass

    label('loc_412E')

    FormationAddMember(ChrTable['阿加特'], 0xFC, 0xFF)

    def _loc_4132(): pass

    label('loc_4132')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_4146(): pass

    label('loc_4146')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4193',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4167',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xFA, 0xFF)

    Jump('loc_417F')

    def _loc_4167(): pass

    label('loc_4167')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_417B',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xFB, 0xFF)

    Jump('loc_417F')

    def _loc_417B(): pass

    label('loc_417B')

    FormationAddMember(ChrTable['雪拉扎德'], 0xFC, 0xFF)

    def _loc_417F(): pass

    label('loc_417F')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_4193(): pass

    label('loc_4193')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_41B8',
    )

    FormationAddMember(ChrTable['提妲'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_41B8(): pass

    label('loc_41B8')

    Return()

# id: 0x0017 offset: 0x41B9
@scena.Code('func_17_41B9')
def func_17_41B9():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_41C9',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_41C9(): pass

    label('loc_41C9')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_41D9',
    )

    FormationDelMember(0x04, 0xFF)

    def _loc_41D9(): pass

    label('loc_41D9')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_41E9',
    )

    FormationDelMember(0x06, 0xFF)

    def _loc_41E9(): pass

    label('loc_41E9')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_41F9',
    )

    FormationDelMember(0x03, 0xFF)

    def _loc_41F9(): pass

    label('loc_41F9')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_4209',
    )

    FormationDelMember(0x05, 0xFF)

    def _loc_4209(): pass

    label('loc_4209')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_4219',
    )

    FormationDelMember(0x02, 0xFF)

    def _loc_4219(): pass

    label('loc_4219')

    Return()

# id: 0x0018 offset: 0x421A
@scena.Code('func_18_421A')
def func_18_421A():
    ChrTalk(
        0x0009,
        (
            '#0050320455V#051F哟，来晚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320456V准备完毕了吗？',
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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【已经没有事了】\n'),
            TXT(0x02, '【选择同行者】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_42D1'),
        (0x00000001, 'loc_4329'),
        (0x00000002, 'loc_4392'),
        (-1, 'loc_43DD'),
    )

    def _loc_42D1(): pass

    label('loc_42D1')

    ChrTalk(
        0x0009,
        (
            '#0050320457V#052F什么，是这样吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320458V#053F算了，办完事\n',
            '就快点回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43DD')

    def _loc_4329(): pass

    label('loc_4329')

    ChrTalk(
        0x0009,
        (
            '#0050320459V#053F喔，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320460V#051F那好，接下来\n',
            '带我们去房间吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1510._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_43DD')

    def _loc_4392(): pass

    label('loc_4392')

    ChrTalk(
        0x0009,
        (
            '#0050320461V#052F什么呀？\n',
            '要更换同行者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x001F)
    FadeIn(300, 0)

    Jump('loc_43DD')

    def _loc_43DD(): pass

    label('loc_43DD')

    Return()

# id: 0x0019 offset: 0x43DE
@scena.Code('func_19_43DE')
def func_19_43DE():
    ChrTalk(
        0x000C,
        (
            '#0070320462V#560F啊，姐姐！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070320463V事已经办完了吗？',
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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【已经没有事了】\n'),
            TXT(0x02, '【选择同行者】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4495'),
        (0x00000001, 'loc_44F1'),
        (0x00000002, 'loc_456C'),
        (-1, 'loc_45B5'),
    )

    def _loc_4495(): pass

    label('loc_4495')

    ChrTalk(
        0x000C,
        (
            '#0070320464V#064F哎呀……是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070320465V#061F我等着，事情办完了\n',
            '就回来这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45B5')

    def _loc_44F1(): pass

    label('loc_44F1')

    ChrTalk(
        0x000C,
        (
            '#0070320466V#560F啊，是这样呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070320467V#061F嘿嘿，那么就拜托\n',
            '旅馆的人领我们去房间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1510._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_45B5')

    def _loc_456C(): pass

    label('loc_456C')

    ChrTalk(
        0x000C,
        (
            '#0070320468V#560F姐姐。\n',
            '要替换同行者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x001F)
    FadeIn(300, 0)

    Jump('loc_45B5')

    def _loc_45B5(): pass

    label('loc_45B5')

    Return()

# id: 0x001A offset: 0x45B6
@scena.Code('func_1A_45B6')
def func_1A_45B6():
    ChrTalk(
        0x0008,
        (
            '#0030320469V#020F哎呀，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320470V事情办完了吗？',
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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【已经没有事了】\n'),
            TXT(0x02, '【选择同行者】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4671'),
        (0x00000001, 'loc_46D7'),
        (0x00000002, 'loc_4740'),
        (-1, 'loc_478B'),
    )

    def _loc_4671(): pass

    label('loc_4671')

    ChrTalk(
        0x0008,
        (
            '#0030320471V#023F啊，是这样吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320472V#020F我们就在这里等着，\n',
            '事情办妥后就回来这里哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_478B')

    def _loc_46D7(): pass

    label('loc_46D7')

    ChrTalk(
        0x0008,
        (
            '#0030320473V#021F呵呵，是吗～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320474V#020F那尽快\n',
            '带我们去房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1510._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_478B')

    def _loc_4740(): pass

    label('loc_4740')

    ChrTalk(
        0x0008,
        (
            '#0030320475V#023F哎呀……\n',
            '要替换同行者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x001F)
    FadeIn(300, 0)

    Jump('loc_478B')

    def _loc_478B(): pass

    label('loc_478B')

    Return()

# id: 0x001B offset: 0x478C
@scena.Code('func_1B_478C')
def func_1B_478C():
    ChrTalk(
        0x000A,
        (
            '#0040320476V#030F哎呀，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320477V已经准备完毕了吗？',
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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【已经没有事了】\n'),
            TXT(0x02, '【选择同行者】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_484B'),
        (0x00000001, 'loc_48AD'),
        (0x00000002, 'loc_4914'),
        (-1, 'loc_4969'),
    )

    def _loc_484B(): pass

    label('loc_484B')

    ChrTalk(
        0x000A,
        (
            '#0040320478V#033F哎呀，是这样呀？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320479V#035F呵，我在这里等着\n',
            '事情办完后就回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4969')

    def _loc_48AD(): pass

    label('loc_48AD')

    ChrTalk(
        0x000A,
        (
            '#0040320480V#035F呵，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320481V#030F那么尽快带我们\n',
            '去房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1510._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_4969')

    def _loc_4914(): pass

    label('loc_4914')

    ChrTalk(
        0x000A,
        (
            '#0040320482V#035F呵，看来正需要\n',
            '我这个天才的实力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x001F)
    FadeIn(300, 0)

    Jump('loc_4969')

    def _loc_4969(): pass

    label('loc_4969')

    Return()

# id: 0x001C offset: 0x496A
@scena.Code('func_1C_496A')
def func_1C_496A():
    ChrTalk(
        0x000B,
        (
            '#0060320483V#040F啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320484V已经准备完毕了吗？',
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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【已经没有事了】\n'),
            TXT(0x02, '【选择同行者】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4A27'),
        (0x00000001, 'loc_4A81'),
        (0x00000002, 'loc_4AEC'),
        (-1, 'loc_4B37'),
    )

    def _loc_4A27(): pass

    label('loc_4A27')

    ChrTalk(
        0x000B,
        (
            '#0060320485V#044F啊，是这样呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320486V#041F我在这里等着\n',
            '事办完后就过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B37')

    def _loc_4A81(): pass

    label('loc_4A81')

    ChrTalk(
        0x000B,
        (
            '#0060320487V#041F呵呵，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320488V#048F那么快点带大家\n',
            '去房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1510._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_4B37')

    def _loc_4AEC(): pass

    label('loc_4AEC')

    ChrTalk(
        0x000B,
        (
            '#0060320489V#040F明白了。\n',
            '要替换同行者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x001F)
    FadeIn(300, 0)

    Jump('loc_4B37')

    def _loc_4B37(): pass

    label('loc_4B37')

    Return()

# id: 0x001D offset: 0x4B38
@scena.Code('func_1D_4B38')
def func_1D_4B38():
    ChrTalk(
        0x000D,
        (
            '#0080320490V#070F哟，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320491V已经准备好了吗？',
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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【已经没有事了】\n'),
            TXT(0x02, '【选择同行者】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4BF1'),
        (0x00000001, 'loc_4C49'),
        (0x00000002, 'loc_4CB2'),
        (-1, 'loc_4CFB'),
    )

    def _loc_4BF1(): pass

    label('loc_4BF1')

    ChrTalk(
        0x000D,
        (
            '#0080320492V#073F噢，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320493V#070F我在这里等着\n',
            '事情办完后就回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CFB')

    def _loc_4C49(): pass

    label('loc_4C49')

    ChrTalk(
        0x000D,
        (
            '#0080320494V#073F噢噢，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320495V#071F那么尽快带我们\n',
            '去房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1510._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_4CFB')

    def _loc_4CB2(): pass

    label('loc_4CB2')

    ChrTalk(
        0x000D,
        (
            '#0080320496V#073F噢……\n',
            '要替换同行者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x001F)
    FadeIn(300, 0)

    Jump('loc_4CFB')

    def _loc_4CFB(): pass

    label('loc_4CFB')

    Return()

# id: 0x001E offset: 0x4CFC
@scena.Code('func_1E_4CFC')
def func_1E_4CFC():
    ChrTalk(
        0x000E,
        (
            '#0180320497V#1062F噢，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320498V还有什么事的话\n',
            '我也来帮忙吧？',
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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【已经没有事了】\n'),
            TXT(0x02, '【选择同行者】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4DC5'),
        (0x00000001, 'loc_4E23'),
        (0x00000002, 'loc_4E8A'),
        (-1, 'loc_4ED6'),
    )

    def _loc_4DC5(): pass

    label('loc_4DC5')

    ChrTalk(
        0x000E,
        (
            '#0180320499V#1064F怎么，不用吩咐？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320500V#1060F那么，我在这里等着\n',
            '完了回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4ED6')

    def _loc_4E23(): pass

    label('loc_4E23')

    ChrTalk(
        0x000E,
        (
            '#0180320501V#1064F噢，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320502V#1061F那么就\n',
            '带我们去房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1510._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_4ED6')

    def _loc_4E8A(): pass

    label('loc_4E8A')

    ChrTalk(
        0x000E,
        (
            '#0180320503V#1061F来了啊。\n',
            '要替换同行者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x001F)
    FadeIn(300, 0)

    Jump('loc_4ED6')

    def _loc_4ED6(): pass

    label('loc_4ED6')

    Return()

# id: 0x001F offset: 0x4ED7
@scena.Code('func_1F_4ED7')
def func_1F_4ED7():
    MapClearFlags(0x00000001)
    CameraMove(64510, 0, -14780, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            0x00FF,
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            ChrTable['凯文神父'],
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
    MapSetFlags(0x00000001)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F95',
    )

    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0008, 0x0080)

    def _loc_4F95(): pass

    label('loc_4F95')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FFD',
    )

    ChrSetFlags(0x0009, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FD3',
    )

    ChrSetPos(0x0009, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4FEE')

    def _loc_4FD3(): pass

    label('loc_4FD3')

    ChrSetPos(0x0009, 18100, 200, 10270, 270)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4FEE(): pass

    label('loc_4FEE')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0009, 0x0080)

    def _loc_4FFD(): pass

    label('loc_4FFD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5090',
    )

    ChrSetFlags(0x000A, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_503B',
    )

    ChrSetPos(0x000A, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5081')

    def _loc_503B(): pass

    label('loc_503B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5066',
    )

    ChrSetPos(0x000A, 18100, 200, 10270, 270)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5081')

    def _loc_5066(): pass

    label('loc_5066')

    ChrSetPos(0x000A, 15510, 200, 10470, 90)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5081(): pass

    label('loc_5081')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000A, 0x0080)

    def _loc_5090(): pass

    label('loc_5090')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_514E',
    )

    ChrSetFlags(0x000B, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_50CE',
    )

    ChrSetPos(0x000B, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_513F')

    def _loc_50CE(): pass

    label('loc_50CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_50F9',
    )

    ChrSetPos(0x000B, 18100, 200, 10270, 270)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_513F')

    def _loc_50F9(): pass

    label('loc_50F9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5124',
    )

    ChrSetPos(0x000B, 15510, 200, 10470, 90)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_513F')

    def _loc_5124(): pass

    label('loc_5124')

    ChrSetPos(0x000B, 15510, 200, 9020, 90)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_513F(): pass

    label('loc_513F')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000B, 0x0080)

    def _loc_514E(): pass

    label('loc_514E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_520C',
    )

    ChrSetFlags(0x000C, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_518C',
    )

    ChrSetPos(0x000C, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_51FD')

    def _loc_518C(): pass

    label('loc_518C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51B7',
    )

    ChrSetPos(0x000C, 18100, 200, 10270, 270)

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_51FD')

    def _loc_51B7(): pass

    label('loc_51B7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51E2',
    )

    ChrSetPos(0x000C, 15510, 200, 10470, 90)

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_51FD')

    def _loc_51E2(): pass

    label('loc_51E2')

    ChrSetPos(0x000C, 15510, 200, 9020, 90)

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_51FD(): pass

    label('loc_51FD')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000C, 0x0080)

    def _loc_520C(): pass

    label('loc_520C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52CA',
    )

    ChrSetFlags(0x000D, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_524A',
    )

    ChrSetPos(0x000D, 18100, 200, 8820, 270)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_52BB')

    def _loc_524A(): pass

    label('loc_524A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5275',
    )

    ChrSetPos(0x000D, 18100, 200, 10270, 270)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_52BB')

    def _loc_5275(): pass

    label('loc_5275')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52A0',
    )

    ChrSetPos(0x000D, 15510, 200, 10470, 90)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_52BB')

    def _loc_52A0(): pass

    label('loc_52A0')

    ChrSetPos(0x000D, 15510, 200, 9020, 90)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_52BB(): pass

    label('loc_52BB')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000D, 0x0080)

    def _loc_52CA(): pass

    label('loc_52CA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_537E',
    )

    ChrSetFlags(0x000E, 0x0004)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5308',
    )

    ChrSetPos(0x000E, 18100, 200, 8820, 0)

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5379')

    def _loc_5308(): pass

    label('loc_5308')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5333',
    )

    ChrSetPos(0x000E, 18100, 200, 10270, 0)

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5379')

    def _loc_5333(): pass

    label('loc_5333')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_535E',
    )

    ChrSetPos(0x000E, 15510, 200, 10470, 90)

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5379')

    def _loc_535E(): pass

    label('loc_535E')

    ChrSetPos(0x000E, 15510, 200, 9020, 90)

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5379(): pass

    label('loc_5379')

    ChrClearFlags(0x000E, 0x0080)

    def _loc_537E(): pass

    label('loc_537E')

    Return()

# id: 0x0020 offset: 0x537F
@scena.Code('func_20_537F')
def func_20_537F():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_4A(0x000F, 255)
    ChrSetPos(0x000F, 79400, 0, 14470, 180)
    ChrSetPos(0x0101, 79500, 0, 13020, 0)
    ChrSetPos(0x0008, 78510, 0, 11820, 0)
    ChrSetPos(0x000C, 80360, 0, 12750, 0)
    ChrSetPos(0x000B, 78510, 0, 12930, 0)
    ChrSetPos(0x0009, 80460, 0, 11810, 0)
    ChrSetPos(0x000A, 78550, 0, 10170, 0)
    ChrSetPos(0x000D, 79750, 0, 10470, 0)
    ChrSetPos(0x000E, 79540, 0, 11620, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetChipByIndex(0x0008, 8)
    ChrSetChipByIndex(0x0009, 9)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x000B, 11)
    ChrSetChipByIndex(0x000C, 12)
    ChrSetChipByIndex(0x000D, 13)
    ChrSetChipByIndex(0x000E, 14)
    CameraMove(80060, 0, 13840, 0)
    OP_67(0, 6520, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(45000, 0)
    OP_6E(281, 0)
    RemoveItem(ItemTable['住宿票券'], 1)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#1240320504V#5P非常感谢\n',
            '大家光临我们旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1240320505V#5P那就先让我\n',
            '带领各位去房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320506V#1006F嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 90, 400)

    @scena.Lambda('lambda_555C')
    def lambda_555C():
        CameraMove(80870, 0, 13830, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_555C)

    CreateThread(0x000F, 0x01, 0x00, func_21_6075)
    WaitForThreadExit(0x000F, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#1240320507V#5P首先，这里是\n',
            '各位女士的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    ChrSetPos(0x000F, 106650, 0, 11300, 180)
    ChrSetPos(0x0101, 108000, 0, 9310, 180)
    ChrSetPos(0x000C, 109430, 0, 10980, 90)
    ChrSetPos(0x000B, 109080, 0, 9920, 120)
    ChrSetPos(0x0008, 107110, 0, 10320, 180)
    ChrSetPos(0x000D, 105160, 0, 14050, 180)
    ChrSetPos(0x0009, 104860, 0, 12720, 180)
    ChrSetPos(0x000A, 105190, 0, 11860, 180)
    ChrSetPos(0x000E, 105900, 0, 13330, 180)
    CameraMove(107830, 0, 7310, 0)
    OP_67(0, 6040, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(45000, 0)
    OP_6E(288, 0)

    @scena.Lambda('lambda_56A2')
    def lambda_56A2():
        CameraMove(108140, 0, 12550, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_56A2)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#0070320508V#061F#5P哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320509V#048F#5P很安稳的气氛，\n',
            '好棒的房间呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320510V#1006F#5P这里，是我们以前\n',
            '来过的房间呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320511V不过，刚到就被派去了空贼基地，\n',
            '结果没有能住上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1240320512V#5P呵呵，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320513V#035F#5P呵，我倒是\n',
            '在这床上休息过一会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010320514V#1019F#2P那只是被雪拉姐\n',
            '灌醉了而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320515V#021F#5P呵呵，我想这次\n',
            '能好好享受了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    ChrSetPos(0x000F, 50100, 0, 25100, 90)
    ChrSetPos(0x0101, 55160, 0, 26790, 270)
    ChrSetPos(0x000C, 55040, 0, 25810, 270)
    ChrSetPos(0x000B, 55200, 0, 25150, 270)
    ChrSetPos(0x0008, 56030, 0, 25930, 270)
    ChrSetPos(0x000D, 54140, 0, 24330, 270)
    ChrSetPos(0x0009, 52100, 0, 25200, 270)
    ChrSetPos(0x000A, 53740, 0, 25950, 270)
    ChrSetPos(0x000E, 52050, 0, 24210, 315)
    CameraMove(50870, 0, 24810, 0)
    OP_67(0, 5890, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(78000, 0)
    OP_6E(286, 0)
    OP_72(0x0014, 0x0020)
    OP_72(0x0014, 0x0010)
    OP_6F(0x0014, 59)

    @scena.Lambda('lambda_5965')
    def lambda_5965():
        CameraMove(54890, 0, 25840, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5965)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000F,
        (
            '#1240320516V#6P这里是各位男士\n',
            '的客房……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1240320517V因为是双人间，请和旁边\n',
            '的房间一起使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 45, 400)

    ChrTalk(
        0x000E,
        (
            '#0180320518V#1062F啊，我是中途加入的，\n',
            '大家先优先选择吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 315, 400)

    ChrTalk(
        0x000D,
        (
            '#0080320519V#073F#2P嗯，怎么办？\n',
            '我哪里都可以哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 90, 400)

    ChrTalk(
        0x0009,
        (
            '#0050320520V#051F#6P我也随便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320521V#035F#5P呵……\n',
            '那么我和阿加特\n',
            '住一起好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0050320522V#555F#6P……稍等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320523V为什么这么突然就\n',
            '选择我呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320524V#031F#5P哈哈哈。\n',
            '就这样决定吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320525V#037F那天晚上，\n',
            '只有你和提妲两个留在了村里，\n',
            '期间发生过什么事嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320526V我要你从头到尾、仔仔细细、一字不漏、\n',
            '老老实实地全讲给我听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320527V#064F#5P啊啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320528V#055F#6P……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320529V#1007F#5P好变态的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010320530V#1028F#5P嗯～说起来\n',
            '我也有些兴趣想知道呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000C, 315, 400)

    ChrTalk(
        0x000C,
        (
            '#0070320531V#065F#2P不，不过……\n',
            '就是在一起说了说话啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0030320532V#021F#5P究竟说了些什么\n',
            '这才至关重要的呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320533V#027F我们也要在睡觉前\n',
            '好好地问问清楚哟～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070301486V#562F#5P啊，唔～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 315, 400)

    ChrTalk(
        0x000B,
        (
            '#0060320535V#045F你们２位真是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320536V#542F不要太乱来了，\n',
            '你们看看，提妲被你们说得都要哭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 225, 400)

    @scena.Lambda('lambda_5E37')
    def lambda_5E37():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_5E37)

    @scena.Lambda('lambda_5E45')
    def lambda_5E45():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5E45)

    @scena.Lambda('lambda_5E53')
    def lambda_5E53():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_5E53)

    @scena.Lambda('lambda_5E61')
    def lambda_5E61():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_5E61)

    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0040320537V#031F#5P呵，那么\n',
            '金和凯文神父就\n',
            '住在旁边的房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320538V#071F#2P啊啊，我没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320539V#1061F#4P呀，这下可有的好玩了，\n',
            '我举双手赞成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1240320540V#6P呵呵，我就带你们\n',
            '去隔壁的房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    CreateThread(0x0008, 0x01, 0x00, func_2A_6192)
    Sleep(200)

    CreateThread(0x000C, 0x01, 0x00, func_2B_61C3)
    Sleep(400)

    CreateThread(0x000B, 0x01, 0x00, func_2C_61F4)
    Sleep(700)

    CreateThread(0x0101, 0x01, 0x00, func_2D_6233)
    Sleep(600)

    CreateThread(0x000A, 0x01, 0x00, func_2E_6278)
    Sleep(700)

    CreateThread(0x000D, 0x01, 0x00, func_2F_62BD)
    Sleep(400)

    CreateThread(0x000E, 0x01, 0x00, func_30_6302)
    Sleep(50)

    CreateThread(0x000F, 0x01, 0x00, func_31_6347)

    @scena.Lambda('lambda_5FB8')
    def lambda_5FB8():
        CameraMove(55620, 0, 25780, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5FB8)

    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    WaitForThreadExit(0x0101, 0x0002)
    OP_63(0x0009)
    Sleep(200)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1200)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0009,
        (
            '#0050320541V#055F#6P喂，喂！\n',
            '在关键时刻怎么全都跑了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1501._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0021 offset: 0x6075
@scena.Code('func_21_6075')
def func_21_6075():
    ChrMoveTo(0x00FE, 80470, 0, 14960, 2000, 0x00)
    Sleep(500)

    OP_72(0x0015, 0x0020)
    OP_72(0x0015, 0x0010)
    PlaySE(6, 0x00, 0x64)
    OP_6F(0x0015, 0)
    OP_70(0x0015, 7)
    OP_73(0x0015)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0022 offset: 0x60BB
@scena.Code('func_22_60BB')
def func_22_60BB():
    ChrWalkTo(0x00FE, 80160, 0, 12690, 2000, 0x00)

    Return()

# id: 0x0023 offset: 0x60D0
@scena.Code('func_23_60D0')
def func_23_60D0():
    ChrWalkTo(0x00FE, 79080, 0, 12690, 2000, 0x00)

    Return()

# id: 0x0024 offset: 0x60E5
@scena.Code('func_24_60E5')
def func_24_60E5():
    ChrWalkTo(0x00FE, 79580, 0, 11960, 2000, 0x00)

    Return()

# id: 0x0025 offset: 0x60FA
@scena.Code('func_25_60FA')
def func_25_60FA():
    ChrWalkTo(0x00FE, 78690, 0, 11960, 2000, 0x00)

    Return()

# id: 0x0026 offset: 0x610F
@scena.Code('func_26_610F')
def func_26_610F():
    ChrWalkTo(0x00FE, 78500, 0, 10980, 2000, 0x00)

    Return()

# id: 0x0027 offset: 0x6124
@scena.Code('func_27_6124')
def func_27_6124():
    ChrWalkTo(0x00FE, 79230, 0, 10470, 2000, 0x00)

    Return()

# id: 0x0028 offset: 0x6139
@scena.Code('func_28_6139')
def func_28_6139():
    ChrWalkTo(0x00FE, 80340, 0, 5340, 2000, 0x00)
    ChrWalkTo(0x00FE, 80250, 0, 10520, 2000, 0x00)

    Return()

# id: 0x0029 offset: 0x6162
@scena.Code('func_29_6162')
def func_29_6162():
    ChrTurnDirection(0x00FE, 0x0008, 400)
    ChrWalkTo(0x00FE, 79940, 0, 5520, 2000, 0x00)
    ChrWalkTo(0x00FE, 79940, 0, 9770, 2000, 0x00)

    Return()

# id: 0x002A offset: 0x6192
@scena.Code('func_2A_6192')
def func_2A_6192():
    ChrSetDirection(0x00FE, 90, 400)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 57490, 0, 25950, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x002B offset: 0x61C3
@scena.Code('func_2B_61C3')
def func_2B_61C3():
    ChrTurnDirection(0x00FE, 0x0008, 400)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 57490, 0, 25950, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x002C offset: 0x61F4
@scena.Code('func_2C_61F4')
def func_2C_61F4():
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 55220, 0, 25950, 2000, 0x00)
    ChrWalkTo(0x00FE, 57490, 0, 25950, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x002D offset: 0x6233
@scena.Code('func_2D_6233')
def func_2D_6233():
    ChrSetDirection(0x00FE, 180, 400)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 55220, 0, 25950, 2000, 0x00)
    ChrWalkTo(0x00FE, 57490, 0, 25950, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x002E offset: 0x6278
@scena.Code('func_2E_6278')
def func_2E_6278():
    ChrTurnDirection(0x00FE, 0x0008, 400)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 55220, 0, 25950, 2000, 0x00)
    ChrWalkTo(0x00FE, 57490, 0, 25950, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x002F offset: 0x62BD
@scena.Code('func_2F_62BD')
def func_2F_62BD():
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 55220, 0, 25950, 2000, 0x00)
    ChrWalkTo(0x00FE, 57490, 0, 25950, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0030 offset: 0x6302
@scena.Code('func_30_6302')
def func_30_6302():
    ChrTurnDirection(0x00FE, 0x0008, 400)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 55220, 0, 25950, 2000, 0x00)
    ChrWalkTo(0x00FE, 57490, 0, 25950, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0031 offset: 0x6347
@scena.Code('func_31_6347')
def func_31_6347():
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 51220, 0, 24000, 2000, 0x00)
    ChrWalkTo(0x00FE, 55220, 0, 25950, 2000, 0x00)
    ChrWalkTo(0x00FE, 57490, 0, 25950, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0032 offset: 0x6399
@scena.Code('func_32_6399')
def func_32_6399():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetChipByIndex(0x0101, 17)
    ChrSetChipByIndex(0x0008, 18)
    ChrSetChipByIndex(0x000B, 19)
    ChrSetChipByIndex(0x000C, 20)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetSubChip(0x000B, 0)
    ChrSetSubChip(0x000C, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetFlags(0x000B, 0x0002)
    ChrSetFlags(0x000C, 0x0002)
    ChrSetPos(0x0101, 110200, 350, 8200, 0)
    ChrSetPos(0x000C, 109600, 350, 5300, 0)
    ChrSetPos(0x0008, 105900, 350, 8300, 0)
    ChrSetPos(0x000B, 105700, 350, 5300, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    CameraMove(109930, 350, 17110, 0)
    OP_67(0, 6050, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6F(0x0019, 15)
    OP_6F(0x001C, 18)
    OP_6F(0x001A, 15)
    OP_6F(0x001B, 15)
    PlaySE(450, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_64B2')
    def lambda_64B2():
        CameraMove(110740, 350, 8100, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_64B2)

    @scena.Lambda('lambda_64CA')
    def lambda_64CA():
        OP_67(0, 6440, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_64CA)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_64F1')
    def lambda_64F1():
        CameraSetDistance(2600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_64F1)

    Sleep(500)

    ChrSetSubChip(0x0101, 15)
    Sleep(100)

    ChrSetSubChip(0x0101, 16)
    Sleep(1000)

    OP_6F(0x0019, 15)
    OP_70(0x0019, 60)
    OP_99(0x0101, 0x00, 0x08, 1000)
    Sleep(1000)

    OP_23(0x01C2)

    @scena.Lambda('lambda_6539')
    def lambda_6539():
        OP_99(0x00FE, 0x08, 0x0C, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6539)

    OP_9E(0x0101, 15, 0, 2000, 4000)
    OP_99(0x0101, 0x0C, 0x0E, 1000)
    ChrSetSubChip(0x0101, 14)
    Sleep(200)

    ChrSetSubChip(0x0101, 17)
    Sleep(200)

    ChrSetSubChip(0x0101, 18)
    Sleep(500)

    ChrSetSubChip(0x0101, 21)
    Sleep(500)

    ChrSetSubChip(0x0101, 18)
    Sleep(500)

    ChrSetSubChip(0x0101, 21)
    Sleep(500)

    ChrSetSubChip(0x0101, 18)
    Sleep(1000)

    Fade(500)

    @scena.Lambda('lambda_65B0')
    def lambda_65B0():
        CameraMove(110750, 0, 7280, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_65B0)

    ChrSetPos(0x0101, 109720, 0, 6420, 180)
    ChrClearFlags(0x0101, 0x0002)
    ChrClearFlags(0x0101, 0x0004)
    ChrSetDirection(0x0101, 180, 0)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 25)
    OP_6F(0x0019, 20)
    OP_70(0x0019, 10)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    CreateThread(0x000C, 0x02, 0x00, func_35_6780)
    ChrSetDirection(0x0101, 270, 400)

    @scena.Lambda('lambda_662D')
    def lambda_662D():
        CameraMove(106910, 0, 6690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_662D)

    ChrWalkTo(0x0101, 105420, 0, 6500, 2000, 0x00)
    ChrSetDirection(0x0101, 0, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    CreateThread(0x0008, 0x02, 0x00, func_33_6725)
    ChrSetDirection(0x0101, 180, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    CreateThread(0x000B, 0x02, 0x00, func_34_6751)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    OP_DC()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '从每天的紧张中解放出来，\n',
            '好好地在床上睡上一觉\n',
            '醒来迎接爽快的清晨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0033 offset: 0x6725
@scena.Code('func_33_6725')
def func_33_6725():
    Sleep(200)

    OP_62(0x00FE, 0x00000190, 1200, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetSubChip(0x00FE, 2)
    Sleep(300)

    ChrSetSubChip(0x00FE, 3)

    Return()

# id: 0x0034 offset: 0x6751
@scena.Code('func_34_6751')
def func_34_6751():
    Sleep(200)

    OP_62(0x00FE, 0x000001F4, 1200, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_99(0x00FE, 0x00, 0x07, 1000)
    OP_99(0x00FE, 0x00, 0x07, 1000)

    Return()

# id: 0x0035 offset: 0x6780
@scena.Code('func_35_6780')
def func_35_6780():
    Sleep(200)

    OP_62(0x00FE, 0x00000320, 1300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_99(0x00FE, 0x00, 0x07, 1000)
    Sleep(500)

    OP_99(0x00FE, 0x08, 0x0A, 1000)

    Return()

# id: 0x0036 offset: 0x67B4
@scena.Code('func_36_67B4')
def func_36_67B4():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetChipByIndex(0x0101, 15)
    ChrSetPos(0x0101, 109300, 200, 13000, 270)
    ChrSetPos(0x0008, 109300, 200, 12030, 270)
    ChrSetPos(0x000B, 106990, 200, 13150, 90)
    ChrSetPos(0x000C, 106980, 200, 12170, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0015, 108200, 800, 12550, 0)
    ChrSetPos(0x0016, 108400, 800, 12980, 90)
    ChrSetPos(0x0017, 108400, 800, 11960, 90)
    ChrSetPos(0x0018, 107530, 800, 11920, 270)
    ChrSetPos(0x0019, 107550, 800, 12940, 270)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    OP_71(0x001D, 0x0004)
    CameraMove(108800, 200, 7080, 0)
    OP_67(0, 7120, -10000, 0)
    CameraSetDistance(2930, 0)
    OP_6C(53000, 0)
    OP_6E(249, 0)

    @scena.Lambda('lambda_68D8')
    def lambda_68D8():
        CameraMove(109020, 200, 13230, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_68D8)

    @scena.Lambda('lambda_68F0')
    def lambda_68F0():
        OP_67(0, 6120, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_68F0)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010320651V#1001F#5P哈，真是有意思㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320652V#061F#6P嘿嘿……\n',
            '真是开心呀⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320653V#048F呵呵，全身心都\n',
            '得到了放松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320654V#021F#2P哎呀，没有喝酒\n',
            '就这么开心，真是好久没这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0101, 1)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010320655V#1019F#5P啊，说错了吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320656V我们钓鱼的时候，\n',
            '不是喝了水果酒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0008, 2)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0030320657V#027F#2P哎呀，那样的轻度饮料\n',
            '怎么能算上酒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0008, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0030320658V#021F#2P是吧～？公主，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320659V#067F#6P啊，啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320660V#045F呵呵……\n',
            '我不做任何评价。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320661V#040F话说回来……\n',
            '艾丝蒂尔对钓鱼\n',
            '真的很拿手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010320662V#1008F#5P嘿嘿，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320663V#061F#6P嗯嗯！\n',
            '因为姐姐经常钓的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320664V#021F#2P呵呵，这孩子从小\n',
            '就对钓鱼很感兴趣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320665V#020F说起来……\n',
            '凯文神父也很拿手啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320666V#1006F#5P啊，嗯。\n',
            '好像也十分喜欢的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320667V甩竿的技巧\n',
            '真的很不错呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320668V#1001F再稍微磨练一下的话\n',
            '说不定就能成为\n',
            '我的一个好对手⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320669V#025F#2P真是的……\n',
            '稍稍夸了一下，尾巴就翘上天了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320670V#061F#6P嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320671V#041F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320672V#048F不知不觉……\n',
            '已经快要傍晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320673V#1004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6DD0')
    def lambda_6DD0():
        CameraMove(109140, 200, 15670, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6DD0)

    @scena.Lambda('lambda_6DE8')
    def lambda_6DE8():
        OP_67(0, 7540, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6DE8)

    @scena.Lambda('lambda_6E00')
    def lambda_6E00():
        OP_6C(28000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6E00)

    @scena.Lambda('lambda_6E10')
    def lambda_6E10():
        CameraSetDistance(2600, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6E10)

    Sleep(1000)

    ChrSetSubChip(0x0101, 2)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010320674V#1026F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(109020, 200, 13230, 0)
    OP_67(0, 6120, -10000, 0)
    CameraSetDistance(2930, 0)
    OP_6C(53000, 0)
    OP_6E(249, 0)
    OP_0D()
    Sleep(200)

    ChrSetSubChip(0x0008, 2)
    Sleep(100)

    ChrSetSubChip(0x000C, 1)
    Sleep(100)

    ChrTalk(
        0x000B,
        (
            '#0060320675V#044F？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320676V#064F#6P姐姐，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010320677V#1016F#5P啊，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetPos(0x0101, 109200, 0, 14020, 0)
    ChrClearFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_6F7E')
    def lambda_6F7E():
        CameraMove(108880, 0, 13830, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6F7E)

    @scena.Lambda('lambda_6F96')
    def lambda_6F96():
        OP_67(0, 6300, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6F96)

    Sleep(1000)

    ChrSetDirection(0x0101, 225, 300)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010320678V#1025F#5P我……\n',
            '我稍微出去散下步。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320679V吃晚饭的时候就回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320680V#020F#2P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320681V#021F迟到的话，可\n',
            '什么都剩不下了哟？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320682V#1016F#5P啊哈哈，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320683V#1006F那么，等会见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    ChrSetFlags(0x0101, 0x0004)
    ChrMoveTo(0x0101, 108450, 0, 14340, 2000, 0x00)
    ChrWalkTo(0x0101, 106450, 0, 14370, 2000, 0x00)

    @scena.Lambda('lambda_70EA')
    def lambda_70EA():
        CameraMove(108160, 0, 13580, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_70EA)

    @scena.Lambda('lambda_7102')
    def lambda_7102():
        OP_6C(53000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7102)

    @scena.Lambda('lambda_7112')
    def lambda_7112():
        ChrWalkTo(0x00FE, 104430, 0, 12920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7112)

    ChrSetSubChip(0x000B, 1)
    Sleep(100)

    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 270, 400)
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_7152')
    def lambda_7152():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7152)

    ChrWalkTo(0x0101, 102500, 0, 13040, 2000, 0x00)
    ChrSetFlags(0x0101, 0x0080)
    WaitForThreadExit(0x0101, 0x0002)
    PlaySE(7, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '#0070320684V#065F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    @scena.Lambda('lambda_71AC')
    def lambda_71AC():
        CameraMove(109020, 200, 13230, 1600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_71AC)

    ChrSetSubChip(0x000C, 0)
    Sleep(100)

    ChrSetSubChip(0x000B, 0)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#0070320685V#063F#6P雪拉姐姐，那……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320686V#524F#2P没关系的，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320687V现在这时候\n',
            '最好还是让她去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320688V#043F难道说……\n',
            '是约修亚的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320689V#065F#6P啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320690V#026F#2P呵呵，你很明白呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0008, 2)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0030320691V#522F#2P这么说来，那个时候也……\n',
            '夕阳也和今天一样的美丽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0380, 3, 0x1C03))
    OP_28(0x0078, 0x04, 0x40)
    OP_28(0x0079, 0x04, 0x40)
    OP_28(0x007A, 0x04, 0x40)
    OP_28(0x007B, 0x04, 0x40)
    OP_28(0x007C, 0x04, 0x40)
    OP_28(0x007D, 0x04, 0x40)
    OP_28(0x00B1, 0x04, 0x40)
    OP_28(0x00B2, 0x04, 0x40)
    OP_28(0x00B3, 0x04, 0x40)
    OP_28(0x00B4, 0x04, 0x40)
    OP_28(0x0097, 0x01, 0x0020)
    OP_28(0x0097, 0x01, 0x0040)

    If(
        (
            (Expr.Eval, "OP_40(0x0381, 0x00)"),
            Expr.Return,
        ),
        'loc_737B',
    )

    RemoveItem(0x0381, 1)
    AddItem(ItemTable['蕾妮的照片'], 1)

    def _loc_737B(): pass

    label('loc_737B')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    OP_6F(0x0015, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 0)
    ChrSetPos(0x0101, 80170, 0, 14940, 270)
    ChrClearFlags(0x0101, 0x0080)
    CameraMove(80170, 0, 14940, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetStatus(0x00FF, 0xFE, 0)
    PlayBGM(15)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0037 offset: 0x7412
@scena.Code('func_37_7412')
def func_37_7412():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0101, 0x0080)
    CameraMove(109500, -250, 13820, 0)
    OP_67(0, 6350, -10000, 0)
    CameraSetDistance(2710, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1500)

    ChrSetSubChip(0x0008, 2)
    Sleep(200)

    ChrSetSubChip(0x000C, 1)
    Sleep(200)

    ChrSetSubChip(0x000B, 1)
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetFlags(0x000E, 0x0080)
    ChrSetSubChip(0x0009, 2)
    ChrSetSubChip(0x000A, 2)
    ChrSetSubChip(0x000D, 1)
    CameraMove(27330, -250, 5710, 0)
    OP_67(0, 9000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(61000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_74E6')
    def lambda_74E6():
        CameraMove(17060, 0, 9800, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_74E6)

    @scena.Lambda('lambda_74FE')
    def lambda_74FE():
        OP_67(0, 8000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_74FE)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(4000)

    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T1500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0038 offset: 0x753D
@scena.Code('func_38_753D')
def func_38_753D():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_75BA'),
        (0x00000001, 'loc_75C0'),
        (-1, 'loc_75C6'),
    )

    def _loc_75BA(): pass

    label('loc_75BA')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_75C6')

    def _loc_75C0(): pass

    label('loc_75C0')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_75C6')

    def _loc_75C6(): pass

    label('loc_75C6')

    Return()

# id: 0x0039 offset: 0x75C7
@scena.Code('func_39_75C7')
def func_39_75C7():
    MapClearFlags(0x00000001)
    CameraMove(64510, 0, -14780, 92)
    FadeIn(0, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            0x00FF,
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
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
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
