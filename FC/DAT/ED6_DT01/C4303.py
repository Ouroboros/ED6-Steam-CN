import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4303   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4303.x'
    header.mapIndex       = 216
    header.bgm            = 35
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

# id: 0x10000 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00273._CH', 'ED6_DT07/CH00273P._CP'),
        ('ED6_DT07/CH00271._CH', 'ED6_DT07/CH00271P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT09/CH11002._CH', 'ED6_DT09/CH11002P._CP'),
        ('ED6_DT09/CH11000._CH', 'ED6_DT09/CH11000P._CP'),
        ('ED6_DT07/CH00272._CH', 'ED6_DT07/CH00272P._CP'),
        ('ED6_DT07/CH00274._CH', 'ED6_DT07/CH00274P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20027._CH', 'ED6_DT06/CH20027P._CP'),
        ('ED6_DT06/CH20028._CH', 'ED6_DT06/CH20028P._CP'),
        ('ED6_DT06/CH20029._CH', 'ED6_DT06/CH20029P._CP'),
        ('ED6_DT06/CH20084._CH', 'ED6_DT06/CH20084P._CP'),
        ('ED6_DT06/CH20077._CH', 'ED6_DT06/CH20077P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH00104._CH', 'ED6_DT07/CH00104P._CP'),
        ('ED6_DT07/CH00114._CH', 'ED6_DT07/CH00114P._CP'),
        ('ED6_DT07/CH00124._CH', 'ED6_DT07/CH00124P._CP'),
        ('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00134P._CP'),
        ('ED6_DT07/CH00144._CH', 'ED6_DT07/CH00144P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP'),
        ('ED6_DT07/CH00164._CH', 'ED6_DT07/CH00164P._CP'),
        ('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00174P._CP'),
        ('ED6_DT06/CH20046._CH', 'ED6_DT06/CH20046P._CP'),
        ('ED6_DT07/CH00270._CH', 'ED6_DT07/CH00270P._CP'),
    ]

# id: 0x10001 offset: 0x266
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雪拉',
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
            name                = '奥利维尔',
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
            name                = '科洛丝',
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
            name                = '阿加特',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '基库',
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
            name                = '理查德上校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 46,
            chipIndex           = 46,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卡西乌斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '机器',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '机器',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '机器',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '机器',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 1780,
            z                   = 1250,
            y                   = 19300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 917534,
            chipIndex           = 30,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 45,
            chipIndex           = 45,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x586
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x586
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x586
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x586
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_59D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x5C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_06_3261)

    def _loc_59D(): pass

    label('loc_59D')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_5A9'),
        (-1, 'loc_5BF'),
    )

    def _loc_5A9(): pass

    label('loc_5A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 1, 0x669)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5BC',
    )

    SetScenaFlags(ScenaFlag(0x00CD, 2, 0x66A))
    Event(0, func_03_708)

    def _loc_5BC(): pass

    label('loc_5BC')

    Jump('loc_5BF')

    def _loc_5BF(): pass

    label('loc_5BF')

    Return()

# id: 0x0001 offset: 0x5C0
@scena.Code('func_01_5C0')
def func_01_5C0():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x39C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D5',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5D5(): pass

    label('loc_5D5')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x3A1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F7',
    )

    ExecExpressionWithVar(
        0x29,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_08_4727)

    def _loc_5F7(): pass

    label('loc_5F7')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x3A2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_60C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_60C(): pass

    label('loc_60C')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x3B3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_621',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_621(): pass

    label('loc_621')

    Return()

# id: 0x0002 offset: 0x622
@scena.Code('func_02_622')
def func_02_622():
    LoadEffect(0x00, 'map\\\\mp007_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 1780, 1500, 19300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(5000)

    LoadEffect(0x01, 'map\\\\mp007_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 1780, 1500, 19300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(5000)

    LoadEffect(0x02, 'map\\\\mp015_00.eff')
    PlayEffect(0x02, 0x02, 0x00FF, 1780, 1500, 19300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0003 offset: 0x708
@scena.Code('func_03_708')
def func_03_708():
    EventBegin(0x00)
    OP_72(0x0006, 0x0020)
    OP_71(0x0006, 0x0004)
    OP_6F(0x0006, 0)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 1000)
    OP_71(0x0000, 0x0020)
    OP_71(0x0001, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_70(0x0000, 1000)
    OP_70(0x0001, 1000)
    OP_70(0x0002, 1000)
    OP_70(0x0003, 1000)
    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 12)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_792',
    )

    ChrSetChipByIndex(0x0103, 14)

    def _loc_792(): pass

    label('loc_792')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7A8',
    )

    ChrSetChipByIndex(0x0104, 16)
    SetScenaFlags(ScenaFlag(0x00DE, 5, 0x6F5))

    def _loc_7A8(): pass

    label('loc_7A8')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7BB',
    )

    ChrSetChipByIndex(0x0106, 20)

    def _loc_7BB(): pass

    label('loc_7BB')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7CE',
    )

    ChrSetChipByIndex(0x0105, 18)

    def _loc_7CE(): pass

    label('loc_7CE')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7E1',
    )

    ChrSetChipByIndex(0x0107, 22)

    def _loc_7E1(): pass

    label('loc_7E1')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7F4',
    )

    ChrSetChipByIndex(0x0108, 24)

    def _loc_7F4(): pass

    label('loc_7F4')

    ChrSetPos(0x0101, -1440, 0, -47330, 0)
    ChrSetPos(0x0102, 720, 0, -47210, 0)

    @scena.Lambda('lambda_081C')
    def lambda_081C():
        ChrSetDirection(0x0101, 45, 0)
        Yield()

        Jump('lambda_081C')

    DispatchAsync2(0x0010, 0x0001, lambda_081C)

    @scena.Lambda('lambda_082D')
    def lambda_082D():
        ChrSetDirection(0x0102, 315, 0)
        Yield()

        Jump('lambda_082D')

    DispatchAsync2(0x0010, 0x0002, lambda_082D)

    @scena.Lambda('lambda_083E')
    def lambda_083E():
        ChrWalkTo(0x00FE, -1750, 0, 11650, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_083E)

    @scena.Lambda('lambda_0859')
    def lambda_0859():
        ChrWalkTo(0x00FE, 1590, 0, 11650, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0859)

    ClearScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_8BC',
    )

    ChrSetPos(0x0000, 970, 0, -49020, 0)

    @scena.Lambda('lambda_08A4')
    def lambda_08A4():
        ChrWalkTo(0x00FE, 750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_08A4)

    Jump('loc_8E8')

    def _loc_8BC(): pass

    label('loc_8BC')

    ChrSetPos(0x0000, -2029, 0, -48950, 0)

    @scena.Lambda('lambda_08D3')
    def lambda_08D3():
        ChrWalkTo(0x00FE, -750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_08D3)

    def _loc_8E8(): pass

    label('loc_8E8')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_8EB(): pass

    label('loc_8EB')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_965',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_936',
    )

    ChrSetPos(0x0001, 970, 0, -49020, 0)

    @scena.Lambda('lambda_091E')
    def lambda_091E():
        ChrWalkTo(0x00FE, 750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_091E)

    Jump('loc_962')

    def _loc_936(): pass

    label('loc_936')

    ChrSetPos(0x0001, -2029, 0, -48950, 0)

    @scena.Lambda('lambda_094D')
    def lambda_094D():
        ChrWalkTo(0x00FE, -750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_094D)

    def _loc_962(): pass

    label('loc_962')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_965(): pass

    label('loc_965')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_9B0',
    )

    ChrSetPos(0x0002, 970, 0, -49020, 0)

    @scena.Lambda('lambda_0998')
    def lambda_0998():
        ChrWalkTo(0x00FE, 750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_0998)

    Jump('loc_9DC')

    def _loc_9B0(): pass

    label('loc_9B0')

    ChrSetPos(0x0002, -2029, 0, -48950, 0)

    @scena.Lambda('lambda_09C7')
    def lambda_09C7():
        ChrWalkTo(0x00FE, -750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_09C7)

    def _loc_9DC(): pass

    label('loc_9DC')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_9DF(): pass

    label('loc_9DF')

    If(
        (
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A59',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_A2A',
    )

    ChrSetPos(0x0003, 970, 0, -49020, 0)

    @scena.Lambda('lambda_0A12')
    def lambda_0A12():
        ChrWalkTo(0x00FE, 750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_0A12)

    Jump('loc_A56')

    def _loc_A2A(): pass

    label('loc_A2A')

    ChrSetPos(0x0003, -2029, 0, -48950, 0)

    @scena.Lambda('lambda_0A41')
    def lambda_0A41():
        ChrWalkTo(0x00FE, -750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_0A41)

    def _loc_A56(): pass

    label('loc_A56')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_A59(): pass

    label('loc_A59')

    FadeIn(2000, 0)
    OP_6E(350, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 0, 600, 18060, 0)

    @scena.Lambda('lambda_0A87')
    def lambda_0A87():
        CameraMove(-610, 0, -1460, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0A87)

    Sleep(1000)

    @scena.Lambda('lambda_0AA4')
    def lambda_0AA4():
        OP_67(0, 3010, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0AA4)

    @scena.Lambda('lambda_0ABC')
    def lambda_0ABC():
        OP_6C(0, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0ABC)

    Sleep(1000)

    @scena.Lambda('lambda_0AD1')
    def lambda_0AD1():
        OP_6E(757, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0AD1)

    Sleep(2000)

    @scena.Lambda('lambda_0AE6')
    def lambda_0AE6():
        CameraMove(130, 1600, 15530, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0AE6)

    @scena.Lambda('lambda_0AFE')
    def lambda_0AFE():
        CameraSetDistance(1490, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AFE)

    WaitForThreadExit(0x0102, 0x0001)
    Sleep(1000)

    @scena.Lambda('lambda_0B18')
    def lambda_0B18():
        CameraMove(0, 270, 15110, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0B18)

    @scena.Lambda('lambda_0B30')
    def lambda_0B30():
        OP_67(0, 4960, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B30)

    Sleep(1000)

    ChrSetFlags(0x0010, 0x0020)
    ChrSetDirection(0x0010, 180, 400)
    TerminateThread(0x0010, 0xFF)
    WaitForThreadExit(0x0102, 0x0003)

    ChrTalk(
        0x0010,
        (
            '#0130140151V#5P#110F……最后还是来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140152V#110F我还一直以为你们不会来了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140153V#002F理查德上校……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140154V受艾莉茜雅女王陛下的委托，\n',
            '我们前来阻止你的计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140155V#012F看来『福音』还没有开始启动。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140156V现在……还来得及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140157V#5P#111F呵呵，那可不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140158V#005F你想做什么！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140159V『辉之环』究竟是什么！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140160V将那个东西弄到手，\n',
            '到底是为了什么目的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(30, 2000, 17430, 0)
    OP_67(0, 2970, -10000, 0)
    CameraSetDistance(980, 0)
    OP_6C(0, 0)
    OP_6E(757, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0130140161V#5P#111F当然是为了借助\n',
            '上天赐予古代人的『七至宝』的力量，\n',
            '去任意支配海洋、大地和天空。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140162V而这『辉之环』就是『七至宝』之一。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140163V假如这东西真的埋藏在这里的话……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140164V对于国家来说意味着什么，\n',
            '我想你们应该不会不明白吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140165V#580F#1P对、对于国家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F2E',
    )

    NpcTalk(
        0x0102,
        '奥利维尔',
        (
            '#0040140166V#035F#2P能得到破坏力不亚于周边国家的\n',
            '强有力的武器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140167V#032F你是这样想的，没错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_1022')

    def _loc_F2E(): pass

    label('loc_F2E')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FAA',
    )

    NpcTalk(
        0x0102,
        '科洛丝',
        (
            '#0060140168V#043F#2P可以得到能与周边国家抗衡的\n',
            '强有力的武器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140169V是这样，对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_1022')

    def _loc_FAA(): pass

    label('loc_FAA')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1022',
    )

    NpcTalk(
        0x0102,
        '金',
        (
            '#0080140170V#074F#2P能得到可以对抗周边国家的\n',
            '强有力的武器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140171V#072F是这样没错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1022(): pass

    label('loc_1022')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_109A',
    )

    ChrTalk(
        0x0102,
        (
            '#0020140172V#015F#2P可以得到能与周边诸国抗衡的\n',
            '具有惊人杀伤力的武器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140173V#012F你是这个意思吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_109A(): pass

    label('loc_109A')

    ChrTalk(
        0x0010,
        (
            '#0130140174V#5P#111F没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140175V#115F你们稍微想想就会明白——\n',
            '与周边国家相比，利贝尔的国力处于劣势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140176V人口是卡尔瓦德的五分之一左右。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140177V至于兵力，\n',
            '还不到埃雷波尼亚的八分之一。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140178V唯一占据优势的就只有导力技术，\n',
            '可谁敢保证我们能一直保持领先。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140179V#112F为了不受到第二次的侵略，\n',
            '我们一定要拥有决定性的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140180V#005F#5P就、就因为这样，\n',
            '所以才非要取得这个古代物品不可吗！？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140181V那么十年前战争，\n',
            '我们能够取得胜利靠的又是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140182V#5P#116F之所以能够击退帝国军的侵略，\n',
            '是因为有卡西乌斯·布莱特的存在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140183V#115F可是，他已经从军队里退役了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140184V守护国家的英雄离开了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140185V#112F或许，也只有奇迹和空之女神\n',
            '才能将那个深爱着自己爱人的英雄\n',
            '再次召唤回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140186V#002F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140187V#5P#110F因此，我就建立了情报部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140188V至少，让王国在情报战方面\n',
            '可以领先于其他国家一步……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140189V利用一切可能的情报网去探寻\n',
            '能够给予利贝尔决定性力量的物品。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140190V当利贝尔陷入苦境的时候，\n',
            '至少可以用它为国家再次带来奇迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140191V#505F#1P那个……不也是奇迹吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140192V#5P#113F什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(30, 2000, 13080, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010140193V#506F#3P嗯，就拿我们这些游击士来说吧，\n',
            '守护大家所珍惜的东西是我们的工作……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140194V#501F可是，守护只是一个人的事情吗？\n',
            '难道被守护的一方就不能守护别人吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140195V在守护对方的同时，\n',
            '将『互相守护』这种信念传达出来，\n',
            '这样，我觉得才是真正的守护。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140196V#5P#112F那……那又怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140197V#002F#3P十年前的战争，我老爸他，\n',
            '并不是独自一人和帝国军战斗的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140198V他是在许许多多人的帮助之下，\n',
            '集合大家的力量一起守护这片国土。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140199V正因为大家相互扶持、相互信任，\n',
            '所以，我们才取得了最终的胜利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140200V上校你不也是其中的一个吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140201V#5P#112F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140202V#003F#3P对于今天发生在我们身上的这些事情，\n',
            '我觉得也是同样的道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140203V当得知上校你的计划的时候，\n',
            '我们根本不知道该怎么办才好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140204V#006F可是，在许多朋友的帮助之下，\n',
            '我们最终还是通过努力来到了这里啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140205V难道你不觉得这是一种奇迹吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140206V#5P#115F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140207V#000F#3P不过……\n',
            '其实这并不是什么奇迹……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140208V我觉得，我们只是通过自身的努力拼搏，\n',
            '让可能实现的事情真正地实现出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140209V#500F假如真的有一天，战争不幸爆发了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140210V只要我们大家能够齐心协力，\n',
            '我想，一定一定可以排除万难的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140211V#508F与那来历不明的古代力量相比，\n',
            '我们的信念、我们的努力才更加可靠啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140212V#014F#4P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ABE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140213V#051F呵呵，真是肺腑之言啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ABE(): pass

    label('loc_1ABE')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B1C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040140214V#031F呵呵，不愧是艾丝蒂尔君。\n',
            '这种乐观向上的精神的确值得嘉许。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B1C(): pass

    label('loc_1B1C')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B6A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060140215V#048F艾丝蒂尔……\n',
            '说得很好，我也觉得是这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B6A(): pass

    label('loc_1B6A')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BAF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140216V#071F哈哈，不愧是卡西乌斯大人的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BAF(): pass

    label('loc_1BAF')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BFF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030140217V#021F真是的……\n',
            '你这孩子什么时候变得如此成熟啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BFF(): pass

    label('loc_1BFF')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C61',
    )

    ChrTalk(
        0x0107,
        (
            '#0070140218V#560F姐姐，你好棒啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070140219V我也觉得那样才是对的呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C61(): pass

    label('loc_1C61')

    ChrTalk(
        0x0010,
        (
            '#0130140220V#5P#118F呵呵……你还挺会说的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140221V的确，也许大家都会有这种信念，\n',
            '但并非所有人都能像你那样坚强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140222V当强大的力量就在你的面前时……\n',
            '要想抵挡这种诱惑谈何容易。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140223V更何况，我为了这一刻的到来，\n',
            '不知付出了多少的准备和心血。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140224V事到如今，难道要我就此罢手吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140225V#013F#4P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140226V#012F……有一个问题，希望上校能解释一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140227V为什么上校你……\n',
            '会知道这个地方的存在？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140228V#5P#113F什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140229V#015F#4P你竟然能找到这个连陛下也不知道其存在，\n',
            '沉睡着禁断之力的古代遗迹……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140230V即使在宝物库建造了通向地下的导力梯，\n',
            '也只能勉强到达这个遗迹的最上层而已……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140231V#012F难以想象单凭情报网的本事\n',
            '竟然可以查到这个地方的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140232V#5P#112F那是因为……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140233V#012F#4P还有，那个『福音』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140234V是使用凌驾于蔡斯中央工房之上的技术\n',
            '所制造出来的谜之导力器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140235V你究竟是从哪里得到那东西的？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140236V#5P#115F……我没有义务回答你这些问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140237V#016F#4P不对……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140238V对于我的种种疑问，\n',
            '你根本就回答不出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140239V#5P#117F#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140240V#580F#3P怎、怎么回事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140241V#016F#4P虽然如此，你却对这里沉睡着『辉之环』\n',
            '这样强大的古代遗物之事是如此地确信。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140242V而且，你也完全明白只有\n',
            '得到黑色导力器才能将其唤醒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140243V因此，这种种迹象都表明，\n',
            '这一切的开端绝对不是你所想出来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140244V我说得对吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140245V#5P#117F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22D1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010140246V#580F#3P这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050140247V#057F和卢安的戴尔蒙市长类似，\n',
            '他的记忆也很可能被人改动过了吧……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_2443')

    def _loc_22D1(): pass

    label('loc_22D1')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_235A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010140246V#580F#3P这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030140249V#022F和空贼团的首领一样，\n',
            '他的记忆很可能也被人操纵着吗……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_2443')

    def _loc_235A(): pass

    label('loc_235A')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23E1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010140246V#580F#3P这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080140251V#072F和那个克鲁茨一样，\n',
            '他的记忆也很可能被人消除掉了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_2443')

    def _loc_23E1(): pass

    label('loc_23E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2443',
    )

    ChrTalk(
        0x0101,
        (
            '#0010140252V#580F#3P这、这是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140253V和那些失去记忆的人情况是一样的吗！？\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2443(): pass

    label('loc_2443')

    ChrTalk(
        0x0010,
        (
            '#0130140254V#5P#117F胡说八道！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140255V……强大力量的存在\n',
            '就是这个地下遗迹的最有力证明！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140256V以我们现在的导力技术，\n',
            '是绝不可能制造出那些人形兵器来的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140257V所以我……\n',
            '我会在我选择的道路上继续走下去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_252C')
    def lambda_252C():
        CameraSetDistance(1290, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_252C)

    @scena.Lambda('lambda_253C')
    def lambda_253C():
        CameraMove(-100, 300, 15360, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_253C)

    @scena.Lambda('lambda_2554')
    def lambda_2554():
        OP_67(0, 7570, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2554)

    @scena.Lambda('lambda_256C')
    def lambda_256C():
        OP_6C(35000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_256C)

    ChrSetRGBAMask(0x0012, 255, 0, 0, 0, 0)
    ChrSetRGBAMask(0x0013, 255, 0, 0, 0, 0)
    ChrSetPos(0x0012, -2000, 7300, 15360, 180)
    ChrSetPos(0x0013, 2000, 7300, 15360, 225)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetFlags(0x0012, 0x0004)
    ChrSetFlags(0x0013, 0x0004)
    ChrSetChipByIndex(0x0012, 27)
    ChrSetChipByIndex(0x0013, 27)

    @scena.Lambda('lambda_25D2')
    def lambda_25D2():
        ChrJumpTo(0x00FE, -4000, 0, 15360, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_25D2)

    ChrSetRGBAMask(0x0012, 100, 100, 255, 255, 100)
    ChrSetRGBAMask(0x0012, 255, 255, 255, 255, 100)
    WaitForThreadExit(0x0012, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    OP_99(0x0012, 0x00, 0x07, 1500)
    ChrSetChipByIndex(0x0012, 26)
    OP_99(0x0012, 0x00, 0x03, 2000)

    @scena.Lambda('lambda_2638')
    def lambda_2638():
        OP_99(0x00FE, 0x03, 0x07, 1300)
        Yield()

        Jump('lambda_2638')

    DispatchAsync2(0x0012, 0x0001, lambda_2638)

    @scena.Lambda('lambda_264B')
    def lambda_264B():
        ChrJumpTo(0x00FE, 4000, 0, 15360, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_264B)

    ChrSetRGBAMask(0x0013, 100, 100, 255, 255, 100)
    ChrSetRGBAMask(0x0013, 255, 255, 255, 255, 100)
    WaitForThreadExit(0x0013, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    OP_99(0x0013, 0x00, 0x07, 1500)
    ChrSetChipByIndex(0x0013, 26)
    OP_99(0x0013, 0x00, 0x03, 2000)

    @scena.Lambda('lambda_26B1')
    def lambda_26B1():
        OP_99(0x00FE, 0x03, 0x07, 1300)
        Yield()

        Jump('lambda_26B1')

    DispatchAsync2(0x0013, 0x0001, lambda_26B1)

    Sleep(1000)

    PlaySE(144, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\mp007_00.eff')
    PlayEffect(0x00, 0x01, 0x00FF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010140258V#580F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140259V#5P#118F如果你们所说的那些是真的，\n',
            '就打败我，然后证明给我看吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140260V如果做不到这一点，\n',
            '你们所说的也只不过是些幼稚的理想罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_27D5')
    def lambda_27D5():
        CameraSetDistance(1000, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_27D5)

    @scena.Lambda('lambda_27E5')
    def lambda_27E5():
        OP_94(0x00, 0x00FE, 0x0000, 0x000001F4, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_27E5)

    Sleep(100)

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0010, 28)
    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x0010, 0x0002)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#0130140261V#5P#114F好好看看吧！\n',
            '继承自『剑圣』的剑技！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140262V#005F#5P信口开河！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140263V#016F#2P那么我们也不用客气，\n',
            '让他知道我们也并非等闲之辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0010, 0x03)

    @scena.Lambda('lambda_28CF')
    def lambda_28CF():
        CameraMove(-100, 300, 17360, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_28CF)

    @scena.Lambda('lambda_28E7')
    def lambda_28E7():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_28E7)

    Sleep(20)

    @scena.Lambda('lambda_2901')
    def lambda_2901():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_2901)

    Sleep(20)

    ClearScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2969',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2951',
    )

    Sleep(20)

    @scena.Lambda('lambda_293F')
    def lambda_293F():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_293F)

    Jump('loc_2966')

    def _loc_2951(): pass

    label('loc_2951')

    @scena.Lambda('lambda_2957')
    def lambda_2957():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_2957)

    def _loc_2966(): pass

    label('loc_2966')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2969(): pass

    label('loc_2969')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29BA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_29A2',
    )

    Sleep(20)

    @scena.Lambda('lambda_2990')
    def lambda_2990():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_2990)

    Jump('loc_29B7')

    def _loc_29A2(): pass

    label('loc_29A2')

    @scena.Lambda('lambda_29A8')
    def lambda_29A8():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_29A8)

    def _loc_29B7(): pass

    label('loc_29B7')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_29BA(): pass

    label('loc_29BA')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2A0B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_29F3',
    )

    Sleep(20)

    @scena.Lambda('lambda_29E1')
    def lambda_29E1():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_29E1)

    Jump('loc_2A08')

    def _loc_29F3(): pass

    label('loc_29F3')

    @scena.Lambda('lambda_29F9')
    def lambda_29F9():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_29F9)

    def _loc_2A08(): pass

    label('loc_2A08')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2A0B(): pass

    label('loc_2A0B')

    If(
        (
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2A5C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2A44',
    )

    Sleep(20)

    @scena.Lambda('lambda_2A32')
    def lambda_2A32():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_2A32)

    Jump('loc_2A59')

    def _loc_2A44(): pass

    label('loc_2A44')

    @scena.Lambda('lambda_2A4A')
    def lambda_2A4A():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_2A4A)

    def _loc_2A59(): pass

    label('loc_2A59')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2A5C(): pass

    label('loc_2A5C')

    Sleep(300)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)
    OP_23(0x0090)
    WaitEffect(0x19, 0x00)
    Battle(0x0000039C, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2A90'),
        (-1, 'loc_2A93'),
    )

    def _loc_2A90(): pass

    label('loc_2A90')

    OP_B4(0x00)

    Return()

    def _loc_2A93(): pass

    label('loc_2A93')

    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x2AC0
@scena.Code('func_04_2AC0')
def func_04_2AC0():
    EventBegin(0x00)
    OP_72(0x0006, 0x0020)
    OP_71(0x0006, 0x0004)
    OP_6F(0x0006, 0)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 1000)
    OP_71(0x0000, 0x0020)
    OP_71(0x0001, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_70(0x0000, 1000)
    OP_70(0x0001, 1000)
    OP_70(0x0002, 1000)
    OP_70(0x0003, 1000)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0010, 29)
    ChrSetPos(0x0010, -710, 300, 15890, 180)
    ChrSetPos(0x0101, -760, 0, 12210, 7)
    ChrSetPos(0x0102, 530, 0, 12680, 344)
    ClearScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2BCB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2BB7',
    )

    ChrSetPos(0x0000, -2370, 0, 13570, 34)

    Jump('loc_2BC8')

    def _loc_2BB7(): pass

    label('loc_2BB7')

    ChrSetPos(0x0000, 1960, 0, 13940, 319)

    def _loc_2BC8(): pass

    label('loc_2BC8')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2BCB(): pass

    label('loc_2BCB')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C0F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2BFB',
    )

    ChrSetPos(0x0001, -2370, 0, 13570, 34)

    Jump('loc_2C0C')

    def _loc_2BFB(): pass

    label('loc_2BFB')

    ChrSetPos(0x0001, 1960, 0, 13940, 319)

    def _loc_2C0C(): pass

    label('loc_2C0C')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2C0F(): pass

    label('loc_2C0F')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2C3F',
    )

    ChrSetPos(0x0002, -2370, 0, 13570, 34)

    Jump('loc_2C50')

    def _loc_2C3F(): pass

    label('loc_2C3F')

    ChrSetPos(0x0002, 1960, 0, 13940, 319)

    def _loc_2C50(): pass

    label('loc_2C50')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2C53(): pass

    label('loc_2C53')

    If(
        (
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C97',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2C83',
    )

    ChrSetPos(0x0003, -2370, 0, 13570, 34)

    Jump('loc_2C94')

    def _loc_2C83(): pass

    label('loc_2C83')

    ChrSetPos(0x0003, 1960, 0, 13940, 319)

    def _loc_2C94(): pass

    label('loc_2C94')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2C97(): pass

    label('loc_2C97')

    CameraMove(-940, 40, 14760, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(326000, 0)
    OP_6E(262, 0)
    PlaySE(144, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\mp007_00.eff')
    PlayEffect(0x00, 0x01, 0x00FF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0010,
        (
            '#0130140264V#5P#118F真不愧是……\n',
            '卡西乌斯上校的孩子啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140265V不过……你们还是迟了一步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(92)

    @scena.Lambda('lambda_2D9B')
    def lambda_2D9B():
        CameraMove(200, 2560, 18960, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D9B)

    @scena.Lambda('lambda_2DB3')
    def lambda_2DB3():
        OP_67(0, 5560, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DB3)

    @scena.Lambda('lambda_2DCB')
    def lambda_2DCB():
        OP_6C(338000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DCB)

    @scena.Lambda('lambda_2DDB')
    def lambda_2DDB():
        OP_6E(455, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2DDB)

    Sleep(1000)

    PlaySE(184, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp007_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010140266V#580F糟糕……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140267V#513F#5P呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_72(0x0005, 0x0020)
    OP_6F(0x0005, 1100)
    OP_70(0x0005, 1500)
    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0002, 1850)
    OP_6F(0x0003, 1880)
    OP_6F(0x0001, 1910)
    OP_6F(0x0000, 1940)
    OP_70(0x0000, 2380)
    OP_70(0x0001, 2380)
    OP_70(0x0002, 2380)
    OP_70(0x0003, 2380)
    Sleep(4000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(133, 0x01, 0x64)

    @scena.Lambda('lambda_2EFD')
    def lambda_2EFD():
        OP_7C(0, 300, 3000, 3000)
        Yield()

        Jump('lambda_2EFD')

    DispatchAsync2(0x0010, 0x0001, lambda_2EFD)

    Sleep(2000)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F4D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070140268V#068F#5P呀啊啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F4D(): pass

    label('loc_2F4D')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F85',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140269V#550F#5P可恶，这是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F85(): pass

    label('loc_2F85')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FC1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040140270V#039F#5P这就是传说中的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FC1(): pass

    label('loc_2FC1')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3014',
    )

    ChrTalk(
        0x0105,
        (
            '#0060140271V#046F#5P是让戴尔蒙市长的古代遗物\n',
            '停止运作的光……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3014(): pass

    label('loc_3014')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3054',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140272V#077F#5P这是……『阴』的气息吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3054(): pass

    label('loc_3054')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_309B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030140273V#523F#5P这是……\n',
            '『导力停止现象』……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_309B(): pass

    label('loc_309B')

    @scena.Lambda('lambda_30A1')
    def lambda_30A1():
        CameraMove(-5080, 5590, -6070, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_30A1)

    @scena.Lambda('lambda_30B9')
    def lambda_30B9():
        OP_67(0, 4890, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_30B9)

    @scena.Lambda('lambda_30D1')
    def lambda_30D1():
        CameraSetDistance(4730, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_30D1)

    @scena.Lambda('lambda_30E1')
    def lambda_30E1():
        OP_6C(44000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_30E1)

    @scena.Lambda('lambda_30F1')
    def lambda_30F1():
        OP_6E(478, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_30F1)

    Sleep(1500)

    TerminateThread(0x0010, 0x01)
    PlaySE(145, 0x00, 0x64)
    LoadEffect(0x02, 'map\\\\mp015_00.eff')
    PlayEffect(0x02, 0xFF, 0x00FF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    PlayEffect(0x02, 0xFF, 0x00FF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0006, 0x0004)
    OP_6F(0x0006, 0)
    OP_70(0x0006, 240)
    Sleep(250)

    PlayEffect(0x02, 0xFF, 0x00FF, 1780, 1400, 19300, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    Sleep(250)

    PlayEffect(0x02, 0xFF, 0x00FF, 1780, 1400, 19300, 0, 0, 0, 2000, 1000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x322A
@scena.Code('func_05_322A')
def func_05_322A():
    ChrSetRGBAMask(0x00FE, 100, 100, 255, 255, 1000)

    @scena.Lambda('lambda_323B')
    def lambda_323B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_323B)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x00FE, 27)
    OP_99(0x00FE, 0x00, 0x07, 2000)

    Return()

# id: 0x0006 offset: 0x3261
@scena.Code('func_06_3261')
def func_06_3261():
    EventBegin(0x00)
    OP_72(0x0006, 0x0020)
    OP_6F(0x0006, 240)
    OP_72(0x0005, 0x0020)
    OP_71(0x0005, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0000, 2380)
    OP_6F(0x0001, 2380)
    OP_6F(0x0002, 2380)
    OP_6F(0x0003, 2380)
    ChrClearFlags(0x0010, 0x0080)

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0010, 29)
    ChrSetPos(0x0010, -710, 300, 15890, 180)
    ChrSetPos(0x0101, -760, 0, 12210, 7)
    ChrSetPos(0x0102, 530, 0, 12680, 344)
    ClearScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3338',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3324',
    )

    ChrSetPos(0x0000, -2370, 0, 13570, 34)

    Jump('loc_3335')

    def _loc_3324(): pass

    label('loc_3324')

    ChrSetPos(0x0000, 1960, 0, 13940, 319)

    def _loc_3335(): pass

    label('loc_3335')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_3338(): pass

    label('loc_3338')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_337C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3368',
    )

    ChrSetPos(0x0001, -2370, 0, 13570, 34)

    Jump('loc_3379')

    def _loc_3368(): pass

    label('loc_3368')

    ChrSetPos(0x0001, 1960, 0, 13940, 319)

    def _loc_3379(): pass

    label('loc_3379')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_337C(): pass

    label('loc_337C')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_33C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_33AC',
    )

    ChrSetPos(0x0002, -2370, 0, 13570, 34)

    Jump('loc_33BD')

    def _loc_33AC(): pass

    label('loc_33AC')

    ChrSetPos(0x0002, 1960, 0, 13940, 319)

    def _loc_33BD(): pass

    label('loc_33BD')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_33C0(): pass

    label('loc_33C0')

    If(
        (
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3404',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_33F0',
    )

    ChrSetPos(0x0003, -2370, 0, 13570, 34)

    Jump('loc_3401')

    def _loc_33F0(): pass

    label('loc_33F0')

    ChrSetPos(0x0003, 1960, 0, 13940, 319)

    def _loc_3401(): pass

    label('loc_3401')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_3404(): pass

    label('loc_3404')

    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 12)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3421',
    )

    ChrSetChipByIndex(0x0103, 14)

    def _loc_3421(): pass

    label('loc_3421')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3434',
    )

    ChrSetChipByIndex(0x0104, 16)

    def _loc_3434(): pass

    label('loc_3434')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3447',
    )

    ChrSetChipByIndex(0x0106, 20)

    def _loc_3447(): pass

    label('loc_3447')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_345A',
    )

    ChrSetChipByIndex(0x0105, 18)

    def _loc_345A(): pass

    label('loc_345A')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_346D',
    )

    ChrSetChipByIndex(0x0107, 22)

    def _loc_346D(): pass

    label('loc_346D')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3480',
    )

    ChrSetChipByIndex(0x0108, 24)

    def _loc_3480(): pass

    label('loc_3480')

    CameraMove(-710, 5300, 15670, 0)
    OP_67(0, 10500, -25720, 0)
    CameraSetDistance(640, 0)
    OP_6C(13000, 0)
    OP_6E(697, 0)
    FadeIn(2000, 0)
    CameraMove(-710, 300, 15670, 3000)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010140275V#580F怎、怎么了，刚才那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140276V#013F虽然表现为导力停止现象，\n',
            '但和以前的应该不一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140277V难道说，有什么东西被解封了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    Sleep(500)

    PlaySE(185, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)
    OP_73(0x0006)

    @scena.Lambda('lambda_35A1')
    def lambda_35A1():
        CameraMove(-560, 1650, 16460, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35A1)

    OP_72(0x0005, 0x0004)
    OP_6F(0x0005, 1300)
    OP_70(0x0005, 1000)
    Sleep(2000)

    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0003, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Sleep(1000)

    Fade(1000)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 1000)
    OP_70(0x0005, 0)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            '#2360140278V',
            (TxtCtl.SetColor, 0x5),
            '……警告……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2360140279V',
            (TxtCtl.SetColor, 0x5),
            '警告全体人员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010140280V#580F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140281V#014F#2P这个装置在说话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    FadeOut(300, 0, 100)
    TalkSetChrName('声音')

    Talk(
        (
            '#2360140282V',
            (TxtCtl.SetColor, 0x5),
            '『辉之环』封印结构的\n',
            '第一结界已确认失效。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2360140283V',
            (TxtCtl.SetColor, 0x5),
            '推测为在封印区域的最深处\n',
            '使用了『福音』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2360140284V',
            (TxtCtl.SetColor, 0x5),
            '『电子驱动塔』启动确认……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(500)

    PlayBGM(35)
    Sleep(500)

    @scena.Lambda('lambda_37D9')
    def lambda_37D9():
        CameraMove(2820, 0, 40, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_37D9)

    @scena.Lambda('lambda_37F1')
    def lambda_37F1():
        OP_67(0, 19430, -25720, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_37F1)

    @scena.Lambda('lambda_3809')
    def lambda_3809():
        CameraSetDistance(1410, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3809)

    @scena.Lambda('lambda_3819')
    def lambda_3819():
        OP_6C(90000, 11000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_3819)

    @scena.Lambda('lambda_3829')
    def lambda_3829():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_3829)

    @scena.Lambda('lambda_3837')
    def lambda_3837():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_3837)

    @scena.Lambda('lambda_3845')
    def lambda_3845():
        ChrSetDirection(0x00FE, 132, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_3845)

    @scena.Lambda('lambda_3853')
    def lambda_3853():
        ChrSetDirection(0x00FE, 222, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_3853)

    Sleep(3000)

    OP_6F(0x0000, 2380)
    OP_70(0x0000, 2850)
    OP_6F(0x0001, 2380)
    OP_70(0x0001, 2850)
    OP_6F(0x0002, 2380)
    OP_70(0x0002, 2850)
    OP_6F(0x0003, 2380)
    OP_70(0x0003, 2850)
    OP_73(0x0003)
    PlaySE(186, 0x00, 0x64)
    OP_6F(0x0000, 2851)
    OP_70(0x0000, 3240)
    OP_6F(0x0001, 2851)
    OP_70(0x0001, 3240)
    OP_6F(0x0002, 2851)
    OP_70(0x0002, 3240)
    OP_6F(0x0003, 2851)
    OP_70(0x0003, 3240)

    @scena.Lambda('lambda_38DE')
    def lambda_38DE():
        OP_67(0, 13510, -25720, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_38DE)

    OP_73(0x0003)
    PlaySE(154, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    Sleep(500)

    Fade(1000)
    OP_6F(0x0006, 240)
    OP_0D()
    Fade(1000)
    TerminateThread(0x0000, 0xFF)
    OP_72(0x0005, 0x0020)
    OP_6F(0x0005, 1100)
    OP_70(0x0005, 1400)
    CameraMove(-510, 300, 15530, 0)
    OP_67(0, 7800, -15530, 0)
    CameraSetDistance(1000, 0)
    OP_6C(357000, 0)
    OP_6E(697, 0)
    OP_66(0x0000)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010140285V#005F这、这是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140286V#012F第一结界……\n',
            '『辉之环』封印结构……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140287V上校，这到底是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140288V#5P#117F不……不知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140289V……我根本没有想到\n',
            '会演变成这种出乎意料的事态……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            '#2360140290V',
            (TxtCtl.SetColor, 0x5),
            '第一结界失效的同时，\n',
            '从『环』内释放出微量干扰波……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2360140291V',
            (TxtCtl.SetColor, 0x5),
            '『环之守护者』的封印解除确认……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2360140292V',
            (TxtCtl.SetColor, 0x5),
            '全体相关人员，\n',
            '请以最快的速度撤离封印区域……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    @scena.Lambda('lambda_3B4B')
    def lambda_3B4B():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_3B4B)

    @scena.Lambda('lambda_3B59')
    def lambda_3B59():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_3B59)

    @scena.Lambda('lambda_3B67')
    def lambda_3B67():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_3B67)

    @scena.Lambda('lambda_3B75')
    def lambda_3B75():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_3B75)

    @scena.Lambda('lambda_3B83')
    def lambda_3B83():
        CameraMove(21480, 4400, 50, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3B83)

    @scena.Lambda('lambda_3B9B')
    def lambda_3B9B():
        OP_6E(1000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3B9B)

    @scena.Lambda('lambda_3BAB')
    def lambda_3BAB():
        OP_67(300, 4890, 20, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3BAB)

    MapSetFlags(0x00000010)
    OP_11(0x00, 0x00, 0x00, 100, 255000, 0)
    Sleep(100)

    OP_12(0x00003A98, 0x00009C40, 0x00001770)
    Sleep(1900)

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x07,
        (
            (Expr.PushLong, 0x1388),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x0018, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x0017, 0x0004)
    ChrSetFlags(0x0018, 0x0004)
    ChrSetFlags(0x0019, 0x0004)
    OP_A1(0x0017, 0x0007)
    OP_A1(0x0018, 0x000A)
    OP_A1(0x0019, 0x000B)
    OP_72(0x0007, 0x0004)
    OP_71(0x0007, 0x0020)
    OP_6F(0x0007, 40)
    OP_70(0x0007, 59)
    ChrSetPos(0x0017, 49760, 0, 0, 90)
    ChrSetPos(0x0018, 36600, 3000, 4140, 90)
    ChrSetPos(0x0019, 36600, 3000, -4140, 90)
    PlaySE(187, 0x00, 0x64)
    OP_B0(0x0004, 0x50)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 1000)

    @scena.Lambda('lambda_3C9A')
    def lambda_3C9A():
        CameraSetDistance(210, 14000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3C9A)

    @scena.Lambda('lambda_3CAA')
    def lambda_3CAA():
        OP_6E(180, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3CAA)

    Sleep(7000)

    OP_20(0x00000BB8)

    @scena.Lambda('lambda_3CC4')
    def lambda_3CC4():
        ChrMoveTo(0x00FE, 11400, 4000, 3300, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0000, lambda_3CC4)

    @scena.Lambda('lambda_3CDF')
    def lambda_3CDF():
        ChrMoveTo(0x00FE, 11400, 4000, -3300, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0000, lambda_3CDF)

    Sleep(3000)

    OP_72(0x0007, 0x0020)
    OP_73(0x0007)
    PlayBGM(45)
    LoadEffect(0x05, 'map\\\\mp030_0.eff')
    Play3DEffect(0x05, 0x00, 0x07, 'Frame8_Bone__7_', 0x000003B6, 0x00000258, 0x000001F4, 0x0000, 0x0000, 0x0000, 0x000002BC, 0x000002BC, 0x000002BC, 0x00000000)
    Sleep(400)

    Play3DEffect(0x05, 0x01, 0x07, 'Frame8_Bone__7_', 0x0000041A, 0xFFFFFF9C, 0x000002BC, 0x0000, 0x0000, 0x0000, 0x00000258, 0x00000258, 0x00000258, 0x00000000)
    Sleep(100)

    Play3DEffect(0x05, 0x02, 0x07, 'Frame8_Bone__7_', 0x000003B6, 0x0000012C, 0x00000384, 0x0000, 0x0000, 0x0000, 0x000002BC, 0x000002BC, 0x000002BC, 0x00000000)
    Sleep(100)

    Play3DEffect(0x05, 0x03, 0x07, 'Frame8_Bone__7_', 0x0000047E, 0x000000C8, 0x000000FA, 0x0000, 0x0000, 0x0000, 0x00000384, 0x00000384, 0x00000384, 0x00000000)

    @scena.Lambda('lambda_3E03')
    def lambda_3E03():
        OP_67(300, -500, 20, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3E03)

    @scena.Lambda('lambda_3E1B')
    def lambda_3E1B():
        CameraMove(16980, 3210, 0, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3E1B)

    @scena.Lambda('lambda_3E33')
    def lambda_3E33():
        CameraSetDistance(700, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3E33)

    @scena.Lambda('lambda_3E43')
    def lambda_3E43():
        OP_6E(730, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3E43)

    Sleep(1000)

    CreateThread(0x0017, 0x03, 0x00, func_07_45C3)
    WaitForThreadExit(0x0018, 0x0000)

    @scena.Lambda('lambda_3E64')
    def lambda_3E64():
        ChrSetDirection(0x00FE, 45, 80)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_3E64)

    @scena.Lambda('lambda_3E72')
    def lambda_3E72():
        ChrMoveTo(0x00FE, 10000, 3000, 6800, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0000, lambda_3E72)

    WaitForThreadExit(0x0019, 0x0000)

    @scena.Lambda('lambda_3E92')
    def lambda_3E92():
        ChrSetDirection(0x00FE, 135, 80)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_3E92)

    @scena.Lambda('lambda_3EA0')
    def lambda_3EA0():
        ChrMoveTo(0x00FE, 10000, 3000, -6800, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0000, lambda_3EA0)

    OP_72(0x000A, 0x0004)
    OP_72(0x000B, 0x0004)
    WaitForThreadExit(0x0017, 0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0xFF)
    Fade(1500)
    OP_66(0x0001)
    ChrSetPos(0x0000, 3380, 0, 950, 90)
    ChrSetPos(0x0001, 3480, 0, -870, 90)
    ChrSetPos(0x0003, 1900, 0, 2270, 90)
    ChrSetPos(0x0002, 2520, 0, -2190, 90)
    MapClearFlags(0x00000010)
    CameraMove(9220, 1300, 140, 0)
    OP_67(0, 7430, -15660, 0)
    CameraSetDistance(1680, 0)
    OP_6C(90000, 0)
    OP_6E(433, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010140293V#509F什、什么呀，这个难看的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140294V#016F各位，请不要放松警惕……\n',
            '这家伙可是『环之守护者』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_401C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030140295V#023F哈哈……\n',
            '这不是在做梦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_401C(): pass

    label('loc_401C')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4065',
    )

    ChrTalk(
        0x0104,
        (
            '#0040140296V#032F这个也是古代文明的遗物吗……！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_4065(): pass

    label('loc_4065')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40AE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060140297V#042F竟然有这样的东西被封在里面……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_40AE(): pass

    label('loc_40AE')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40FD',
    )

    ChrTalk(
        0x0107,
        (
            '#0070140298V#065F难以置信……\n',
            '竟然有这么大的人形兵器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_40FD(): pass

    label('loc_40FD')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4140',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140299V#055F喂喂……要和它战斗吗！？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_4140(): pass

    label('loc_4140')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_418F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140300V#077F不要被迷惑了！\n',
            '这家伙……必定非同寻常！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_418F(): pass

    label('loc_418F')

    WaitForThreadExit(0x0000, 0x0000)
    OP_72(0x0007, 0x0020)
    OP_73(0x0007)

    @scena.Lambda('lambda_41A2')
    def lambda_41A2():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_41A2)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            '#2370140301V',
            (TxtCtl.SetColor, 0x2),
            '#15A门电路固定……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    Talk(
        (
            '#2370140302V',
            (TxtCtl.SetColor, 0x2),
            '#25A导力供给恢复……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(2700)

    Talk(
        (
            '#2370140303V',
            (TxtCtl.SetColor, 0x2),
            '#26A再启动完成……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(2500)

    Talk(
        (
            '#2370140304V',
            (TxtCtl.SetColor, 0x2),
            '#45AMODE：搜索入侵敌人……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(3000)

    OP_B0(0x0007, 0x08)
    OP_6F(0x0007, 230)
    OP_70(0x0007, 236)
    OP_73(0x0007)
    PlaySE(237, 0x00, 0x64)
    OP_B0(0x0007, 0x0F)
    OP_6F(0x0007, 237)
    OP_70(0x0007, 243)
    OP_73(0x0007)
    PlaySE(238, 0x00, 0x64)
    OP_7C(0, 300, 3000, 100)

    Talk(
        (
            '#2370140305V',
            (TxtCtl.SetColor, 0x2),
            '#15A坐标确认……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(300)

    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_B0(0x0007, 0x07)
    OP_6F(0x0007, 244)
    OP_70(0x0007, 249)
    OP_73(0x0007)
    PlaySE(237, 0x00, 0x64)
    OP_B0(0x0007, 0x0F)
    OP_6F(0x0007, 250)
    OP_70(0x0007, 254)
    OP_73(0x0007)
    PlaySE(238, 0x00, 0x64)
    OP_7C(0, 300, 3000, 100)
    Sleep(200)

    Talk(
        (
            '#2370140306V',
            (TxtCtl.SetColor, 0x2),
            '#30A封印结构设施·最深处……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    StopEffect(0x02, 0x02)
    StopEffect(0x03, 0x02)
    OP_B0(0x0007, 0x0F)
    OP_6F(0x0007, 254)
    OP_70(0x0007, 278)
    OP_73(0x0007)
    OP_7C(0, 300, 3000, 100)
    PlaySE(238, 0x00, 0x64)
    OP_B0(0x0007, 0x14)
    OP_6F(0x0007, 279)
    OP_70(0x0007, 288)
    OP_73(0x0007)
    OP_7C(0, 300, 3000, 100)
    PlaySE(238, 0x00, 0x64)
    OP_B0(0x0007, 0x0A)
    OP_6F(0x0007, 293)
    OP_70(0x0007, 307)
    OP_73(0x0007)
    OP_7C(0, 300, 3000, 100)
    PlaySE(238, 0x00, 0x64)
    OP_B0(0x0007, 0x0F)
    OP_6F(0x0007, 308)
    OP_70(0x0007, 315)
    OP_73(0x0007)
    OP_7C(0, 300, 3000, 100)
    PlaySE(238, 0x00, 0x64)

    Talk(
        (
            '#2370140307V',
            (TxtCtl.SetColor, 0x2),
            '#27A『环之守护者』幻想乐曲…',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_B0(0x0007, 0x0F)
    OP_6F(0x0007, 289)
    OP_70(0x0007, 292)
    OP_73(0x0007)
    OP_7C(0, 300, 3000, 100)
    PlaySE(238, 0x00, 0x64)
    OP_B0(0x0007, 0x0C)
    OP_6F(0x0007, 316)
    OP_70(0x0007, 324)
    OP_73(0x0007)
    OP_B0(0x0007, 0x09)
    OP_6F(0x0007, 325)
    OP_70(0x0007, 329)
    OP_73(0x0007)
    OP_B0(0x0007, 0x07)
    OP_6F(0x0007, 330)
    OP_70(0x0007, 332)
    OP_73(0x0007)
    OP_7C(0, 300, 3000, 100)
    PlaySE(238, 0x00, 0x64)
    Sleep(1500)

    Talk(
        (
            '#2370140308V',
            (TxtCtl.SetColor, 0x2),
            '#35A搜索入侵敌人，行动再次开始……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1800)

    Sleep(100)

    OP_7C(0, 200, 3000, 3000)
    Sleep(2000)

    OP_56(0x00)
    PlaySE(163, 0x00, 0x64)
    PlaySE(236, 0x00, 0x5A)
    OP_B0(0x0007, 0x0F)
    OP_6F(0x0007, 333)
    OP_70(0x0007, 382)
    ChrSetFlags(0x0017, 0x0004)

    @scena.Lambda('lambda_4540')
    def lambda_4540():
        ChrMoveToRelativeAsync(0x0017, -12000, -6000, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_4540)

    @scena.Lambda('lambda_455B')
    def lambda_455B():
        CameraMove(8900, 5600, 110, 500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_455B)

    @scena.Lambda('lambda_4573')
    def lambda_4573():
        CameraSetDistance(1380, 500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4573)

    @scena.Lambda('lambda_4583')
    def lambda_4583():
        OP_67(0, -130, -18290, 500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4583)

    Sleep(500)

    TerminateThread(0x0017, 0xFF)
    OP_72(0x0007, 0x0008)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(72, 320, 56, 3)
    Battle(0x000003A1, 0x00100009, 0x00, 0x0000, 0xFF)

    Return()

# id: 0x0007 offset: 0x45C3
@scena.Code('func_07_45C3')
def func_07_45C3():
    OP_B0(0x0007, 0x0B)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_45D1(): pass

    label('loc_45D1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_46F1',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_45EE')
    def lambda_45EE():
        ChrMoveTo(0x00FE, 16100, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_45EE)

    OP_B0(0x0007, 0x0A)
    OP_6F(0x0007, 141)
    OP_70(0x0007, 146)
    OP_73(0x0007)

    @scena.Lambda('lambda_461E')
    def lambda_461E():
        ChrMoveTo(0x00FE, 16100, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_461E)

    OP_B0(0x0007, 0x0F)
    OP_6F(0x0007, 147)
    OP_70(0x0007, 150)
    OP_73(0x0007)
    PlaySE(236, 0x00, 0x64)
    OP_7C(0, 300, 3000, 100)
    OP_4A(0x0017, 0)
    Sleep(100)

    OP_4B(0x0017, 0)

    @scena.Lambda('lambda_4671')
    def lambda_4671():
        ChrMoveTo(0x00FE, 16100, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_4671)

    OP_B0(0x0007, 0x0A)
    OP_6F(0x0007, 151)
    OP_70(0x0007, 156)
    OP_73(0x0007)

    @scena.Lambda('lambda_46A1')
    def lambda_46A1():
        ChrMoveTo(0x00FE, 16100, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_46A1)

    OP_B0(0x0007, 0x0F)
    OP_6F(0x0007, 157)
    OP_70(0x0007, 159)
    OP_73(0x0007)
    PlaySE(236, 0x00, 0x64)
    OP_7C(0, 300, 3000, 100)
    OP_4A(0x0017, 0)
    Sleep(100)

    OP_4B(0x0017, 0)

    Jump('loc_45D1')

    def _loc_46F1(): pass

    label('loc_46F1')

    OP_73(0x0007)
    OP_6F(0x0007, 180)
    OP_70(0x0007, 209)
    Sleep(1000)

    PlaySE(236, 0x00, 0x64)
    OP_73(0x0007)
    OP_71(0x0007, 0x0020)
    OP_6F(0x0007, 40)
    OP_70(0x0007, 59)
    OP_B0(0x0007, 0x0F)

    Return()

# id: 0x0008 offset: 0x4727
@scena.Code('func_08_4727')
def func_08_4727():
    EventBegin(0x00)
    OP_72(0x0006, 0x0020)
    OP_6F(0x0006, 240)
    OP_72(0x0005, 0x0020)
    OP_71(0x0005, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0000, 3260)
    OP_6F(0x0001, 3260)
    OP_6F(0x0002, 3260)
    OP_6F(0x0003, 3260)

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x07,
        (
            (Expr.PushLong, 0x1388),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A1(0x0017, 0x0008)
    OP_72(0x0008, 0x0004)
    OP_6F(0x0008, 20)
    CameraMove(-200, 7250, -130, 0)
    OP_67(0, 2930, -10000, 0)
    CameraSetDistance(2380, 0)
    OP_6C(134000, 0)
    OP_6E(434, 0)
    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 12)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_47F6',
    )

    ChrSetChipByIndex(0x0103, 14)

    def _loc_47F6(): pass

    label('loc_47F6')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4809',
    )

    ChrSetChipByIndex(0x0104, 16)

    def _loc_4809(): pass

    label('loc_4809')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_481C',
    )

    ChrSetChipByIndex(0x0106, 20)

    def _loc_481C(): pass

    label('loc_481C')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_482F',
    )

    ChrSetChipByIndex(0x0105, 18)

    def _loc_482F(): pass

    label('loc_482F')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4842',
    )

    ChrSetChipByIndex(0x0107, 22)

    def _loc_4842(): pass

    label('loc_4842')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4855',
    )

    ChrSetChipByIndex(0x0108, 24)

    def _loc_4855(): pass

    label('loc_4855')

    ChrSetPos(0x0017, 5900, 0, -30, 90)
    ChrSetPos(0x0000, -6050, 0, -660, 90)
    ChrSetPos(0x0001, -6050, 0, 660, 90)
    ChrSetPos(0x0002, -4270, 0, -2020, 90)
    ChrSetPos(0x0003, -4270, 0, 2020, 90)
    OP_6F(0x0008, 22)
    OP_70(0x0008, 41)
    OP_71(0x0008, 0x0020)
    FadeIn(1000, 0)
    CameraMove(-200, 2250, -130, 3000)

    ChrTalk(
        0x0101,
        (
            '#0010140309V#580F为、为什么打不倒它！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020140310V#016F它还打算继续吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    Sleep(200)

    Fade(1000)

    @scena.Lambda('lambda_495C')
    def lambda_495C():
        OP_6C(90000, 11000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_495C)

    CameraMove(5470, 1000, -180, 0)
    OP_67(0, 8560, -10000, 0)
    CameraSetDistance(1940, 0)
    OP_6C(134000, 0)
    OP_6E(434, 0)
    OP_72(0x0008, 0x0020)
    OP_6F(0x0008, 42)
    OP_70(0x0008, 64)
    OP_21()
    PlayBGM(46)
    OP_73(0x0008)
    PlaySE(239, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    OP_6F(0x0008, 65)
    OP_70(0x0008, 80)
    Sleep(500)

    @scena.Lambda('lambda_49EB')
    def lambda_49EB():
        CameraMove(5470, 3000, -180, 5500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_49EB)

    @scena.Lambda('lambda_4A03')
    def lambda_4A03():
        CameraSetDistance(3390, 600)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4A03)

    OP_73(0x0008)
    OP_6F(0x0008, 81)
    OP_70(0x0008, 107)
    OP_7C(0, 500, 3000, 100)
    OP_73(0x0008)
    PlaySE(240, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    OP_6F(0x0008, 108)
    OP_70(0x0008, 110)
    OP_73(0x0008)
    OP_7C(0, 500, 3000, 100)

    @scena.Lambda('lambda_4A70')
    def lambda_4A70():
        CameraSetDistance(1870, 3500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4A70)

    OP_6F(0x0008, 112)
    OP_70(0x0008, 151)
    OP_73(0x0008)
    OP_7C(0, 600, 3000, 100)
    TerminateThread(0x0000, 0x03)

    @scena.Lambda('lambda_4AA6')
    def lambda_4AA6():
        OP_67(0, 160, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_4AA6)

    PlaySE(241, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0008, 152)
    OP_70(0x0008, 174)
    OP_73(0x0008)
    PlaySE(241, 0x00, 0x64)
    OP_7C(0, 300, 3000, 100)

    @scena.Lambda('lambda_4AF3')
    def lambda_4AF3():
        CameraSetDistance(1870, 2600)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4AF3)

    OP_6F(0x0008, 175)
    OP_70(0x0008, 206)
    OP_73(0x0008)
    PlaySE(242, 0x00, 0x64)

    @scena.Lambda('lambda_4B19')
    def lambda_4B19():
        OP_6E(651, 300)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4B19)

    @scena.Lambda('lambda_4B29')
    def lambda_4B29():
        CameraSetDistance(3200, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4B29)

    OP_7C(0, 300, 3000, 100)
    OP_6F(0x0008, 207)
    OP_70(0x0008, 250)
    Sleep(300)

    @scena.Lambda('lambda_4B5D')
    def lambda_4B5D():
        OP_6E(409, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4B5D)

    OP_73(0x0008)
    OP_71(0x0008, 0x0020)
    OP_6F(0x0008, 251)
    OP_70(0x0008, 270)
    WaitForThreadExit(0x0000, 0x0003)
    WaitForThreadExit(0x0000, 0x0002)
    TerminateThread(0x0000, 0xFF)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            '#2370140311V',
            (TxtCtl.SetColor, 0x2),
            '#35AMODE：彻底歼灭……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 300, 3000, 100)
    Sleep(2000)

    Sleep(1000)

    Talk(
        (
            '#2370140312V',
            (TxtCtl.SetColor, 0x2),
            '#35A『环之守护者』幻想乐曲…',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 300, 3000, 100)
    Sleep(1500)

    OP_B0(0x0007, 0x0C)
    OP_6F(0x0007, 316)
    OP_70(0x0007, 324)
    OP_73(0x0007)
    OP_B0(0x0007, 0x09)
    OP_6F(0x0007, 325)
    OP_70(0x0007, 329)
    OP_73(0x0007)
    OP_B0(0x0007, 0x07)
    OP_6F(0x0007, 330)
    OP_70(0x0007, 332)
    OP_73(0x0007)
    OP_7C(0, 300, 3000, 100)

    Talk(
        (
            '#2370140313V',
            (TxtCtl.SetColor, 0x2),
            '#36A现在再次展开歼灭行动……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1300)

    OP_7C(0, 200, 3000, 3000)
    Sleep(2000)

    OP_56(0x00)
    OP_72(0x0008, 0x0020)
    OP_73(0x0008)

    @scena.Lambda('lambda_4CDA')
    def lambda_4CDA():
        OP_67(0, 4190, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4CDA)

    @scena.Lambda('lambda_4CF2')
    def lambda_4CF2():
        CameraSetDistance(2400, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4CF2)

    OP_6F(0x0008, 320)
    OP_70(0x0008, 334)
    OP_73(0x0008)
    LoadEffect(0x04, 'map\\\\mp021_04.eff')
    PlayEffect(0x04, 0xFF, 0x00FF, 5470, 3000, -180, 0, 90, 0, 7000, 7000, 7000, 0x00FF, 0, 0, 0, 0)
    PlaySE(243, 0x00, 0x64)

    @scena.Lambda('lambda_4D61')
    def lambda_4D61():
        CameraSetDistance(6000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4D61)

    OP_7C(0, 500, 3000, 3000)
    OP_6F(0x0008, 336)
    OP_70(0x0008, 345)
    Sleep(1000)

    TerminateThread(0x0000, 0xFF)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x000003A2, 0x00100008, 0x00, 0x0080, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_4DB5'),
        (-1, 'loc_4DB8'),
    )

    def _loc_4DB5(): pass

    label('loc_4DB5')

    OP_B4(0x00)

    Return()

    def _loc_4DB8(): pass

    label('loc_4DB8')

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0x4),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_4DC7',
    )

    WaitEffect(0x19, 0x01)

    def _loc_4DC7(): pass

    label('loc_4DC7')

    OP_71(0x0008, 0x0004)
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0x4DD1
@scena.Code('func_09_4DD1')
def func_09_4DD1():
    EventBegin(0x00)
    FadeIn(2000, 0)
    OP_72(0x0006, 0x0020)
    OP_6F(0x0006, 240)
    OP_72(0x0005, 0x0020)
    OP_71(0x0005, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0000, 3260)
    OP_6F(0x0001, 3260)
    OP_6F(0x0002, 3260)
    OP_6F(0x0003, 3260)
    RemoveItem(0x0357, 1)

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x07,
        (
            (Expr.PushLong, 0x1388),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A1(0x0017, 0x0009)
    OP_72(0x0009, 0x0004)
    OP_6F(0x0009, 275)
    CameraMove(1640, 0, -1300, 0)
    OP_67(0, 6640, -10000, 0)
    CameraSetDistance(2960, 0)
    OP_6C(111000, 0)
    OP_6E(418, 0)
    ChrSetPos(0x0017, 5900, 0, -30, 75)
    ChrSetPos(0x0010, -4780, 0, 6090, 137)
    ChrSetFlags(0x0010, 0x0080)

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0010, 29)
    FormationDelMember(0x00, 0xFF)
    FormationDelMember(0x01, 0xFF)
    FormationAddMember(0x00, 0xFF)
    FormationAddMember(0x01, 0xFF)
    ChrSetPos(0x0101, -2910, 0, -3850, 47)
    ChrSetPos(0x0102, -1740, 0, -6390, 6)
    ChrSetPos(0x0000, -4710, 0, 610, 127)
    ChrSetPos(0x0001, -5270, 0, -1970, 111)
    ChrSetChipByIndex(0x0101, 37)
    ChrSetChipByIndex(0x0102, 38)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F35',
    )

    ChrSetChipByIndex(0x0103, 39)

    def _loc_4F35(): pass

    label('loc_4F35')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F48',
    )

    ChrSetChipByIndex(0x0104, 40)

    def _loc_4F48(): pass

    label('loc_4F48')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F5B',
    )

    ChrSetChipByIndex(0x0106, 42)

    def _loc_4F5B(): pass

    label('loc_4F5B')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F6E',
    )

    ChrSetChipByIndex(0x0105, 41)

    def _loc_4F6E(): pass

    label('loc_4F6E')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F81',
    )

    ChrSetChipByIndex(0x0107, 43)

    def _loc_4F81(): pass

    label('loc_4F81')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F94',
    )

    ChrSetChipByIndex(0x0108, 44)

    def _loc_4F94(): pass

    label('loc_4F94')

    ChrSetSubChip(0x0000, 3)
    ChrSetSubChip(0x0001, 3)
    ChrSetSubChip(0x0002, 3)
    ChrSetSubChip(0x0003, 3)
    LoadEffect(0x00, 'monster\\\\ms10000.eff')
    LoadEffect(0x01, 'monster\\\\ms10001.eff')
    LoadEffect(0x02, 'monster\\\\ms10002.eff')
    LoadEffect(0x03, 'monster\\msc0270b.eff')

    @scena.Lambda('lambda_500A')
    def lambda_500A():
        CameraSetDistance(2530, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_500A)

    @scena.Lambda('lambda_501A')
    def lambda_501A():
        OP_6C(69000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_501A)

    Sleep(4000)

    ChrTalk(
        0x0101,
        (
            '#0010140314V#581F呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140315V总算、总算打倒了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140316V#013F嗯……\n',
            '好像已经不能动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0010, 0x0080)
    ChrSetChipByIndex(0x0010, 36)
    ChrSetSubChip(0x0010, 0)
    OP_66(0x0000)
    CameraMove(-880, 0, 620, 2000)

    ChrTalk(
        0x0010,
        (
            '#0130140317V#5P#112F『环之守护者』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140318V这家伙本来的使命应该是为了\n',
            '将意图封印『辉之环』的设施破坏掉……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140319V然而在『辉之环』成功被封印的同时，\n',
            '它也在刚才的门里停止了机能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140320V#115F难道说……围绕着这个『辉之环』，\n',
            '古代人曾有那么一段互相对立的历史？\n',
            '还是另有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140321V#116F可是……\n',
            '关键的『辉之环』在哪里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_B0(0x0009, 0x03)
    OP_6F(0x0009, 275)
    OP_70(0x0009, 280)
    Sleep(1000)

    OP_62(0x0000, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0003, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0002, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0001, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_21()
    OP_73(0x0009)
    OP_B0(0x0009, 0x0C)
    OP_6F(0x0009, 281)
    OP_70(0x0009, 285)
    OP_73(0x0009)
    PlayBGM(45)
    OP_B0(0x0009, 0x14)
    OP_6F(0x0009, 286)
    OP_70(0x0009, 295)
    OP_73(0x0009)
    OP_B0(0x0009, 0x0F)
    OP_7C(0, 300, 3000, 100)
    PlaySE(236, 0x00, 0x64)

    ChrTalk(
        0x0010,
        (
            '#0130140322V#113F#5P#26A怎么……\n',
            '它还能动吗！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1200)

    OP_72(0x0009, 0x0020)
    Sleep(100)

    OP_7C(0, 100, 3000, 6000)
    Sleep(900)

    @scena.Lambda('lambda_5368')
    def lambda_5368():
        CameraMove(1630, 550, -840, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5368)

    CreateThread(0x0017, 0x01, 0x00, func_0A_9DBE)
    Sleep(500)

    WaitForThreadExit(0x0017, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_53D2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030140323V#522F#5P呜……\n',
            '身体动弹不了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_553E')

    def _loc_53D2(): pass

    label('loc_53D2')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5423',
    )

    ChrTalk(
        0x0104,
        (
            '#0040140324V#034F#5P竟、竟然让本人完全不能动弹……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_553E')

    def _loc_5423(): pass

    label('loc_5423')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_546E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140325V#550F#5P可恶……\n',
            '身体完全不听使唤！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_553E')

    def _loc_546E(): pass

    label('loc_546E')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_54B6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070140326V#069F#5P啊，我已经站不起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_553E')

    def _loc_54B6(): pass

    label('loc_54B6')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_54FA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140327V#077F#5P呜……还是不行吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_553E')

    def _loc_54FA(): pass

    label('loc_54FA')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_553E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060140328V#541F#5P已经……动不了了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_553E(): pass

    label('loc_553E')

    ChrTalk(
        0x0101,
        (
            '#0010140329V#581F#5P约、约修亚……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_66(0x0001)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020140330V#016F#2P艾丝蒂尔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_559E')
    def lambda_559E():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_559E')

    DispatchAsync2(0x0102, 0x0002, lambda_559E)

    ChrSetChipByIndex(0x0102, 12)
    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x0102, -1510, 0, -3240, 500, 4000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_72(0x0009, 0x0020)
    OP_73(0x0009)
    OP_B0(0x0009, 0x06)
    OP_6F(0x0009, 210)
    OP_70(0x0009, 213)

    @scena.Lambda('lambda_55F3')
    def lambda_55F3():
        OP_6C(70000, 1700)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_55F3)

    @scena.Lambda('lambda_5603')
    def lambda_5603():
        OP_67(0, -1770, -30160, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_5603)

    @scena.Lambda('lambda_561B')
    def lambda_561B():
        CameraMove(2730, 3000, -2190, 1700)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_561B)

    @scena.Lambda('lambda_5633')
    def lambda_5633():
        CameraSetDistance(770, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_5633)

    OP_73(0x0009)
    OP_B0(0x0009, 0x06)
    OP_6F(0x0009, 214)
    OP_70(0x0009, 221)
    OP_73(0x0009)
    WaitForThreadExit(0x0000, 0x0001)
    ChrSetPos(0x001A, 1980, 5000, 1220, 0)
    PlayEffect(0x03, 0xFF, 0x0010, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)
    Sleep(100)

    OP_7C(0, 200, 3000, 1000)
    OP_B0(0x0009, 0x0D)
    OP_73(0x0009)
    OP_6F(0x0009, 222)
    OP_70(0x0009, 226)
    OP_73(0x0009)

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0010, 28)
    ChrSetPos(0x0010, -440, 0, 4310, 119)
    ChrSetPos(0x001B, -440, 0, 4310, 119)
    ChrSetPos(0x001C, -440, 0, 4310, 119)
    ChrSetPos(0x001D, -440, 0, 4310, 119)
    ChrSetPos(0x001E, -440, 0, 4310, 119)

    @scena.Lambda('lambda_5739')
    def lambda_5739():
        CameraMove(1680, 1900, 600, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_5739)

    @scena.Lambda('lambda_5751')
    def lambda_5751():
        OP_67(0, 12070, -30160, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5751)

    @scena.Lambda('lambda_5769')
    def lambda_5769():
        CameraSetDistance(740, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_5769)

    @scena.Lambda('lambda_5779')
    def lambda_5779():
        OP_6C(18000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_5779)

    @scena.Lambda('lambda_5789')
    def lambda_5789():
        OP_6E(512, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_5789)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_7C(0, 600, 3000, 100)

    @scena.Lambda('lambda_57B3')
    def lambda_57B3():
        ChrSetDirection(0x00FE, 120, 50)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_57B3)

    ChrSetDirection(0x0017, 110, 0)
    OP_B0(0x0009, 0x0D)
    OP_6F(0x0009, 227)
    OP_70(0x0009, 259)
    OP_73(0x0009)
    OP_71(0x0009, 0x0020)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 50)
    OP_70(0x0009, 69)
    WaitForThreadExit(0x0000, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010140331V#5P#004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140332V#5P#114F……休想得逞！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140333V#014F#5P上、上校……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140334V#5P#112F这家伙由我来对付！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140335V你们赶快离开这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140336V#580F#5P可、可是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140337V#5P#114F你们刚才已经和这家伙拼死战斗过了！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140338V所以，我也应该做些什么了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140339V或多或少可以拖延一些时间！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x001B, 0x0004)
    ChrSetFlags(0x001C, 0x0004)
    ChrSetFlags(0x001D, 0x0004)
    ChrSetFlags(0x001E, 0x0004)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetRGBAMask(0x001B, 255, 255, 255, 200, 0)
    ChrSetRGBAMask(0x001C, 255, 255, 255, 150, 0)
    ChrSetRGBAMask(0x001D, 255, 255, 255, 100, 0)
    ChrSetRGBAMask(0x001E, 255, 255, 255, 50, 0)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrSetFlags(0x001B, 0x0040)
    ChrSetFlags(0x001C, 0x0040)
    ChrSetFlags(0x001D, 0x0040)
    ChrSetFlags(0x001E, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetChipByIndex(0x0010, 8)
    ChrSetChipByIndex(0x001B, 8)
    ChrSetChipByIndex(0x001C, 8)
    ChrSetChipByIndex(0x001D, 8)
    ChrSetChipByIndex(0x001E, 8)

    @scena.Lambda('lambda_59F9')
    def lambda_59F9():
        ChrWalkTo(0x00FE, 3510, 0, 1230, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_59F9)

    Sleep(50)

    @scena.Lambda('lambda_5A19')
    def lambda_5A19():
        ChrWalkTo(0x00FE, 3510, 0, 1230, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0000, lambda_5A19)

    Sleep(50)

    @scena.Lambda('lambda_5A39')
    def lambda_5A39():
        ChrWalkTo(0x00FE, 3510, 0, 1230, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0000, lambda_5A39)

    Sleep(50)

    @scena.Lambda('lambda_5A59')
    def lambda_5A59():
        ChrWalkTo(0x00FE, 3510, 0, 1230, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0000, lambda_5A59)

    Sleep(50)

    @scena.Lambda('lambda_5A79')
    def lambda_5A79():
        ChrWalkTo(0x00FE, 3510, 0, 1230, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0000, lambda_5A79)

    WaitForThreadExit(0x0010, 0x0000)
    Fade(1000)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CameraMove(6200, 3370, 160, 0)
    OP_67(0, 12070, -30160, 0)
    CameraSetDistance(850, 0)
    OP_6C(152000, 0)
    OP_6E(512, 0)

    @scena.Lambda('lambda_5B15')
    def lambda_5B15():
        CameraMove(5750, 2370, -170, 15000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_5B15)

    @scena.Lambda('lambda_5B2D')
    def lambda_5B2D():
        OP_67(0, 4050, -30160, 15000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5B2D)

    @scena.Lambda('lambda_5B45')
    def lambda_5B45():
        CameraSetDistance(970, 15000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_5B45)

    @scena.Lambda('lambda_5B55')
    def lambda_5B55():
        OP_6C(97000, 15000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_5B55)

    @scena.Lambda('lambda_5B65')
    def lambda_5B65():
        OP_6E(561, 15000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_5B65)

    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x0010, 0xFF)
    ChrSetChipByIndex(0x001B, 8)
    ChrSetChipByIndex(0x001C, 8)
    ChrSetChipByIndex(0x001D, 8)
    ChrSetChipByIndex(0x001E, 8)
    ChrSetChipByIndex(0x0010, 8)
    ChrSetPos(0x001B, 5370, 0, 710, 139)
    ChrSetPos(0x001C, 5370, 0, 710, 139)
    ChrSetPos(0x001D, 5370, 0, 710, 139)
    ChrSetPos(0x001E, 5370, 0, 710, 139)
    ChrSetPos(0x0010, 5370, 0, 710, 139)
    OP_72(0x0009, 0x0020)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 126)
    CreateThread(0x0010, 0x00, 0x00, func_0B_9ECE)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, func_0B_9ECE)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, func_0B_9ECE)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, func_0B_9ECE)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, func_0B_9ECE)
    WaitForThreadExit(0x0010, 0x0000)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_B0(0x0009, 0x1E)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 126)
    CreateThread(0x0010, 0x00, 0x00, func_0C_9F1B)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, func_0C_9F1B)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, func_0C_9F1B)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, func_0C_9F1B)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, func_0C_9F1B)
    WaitForThreadExit(0x0010, 0x0000)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_B0(0x0009, 0x1E)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 126)
    CreateThread(0x0010, 0x00, 0x00, func_0D_9F67)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, func_0D_9F67)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, func_0D_9F67)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, func_0D_9F67)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, func_0D_9F67)
    WaitForThreadExit(0x0010, 0x0000)
    OP_73(0x0009)
    OP_B0(0x0009, 0x0F)
    OP_73(0x0009)
    OP_6F(0x0009, 510)
    OP_70(0x0009, 530)
    CreateThread(0x0010, 0x00, 0x00, func_0E_9F8F)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, func_0E_9F8F)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, func_0E_9F8F)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, func_0E_9F8F)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, func_0E_9F8F)
    Sleep(600)

    PlaySE(237, 0x00, 0x64)
    OP_73(0x0009)
    PlaySE(85, 0x00, 0x64)
    OP_7C(0, 1000, 3000, 100)
    CreateThread(0x0010, 0x00, 0x00, func_0F_9FF9)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, func_0F_9FF9)
    Sleep(50)

    OP_7C(0, 200, 3000, 3000)
    CreateThread(0x001C, 0x00, 0x00, func_0F_9FF9)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, func_0F_9FF9)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, func_0F_9FF9)
    WaitForThreadExit(0x0010, 0x0000)
    OP_7C(0, 1, 3000, 10)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 3900, 3300, 1120, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0009, 227)
    OP_70(0x0009, 254)
    CreateThread(0x0010, 0x00, 0x00, func_10_A02B)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, func_10_A02B)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, func_10_A02B)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, func_10_A02B)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, func_10_A02B)
    WaitForThreadExit(0x0010, 0x0000)
    OP_73(0x0009)
    CreateThread(0x0010, 0x00, 0x00, func_11_A053)
    Sleep(430)

    OP_B0(0x0009, 0x32)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 115)
    Sleep(200)

    OP_B0(0x0009, 0x32)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 115)
    Sleep(200)

    OP_B0(0x0009, 0x50)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 126)
    OP_73(0x0009)
    OP_B0(0x0009, 0x0F)
    OP_73(0x0009)
    OP_6F(0x0009, 510)
    OP_70(0x0009, 531)
    Sleep(200)

    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)

    @scena.Lambda('lambda_5F2E')
    def lambda_5F2E():
        ChrSetDirection(0x00FE, 46, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5F2E)

    Sleep(650)

    PlaySE(237, 0x00, 0x64)
    OP_73(0x0009)
    OP_6F(0x0009, 227)
    OP_70(0x0009, 254)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_5F5C')
    def lambda_5F5C():
        ChrMoveTo(0x00FE, 740, 0, 1920, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5F5C)

    ChrSetSubChip(0x0010, 7)
    Sleep(200)

    @scena.Lambda('lambda_5F81')
    def lambda_5F81():
        ChrMoveTo(0x00FE, 740, 0, 1920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5F81)

    Sleep(200)

    @scena.Lambda('lambda_5FA1')
    def lambda_5FA1():
        ChrMoveTo(0x00FE, 740, 0, 1920, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5FA1)

    Sleep(200)

    @scena.Lambda('lambda_5FC1')
    def lambda_5FC1():
        ChrMoveTo(0x00FE, 740, 0, 1920, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5FC1)

    @scena.Lambda('lambda_5FDC')
    def lambda_5FDC():
        OP_99(0x00FE, 0x07, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_5FDC)

    Sleep(500)

    CreateThread(0x0010, 0x00, 0x00, func_12_A130)
    Sleep(50)

    ChrClearFlags(0x001B, 0x0080)
    CreateThread(0x001B, 0x00, 0x00, func_12_A130)
    Sleep(50)

    ChrClearFlags(0x001C, 0x0080)
    CreateThread(0x001C, 0x00, 0x00, func_12_A130)
    Sleep(50)

    ChrClearFlags(0x001D, 0x0080)
    CreateThread(0x001D, 0x00, 0x00, func_12_A130)
    Sleep(50)

    ChrClearFlags(0x001E, 0x0080)
    CreateThread(0x001E, 0x00, 0x00, func_12_A130)
    Sleep(350)

    OP_B0(0x0009, 0x1E)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 112)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 4890, 1500, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(150)

    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 4890, 2500, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_73(0x0009)
    OP_B0(0x0009, 0x1E)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 112)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 4890, 2800, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(150)

    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 4890, 3300, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_73(0x0009)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 126)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 4890, 2800, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(150)

    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 4890, 2500, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_73(0x0009)
    OP_71(0x0009, 0x0020)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 50)
    OP_70(0x0009, 69)

    ChrTalk(
        0x0101,
        (
            '#0010140340V#004F#2P好、好厉害……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140341V#012F#2P不愧是继承了父亲的剑术……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrTurnDirection(0x0010, 0x0101, 800)

    ChrTalk(
        0x0010,
        (
            '#0130140342V#5P#114F还在那做什么！\n',
            '快走！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0009, 0x0020)

    @scena.Lambda('lambda_62B4')
    def lambda_62B4():
        CameraSetDistance(640, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_62B4)

    @scena.Lambda('lambda_62C4')
    def lambda_62C4():
        OP_6C(139000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_62C4)

    @scena.Lambda('lambda_62D4')
    def lambda_62D4():
        CameraMove(390, 0, 1360, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_62D4)

    @scena.Lambda('lambda_62EC')
    def lambda_62EC():
        OP_6E(561, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_62EC)

    @scena.Lambda('lambda_62FC')
    def lambda_62FC():
        OP_67(0, 16200, -30160, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_62FC)

    @scena.Lambda('lambda_6314')
    def lambda_6314():
        ChrSetDirection(0x00FE, 90, 100)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_6314)

    OP_B0(0x0009, 0x32)
    OP_6F(0x0009, 489)
    OP_70(0x0009, 444)
    OP_73(0x0009)
    OP_B0(0x0009, 0x1E)
    OP_6F(0x0009, 443)
    OP_70(0x0009, 421)
    Sleep(60)

    ChrJumpTo(0x0010, -80, 0, 2370, 500, 6000)
    ChrSetDirection(0x0010, 14, 800)
    OP_73(0x0009)
    PlaySE(85, 0x00, 0x50)
    OP_7C(0, 600, 3000, 100)
    WaitForThreadExit(0x0010, 0x0001)
    Sleep(100)

    ChrSetChipByIndex(0x0010, 33)
    PlaySE(504, 0x00, 0x64)
    OP_99(0x0010, 0x00, 0x01, 2000)

    @scena.Lambda('lambda_63A2')
    def lambda_63A2():
        CameraMove(0, 2800, -50, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_63A2)

    @scena.Lambda('lambda_63BA')
    def lambda_63BA():
        OP_67(0, 15760, -30160, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_63BA)

    @scena.Lambda('lambda_63D2')
    def lambda_63D2():
        OP_6C(130000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_63D2)

    OP_9E(0x0010, 80, 0, 250, 30000)
    LoadEffect(0x00, 'map\\\\mp009_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 100, 1000, 3150, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_6443')
    def lambda_6443():
        OP_99(0x00FE, 0x02, 0x05, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6443)

    OP_B0(0x0009, 0x96)
    OP_6F(0x0009, 421)
    OP_70(0x0009, 443)
    CreateThread(0x0020, 0x00, 0x00, func_13_A1F1)
    Sleep(20)

    CreateThread(0x001B, 0x00, 0x00, func_13_A1F1)
    Sleep(20)

    OP_7C(0, 100, 3000, 5000)
    CreateThread(0x001C, 0x00, 0x00, func_13_A1F1)
    Sleep(20)

    CreateThread(0x001D, 0x00, 0x00, func_13_A1F1)
    Sleep(20)

    CreateThread(0x001E, 0x00, 0x00, func_13_A1F1)
    OP_73(0x0009)
    OP_B0(0x0009, 0x1E)
    OP_6F(0x0009, 444)
    OP_70(0x0009, 489)
    Sleep(400)

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_64DE')
    def lambda_64DE():
        ChrMoveTo(0x00FE, 830, 0, 1290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_64DE)

    @scena.Lambda('lambda_64F9')
    def lambda_64F9():
        OP_99(0x00FE, 0x06, 0x0B, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_64F9)

    @scena.Lambda('lambda_6509')
    def lambda_6509():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_6509')

    DispatchAsync2(0x0010, 0x0002, lambda_6509)

    Sleep(1300)

    Sleep(100)

    @scena.Lambda('lambda_6524')
    def lambda_6524():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_6524)

    OP_73(0x0009)

    @scena.Lambda('lambda_6535')
    def lambda_6535():
        CameraSetDistance(680, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6535)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 515)
    OP_70(0x0009, 526)
    OP_73(0x0009)
    PlaySE(237, 0x00, 0x64)
    OP_6F(0x0009, 527)
    OP_70(0x0009, 530)
    OP_73(0x0009)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 3160, 1480, 1320, 0)

    ChrTalk(
        0x0010,
        (
            '#0130140343V#36A#117F呜、呜哦哦哦哦！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 531)
    OP_70(0x0009, 587)
    WaitForThreadExit(0x0000, 0x0003)

    @scena.Lambda('lambda_65D3')
    def lambda_65D3():
        OP_67(0, 6790, -30160, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_65D3)

    OP_73(0x0009)
    OP_71(0x0009, 0x0020)
    OP_6F(0x0009, 588)
    OP_70(0x0009, 607)

    ChrTalk(
        0x0101,
        (
            '#0010140344V#580F#2P上、上校！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140345V#016F#2P可恶……怎么办！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6653')
    def lambda_6653():
        CameraMove(5700, 2800, 380, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6653)

    ChrTalk(
        0x0010,
        (
            '#0130140346V#5P#117F快、快点离开这里！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140347V在和你们的决斗失败之时……\n',
            '我的命运……就已经到尽头了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140348V#580F#1P怎、怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140349V#5P#118F因此……\n',
            '你们不用在意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140350V我的计划还是以失败告终了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140351V在最后的时刻可以帮助你们，\n',
            '算是表达……我的歉意吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0011, 260, 0, -8970, 154)

    NpcTalk(
        0x0011,
        '男性的声音',
        (
            '#0160140352V#1P哎呀呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '男性的声音',
        (
            '#0160140353V#1P只要坚持自己的信念，\n',
            '就一定会找到取胜的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '男性的声音',
        (
            '#0160140354V#1P我教给你的这些，难道都忘记了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x0000015E, 2400, 0x02, 0x07, 0x00000050, 0x01)
    WaitForThreadExit(0x0000, 0x0000)
    LoadEffect(0x00, 'battle\\\\mgaria0.eff')
    LoadEffect(0x01, 'craft\\\\cr201_01.eff')
    LoadEffect(0x02, 'monster\\\\ms10002.eff')
    LoadEffect(0x03, 'monster\\\\ms10001.eff')
    LoadEffect(0x04, 'map\\\\mp021_04.eff')
    OP_26(132)
    OP_26(521)
    OP_26(136)
    ChrSetFlags(0x0020, 0x0080)
    OP_72(0x0009, 0x0020)
    OP_73(0x0009)
    OP_71(0x0009, 0x0020)
    OP_B0(0x0009, 0x08)
    OP_6F(0x0009, 588)
    OP_70(0x0009, 607)

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0x4),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_73B1',
    )

    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001D, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001E, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001F, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_6973')
    def lambda_6973():
        ChrSetRGBAMask(0x001B, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_6973)

    @scena.Lambda('lambda_6985')
    def lambda_6985():
        ChrSetRGBAMask(0x001B, 255, 255, 255, 200, 700)

        ExitThread()

    DispatchAsync(0x001B, 0x0003, lambda_6985)

    @scena.Lambda('lambda_6997')
    def lambda_6997():
        ChrSetRGBAMask(0x001C, 255, 255, 255, 160, 900)

        ExitThread()

    DispatchAsync(0x001C, 0x0003, lambda_6997)

    @scena.Lambda('lambda_69A9')
    def lambda_69A9():
        ChrSetRGBAMask(0x001D, 255, 255, 255, 120, 1100)

        ExitThread()

    DispatchAsync(0x001D, 0x0003, lambda_69A9)

    @scena.Lambda('lambda_69BB')
    def lambda_69BB():
        ChrSetRGBAMask(0x001E, 255, 255, 255, 80, 1300)

        ExitThread()

    DispatchAsync(0x001E, 0x0003, lambda_69BB)

    @scena.Lambda('lambda_69CD')
    def lambda_69CD():
        ChrSetRGBAMask(0x001F, 255, 255, 255, 40, 1500)

        ExitThread()

    DispatchAsync(0x001F, 0x0003, lambda_69CD)

    CreateThread(0x0011, 0x00, 0x00, func_15_A2BF)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, func_15_A2BF)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, func_15_A2BF)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, func_15_A2BF)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, func_15_A2BF)
    Sleep(50)

    CreateThread(0x001F, 0x00, 0x00, func_15_A2BF)

    @scena.Lambda('lambda_6A22')
    def lambda_6A22():
        CameraMove(5630, 2800, -60, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6A22)

    @scena.Lambda('lambda_6A3A')
    def lambda_6A3A():
        OP_67(0, 16840, -30160, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6A3A)

    @scena.Lambda('lambda_6A52')
    def lambda_6A52():
        CameraSetDistance(510, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_6A52)

    @scena.Lambda('lambda_6A62')
    def lambda_6A62():
        OP_6C(73000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_6A62)

    @scena.Lambda('lambda_6A72')
    def lambda_6A72():
        OP_6E(926, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_6A72)

    OP_A6(0x0007)
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    PlaySE(132, 0x00, 0x64)
    PlaySE(521, 0x00, 0x64)
    PlaySE(245, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x00FF, 4650, 2500, 3240, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    ChrTalk(
        0x0011,
        (
            '#0160140355V#10A嘿呀！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_72(0x0009, 0x0020)
    OP_B0(0x0009, 0x0D)
    OP_6F(0x0009, 646)
    OP_70(0x0009, 684)
    CreateThread(0x0010, 0x00, 0x00, func_14_A254)
    OP_73(0x0009)
    OP_71(0x0009, 0x0020)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 685)
    OP_70(0x0009, 703)
    WaitForThreadExit(0x0000, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010140356V#004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140357V#014F#2P难道是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0009, 0x0020)

    @scena.Lambda('lambda_6B7B')
    def lambda_6B7B():
        CameraMove(5610, 1150, -1750, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6B7B)

    @scena.Lambda('lambda_6B93')
    def lambda_6B93():
        OP_67(0, 26710, -30160, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6B93)

    @scena.Lambda('lambda_6BAB')
    def lambda_6BAB():
        CameraSetDistance(460, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_6BAB)

    @scena.Lambda('lambda_6BBB')
    def lambda_6BBB():
        OP_6C(18000, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_6BBB)

    @scena.Lambda('lambda_6BCB')
    def lambda_6BCB():
        OP_6E(698, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_6BCB)

    CreateThread(0x0011, 0x00, 0x00, func_16_A370)
    Sleep(35)

    CreateThread(0x001B, 0x00, 0x00, func_16_A370)
    Sleep(35)

    CreateThread(0x001C, 0x00, 0x00, func_16_A370)
    Sleep(35)

    CreateThread(0x001D, 0x00, 0x00, func_16_A370)
    Sleep(35)

    CreateThread(0x001E, 0x00, 0x00, func_16_A370)
    Sleep(35)

    CreateThread(0x001F, 0x00, 0x00, func_16_A370)
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_A6(0x0007)
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    PlaySE(132, 0x00, 0x64)
    PlaySE(521, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x00FF, 5190, 0, -3170, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    ChrTalk(
        0x0011,
        (
            '#0160140358V#10A嘿呀！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_6F(0x0009, 746)
    OP_70(0x0009, 773)
    Sleep(500)

    PlaySE(236, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    WaitForThreadExit(0x0011, 0x0000)
    Sleep(900)

    CreateThread(0x0011, 0x00, 0x00, func_17_A3E4)
    Sleep(35)

    CreateThread(0x001B, 0x00, 0x00, func_17_A3E4)
    Sleep(35)

    CreateThread(0x001C, 0x00, 0x00, func_17_A3E4)
    Sleep(35)

    CreateThread(0x001D, 0x00, 0x00, func_17_A3E4)
    Sleep(35)

    CreateThread(0x001E, 0x00, 0x00, func_17_A3E4)
    Sleep(35)

    CreateThread(0x001F, 0x00, 0x00, func_17_A3E4)
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_73(0x0009)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    Sleep(350)

    PlayEffect(0x03, 0xFF, 0x00FF, 5690, 4400, -2090, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(521, 0x00, 0x64)
    PlaySE(136, 0x00, 0x64)

    ChrTalk(
        0x0011,
        (
            '#0160140359V#10A喝————！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(100)

    OP_6F(0x0009, 774)
    OP_70(0x0009, 795)
    Sleep(215)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayEffect(0x04, 0xFF, 0x00FF, 6210, 400, -720, 0, 90, 0, 7000, 7000, 7000, 0x00FF, 0, 0, 0, 0)
    PlaySE(236, 0x00, 0x64)
    OP_7C(500, 500, 2000, 100)
    OP_73(0x0009)
    Sleep(1000)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    Fade(1500)
    CameraMove(6150, 200, -1670, 0)
    OP_67(0, 19180, -30160, 0)
    CameraSetDistance(500, 0)
    OP_6C(66000, 0)
    OP_6E(702, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_6E2E')
    def lambda_6E2E():
        CameraMove(6150, 850, -1670, 4500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_6E2E)

    @scena.Lambda('lambda_6E46')
    def lambda_6E46():
        OP_6C(135000, 4500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_6E46)

    @scena.Lambda('lambda_6E56')
    def lambda_6E56():
        OP_67(0, 11370, -30160, 4500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6E56)

    Sleep(1000)

    PlayEffect(0x01, 0x01, 0x0011, 0, 0, 0, 0, 0, 0, 1800, 1800, 1800, 0x00FF, 0, 0, 0, 0)
    Sleep(1250)

    OP_B0(0x0009, 0x08)
    OP_6F(0x0009, 796)
    OP_70(0x0009, 815)
    OP_73(0x0009)
    WaitForThreadExit(0x0000, 0x0002)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    @scena.Lambda('lambda_6ECF')
    def lambda_6ECF():
        CameraSetDistance(590, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6ECF)

    @scena.Lambda('lambda_6EDF')
    def lambda_6EDF():
        CameraMove(7980, 1430, -610, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_6EDF)

    PlaySE(132, 0x00, 0x64)
    CreateThread(0x0011, 0x00, 0x00, func_18_A466)
    Sleep(15)

    CreateThread(0x001B, 0x00, 0x00, func_18_A466)
    Sleep(15)

    CreateThread(0x001C, 0x00, 0x00, func_18_A466)
    Sleep(15)

    CreateThread(0x001D, 0x00, 0x00, func_18_A466)
    Sleep(15)

    CreateThread(0x001E, 0x00, 0x00, func_18_A466)
    Sleep(15)

    CreateThread(0x001F, 0x00, 0x00, func_18_A466)
    PlaySE(521, 0x00, 0x64)
    OP_4A(0x0000, 255)
    OP_4A(0x001B, 0)
    OP_4A(0x001C, 0)
    OP_4A(0x001D, 0)
    OP_4A(0x001E, 0)
    OP_4A(0x0011, 0)
    ChrSetSubChip(0x001B, 7)
    ChrSetSubChip(0x001C, 7)
    ChrSetSubChip(0x001D, 7)
    ChrSetSubChip(0x001E, 7)
    ChrSetSubChip(0x0011, 7)
    OP_6F(0x0009, 816)
    StopEffect(0x01, 0x00)
    OP_20(0x00000BB8)
    PlayEffect(0x02, 0xFF, 0x00FF, 5800, 2800, -720, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    CameraSetDistance(480, 500)
    OP_4B(0x0000, 255)
    OP_4B(0x001B, 0)
    OP_4B(0x001C, 0)
    OP_4B(0x001D, 0)
    OP_4B(0x001E, 0)
    OP_4B(0x001E, 0)
    OP_4B(0x0011, 0)
    PlaySE(246, 0x00, 0x64)

    ChrTalk(
        0x0011,
        (
            '#0160140360V#10A哼！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    LoadEffect(0x04, 'map\\\\mp031_0.eff')
    PlayEffect(0x04, 0xFF, 0x00FF, 7600, 1730, -590, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_20(0x00000BB8)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 816)
    OP_70(0x0009, 843)
    OP_73(0x0009)
    Fade(1000)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    TerminateThread(0x0011, 0xFF)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 255, 0)
    ChrSetSubChip(0x0011, 13)
    OP_21()

    ChrTalk(
        0x0011,
        (
            '#0160140361V呼……这种东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 270, 400)
    PlayBGM(1)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0160140362V#080F我回来了。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140363V真是好久没见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(3230, 700, -1570, 0)
    OP_67(0, 7990, -10000, 0)
    CameraSetDistance(3510, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -1170, 0, 380, 0)
    ChrSetPos(0x0102, -1160, 0, -890, 0)
    ChrSetPos(0x0000, -400, 0, -2790, 0)
    ChrSetPos(0x0001, 2090, 0, -3410, 0)
    ChrSetChipByIndex(0x0000, 65535)
    ChrSetChipByIndex(0x0001, 65535)
    ChrSetChipByIndex(0x0002, 65535)
    ChrSetChipByIndex(0x0003, 65535)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)

    @scena.Lambda('lambda_71D0')
    def lambda_71D0():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_71D0')

    DispatchAsync2(0x0000, 0x0003, lambda_71D0)

    @scena.Lambda('lambda_71E1')
    def lambda_71E1():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_71E1')

    DispatchAsync2(0x0001, 0x0003, lambda_71E1)

    @scena.Lambda('lambda_71F2')
    def lambda_71F2():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_71F2')

    DispatchAsync2(0x0002, 0x0003, lambda_71F2)

    @scena.Lambda('lambda_7203')
    def lambda_7203():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_7203')

    DispatchAsync2(0x0003, 0x0003, lambda_7203)

    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010140364V#580F老、老、老……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010140365V#005F#5S老爸！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_7272')
    def lambda_7272():
        CameraMove(190, 0, -590, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_7272)

    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0011, 2340, 0, -650, 2000, 6000)
    PlaySE(164, 0x00, 0x64)
    ChrSetSubChip(0x0011, 10)
    Sleep(200)

    ChrClearFlags(0x0011, 0x0020)
    ChrSetChipByIndex(0x0011, 9)
    ChrSetSubChip(0x0011, 0)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0011, 660, 0, -700, 500, 2000)
    WaitForThreadExit(0x0000, 0x0000)

    ChrTalk(
        0x0011,
        (
            '#0160140366V#085F虽然经历了不少修行，\n',
            '可是还差得很远呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140367V#080F不过，这次就算你们合格吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140368V#005F什、什么合格不合格啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140369V怎么回事啊，老爸！\n',
            '你怎么会跑这里来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E50')

    def _loc_73B1(): pass

    label('loc_73B1')

    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001D, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001E, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001F, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_73FC')
    def lambda_73FC():
        ChrSetRGBAMask(0x001B, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_73FC)

    @scena.Lambda('lambda_740E')
    def lambda_740E():
        ChrSetRGBAMask(0x001B, 255, 255, 255, 200, 700)

        ExitThread()

    DispatchAsync(0x001B, 0x0003, lambda_740E)

    @scena.Lambda('lambda_7420')
    def lambda_7420():
        ChrSetRGBAMask(0x001C, 255, 255, 255, 160, 900)

        ExitThread()

    DispatchAsync(0x001C, 0x0003, lambda_7420)

    @scena.Lambda('lambda_7432')
    def lambda_7432():
        ChrSetRGBAMask(0x001D, 255, 255, 255, 120, 1100)

        ExitThread()

    DispatchAsync(0x001D, 0x0003, lambda_7432)

    @scena.Lambda('lambda_7444')
    def lambda_7444():
        ChrSetRGBAMask(0x001E, 255, 255, 255, 80, 1300)

        ExitThread()

    DispatchAsync(0x001E, 0x0003, lambda_7444)

    @scena.Lambda('lambda_7456')
    def lambda_7456():
        ChrSetRGBAMask(0x001F, 255, 255, 255, 40, 1500)

        ExitThread()

    DispatchAsync(0x001F, 0x0003, lambda_7456)

    CreateThread(0x0011, 0x00, 0x00, func_19_A498)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, func_19_A498)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, func_19_A498)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, func_19_A498)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, func_19_A498)
    Sleep(50)

    CreateThread(0x001F, 0x00, 0x00, func_19_A498)

    @scena.Lambda('lambda_74AB')
    def lambda_74AB():
        CameraMove(2340, 1150, 10, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_74AB)

    @scena.Lambda('lambda_74C3')
    def lambda_74C3():
        OP_67(0, 8830, -30160, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_74C3)

    @scena.Lambda('lambda_74DB')
    def lambda_74DB():
        CameraSetDistance(640, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_74DB)

    @scena.Lambda('lambda_74EB')
    def lambda_74EB():
        OP_6C(82000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_74EB)

    @scena.Lambda('lambda_74FB')
    def lambda_74FB():
        OP_6E(602, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_74FB)

    OP_A6(0x0007)
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    PlaySE(132, 0x00, 0x64)
    PlaySE(521, 0x00, 0x64)
    PlaySE(245, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x00FF, 4650, 2500, 3240, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    ChrTalk(
        0x0011,
        (
            '#0160140370V#10A嘿呀！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_20(0x000005DC)
    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 12)
    ChrTurnDirection(0x0101, 0x0017, 0)
    ChrTurnDirection(0x0102, 0x0017, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75A2',
    )

    ChrSetChipByIndex(0x0103, 14)
    ChrTurnDirection(0x0103, 0x0017, 0)

    def _loc_75A2(): pass

    label('loc_75A2')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75BC',
    )

    ChrSetChipByIndex(0x0104, 16)
    ChrTurnDirection(0x0104, 0x0017, 0)

    def _loc_75BC(): pass

    label('loc_75BC')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75D6',
    )

    ChrSetChipByIndex(0x0106, 20)
    ChrTurnDirection(0x0106, 0x0017, 0)

    def _loc_75D6(): pass

    label('loc_75D6')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75F0',
    )

    ChrSetChipByIndex(0x0105, 18)
    ChrTurnDirection(0x0105, 0x0017, 0)

    def _loc_75F0(): pass

    label('loc_75F0')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_760A',
    )

    ChrSetChipByIndex(0x0107, 22)
    ChrTurnDirection(0x0107, 0x0017, 0)

    def _loc_760A(): pass

    label('loc_760A')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7624',
    )

    ChrSetChipByIndex(0x0108, 24)
    ChrTurnDirection(0x0108, 0x0017, 0)

    def _loc_7624(): pass

    label('loc_7624')

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_72(0x0009, 0x0020)
    OP_B0(0x0009, 0x0D)
    OP_6F(0x0009, 646)
    OP_70(0x0009, 684)
    CreateThread(0x0010, 0x00, 0x00, func_14_A254)
    OP_73(0x0009)
    OP_71(0x0009, 0x0020)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 685)
    OP_70(0x0009, 703)
    WaitForThreadExit(0x0000, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010140371V#004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140357V#014F#2P难道是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    TerminateThread(0x0011, 0xFF)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 255, 0)
    ChrSetSubChip(0x0011, 13)
    ChrTurnDirection(0x0011, 0x0101, 800)
    OP_21()
    PlayBGM(43)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0160140373V#5P#087F就是现在！把它彻底击溃！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetStatus(0x0000, 0xFA, 1)
    ChrSetStatus(0x0001, 0xFA, 1)
    ChrSetStatus(0x0002, 0xFA, 1)
    ChrSetStatus(0x0003, 0xFA, 1)
    ChrSetStatus(0x0004, 0xFA, 1)
    ChrSetStatus(0x0005, 0xFA, 1)
    ChrSetStatus(0x0006, 0xFA, 1)
    ChrSetStatus(0x0007, 0xFA, 1)
    ChrSetStatus(0x0000, 0x05, 200)
    ChrSetStatus(0x0001, 0x05, 200)
    ChrSetStatus(0x0002, 0x05, 200)
    ChrSetStatus(0x0003, 0x05, 200)
    ChrSetStatus(0x0004, 0x05, 200)
    ChrSetStatus(0x0005, 0x05, 200)
    ChrSetStatus(0x0006, 0x05, 200)
    ChrSetStatus(0x0007, 0x05, 200)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_778E',
    )

    FormationDelMember(0x02, 0xFF)
    FormationAddMember(0x02, 0xFF)

    def _loc_778E(): pass

    label('loc_778E')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_77A2',
    )

    FormationDelMember(0x03, 0xFF)
    FormationAddMember(0x03, 0xFF)

    def _loc_77A2(): pass

    label('loc_77A2')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_77B6',
    )

    FormationDelMember(0x05, 0xFF)
    FormationAddMember(0x05, 0xFF)

    def _loc_77B6(): pass

    label('loc_77B6')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_77CA',
    )

    FormationDelMember(0x04, 0xFF)
    FormationAddMember(0x04, 0xFF)

    def _loc_77CA(): pass

    label('loc_77CA')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_77DE',
    )

    FormationDelMember(0x06, 0xFF)
    FormationAddMember(0x06, 0xFF)

    def _loc_77DE(): pass

    label('loc_77DE')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_77F2',
    )

    FormationDelMember(0x07, 0xFF)
    FormationAddMember(0x07, 0xFF)

    def _loc_77F2(): pass

    label('loc_77F2')

    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 12)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_780F',
    )

    ChrSetChipByIndex(0x0103, 14)

    def _loc_780F(): pass

    label('loc_780F')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7825',
    )

    ChrSetChipByIndex(0x0104, 16)
    SetScenaFlags(ScenaFlag(0x00DE, 5, 0x6F5))

    def _loc_7825(): pass

    label('loc_7825')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7838',
    )

    ChrSetChipByIndex(0x0106, 20)

    def _loc_7838(): pass

    label('loc_7838')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_784B',
    )

    ChrSetChipByIndex(0x0105, 18)

    def _loc_784B(): pass

    label('loc_784B')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_785E',
    )

    ChrSetChipByIndex(0x0107, 22)

    def _loc_785E(): pass

    label('loc_785E')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7871',
    )

    ChrSetChipByIndex(0x0108, 24)

    def _loc_7871(): pass

    label('loc_7871')

    ChrSetPos(0x0101, -2910, 0, -3850, 47)
    ChrSetPos(0x0102, -1510, 0, -3240, 47)
    ChrSetPos(0x0002, -4710, 0, 610, 127)
    ChrSetPos(0x0003, -5270, 0, -1970, 111)
    ChrTurnDirection(0x0000, 0x0017, 0)
    ChrTurnDirection(0x0001, 0x0017, 0)
    ChrTurnDirection(0x0002, 0x0017, 0)
    ChrTurnDirection(0x0003, 0x0017, 0)
    WaitEffect(0x19, 0x00)
    Battle(0x000003B3, 0x0010000A, 0x00, 0x0000, 0xFF)
    WaitEffect(0x19, 0x01)
    EventBegin(0x00)
    FormationDelMember(0x00, 0xFF)
    FormationDelMember(0x01, 0xFF)
    FormationAddMember(0x00, 0xFF)
    FormationAddMember(0x01, 0xFF)
    OP_72(0x0006, 0x0020)
    OP_6F(0x0006, 240)
    OP_72(0x0005, 0x0020)
    OP_71(0x0005, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0000, 3260)
    OP_6F(0x0001, 3260)
    OP_6F(0x0002, 3260)
    OP_6F(0x0003, 3260)

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x07,
        (
            (Expr.PushLong, 0x1388),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A1(0x0017, 0x0009)
    OP_72(0x0009, 0x0020)
    OP_72(0x0009, 0x0004)
    OP_6F(0x0009, 843)
    OP_70(0x0009, 843)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    TerminateThread(0x0011, 0xFF)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 255, 0)
    ChrClearFlags(0x0011, 0x0020)
    ChrSetChipByIndex(0x0011, 9)
    ChrSetSubChip(0x0011, 0)
    ChrSetPos(0x0011, 3450, 0, 6350, 209)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 3590, 1600, 5110, 0)
    ChrSetSubChip(0x0010, 0)
    ChrSetChipByIndex(0x0010, 32)
    ChrSetPos(0x0010, 4790, 0, 6510, 0)
    CameraMove(21280, 0, -530, 0)
    OP_67(0, 7990, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -1170, 0, 380, 0)
    ChrSetPos(0x0102, -1160, 0, -890, 0)
    ChrSetPos(0x0000, -400, 0, -2790, 0)
    ChrSetPos(0x0001, 2090, 0, -3410, 0)
    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 12)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7A8D',
    )

    ChrSetChipByIndex(0x0103, 14)

    def _loc_7A8D(): pass

    label('loc_7A8D')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7AA3',
    )

    ChrSetChipByIndex(0x0104, 16)
    SetScenaFlags(ScenaFlag(0x00DE, 5, 0x6F5))

    def _loc_7AA3(): pass

    label('loc_7AA3')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7AB6',
    )

    ChrSetChipByIndex(0x0106, 20)

    def _loc_7AB6(): pass

    label('loc_7AB6')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7AC9',
    )

    ChrSetChipByIndex(0x0105, 18)

    def _loc_7AC9(): pass

    label('loc_7AC9')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7ADC',
    )

    ChrSetChipByIndex(0x0107, 22)

    def _loc_7ADC(): pass

    label('loc_7ADC')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7AEF',
    )

    ChrSetChipByIndex(0x0108, 24)

    def _loc_7AEF(): pass

    label('loc_7AEF')

    ChrTurnDirection(0x0000, 0x0017, 0)
    ChrTurnDirection(0x0001, 0x0017, 0)
    ChrTurnDirection(0x0002, 0x0017, 0)
    ChrTurnDirection(0x0003, 0x0017, 0)
    FadeIn(2000, 0)
    CameraMove(11670, 0, 850, 4000)
    Fade(1000)
    CameraMove(3700, 0, -1810, 0)
    OP_67(0, 7990, -10000, 0)
    CameraSetDistance(2820, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitEffect(0x19, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010140374V#007F终于、终于胜利啦～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140375V#2P……辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(1)
    ChrSetChipByIndex(0x0000, 65535)
    ChrSetChipByIndex(0x0001, 65535)
    ChrSetChipByIndex(0x0002, 65535)
    ChrSetChipByIndex(0x0003, 65535)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)

    @scena.Lambda('lambda_7BEF')
    def lambda_7BEF():
        CameraMove(190, 0, -590, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_7BEF)

    @scena.Lambda('lambda_7C07')
    def lambda_7C07():
        CameraSetDistance(3300, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_7C07)

    @scena.Lambda('lambda_7C17')
    def lambda_7C17():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_7C17)

    @scena.Lambda('lambda_7C25')
    def lambda_7C25():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_7C25)

    @scena.Lambda('lambda_7C33')
    def lambda_7C33():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0003, lambda_7C33)

    @scena.Lambda('lambda_7C41')
    def lambda_7C41():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0003, lambda_7C41)

    Sleep(1500)

    @scena.Lambda('lambda_7C54')
    def lambda_7C54():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_7C54')

    DispatchAsync2(0x0000, 0x0003, lambda_7C54)

    @scena.Lambda('lambda_7C65')
    def lambda_7C65():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_7C65')

    DispatchAsync2(0x0001, 0x0003, lambda_7C65)

    @scena.Lambda('lambda_7C76')
    def lambda_7C76():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_7C76')

    DispatchAsync2(0x0002, 0x0003, lambda_7C76)

    @scena.Lambda('lambda_7C87')
    def lambda_7C87():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_7C87')

    DispatchAsync2(0x0003, 0x0003, lambda_7C87)

    @scena.Lambda('lambda_7C98')
    def lambda_7C98():
        ChrWalkTo(0x0011, 700, 0, -750, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7C98)

    WaitForThreadExit(0x0011, 0x0001)
    ChrSetDirection(0x0011, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0160140362V#080F我回来了。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140363V真是好久没有见到你们了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140378V#580F老、老、老……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010140379V#005F#5S老爸！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140380V#085F虽然到最后还是有点疏忽大意，\n',
            '不过，修行的成果总算体现出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140381V#080F你们合格了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140368V#005F什、什么合格不合格啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140369V怎么回事啊，老爸！\n',
            '你怎么会跑到这里来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7E50(): pass

    label('loc_7E50')

    ChrTalk(
        0x0011,
        (
            '#0160140384V#084F你问我怎么会到这里来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140385V#081F随便过来看看不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140386V#509F什、什么叫做随便过来看看啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140387V#019F哈哈……太好了。\n',
            '爸爸您依然还是那么的精力充沛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140388V#080F哦哦……\n',
            '你看起来好像长高了一些嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140389V怎么样，为了保护我这宝贝女儿，\n',
            '这段时间你吃了不少苦头吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140390V#009F这、这是什么意思！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140391V#019F呵呵，没有那回事啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140392V#010F而且我和艾丝蒂尔一直是互相扶持的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140393V所以我们才能走到今天这一步啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140394V#080F这样啊……\n',
            '看来是一次很不错的旅行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_809C')
    def lambda_809C():
        CameraMove(720, 0, -2650, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_809C)

    WaitForThreadExit(0x0000, 0x0000)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_82B6',
    )

    ChrTalk(
        0x0103,
        (
            '#0030140395V#021F老师……您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0011, 970, 0, -1920, 2000, 0x00)
    ChrTurnDirection(0x0011, 0x0103, 400)

    ChrTalk(
        0x0011,
        (
            '#0160140396V#080F我回来了，雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140397V我不在的这段时间，\n',
            '协会的工作肯定让你忙不过来吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030140398V#027F是啊，很辛苦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140399V不过也是很好的修行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140400V#081F不愧是我最优秀的徒弟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140401V#080F艾丝蒂尔和约修亚在协会\n',
            '工作得怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030140402V#020F这个嘛……\n',
            '已经不能再算是见习的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140403V#021F不过，他们有没有意识到\n',
            '自己已经达到了一个更高的程度，\n',
            '这点我就不太清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_82B6(): pass

    label('loc_82B6')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_84F0',
    )

    ChrTalk(
        0x0104,
        (
            '#0040140404V#030F呵呵，初次见面。\n',
            '卡西乌斯·布莱特大人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140405V本人名为奥利维尔·朗海姆，\n',
            '是来自帝国的演奏家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0011, 970, 0, -1920, 2000, 0x00)
    ChrTurnDirection(0x0011, 0x0104, 400)

    ChrTalk(
        0x0011,
        (
            '#0160140406V#084F哦，是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140407V#080F事情告一段落之后，\n',
            '就和我说说整个事情的经过吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140408V还有，非常感谢你能在这次事件里\n',
            '全力协助我那两个孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040140409V#031F没什么，大人您太客气了。\n',
            '这也是一次很有意义的体验嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140410V#030F而且，您的功夫真是了得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140411V能亲眼看到传说中的大人的英姿，\n',
            '真是让人大饱眼福啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140412V#080F呵呵……\n',
            '我也还在修行中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_84F0(): pass

    label('loc_84F0')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_86FC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140413V#054F喂，大叔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050140414V神秘失踪了那么多天，\n',
            '究竟跑到哪游山玩水去了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0011, 970, 0, -1920, 2000, 0x00)
    ChrTurnDirection(0x0011, 0x0106, 400)

    ChrTalk(
        0x0011,
        (
            '#0160140415V#084F哦，不良青年。\n',
            '我从博士那里听说了你的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140416V#081F看来你也相当地努力嘛。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140417V了不起，了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050140418V#057F不、不要把我当成小鬼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140419V#080F开个玩笑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140420V调查特务兵那件差事，\n',
            '我知道你做得十分尽职尽责。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140421V而且还给我那两个孩子不少的帮助，\n',
            '不管怎么说，还真是要感谢你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050140422V#055F这、这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_86FC(): pass

    label('loc_86FC')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_88A6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070140423V#560F卡西乌斯叔叔……\n',
            '好久没有见到你了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0011, 970, 0, -1920, 2000, 0x00)
    ChrTurnDirection(0x0011, 0x0107, 400)

    ChrTalk(
        0x0011,
        (
            '#0160140424V#080F哎哟，是提妲啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140425V一年多没见了，\n',
            '你长高了不少啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140426V听说你和艾丝蒂尔还有约修亚\n',
            '成了好朋友对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070140427V#067F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070140428V姐姐他们把我当做妹妹一样爱护呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140429V#081F哈哈，那就太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140430V不过他们俩还不是很可靠，\n',
            '还请你多多指点他们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_88A6(): pass

    label('loc_88A6')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A91',
    )

    ChrTalk(
        0x0105,
        (
            '#0060140431V#048F卡西乌斯先生。\n',
            '您好，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0011, 970, 0, -1920, 2000, 0x00)
    ChrTurnDirection(0x0011, 0x0105, 400)

    ChrTalk(
        0x0011,
        (
            '#0160140432V#080F公主殿下。\n',
            '我们差不多有半年没见了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140433V我听说你之前被囚禁起来了，\n',
            '现在能平安无事也总算是让我放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060140434V#041F呵呵，谢谢卡西乌斯先生关心。\n',
            '这也多亏了艾丝蒂尔他们的帮助啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140435V#040F对了，今年的王立学院学园祭，\n',
            '艾丝蒂尔他们一起参加了舞台剧呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140436V卡西乌斯先生如果也能看到就好了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140437V#084F哦……\n',
            '那还真是可惜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A91(): pass

    label('loc_8A91')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8CB5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140438V#070F哟，大人。\n',
            '您回来得还真晚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140439V我已经等了您好久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0011, 970, 0, -1920, 2000, 0x00)
    ChrTurnDirection(0x0011, 0x0108, 400)

    ChrTalk(
        0x0011,
        (
            '#0160140440V#082F抱歉啊，金。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140441V特地把你从共和国叫过来，\n',
            '真是麻烦你了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140442V因为我实在放不下心，\n',
            '所以才让你过来帮帮这些年轻人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080140443V#071F没什么，请别放在心上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140444V就算您不叫我来，\n',
            '我自己也会来王国走走啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140445V#070F而且还能见识到大人引以为豪的\n',
            '两个孩子的精彩表现……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140446V这段时间真的过得很愉快啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140447V#080F是吗……\n',
            '你能这么说我也很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8CB5(): pass

    label('loc_8CB5')

    ChrTalk(
        0x0101,
        (
            '#0010140448V#005F这、这里可不是聊天叙旧的地方吧！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140449V#007F真是的～才刚回来，\n',
            '又把我们的风头给抢走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0010, 0xFF)
    ChrSetChipByIndex(0x0010, 31)
    ChrSetSubChip(0x0010, 0)
    ChrSetPos(0x0010, 2670, 0, 6490, 180)
    ChrSetPos(0x000E, -1860, 0, -15040, 0)

    ChrTalk(
        0x000E,
        (
            '#0540140450V#3P哎呀呀……\n',
            '看来总算是把危机解决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8D9F')
    def lambda_8D9F():
        CameraMove(1200, 0, -3730, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_8D9F)

    ChrClearFlags(0x000E, 0x0080)

    @scena.Lambda('lambda_8DBC')
    def lambda_8DBC():
        ChrWalkTo(0x00FE, 1030, 0, -4810, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_8DBC)

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E28',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8DF2',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ChrSetChipByIndex(0x000D, 5)

    Jump('loc_8E28')

    def _loc_8DF2(): pass

    label('loc_8DF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E05',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    ChrSetChipByIndex(0x0008, 5)

    Jump('loc_8E28')

    def _loc_8E05(): pass

    label('loc_8E05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E18',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ChrSetChipByIndex(0x0009, 5)

    Jump('loc_8E28')

    def _loc_8E18(): pass

    label('loc_8E18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E28',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    ChrSetChipByIndex(0x000A, 5)

    def _loc_8E28(): pass

    label('loc_8E28')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E7F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E49',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ChrSetChipByIndex(0x000D, 1)

    Jump('loc_8E7F')

    def _loc_8E49(): pass

    label('loc_8E49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E5C',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    ChrSetChipByIndex(0x0008, 1)

    Jump('loc_8E7F')

    def _loc_8E5C(): pass

    label('loc_8E5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E6F',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ChrSetChipByIndex(0x0009, 1)

    Jump('loc_8E7F')

    def _loc_8E6F(): pass

    label('loc_8E6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E7F',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    ChrSetChipByIndex(0x000A, 1)

    def _loc_8E7F(): pass

    label('loc_8E7F')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8ED6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8EA0',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ChrSetChipByIndex(0x000D, 0)

    Jump('loc_8ED6')

    def _loc_8EA0(): pass

    label('loc_8EA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8EB3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    ChrSetChipByIndex(0x0008, 0)

    Jump('loc_8ED6')

    def _loc_8EB3(): pass

    label('loc_8EB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8EC6',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ChrSetChipByIndex(0x0009, 0)

    Jump('loc_8ED6')

    def _loc_8EC6(): pass

    label('loc_8EC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8ED6',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    ChrSetChipByIndex(0x000A, 0)

    def _loc_8ED6(): pass

    label('loc_8ED6')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8F2D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8EF7',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ChrSetChipByIndex(0x000D, 2)

    Jump('loc_8F2D')

    def _loc_8EF7(): pass

    label('loc_8EF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F0A',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    ChrSetChipByIndex(0x0008, 2)

    Jump('loc_8F2D')

    def _loc_8F0A(): pass

    label('loc_8F0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F1D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ChrSetChipByIndex(0x0009, 2)

    Jump('loc_8F2D')

    def _loc_8F1D(): pass

    label('loc_8F1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F2D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    ChrSetChipByIndex(0x000A, 2)

    def _loc_8F2D(): pass

    label('loc_8F2D')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8F84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F4E',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ChrSetChipByIndex(0x000D, 3)

    Jump('loc_8F84')

    def _loc_8F4E(): pass

    label('loc_8F4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F61',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    ChrSetChipByIndex(0x0008, 3)

    Jump('loc_8F84')

    def _loc_8F61(): pass

    label('loc_8F61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F74',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ChrSetChipByIndex(0x0009, 3)

    Jump('loc_8F84')

    def _loc_8F74(): pass

    label('loc_8F74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F84',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    ChrSetChipByIndex(0x000A, 3)

    def _loc_8F84(): pass

    label('loc_8F84')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FDB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8FA5',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ChrSetChipByIndex(0x000D, 4)

    Jump('loc_8FDB')

    def _loc_8FA5(): pass

    label('loc_8FA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8FB8',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    ChrSetChipByIndex(0x0008, 4)

    Jump('loc_8FDB')

    def _loc_8FB8(): pass

    label('loc_8FB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8FCB',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ChrSetChipByIndex(0x0009, 4)

    Jump('loc_8FDB')

    def _loc_8FCB(): pass

    label('loc_8FCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8FDB',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    ChrSetChipByIndex(0x000A, 4)

    def _loc_8FDB(): pass

    label('loc_8FDB')

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 110, 0, -17400, 0)

    @scena.Lambda('lambda_8FF7')
    def lambda_8FF7():
        ChrWalkTo(0x00FE, 2700, 0, -7520, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_8FF7)

    Sleep(200)

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -2180, 0, -17210, 0)

    @scena.Lambda('lambda_902D')
    def lambda_902D():
        ChrWalkTo(0x00FE, -1170, 0, -7620, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_902D)

    Sleep(200)

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -1530, 0, -17240, 0)

    @scena.Lambda('lambda_9063')
    def lambda_9063():
        ChrWalkTo(0x00FE, 240, 0, -8890, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_9063)

    Sleep(200)

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -720, 0, -17320, 0)

    @scena.Lambda('lambda_9099')
    def lambda_9099():
        ChrWalkTo(0x00FE, 1370, 0, -8690, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_9099)

    Sleep(1000)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)

    @scena.Lambda('lambda_90C9')
    def lambda_90C9():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_90C9)

    @scena.Lambda('lambda_90D7')
    def lambda_90D7():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_90D7)

    @scena.Lambda('lambda_90E5')
    def lambda_90E5():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_90E5)

    @scena.Lambda('lambda_90F3')
    def lambda_90F3():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0003, lambda_90F3)

    @scena.Lambda('lambda_9101')
    def lambda_9101():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0003, lambda_9101)

    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0000, 0x0000)

    ChrTalk(
        0x0011,
        (
            '#0160140451V#080F哦，博士。\n',
            '你们来得还真是慢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0540140452V#102F#2P你先行一步之后，\n',
            '就有大批人形兵器涌了过来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140453V我们也是好不容易将它们击退的，\n',
            '然后才赶到这里来啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140454V#101F终于……\n',
            '一切都处理妥当了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140455V#085F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140456V#080F虽然还残留有很多的事情，\n',
            '不过总算是了结一件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140457V#505F可、可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140458V那些被情报部操控的正规军\n',
            '不是已经迫近王城了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140459V#013F#6P的确……\n',
            '而且警备飞艇也来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140460V#012F爸爸您来的时候，\n',
            '王都地上的情况怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 315, 400)

    @scena.Lambda('lambda_9340')
    def lambda_9340():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_9340)

    @scena.Lambda('lambda_934E')
    def lambda_934E():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_934E)

    ChrTalk(
        0x0011,
        (
            '#0160140461V#080F#5P啊啊。\n',
            '这点你们不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140462V我刚回到利贝尔的时候，\n',
            '就已经拜托摩尔根将军处理这件事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140463V而且希德少校也采取了行动，\n',
            '相信这场动乱很快就可以平息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140464V#005F这、这样就～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140465V#2P呵呵……原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140466V在来这里之前，\n',
            '原来就已经处理好了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)

    @scena.Lambda('lambda_94B4')
    def lambda_94B4():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_94B4)

    @scena.Lambda('lambda_94C2')
    def lambda_94C2():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_94C2)

    @scena.Lambda('lambda_94D0')
    def lambda_94D0():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_94D0)

    @scena.Lambda('lambda_94DE')
    def lambda_94DE():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0003, lambda_94DE)

    @scena.Lambda('lambda_94EC')
    def lambda_94EC():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0003, lambda_94EC)

    OP_20(0x000005DC)

    @scena.Lambda('lambda_94FF')
    def lambda_94FF():
        CameraMove(2300, 0, 2700, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_94FF)

    OP_6C(44000, 4000)
    OP_21()
    PlayBGM(83)
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0160140467V#082F#4P……你醒过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140468V#5P#118F摩尔根将军被我们严密监视着……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140469V希德的亲属也被列为了人质，\n',
            '谅他也不敢背叛我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140470V不过……到了最后，\n',
            '他们还是都被你救出来了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140471V#085F#4P啊，就算是这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140472V#080F可是理查德，\n',
            '我也只不过是稍微帮了点忙而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140473V即使我没有回到王国，\n',
            '他们自己也会想办法度过这个难关的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140474V#5P#115F不……终归还是实力的问题。\n',
            '由始至终，你都是一位英雄……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140475V#116F自从你离开了军队之后，\n',
            '我感到很不安……可又无计可施……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140476V如果国家再次受到侵略的话，\n',
            '我想，难以像上次那样再有奇迹发生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140477V因此……我就把希望寄托到了别的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130140478V#118F假如你还是继续留在军中的话，\n',
            '今天的事情，我敢保证不会发生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140479V#082F#4P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_984E')
    def lambda_984E():
        CameraMove(3460, 0, 7840, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_984E)

    @scena.Lambda('lambda_9866')
    def lambda_9866():
        CameraSetDistance(2800, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_9866)

    ChrWalkTo(0x0011, 2200, 0, 3860, 2000, 0x00)
    Sleep(500)

    ChrSetFlags(0x0011, 0x0020)
    ChrSetChipByIndex(0x0011, 35)
    ChrSetSubChip(0x0011, 0)
    ChrWalkTo(0x0011, 2440, 0, 5480, 10000, 0x00)
    ChrSetSubChip(0x0011, 1)

    @scena.Lambda('lambda_98B7')
    def lambda_98B7():
        ChrWalkTo(0x0011, 2600, 0, 6440, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_98B7)

    PlaySE(507, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_98DC')
    def lambda_98DC():
        ChrWalkTo(0x0011, 2600, 0, 6440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_98DC)

    PlaySE(553, 0x00, 0x64)
    ChrSetChipByIndex(0x0010, 7)
    ChrSetSubChip(0x0010, 0)
    ChrJumpTo(0x0010, 2780, 0, 9350, 600, 3000)
    PlaySE(554, 0x00, 0x64)
    ChrSetChipByIndex(0x0010, 32)
    ChrJumpTo(0x0010, 2780, 0, 10330, 300, 1000)
    Sleep(1000)

    ChrSetChipByIndex(0x0011, 9)
    ChrSetSubChip(0x0011, 0)
    Sleep(300)

    @scena.Lambda('lambda_9952')
    def lambda_9952():
        OP_99(0x0010, 0x00, 0x02, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_9952)

    OP_9E(0x0010, 20, 0, 400, 6000)

    ChrTalk(
        0x0010,
        (
            '#0130140480V#5P#117F呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140481V#087F#4P理查德，你这个懦夫！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140482V你若总是希望我再次出现来帮你，\n',
            '那就是你天大的错误了！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140483V你拥有那样优秀的能力，\n',
            '为何就不能靠自己去闯出一片天地呢！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140484V我不也是因为你坐镇军中，\n',
            '所以才安心地辞去了军务吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140485V#5P#113F上、上校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140486V#086F#4P我……并不是你想象的那样无所不能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140487V十年前，我也是因为有将军和你的帮助，\n',
            '所以才能和大家一起，取得最后的胜利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140488V其实，我只是一个不能保护自己最重要的人，\n',
            '最终选择了逃避现实的男人而已！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130140489V#5P#113F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140490V#003F……老爸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140491V#085F#4P不过……\n',
            '我已经不打算再逃避了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140492V#082F因此，理查德，\n',
            '你也不要像我那样继续逃避了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140493V在偿还自己犯下的罪孽的同时，\n',
            '好好反思一下自己还有哪些不足吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    TalkSetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，在众人的努力阻止之下，\n',
            '情报部发动的政变计划最后以失败告终。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '摩尔根将军和希德少校\n',
            '也成功收拾了王国军部队内部的混乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '参与发动这次政变的\n',
            '情报部相关人员也在王国各地相继被捕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '一周之后——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    MapClearFlags(0x02000000)
    OP_20(0x000007D0)
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x9DBE
@scena.Code('func_0A_9DBE')
def func_0A_9DBE():
    OP_66(0x0001)

    @scena.Lambda('lambda_9DC7')
    def lambda_9DC7():
        CameraMove(4690, 2000, -1350, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9DC7)

    @scena.Lambda('lambda_9DDF')
    def lambda_9DDF():
        OP_67(0, 2630, -27100, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9DDF)

    @scena.Lambda('lambda_9DF7')
    def lambda_9DF7():
        OP_6C(85000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9DF7)

    OP_7C(0, 51, 3000, 5000)
    OP_B0(0x0009, 0x14)
    OP_6F(0x0009, 296)
    OP_70(0x0009, 336)
    OP_73(0x0009)
    PlaySE(244, 0x00, 0x64)
    OP_B0(0x0009, 0x19)
    OP_6F(0x0009, 337)
    OP_70(0x0009, 407)
    Sleep(100)

    OP_7C(0, 100, 3000, 6000)

    @scena.Lambda('lambda_9E5A')
    def lambda_9E5A():
        CameraSetDistance(1110, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_9E5A)

    OP_73(0x0009)
    OP_B0(0x0009, 0x16)
    OP_6F(0x0009, 408)
    OP_70(0x0009, 445)
    OP_73(0x0009)
    OP_B0(0x0009, 0x13)
    OP_6F(0x0009, 446)
    OP_70(0x0009, 480)
    OP_73(0x0009)
    OP_B0(0x0009, 0x10)
    OP_6F(0x0009, 481)
    OP_70(0x0009, 494)
    OP_73(0x0009)

    @scena.Lambda('lambda_9EAC')
    def lambda_9EAC():
        CameraSetDistance(1300, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_9EAC)

    OP_71(0x0009, 0x0020)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 50)
    OP_70(0x0009, 69)

    Return()

# id: 0x000B offset: 0x9ECE
@scena.Code('func_0B_9ECE')
def func_0B_9ECE():
    ChrMoveTo(0x00FE, 2720, 0, 2110, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 28)
    Sleep(100)

    @scena.Lambda('lambda_9EFC')
    def lambda_9EFC():
        OP_99(0x00FE, 0x00, 0x01, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9EFC)

    ChrMoveTo(0x00FE, 4820, 2000, 790, 10000, 0x00)

    Return()

# id: 0x000C offset: 0x9F1B
@scena.Code('func_0C_9F1B')
def func_0C_9F1B():
    @scena.Lambda('lambda_9F21')
    def lambda_9F21():
        OP_99(0x00FE, 0x05, 0x0B, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9F21)

    ChrJumpTo(0x00FE, 4260, 0, 2930, 300, 10000)

    @scena.Lambda('lambda_9F48')
    def lambda_9F48():
        OP_99(0x00FE, 0x00, 0x01, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9F48)

    ChrMoveTo(0x00FE, 4820, 2000, 790, 10000, 0x00)

    Return()

# id: 0x000D offset: 0x9F67
@scena.Code('func_0D_9F67')
def func_0D_9F67():
    @scena.Lambda('lambda_9F6D')
    def lambda_9F6D():
        OP_99(0x00FE, 0x05, 0x0B, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9F6D)

    ChrJumpTo(0x00FE, 3310, 0, 1740, 300, 8000)

    Return()

# id: 0x000E offset: 0x9F8F
@scena.Code('func_0E_9F8F')
def func_0E_9F8F():
    Sleep(250)

    @scena.Lambda('lambda_9F9A')
    def lambda_9F9A():
        ChrJumpTo(0x00FE, 1410, 0, 3720, 500, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9F9A)

    Sleep(600)

    @scena.Lambda('lambda_9FBD')
    def lambda_9FBD():
        ChrJumpTo(0x00FE, 2570, 0, 4370, 300, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9FBD)

    Sleep(300)

    @scena.Lambda('lambda_9FE0')
    def lambda_9FE0():
        ChrJumpTo(0x00FE, 3330, 2890, 3960, 4000, 10000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9FE0)

    Return()

# id: 0x000F offset: 0x9FF9
@scena.Code('func_0F_9FF9')
def func_0F_9FF9():
    ChrSetFlags(0x00FE, 0x0004)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_A009')
    def lambda_A009():
        OP_99(0x00FE, 0x00, 0x01, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_A009)

    ChrJumpTo(0x00FE, 3350, 2450, 1360, 1000, 6000)

    Return()

# id: 0x0010 offset: 0xA02B
@scena.Code('func_10_A02B')
def func_10_A02B():
    @scena.Lambda('lambda_A031')
    def lambda_A031():
        OP_99(0x00FE, 0x05, 0x0B, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_A031)

    ChrJumpTo(0x00FE, 2300, 0, 3430, 300, 6000)

    Return()

# id: 0x0011 offset: 0xA053
@scena.Code('func_11_A053')
def func_11_A053():
    ChrSetPos(0x001A, 5140, 2450, 340, 0)
    PlayEffect(0x03, 0xFF, 0x0010, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)
    Sleep(200)

    ChrSetPos(0x001A, 5140, 2450, 340, 0)
    PlayEffect(0x03, 0xFF, 0x0010, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)
    Sleep(200)

    ChrSetPos(0x001A, 5140, 2450, 340, 0)
    PlayEffect(0x03, 0xFF, 0x0010, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)

    Return()

# id: 0x0012 offset: 0xA130
@scena.Code('func_12_A130')
def func_12_A130():
    ChrSetSubChip(0x00FE, 11)
    ChrSetPos(0x00FE, 740, 0, 1920, 46)
    ChrTurnDirection(0x00FE, 0x0017, 400)
    ChrJumpTo(0x00FE, 4480, 0, 730, 500, 4000)
    Sleep(50)

    @scena.Lambda('lambda_A16F')
    def lambda_A16F():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 3000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_A16F)

    OP_99(0x00FE, 0x00, 0x02, 2000)
    ChrSetFlags(0x00FE, 0x0002)

    @scena.Lambda('lambda_A19B')
    def lambda_A19B():
        OP_99(0x00FE, 0x20, 0x31, 3500)
        Yield()

        Jump('lambda_A19B')

    DispatchAsync2(0x00FE, 0x0002, lambda_A19B)

    WaitForThreadExit(0x00FE, 0x0001)
    TerminateThread(0x00FE, 0x02)
    ChrClearFlags(0x00FE, 0x0002)
    ChrTurnDirection(0x00FE, 0x0017, 0)

    @scena.Lambda('lambda_A1C3')
    def lambda_A1C3():
        OP_99(0x00FE, 0x05, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A1C3)

    Sleep(1000)

    ChrJumpTo(0x00FE, 780, 0, 4600, 500, 6000)
    ChrTurnDirection(0x00FE, 0x0017, 0)

    Return()

# id: 0x0013 offset: 0xA1F1
@scena.Code('func_13_A1F1')
def func_13_A1F1():
    ChrSetChipByIndex(0x00FE, 45)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, 100, -600, 3150, 0)

    @scena.Lambda('lambda_A226')
    def lambda_A226():
        OP_99(0x00FE, 0x00, 0x07, 3000)
        Yield()

        Jump('lambda_A226')

    DispatchAsync2(0x00FE, 0x0001, lambda_A226)

    ChrJumpTo(0x00FE, -4070, -600, 4059, 4000, 4000)
    TerminateThread(0x00FE, 0x01)
    ChrSetSubChip(0x00FE, 8)

    Return()

# id: 0x0014 offset: 0xA254
@scena.Code('func_14_A254')
def func_14_A254():
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 3590, 1600, 5110, 0)
    ChrSetChipByIndex(0x0010, 7)
    ChrSetSubChip(0x0010, 0)
    ChrJumpTo(0x0010, 4520, 0, 6090, 2000, 4000)
    ChrSetChipByIndex(0x0010, 32)
    ChrJumpTo(0x0010, 4790, 0, 6510, 400, 4000)
    ChrJumpToRelative(0x0010, 0, 0, 0, 200, 4000)

    Return()

# id: 0x0015 offset: 0xA2BF
@scena.Code('func_15_A2BF')
def func_15_A2BF():
    ChrSetChipByIndex(0x00FE, 34)
    ChrSetSubChip(0x00FE, 1)
    ChrSetPos(0x00FE, 260, 0, -8970, 154)
    ChrClearFlags(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetSubChip(0x00FE, 1)
    ChrWalkTo(0x00FE, 2320, 0, -1770, 10000, 0x00)
    ChrSetSubChip(0x00FE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A321',
    )

    PlaySE(163, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    def _loc_A321(): pass

    label('loc_A321')

    ChrJumpTo(0x00FE, 4480, 1820, 3340, 1900, 1000)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrSetSubChip(0x00FE, 1)

    @scena.Lambda('lambda_A346')
    def lambda_A346():
        ChrSetDirection(0x00FE, 77, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A346)

    ChrJumpTo(0x00FE, 1760, 0, -980, 200, 3000)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetSubChip(0x00FE, 10)

    Return()

# id: 0x0016 offset: 0xA370
@scena.Code('func_16_A370')
def func_16_A370():
    ChrSetSubChip(0x00FE, 4)

    @scena.Lambda('lambda_A37B')
    def lambda_A37B():
        ChrSetDirection(0x00FE, 170, 1200)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_A37B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A393',
    )

    PlaySE(163, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    def _loc_A393(): pass

    label('loc_A393')

    ChrJumpTo(0x00FE, 3710, 0, -2700, 500, 7000)
    TerminateThread(0x00FE, 0x03)
    ChrSetDirection(0x00FE, 90, 1200)
    ChrSetDirection(0x00FE, 180, 0)
    ChrSetSubChip(0x00FE, 5)
    ChrSetDirection(0x00FE, 135, 1200)
    Sleep(100)

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrSetDirection(0x00FE, 0, 1200)
    ChrSetDirection(0x00FE, 90, 400)
    ChrSetSubChip(0x00FE, 6)

    Return()

# id: 0x0017 offset: 0xA3E4
@scena.Code('func_17_A3E4')
def func_17_A3E4():
    ChrSetSubChip(0x00FE, 11)

    @scena.Lambda('lambda_A3EF')
    def lambda_A3EF():
        ChrSetDirection(0x00FE, 90, 800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_A3EF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A407',
    )

    PlaySE(163, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    def _loc_A407(): pass

    label('loc_A407')

    ChrJumpTo(0x00FE, 5690, 4600, -2090, 6000, 7000)
    ChrSetSubChip(0x00FE, 12)
    OP_A6(0x0007)
    Sleep(250)

    ChrMoveTo(0x00FE, 5420, 2230, -2530, 15000, 0x00)
    Sleep(500)

    ChrSetSubChip(0x00FE, 11)
    ChrJumpTo(0x00FE, 1380, 0, -990, 500, 4000)
    ChrSetSubChip(0x00FE, 6)

    Return()

# id: 0x0018 offset: 0xA466
@scena.Code('func_18_A466')
def func_18_A466():
    ChrSetSubChip(0x00FE, 7)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A47B',
    )

    PlaySE(163, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    def _loc_A47B(): pass

    label('loc_A47B')

    ChrJumpTo(0x00FE, 7600, 1730, -590, 3000, 12000)
    ChrSetSubChip(0x00FE, 6)

    Return()

# id: 0x0019 offset: 0xA498
@scena.Code('func_19_A498')
def func_19_A498():
    ChrSetChipByIndex(0x00FE, 34)
    ChrSetSubChip(0x00FE, 1)
    ChrSetPos(0x00FE, 260, 0, -8970, 154)
    ChrClearFlags(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetSubChip(0x00FE, 1)
    ChrWalkTo(0x00FE, 2320, 0, -1770, 10000, 0x00)
    ChrSetSubChip(0x00FE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A4FA',
    )

    PlaySE(163, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    def _loc_A4FA(): pass

    label('loc_A4FA')

    ChrJumpTo(0x00FE, 4480, 1820, 3340, 1900, 1000)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrSetSubChip(0x00FE, 1)

    @scena.Lambda('lambda_A51F')
    def lambda_A51F():
        ChrSetDirection(0x00FE, 77, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A51F)

    ChrJumpTo(0x00FE, 2900, 0, 5660, 200, 3000)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetSubChip(0x00FE, 10)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
