import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1410_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1410   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '王国军士兵'),
    TXT(0x02, '王国军士兵'),
    TXT(0x03, '摩尔根将军'),
    TXT(0x04, '诺朗'),
    TXT(0x05, '艾蕾米亚'),
    TXT(0x06, '阿尔宾'),
    TXT(0x07, '蔡尔德'),
    TXT(0x08, '马尔科'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1410.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x29B7
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
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH02083._CH', 'ED6_DT07/CH02083P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 104300,
            z                   = 0,
            y                   = 107600,
            direction           = 0,
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
            x                   = 201700,
            z                   = 0,
            y                   = 109600,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 209550,
            z                   = 200,
            y                   = 11820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 18100,
            z                   = 0,
            y                   = 16400,
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
            x                   = 15350,
            z                   = 0,
            y                   = 15480,
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
            x                   = 20700,
            z                   = 0,
            y                   = 13230,
            direction           = 191,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 23470,
            z                   = 0,
            y                   = 12150,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 23470,
            z                   = 0,
            y                   = 12150,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
    )

# id: 0x10003 offset: 0x1E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1E2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1E2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 17690,
            triggerZ            = 0,
            triggerY            = 14350,
            triggerRange        = 800,
            actorX              = 18100,
            actorZ              = 1500,
            actorY              = 16400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 207600,
            triggerZ            = 0,
            triggerY            = 11880,
            triggerRange        = 800,
            actorX              = 209550,
            actorZ              = 1500,
            actorY              = 11820,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 123890,
            triggerZ            = 0,
            triggerY            = 11990,
            triggerRange        = 800,
            actorX              = 123890,
            actorZ              = 800,
            actorY              = 11990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x24E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_26C',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000F, 0x0080)

    Jump('loc_29D')

    def _loc_26C(): pass

    label('loc_26C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_276',
    )

    Jump('loc_29D')

    def _loc_276(): pass

    label('loc_276')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_296',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrPos(0x0009, 206990, -20, 101510, 45)

    Jump('loc_29D')

    def _loc_296(): pass

    label('loc_296')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_29D',
    )

    def _loc_29D(): pass

    label('loc_29D')

    Return()

# id: 0x0001 offset: 0x29E
@scena.Code('Init')
def Init():
    OP_72(0x0003, 0x0010)
    OP_72(0x0004, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2B2',
    )

    Jump('loc_2D1')

    def _loc_2B2(): pass

    label('loc_2B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2BC',
    )

    Jump('loc_2D1')

    def _loc_2BC(): pass

    label('loc_2BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2CA',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_2D1')

    def _loc_2CA(): pass

    label('loc_2CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2D1',
    )

    def _loc_2D1(): pass

    label('loc_2D1')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_302',
    )

    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_79(0x05, 0x0002)
    OP_79(0x06, 0x0002)
    OP_79(0x07, 0x0002)
    OP_79(0x08, 0x0002)
    OP_7B()

    def _loc_302(): pass

    label('loc_302')

    Return()

# id: 0x0002 offset: 0x303
@scena.Code('ReInit')
def ReInit():
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
        'loc_328',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_46A')

    def _loc_328(): pass

    label('loc_328')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_341',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_46A')

    def _loc_341(): pass

    label('loc_341')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35A',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_46A')

    def _loc_35A(): pass

    label('loc_35A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_373',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_46A')

    def _loc_373(): pass

    label('loc_373')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38C',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_46A')

    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A5',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_46A')

    def _loc_3A5(): pass

    label('loc_3A5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BE',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_46A')

    def _loc_3BE(): pass

    label('loc_3BE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D7',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_46A')

    def _loc_3D7(): pass

    label('loc_3D7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F0',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_46A')

    def _loc_3F0(): pass

    label('loc_3F0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_409',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_46A')

    def _loc_409(): pass

    label('loc_409')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_422',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_46A')

    def _loc_422(): pass

    label('loc_422')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43B',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_46A')

    def _loc_43B(): pass

    label('loc_43B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_454',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_46A')

    def _loc_454(): pass

    label('loc_454')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_46A',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_46A(): pass

    label('loc_46A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_47F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_46A')

    def _loc_47F(): pass

    label('loc_47F')

    Return()

# id: 0x0003 offset: 0x480
@scena.Code('func_03_480')
def func_03_480():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4A3',
    )

    OP_8D(0x00FE, 20000, 13500, 21500, 11750, 1500)

    Jump('func_03_480')

    def _loc_4A3(): pass

    label('loc_4A3')

    Return()

# id: 0x0004 offset: 0x4A4
@scena.Code('func_04_4A4')
def func_04_4A4():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x4A9
@scena.Code('func_05_4A9')
def func_05_4A9():
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
    ClearChrFlags(0x000A, 0x0010)
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
        'loc_539',
    )

    Jump('loc_57B')

    def _loc_539(): pass

    label('loc_539')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_555',
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

    Jump('loc_57B')

    def _loc_555(): pass

    label('loc_555')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_571',
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

    Jump('loc_57B')

    def _loc_571(): pass

    label('loc_571')

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_57B(): pass

    label('loc_57B')

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

    SetChrFlags(0x000A, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C6B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 7, 0x2097)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_934',
    )

    ChrTalk(
        0x000A,
        (
            '#0600350352V#160F嗯，是你们呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350353V『塔』被压制住了，辛苦你们了……还有，\n',
            '本来应该慰劳你们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350354V#166F但是现在这个形势下\n',
            '我连说些客套话的工夫都没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350355V有机会的话再招待你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350356V#1015F哎呀，真是可惜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350357V#1043F的确和以前相比\n',
            '状况已经改变了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_724',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350358V#053F而且还是往坏的方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_79D')

    def _loc_724(): pass

    label('loc_724')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_762',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350359V#026F而且还是往坏的方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_79D')

    def _loc_762(): pass

    label('loc_762')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_79D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350360V#072F而且还是往坏的方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_79D(): pass

    label('loc_79D')

    ChrTalk(
        0x000A,
        (
            '#0600350361V#160F由于那个发生器的作用，\n',
            '据点间的通信恢复了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350362V果然这个导力停止现象\n',
            '是在王国全境内发生的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350363V我想你们已经见到了，\n',
            '现在这个关所也处于危险状态中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350364V总之不能让敌人乘虚而入，\n',
            '这就是尽了军人的本分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350365V我也期待你们游击士的工作\n',
            '能有更好的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350366V#1006F嗯！加油呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350367V#1042F为了不负您的期待，我们会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)
    OP_A2(0x2097)

    Jump('loc_C68')

    def _loc_934(): pass

    label('loc_934')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_BE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_9C4',
    )

    ChrTalk(
        0x000A,
        (
            '#0600350368V#160F总之不能让敌人乘虚而入，\n',
            '这就是尽了军人的本分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350369V你们游击士的工作也是，\n',
            '希望能有更好的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE6')

    def _loc_9C4(): pass

    label('loc_9C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B39',
    )

    ChrTalk(
        0x000A,
        (
            '#0600350370V#160F继续整顿防备，\n',
            '不能使用导力兵器真糟糕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350371V如果敌人来进攻的话，\n',
            '只能靠白兵战死守大门了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350372V#163F不过，敌人也是一样。\n',
            '胜算都是五五成。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350373V我想精于算计的帝国，\n',
            '不会做出这样危险的决定……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350374V#160F不过，希望这至少\n',
            '不是我们单方面的想法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350375V要经常做好最坏的心理准备，\n',
            '保卫国家是国民的职责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_BE6')

    def _loc_B39(): pass

    label('loc_B39')

    ChrTalk(
        0x000A,
        (
            '#0600350376V#166F敌人也一样不能使用导力兵器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350377V这样的话，除了白兵战\n',
            '之外就没有其它的战斗手段了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350378V像这样的消耗战\n',
            '我认为帝国不会来硬碰硬的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE6(): pass

    label('loc_BE6')

    Jump('loc_C68')

    def _loc_BE9(): pass

    label('loc_BE9')

    ChrTalk(
        0x000A,
        (
            '#0600350368V#160F总之不能让敌人乘虚而入，\n',
            '这就是尽了军人的本分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600350369V你们游击士的工作也是，\n',
            '希望能有更好的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_C68(): pass

    label('loc_C68')

    Jump('loc_126B')

    def _loc_C6B(): pass

    label('loc_C6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_DC1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0349, 7, 0x1A4F)),
            Expr.Return,
        ),
        'loc_CCF',
    )

    ChrTalk(
        0x000A,
        (
            '#0600320399V#163F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600320398V请帮我们弄清这事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBE')

    def _loc_CCF(): pass

    label('loc_CCF')

    ChrTalk(
        0x000A,
        (
            '#0600320394V#160F嗯，是你们呀。\n',
            '捕获作战辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600320395V#166F有什么要问的吗，\n',
            '看你的脸我就明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600320396V#163F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600320397V……关于这件事\n',
            '我也说不好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600320398V请帮我们弄清这事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A4F)

    def _loc_DBE(): pass

    label('loc_DBE')

    Jump('loc_126B')

    def _loc_DC1(): pass

    label('loc_DC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_126B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0349, 6, 0x1A4E)),
            Expr.Return,
        ),
        'loc_E41',
    )

    ChrTalk(
        0x000A,
        (
            '#0600311465V#160F我们会协助协会\n',
            '也是因为互相信赖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311466V有什么事件发生的话\n',
            '希望你们马上联络军方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126B')

    def _loc_E41(): pass

    label('loc_E41')

    ChrTalk(
        0x000A,
        (
            '#0600311467V#160F什么，我还以为是谁呢，\n',
            '这不是卡西乌斯的女儿嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311468V在王都辛苦你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311469V听说结社在洛连特也发动\n',
            '了骚乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311470V#1003F嗯，虽然很糟糕，\n',
            '不过总算解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311471V#053F啊，真是经历了\n',
            '非常大的灾难呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600311472V#163F嗯，是这样呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311473V果然是结社的人，\n',
            '好象都是些很难对付的家伙呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311474V看来今后提高警戒\n',
            '是很有必要的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311475V#160F真巧，是你们呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311476V你们现在在这个地方\n',
            '进行工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311477V#1011F啊，嗯，是这样呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010311478V在帮助柏斯支部\n',
            '消灭通缉魔兽呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600311479V#165F原来如此……\n',
            '剿灭魔兽真是多呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311480V#160F不过，有什么事件发生的话\n',
            '希望你们马上联络军方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311481V我们会协助协会\n',
            '也是因为互相信赖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311482V特别是最近，因为\n',
            '出现邪恶组织的关系呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11C0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311483V#027F如果有什么事的话\n',
            '通过支部联络我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030311484V这样就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_121A')

    def _loc_11C0(): pass

    label('loc_11C0')

    ChrTalk(
        0x0106,
        (
            '#0050311485V#050F如果有什么事的话\n',
            '通过支部联络我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311486V这样就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_121A(): pass

    label('loc_121A')

    ChrTalk(
        0x000A,
        (
            '#0600311487V#160F嗯，就这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311488V但请务必……\n',
            '不要太逞强呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A4E)

    def _loc_126B(): pass

    label('loc_126B')

    SetChrSubChip(0x000A, 0)
    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x1274
@scena.Code('func_06_1274')
def func_06_1274():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1368',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_131B',
    )

    ChrTalk(
        0x00FE,
        (
            '现在这时候\n',
            '帝国军似乎没什么行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但相反来说\n',
            '却更让人更紧张了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看，不是有句话说\n',
            '暴风雨前的宁静吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和那个一样的感觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_1365')

    def _loc_131B(): pass

    label('loc_131B')

    ChrTalk(
        0x00FE,
        (
            '现在这时候\n',
            '帝国军似乎没什么行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但相反来说\n',
            '却更让人更紧张了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1365(): pass

    label('loc_1365')

    Jump('loc_163C')

    def _loc_1368(): pass

    label('loc_1368')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_13F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13CC',
    )

    ChrTalk(
        0x00FE,
        (
            '现在几乎所有的士兵\n',
            '都有出勤命令了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论怎样现在可是王国最大危机呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_13F5')

    def _loc_13CC(): pass

    label('loc_13CC')

    ChrTalk(
        0x00FE,
        (
            '现在几乎所有的士兵\n',
            '都有出勤命令了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13F5(): pass

    label('loc_13F5')

    Jump('loc_163C')

    def _loc_13F8(): pass

    label('loc_13F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_14C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_144F',
    )

    ChrTalk(
        0x00FE,
        (
            '看来这里也要\n',
            '重新进行通常勤务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真想再\n',
            '稍微喘口气呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14C3')

    def _loc_144F(): pass

    label('loc_144F')

    ChrTalk(
        0x00FE,
        (
            '看来这里也要\n',
            '重新进行通常勤务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为旁边就是帝国，\n',
            '不能掉以轻心的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真想再\n',
            '稍微喘口气呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_14C3(): pass

    label('loc_14C3')

    Jump('loc_163C')

    def _loc_14C6(): pass

    label('loc_14C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_156E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1512',
    )

    ChrTalk(
        0x00FE,
        (
            '但我们也为许会\n',
            '出动进行龙的搜索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不安呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156B')

    def _loc_1512(): pass

    label('loc_1512')

    ChrTalk(
        0x00FE,
        (
            '关所也被\n',
            '命令待命了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但我们也为许会\n',
            '出动进行龙的搜索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不安呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_156B(): pass

    label('loc_156B')

    Jump('loc_163C')

    def _loc_156E(): pass

    label('loc_156E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_163C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_15CB',
    )

    ChrTalk(
        0x00FE,
        (
            '这段时期洛连特\n',
            '的浓雾真厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉人简直就像\n',
            '在牛奶中游泳一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_163C')

    def _loc_15CB(): pass

    label('loc_15CB')

    ChrTalk(
        0x00FE,
        (
            '这段时期我作为增援被派遣\n',
            '洛连特地区来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，好大的雾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉人简直就像\n',
            '在牛奶中游泳一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_163C(): pass

    label('loc_163C')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x1640
@scena.Code('func_07_1640')
def func_07_1640():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1711',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1699',
    )

    ChrTalk(
        0x00FE,
        (
            '这次帝国那边\n',
            '什么反应也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是互不侵犯条约的效果吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_170E')

    def _loc_1699(): pass

    label('loc_1699')

    ChrTalk(
        0x00FE,
        (
            '这次帝国那边\n',
            '什么反应也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '过去就算有点人员调动\n',
            '他们就会赶过来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是互不侵犯条约的效果吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_170E(): pass

    label('loc_170E')

    Jump('loc_184F')

    def _loc_1711(): pass

    label('loc_1711')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_17F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1787',
    )

    ChrTalk(
        0x00FE,
        (
            '龙好象逃进峡谷里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从那边的山岳地带翻过去\n',
            '就是帝国的国境了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是个很难出手的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17EF')

    def _loc_1787(): pass

    label('loc_1787')

    ChrTalk(
        0x00FE,
        (
            '龙好象逃进峡谷里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那边的山岳地带就算是\n',
            '飞行舰队也很难出手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将军大人要怎么办呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_17EF(): pass

    label('loc_17EF')

    Jump('loc_184F')

    def _loc_17F2(): pass

    label('loc_17F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_184F',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然缔结了互不侵犯条约，\n',
            '但警戒还是那么严密。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该不会让\n',
            '帝国看到空隙了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_184F(): pass

    label('loc_184F')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x1853
@scena.Code('func_08_1853')
def func_08_1853():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0x1858
@scena.Code('func_09_1858')
def func_09_1858():
    TalkBegin(0x000B)
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
            TXT(0x02, '休息\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18C4',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x54)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_18C4(): pass

    label('loc_18C4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18DA',
    )

    OP_0D()
    OP_A9(0x55)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_18DA(): pass

    label('loc_18DA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18F4',
    )

    FadeIn(300, 0)
    TalkEnd(0x000B)

    Return()

    def _loc_18F4(): pass

    label('loc_18F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_19DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1980',
    )

    ChrTalk(
        0x000B,
        (
            '士兵们都在发抖呢，\n',
            '帝国真的会来吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '已经有了互不侵犯条约，\n',
            '我想应该不可能吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '士兵们有点\n',
            '神经过敏罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_19D8')

    def _loc_1980(): pass

    label('loc_1980')

    ChrTalk(
        0x000B,
        (
            '士兵们都在发抖呢，\n',
            '帝国真的会来吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '已经有了互不侵犯条约，\n',
            '我想应该不可能吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19D8(): pass

    label('loc_19D8')

    Jump('loc_1EA6')

    def _loc_19DB(): pass

    label('loc_19DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1ABD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A68',
    )

    ChrTalk(
        0x000B,
        (
            '哟，欢迎来到关所的酒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '虽然看上去是戒严状态，\n',
            '但还是来一杯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '放心吧，不会这么简单\n',
            '就发生武装冲突的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_1ABA')

    def _loc_1A68(): pass

    label('loc_1A68')

    ChrTalk(
        0x000B,
        (
            '虽然看上去是戒严状态，\n',
            '但还是来一杯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不会这么简单\n',
            '就发生武装冲突的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ABA(): pass

    label('loc_1ABA')

    Jump('loc_1EA6')

    def _loc_1ABD(): pass

    label('loc_1ABD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 0, 0x1A50)),
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1CE4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C93',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1B7D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1B38',
    )

    ChrTalk(
        0x000B,
        (
            '龙的事件解决了，\n',
            '现在也能放松一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '接下来，现在\n',
            '开始准备晚饭了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B7A')

    def _loc_1B38(): pass

    label('loc_1B38')

    ChrTalk(
        0x000B,
        (
            '哟，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '龙的事件解决了，\n',
            '现在也能放松一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1B7A(): pass

    label('loc_1B7A')

    Jump('loc_1C90')

    def _loc_1B7D(): pass

    label('loc_1B7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1C36',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1BE0',
    )

    ChrTalk(
        0x000B,
        (
            '因为龙的事件，\n',
            '这里处于戒严状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '士兵们也准备出动了，\n',
            '好像都在待命呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C33')

    def _loc_1BE0(): pass

    label('loc_1BE0')

    ChrTalk(
        0x000B,
        (
            '因为龙的事件，\n',
            '这里处于戒严状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哎呀哎呀，这里最近\n',
            '一直都很和平呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1C33(): pass

    label('loc_1C33')

    Jump('loc_1C90')

    def _loc_1C36(): pass

    label('loc_1C36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1C90',
    )

    ChrTalk(
        0x000B,
        (
            '哟，欢迎来到关所的酒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '虽然拿不出象样的东西，\n',
            '但至少还是能填饱肚子的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C90(): pass

    label('loc_1C90')

    Jump('loc_1CE1')

    def _loc_1C93(): pass

    label('loc_1C93')

    ChrTalk(
        0x000B,
        (
            '看样子还真是次\n',
            '厉害的旅行呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那就来一杯，\n',
            '我还想听听你们的故事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1CE1(): pass

    label('loc_1CE1')

    Jump('loc_1EA6')

    def _loc_1CE4(): pass

    label('loc_1CE4')

    ChrTalk(
        0x000B,
        (
            '哟，欢迎来到关所的酒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000B, 0x0104, 400)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '哎呀，是你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F呵，好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '自从那时入境利贝尔王国时\n',
            '碰过面到现在一直都没见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '喔，你果然是\n',
            '那个帝国旅行者呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么旅行怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F啊啊，真是\n',
            '超乎想象的愉快呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#035F只能用一场大冒险\n',
            '来形容的这次旅行呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哎呀，那还真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那就来一杯，\n',
            '我还想听听旅行中的故事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F呵，等到时候\n',
            '我会找你喝一杯的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A50)
    OP_A2(0x0002)
    def _loc_1EA6(): pass

    label('loc_1EA6')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x1EAA
@scena.Code('func_0A_1EAA')
def func_0A_1EAA():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1F07',
    )

    ChrTalk(
        0x00FE,
        (
            '为什么王国全境\n',
            '的导力器都停止了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想老板一定会认为\n',
            '是导力器坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21AB')

    def _loc_1F07(): pass

    label('loc_1F07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1FEE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F9E',
    )

    ChrTalk(
        0x00FE,
        (
            '这个关所经常会发生骚乱，\n',
            '不过这次有些特别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从士兵们的脸上也\n',
            '感觉到了平日没有的紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望什么也没发生就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_1FEB')

    def _loc_1F9E(): pass

    label('loc_1F9E')

    ChrTalk(
        0x00FE,
        (
            '这个关所经常会发生骚乱，\n',
            '不过这次有些特别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么也没发生就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FEB(): pass

    label('loc_1FEB')

    Jump('loc_21AB')

    def _loc_1FEE(): pass

    label('loc_1FEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_203A',
    )

    ChrTalk(
        0x00FE,
        (
            '终于这个关所也\n',
            '恢复平静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下晚上\n',
            '终于能睡个好觉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21AB')

    def _loc_203A(): pass

    label('loc_203A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2094',
    )

    ChrTalk(
        0x00FE,
        (
            '龙的捕获作战\n',
            '真是拖了好长时间呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看了士兵们的表情\n',
            '心里就会感到不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21AB')

    def _loc_2094(): pass

    label('loc_2094')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_21AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_211C',
    )

    ChrTalk(
        0x00FE,
        (
            '登山家虽然很有气魄，\n',
            '但总觉得土土的呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这点上，理查德上校\n',
            '相当的出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀啊，为什么要\n',
            '发动政变呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21AB')

    def _loc_211C(): pass

    label('loc_211C')

    ChrTalk(
        0x00FE,
        (
            '那边的客人们\n',
            '好象要去登山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，那些登山家\n',
            '的确很有男子气概……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我，对那些汗臭\n',
            '非常头痛呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是喜欢\n',
            '更加潇洒的男性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_21AB(): pass

    label('loc_21AB')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x21AF
@scena.Code('func_0B_21AF')
def func_0B_21AF():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2264',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_220E',
    )

    ChrTalk(
        0x00FE,
        (
            '漫长的等待有了价值，\n',
            '登山许可终于下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，准备出发登山吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2261')

    def _loc_220E(): pass

    label('loc_220E')

    ChrTalk(
        0x00FE,
        (
            '等待终于有了价值，\n',
            '登山许可下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '跟蔡尔德说的一样，\n',
            '耐心等就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_2261(): pass

    label('loc_2261')

    Jump('loc_2446')

    def _loc_2264(): pass

    label('loc_2264')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_235F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_22C1',
    )

    ChrTalk(
        0x00FE,
        (
            '不管军队怎么说，\n',
            '登山是不能中止的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干脆不管警告，\n',
            '现在就出发吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235C')

    def _loc_22C1(): pass

    label('loc_22C1')

    ChrTalk(
        0x00FE,
        (
            '王国军发来劝告，\n',
            '要我们中止登山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都准备了好几个月了，\n',
            '简直是开玩笑嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都走到这了，\n',
            '竟然不能上山……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干脆不管警告，\n',
            '马上就出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_235C(): pass

    label('loc_235C')

    Jump('loc_2446')

    def _loc_235F(): pass

    label('loc_235F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2446',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_23BE',
    )

    ChrTalk(
        0x00FE,
        (
            '我们可是山的孩子。\n',
            '准备登上国境的山脉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在为了准备\n',
            '留在这个关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2446')

    def _loc_23BE(): pass

    label('loc_23BE')

    ChrTalk(
        0x00FE,
        (
            '我们可是山的孩子。\n',
            '准备登上国境的山脉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '迷雾峡谷的西面\n',
            '还有很多未被踏足的山脉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我们来说\n',
            '实在是很块有魅力的地区呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_2446(): pass

    label('loc_2446')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x244A
@scena.Code('func_0C_244A')
def func_0C_244A():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2543',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_24AC',
    )

    ChrTalk(
        0x00FE,
        (
            '路线必须\n',
            '严格地进行确认。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样这次挑战的\n',
            '是前人未踏足过的山呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2540')

    def _loc_24AC(): pass

    label('loc_24AC')

    ChrTalk(
        0x00FE,
        (
            '嗯，根据今天的风向\n',
            '可以暂时不用担心雾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，路线必须\n',
            '严格地进行确认。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样挑战的可是未踏足过的山峰。\n',
            '一定要尽可能的慎重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_2540(): pass

    label('loc_2540')

    Jump('loc_2704')

    def _loc_2543(): pass

    label('loc_2543')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_264C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_25A2',
    )

    ChrTalk(
        0x00FE,
        (
            '耐心等待的话\n',
            '也许会有好结果的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的伙伴阿尔宾，应该\n',
            '变得再耐心点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2649')

    def _loc_25A2(): pass

    label('loc_25A2')

    ChrTalk(
        0x00FE,
        (
            '因为军队的劝告，我们\n',
            '只能在这里等待……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候，\n',
            '就是考验忍耐力的时候呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之就算着急也没用，\n',
            '只有慢慢等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '耐心等待的话\n',
            '也许会有好结果的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_2649(): pass

    label('loc_2649')

    Jump('loc_2704')

    def _loc_264C(): pass

    label('loc_264C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2704',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_26AD',
    )

    ChrTalk(
        0x00FE,
        (
            '迷雾峡谷周围环境…\n',
            '特别是天气很容易变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们必须慎重地\n',
            '看清楚变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2704')

    def _loc_26AD(): pass

    label('loc_26AD')

    ChrTalk(
        0x00FE,
        (
            '食物的分配，\n',
            '装备的检查都完成了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之后就等进山了，\n',
            '只剩等一个好时机了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_2704(): pass

    label('loc_2704')

    TalkEnd(0x000E)

    Return()

# id: 0x000D offset: 0x2708
@scena.Code('func_0D_2708')
def func_0D_2708():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_27F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27AB',
    )

    ChrTalk(
        0x00FE,
        (
            '我虽是帝国人，\n',
            '但帝国真的会行动吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然和利贝尔王国\n',
            '刚刚缔结了互不侵犯条约……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '突然像这样背信的行动\n',
            '也是祖国不想有的吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_27F4')

    def _loc_27AB(): pass

    label('loc_27AB')

    ChrTalk(
        0x00FE,
        (
            '但帝国真的会行动吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和利贝尔王国刚刚才\n',
            '缔结了互不侵犯条约……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27F4(): pass

    label('loc_27F4')

    Jump('loc_2958')

    def _loc_27F7(): pass

    label('loc_27F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2958',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28DB',
    )

    ChrTalk(
        0x00FE,
        (
            '因定期船停航，只能\n',
            '从陆路回帝国了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '遇到这样的情况\n',
            '真是做梦也没想到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我身为帝国商人的一员\n',
            '祝愿祖国的繁荣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，那应该能通过\n',
            '和平的方式达成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两国间的关系紧张\n',
            '实在是可惜呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_2958')

    def _loc_28DB(): pass

    label('loc_28DB')

    ChrTalk(
        0x00FE,
        (
            '我身为帝国商人的一员\n',
            '祈祷祖国的繁荣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，那应该能通过\n',
            '和平的方式达成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两国间的关系紧张\n',
            '实在是可惜呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2958(): pass

    label('loc_2958')

    TalkEnd(0x000F)

    Return()

# id: 0x000E offset: 0x295C
@scena.Code('func_0E_295C')
def func_0E_295C():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
