import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4303   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雪拉'),
    TXT(0x02, '奥利维尔'),
    TXT(0x03, '科洛丝'),
    TXT(0x04, '阿加特'),
    TXT(0x05, '提妲'),
    TXT(0x06, '金'),
    TXT(0x07, '拉赛尔博士'),
    TXT(0x08, '基库'),
    TXT(0x09, '理查德上校'),
    TXT(0x0A, '卡西乌斯'),
    TXT(0x0B, '机器'),
    TXT(0x0C, '机器'),
    TXT(0x0D, '机器'),
    TXT(0x0E, '机器'),
    TXT(0x0F, '　'),
    TXT(0x10, '　'),
    TXT(0x11, '　'),
    TXT(0x12, '　'),
    TXT(0x13, '　'),
    TXT(0x14, '　'),
    TXT(0x15, '　'),
    TXT(0x16, '　'),
    TXT(0x17, '　'),
    TXT(0x18, '　'),
    TXT(0x19, '　'),
    TXT(0x1A, ''),
]

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

# id: 0xFFFF offset: 0x9ECF
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

# id: 0x10001 offset: 0xEC
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

# id: 0x10002 offset: 0x266
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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

# id: 0x10003 offset: 0x586
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x586
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x586
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x586
@scena.Code('PreInit')
def PreInit():
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
    Event(0, 0x0006)

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
    Event(0, 0x0003)

    def _loc_5BC(): pass

    label('loc_5BC')

    Jump('loc_5BF')

    def _loc_5BF(): pass

    label('loc_5BF')

    Return()

# id: 0x0001 offset: 0x5C0
@scena.Code('Init')
def Init():
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

    Event(0, 0x0008)

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
@scena.Code('ReInit')
def ReInit():
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
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)

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

    SetChrChipByIndex(0x0103, 14)

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

    SetChrChipByIndex(0x0104, 16)
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

    SetChrChipByIndex(0x0106, 20)

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

    SetChrChipByIndex(0x0105, 18)

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

    SetChrChipByIndex(0x0107, 22)

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

    SetChrChipByIndex(0x0108, 24)

    def _loc_7F4(): pass

    label('loc_7F4')

    SetChrPos(0x0101, -1440, 0, -47330, 0)
    SetChrPos(0x0102, 720, 0, -47210, 0)

    @scena.Lambda('lambda_081C')
    def lambda_081C():
        SetChrDirection(0x0101, 45, 0)
        Yield()

        Jump('lambda_081C')

    DispatchAsync2(0x0010, 0x0001, lambda_081C)

    @scena.Lambda('lambda_082D')
    def lambda_082D():
        SetChrDirection(0x0102, 315, 0)
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

    SetChrPos(0x0000, 970, 0, -49020, 0)

    @scena.Lambda('lambda_08A4')
    def lambda_08A4():
        ChrWalkTo(0x00FE, 750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_08A4)

    Jump('loc_8E8')

    def _loc_8BC(): pass

    label('loc_8BC')

    SetChrPos(0x0000, -2029, 0, -48950, 0)

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

    SetChrPos(0x0001, 970, 0, -49020, 0)

    @scena.Lambda('lambda_091E')
    def lambda_091E():
        ChrWalkTo(0x00FE, 750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_091E)

    Jump('loc_962')

    def _loc_936(): pass

    label('loc_936')

    SetChrPos(0x0001, -2029, 0, -48950, 0)

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

    SetChrPos(0x0002, 970, 0, -49020, 0)

    @scena.Lambda('lambda_0998')
    def lambda_0998():
        ChrWalkTo(0x00FE, 750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_0998)

    Jump('loc_9DC')

    def _loc_9B0(): pass

    label('loc_9B0')

    SetChrPos(0x0002, -2029, 0, -48950, 0)

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

    SetChrPos(0x0003, 970, 0, -49020, 0)

    @scena.Lambda('lambda_0A12')
    def lambda_0A12():
        ChrWalkTo(0x00FE, 750, 0, 9730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_0A12)

    Jump('loc_A56')

    def _loc_A2A(): pass

    label('loc_A2A')

    SetChrPos(0x0003, -2029, 0, -48950, 0)

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
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 0, 600, 18060, 0)

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

    SetChrFlags(0x0010, 0x0020)
    SetChrDirection(0x0010, 180, 400)
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
        'loc_ED9',
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

    Jump('loc_FB9')

    def _loc_ED9(): pass

    label('loc_ED9')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F4B',
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

    Jump('loc_FB9')

    def _loc_F4B(): pass

    label('loc_F4B')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FB9',
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

    def _loc_FB9(): pass

    label('loc_FB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1027',
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

    def _loc_1027(): pass

    label('loc_1027')

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
        'loc_1983',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140213V#051F呵呵，真是肺腑之言啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1983(): pass

    label('loc_1983')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19DC',
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

    def _loc_19DC(): pass

    label('loc_19DC')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A25',
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

    def _loc_1A25(): pass

    label('loc_1A25')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A65',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140216V#071F哈哈，不愧是卡西乌斯大人的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A65(): pass

    label('loc_1A65')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AB0',
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

    def _loc_1AB0(): pass

    label('loc_1AB0')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B08',
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

    def _loc_1B08(): pass

    label('loc_1B08')

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
        'loc_20EC',
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

    Jump('loc_2240')

    def _loc_20EC(): pass

    label('loc_20EC')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_216B',
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

    Jump('loc_2240')

    def _loc_216B(): pass

    label('loc_216B')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21E8',
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

    Jump('loc_2240')

    def _loc_21E8(): pass

    label('loc_21E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2240',
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

    def _loc_2240(): pass

    label('loc_2240')

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

    @scena.Lambda('lambda_2315')
    def lambda_2315():
        CameraSetDistance(1290, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_2315)

    @scena.Lambda('lambda_2325')
    def lambda_2325():
        CameraMove(-100, 300, 15360, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2325)

    @scena.Lambda('lambda_233D')
    def lambda_233D():
        OP_67(0, 7570, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_233D)

    @scena.Lambda('lambda_2355')
    def lambda_2355():
        OP_6C(35000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2355)

    ChrSetRGBAMask(0x0012, 255, 0, 0, 0, 0)
    ChrSetRGBAMask(0x0013, 255, 0, 0, 0, 0)
    SetChrPos(0x0012, -2000, 7300, 15360, 180)
    SetChrPos(0x0013, 2000, 7300, 15360, 225)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0013, 0x0004)
    SetChrChipByIndex(0x0012, 27)
    SetChrChipByIndex(0x0013, 27)

    @scena.Lambda('lambda_23BB')
    def lambda_23BB():
        ChrJumpTo(0x00FE, -4000, 0, 15360, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_23BB)

    ChrSetRGBAMask(0x0012, 100, 100, 255, 255, 100)
    ChrSetRGBAMask(0x0012, 255, 255, 255, 255, 100)
    WaitForThreadExit(0x0012, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    OP_99(0x0012, 0x00, 0x07, 1500)
    SetChrChipByIndex(0x0012, 26)
    OP_99(0x0012, 0x00, 0x03, 2000)

    @scena.Lambda('lambda_2421')
    def lambda_2421():
        OP_99(0x00FE, 0x03, 0x07, 1300)
        Yield()

        Jump('lambda_2421')

    DispatchAsync2(0x0012, 0x0001, lambda_2421)

    @scena.Lambda('lambda_2434')
    def lambda_2434():
        ChrJumpTo(0x00FE, 4000, 0, 15360, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_2434)

    ChrSetRGBAMask(0x0013, 100, 100, 255, 255, 100)
    ChrSetRGBAMask(0x0013, 255, 255, 255, 255, 100)
    WaitForThreadExit(0x0013, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    OP_99(0x0013, 0x00, 0x07, 1500)
    SetChrChipByIndex(0x0013, 26)
    OP_99(0x0013, 0x00, 0x03, 2000)

    @scena.Lambda('lambda_249A')
    def lambda_249A():
        OP_99(0x00FE, 0x03, 0x07, 1300)
        Yield()

        Jump('lambda_249A')

    DispatchAsync2(0x0013, 0x0001, lambda_249A)

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

    @scena.Lambda('lambda_25AF')
    def lambda_25AF():
        CameraSetDistance(1000, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_25AF)

    @scena.Lambda('lambda_25BF')
    def lambda_25BF():
        OP_94(0x00, 0x00FE, 0x0000, 0x000001F4, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_25BF)

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

    SetChrChipByIndex(0x0010, 28)
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

    @scena.Lambda('lambda_269A')
    def lambda_269A():
        CameraMove(-100, 300, 17360, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_269A)

    @scena.Lambda('lambda_26B2')
    def lambda_26B2():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_26B2)

    Sleep(20)

    @scena.Lambda('lambda_26CC')
    def lambda_26CC():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_26CC)

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
        'loc_2734',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_271C',
    )

    Sleep(20)

    @scena.Lambda('lambda_270A')
    def lambda_270A():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_270A)

    Jump('loc_2731')

    def _loc_271C(): pass

    label('loc_271C')

    @scena.Lambda('lambda_2722')
    def lambda_2722():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_2722)

    def _loc_2731(): pass

    label('loc_2731')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2734(): pass

    label('loc_2734')

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
        'loc_2785',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_276D',
    )

    Sleep(20)

    @scena.Lambda('lambda_275B')
    def lambda_275B():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_275B)

    Jump('loc_2782')

    def _loc_276D(): pass

    label('loc_276D')

    @scena.Lambda('lambda_2773')
    def lambda_2773():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_2773)

    def _loc_2782(): pass

    label('loc_2782')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2785(): pass

    label('loc_2785')

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
        'loc_27D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_27BE',
    )

    Sleep(20)

    @scena.Lambda('lambda_27AC')
    def lambda_27AC():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_27AC)

    Jump('loc_27D3')

    def _loc_27BE(): pass

    label('loc_27BE')

    @scena.Lambda('lambda_27C4')
    def lambda_27C4():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_27C4)

    def _loc_27D3(): pass

    label('loc_27D3')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_27D6(): pass

    label('loc_27D6')

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
        'loc_2827',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_280F',
    )

    Sleep(20)

    @scena.Lambda('lambda_27FD')
    def lambda_27FD():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_27FD)

    Jump('loc_2824')

    def _loc_280F(): pass

    label('loc_280F')

    @scena.Lambda('lambda_2815')
    def lambda_2815():
        OP_92(0x00FE, 0x0010, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_2815)

    def _loc_2824(): pass

    label('loc_2824')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2827(): pass

    label('loc_2827')

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
        (0x00000001, 'loc_285B'),
        (-1, 'loc_285E'),
    )

    def _loc_285B(): pass

    label('loc_285B')

    OP_B4(0x00)

    Return()

    def _loc_285E(): pass

    label('loc_285E')

    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x288B
@scena.Code('func_04_288B')
def func_04_288B():
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
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0010, 29)
    SetChrPos(0x0010, -710, 300, 15890, 180)
    SetChrPos(0x0101, -760, 0, 12210, 7)
    SetChrPos(0x0102, 530, 0, 12680, 344)
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
        'loc_2996',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2982',
    )

    SetChrPos(0x0000, -2370, 0, 13570, 34)

    Jump('loc_2993')

    def _loc_2982(): pass

    label('loc_2982')

    SetChrPos(0x0000, 1960, 0, 13940, 319)

    def _loc_2993(): pass

    label('loc_2993')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2996(): pass

    label('loc_2996')

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
        'loc_29DA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_29C6',
    )

    SetChrPos(0x0001, -2370, 0, 13570, 34)

    Jump('loc_29D7')

    def _loc_29C6(): pass

    label('loc_29C6')

    SetChrPos(0x0001, 1960, 0, 13940, 319)

    def _loc_29D7(): pass

    label('loc_29D7')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_29DA(): pass

    label('loc_29DA')

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
        'loc_2A1E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2A0A',
    )

    SetChrPos(0x0002, -2370, 0, 13570, 34)

    Jump('loc_2A1B')

    def _loc_2A0A(): pass

    label('loc_2A0A')

    SetChrPos(0x0002, 1960, 0, 13940, 319)

    def _loc_2A1B(): pass

    label('loc_2A1B')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2A1E(): pass

    label('loc_2A1E')

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
        'loc_2A62',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2A4E',
    )

    SetChrPos(0x0003, -2370, 0, 13570, 34)

    Jump('loc_2A5F')

    def _loc_2A4E(): pass

    label('loc_2A4E')

    SetChrPos(0x0003, 1960, 0, 13940, 319)

    def _loc_2A5F(): pass

    label('loc_2A5F')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2A62(): pass

    label('loc_2A62')

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

    @scena.Lambda('lambda_2B5C')
    def lambda_2B5C():
        CameraMove(200, 2560, 18960, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2B5C)

    @scena.Lambda('lambda_2B74')
    def lambda_2B74():
        OP_67(0, 5560, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B74)

    @scena.Lambda('lambda_2B8C')
    def lambda_2B8C():
        OP_6C(338000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2B8C)

    @scena.Lambda('lambda_2B9C')
    def lambda_2B9C():
        OP_6E(455, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2B9C)

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

    @scena.Lambda('lambda_2CB4')
    def lambda_2CB4():
        OP_7C(0, 300, 3000, 3000)
        Yield()

        Jump('lambda_2CB4')

    DispatchAsync2(0x0010, 0x0001, lambda_2CB4)

    Sleep(2000)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CFF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070140268V#068F#5P呀啊啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CFF(): pass

    label('loc_2CFF')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D32',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140269V#550F#5P可恶，这是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D32(): pass

    label('loc_2D32')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D69',
    )

    ChrTalk(
        0x0104,
        (
            '#0040140270V#039F#5P这就是传说中的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D69(): pass

    label('loc_2D69')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DB7',
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

    def _loc_2DB7(): pass

    label('loc_2DB7')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DF2',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140272V#077F#5P这是……『阴』的气息吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DF2(): pass

    label('loc_2DF2')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E34',
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

    def _loc_2E34(): pass

    label('loc_2E34')

    @scena.Lambda('lambda_2E3A')
    def lambda_2E3A():
        CameraMove(-5080, 5590, -6070, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2E3A)

    @scena.Lambda('lambda_2E52')
    def lambda_2E52():
        OP_67(0, 4890, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E52)

    @scena.Lambda('lambda_2E6A')
    def lambda_2E6A():
        CameraSetDistance(4730, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E6A)

    @scena.Lambda('lambda_2E7A')
    def lambda_2E7A():
        OP_6C(44000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2E7A)

    @scena.Lambda('lambda_2E8A')
    def lambda_2E8A():
        OP_6E(478, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_2E8A)

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

    SetMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x2FC3
@scena.Code('func_05_2FC3')
def func_05_2FC3():
    ChrSetRGBAMask(0x00FE, 100, 100, 255, 255, 1000)

    @scena.Lambda('lambda_2FD4')
    def lambda_2FD4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_2FD4)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x00FE, 27)
    OP_99(0x00FE, 0x00, 0x07, 2000)

    Return()

# id: 0x0006 offset: 0x2FFA
@scena.Code('func_06_2FFA')
def func_06_2FFA():
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
    ClearChrFlags(0x0010, 0x0080)

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0010, 29)
    SetChrPos(0x0010, -710, 300, 15890, 180)
    SetChrPos(0x0101, -760, 0, 12210, 7)
    SetChrPos(0x0102, 530, 0, 12680, 344)
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
        'loc_30D1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_30BD',
    )

    SetChrPos(0x0000, -2370, 0, 13570, 34)

    Jump('loc_30CE')

    def _loc_30BD(): pass

    label('loc_30BD')

    SetChrPos(0x0000, 1960, 0, 13940, 319)

    def _loc_30CE(): pass

    label('loc_30CE')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_30D1(): pass

    label('loc_30D1')

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
        'loc_3115',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3101',
    )

    SetChrPos(0x0001, -2370, 0, 13570, 34)

    Jump('loc_3112')

    def _loc_3101(): pass

    label('loc_3101')

    SetChrPos(0x0001, 1960, 0, 13940, 319)

    def _loc_3112(): pass

    label('loc_3112')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_3115(): pass

    label('loc_3115')

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
        'loc_3159',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3145',
    )

    SetChrPos(0x0002, -2370, 0, 13570, 34)

    Jump('loc_3156')

    def _loc_3145(): pass

    label('loc_3145')

    SetChrPos(0x0002, 1960, 0, 13940, 319)

    def _loc_3156(): pass

    label('loc_3156')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_3159(): pass

    label('loc_3159')

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
        'loc_319D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3189',
    )

    SetChrPos(0x0003, -2370, 0, 13570, 34)

    Jump('loc_319A')

    def _loc_3189(): pass

    label('loc_3189')

    SetChrPos(0x0003, 1960, 0, 13940, 319)

    def _loc_319A(): pass

    label('loc_319A')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_319D(): pass

    label('loc_319D')

    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31BA',
    )

    SetChrChipByIndex(0x0103, 14)

    def _loc_31BA(): pass

    label('loc_31BA')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31CD',
    )

    SetChrChipByIndex(0x0104, 16)

    def _loc_31CD(): pass

    label('loc_31CD')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31E0',
    )

    SetChrChipByIndex(0x0106, 20)

    def _loc_31E0(): pass

    label('loc_31E0')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31F3',
    )

    SetChrChipByIndex(0x0105, 18)

    def _loc_31F3(): pass

    label('loc_31F3')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3206',
    )

    SetChrChipByIndex(0x0107, 22)

    def _loc_3206(): pass

    label('loc_3206')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3219',
    )

    SetChrChipByIndex(0x0108, 24)

    def _loc_3219(): pass

    label('loc_3219')

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

    @scena.Lambda('lambda_332B')
    def lambda_332B():
        CameraMove(-560, 1650, 16460, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_332B)

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
    SetChrName('声音')

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
    SetChrName('声音')

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

    @scena.Lambda('lambda_3540')
    def lambda_3540():
        CameraMove(2820, 0, 40, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3540)

    @scena.Lambda('lambda_3558')
    def lambda_3558():
        OP_67(0, 19430, -25720, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3558)

    @scena.Lambda('lambda_3570')
    def lambda_3570():
        CameraSetDistance(1410, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3570)

    @scena.Lambda('lambda_3580')
    def lambda_3580():
        OP_6C(90000, 11000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_3580)

    @scena.Lambda('lambda_3590')
    def lambda_3590():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_3590)

    @scena.Lambda('lambda_359E')
    def lambda_359E():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_359E)

    @scena.Lambda('lambda_35AC')
    def lambda_35AC():
        SetChrDirection(0x00FE, 132, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_35AC)

    @scena.Lambda('lambda_35BA')
    def lambda_35BA():
        SetChrDirection(0x00FE, 222, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_35BA)

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

    @scena.Lambda('lambda_3645')
    def lambda_3645():
        OP_67(0, 13510, -25720, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3645)

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
    SetChrName('声音')

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

    @scena.Lambda('lambda_388A')
    def lambda_388A():
        SetChrDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_388A)

    @scena.Lambda('lambda_3898')
    def lambda_3898():
        SetChrDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_3898)

    @scena.Lambda('lambda_38A6')
    def lambda_38A6():
        SetChrDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_38A6)

    @scena.Lambda('lambda_38B4')
    def lambda_38B4():
        SetChrDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_38B4)

    @scena.Lambda('lambda_38C2')
    def lambda_38C2():
        CameraMove(21480, 4400, 50, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38C2)

    @scena.Lambda('lambda_38DA')
    def lambda_38DA():
        OP_6E(1000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_38DA)

    @scena.Lambda('lambda_38EA')
    def lambda_38EA():
        OP_67(300, 4890, 20, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_38EA)

    SetMapFlags(0x00000010)
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

    SetChrFlags(0x0017, 0x0040)
    SetChrFlags(0x0018, 0x0040)
    SetChrFlags(0x0019, 0x0040)
    SetChrFlags(0x0017, 0x0004)
    SetChrFlags(0x0018, 0x0004)
    SetChrFlags(0x0019, 0x0004)
    OP_A1(0x0017, 0x0007)
    OP_A1(0x0018, 0x000A)
    OP_A1(0x0019, 0x000B)
    OP_72(0x0007, 0x0004)
    OP_71(0x0007, 0x0020)
    OP_6F(0x0007, 40)
    OP_70(0x0007, 59)
    SetChrPos(0x0017, 49760, 0, 0, 90)
    SetChrPos(0x0018, 36600, 3000, 4140, 90)
    SetChrPos(0x0019, 36600, 3000, -4140, 90)
    PlaySE(187, 0x00, 0x64)
    OP_B0(0x0004, 0x50)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 1000)

    @scena.Lambda('lambda_39D9')
    def lambda_39D9():
        CameraSetDistance(210, 14000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_39D9)

    @scena.Lambda('lambda_39E9')
    def lambda_39E9():
        OP_6E(180, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_39E9)

    Sleep(7000)

    OP_20(0x00000BB8)

    @scena.Lambda('lambda_3A03')
    def lambda_3A03():
        ChrMoveTo(0x00FE, 11400, 4000, 3300, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0000, lambda_3A03)

    @scena.Lambda('lambda_3A1E')
    def lambda_3A1E():
        ChrMoveTo(0x00FE, 11400, 4000, -3300, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0000, lambda_3A1E)

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

    @scena.Lambda('lambda_3B42')
    def lambda_3B42():
        OP_67(300, -500, 20, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3B42)

    @scena.Lambda('lambda_3B5A')
    def lambda_3B5A():
        CameraMove(16980, 3210, 0, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3B5A)

    @scena.Lambda('lambda_3B72')
    def lambda_3B72():
        CameraSetDistance(700, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3B72)

    @scena.Lambda('lambda_3B82')
    def lambda_3B82():
        OP_6E(730, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3B82)

    Sleep(1000)

    CreateThread(0x0017, 0x03, 0x00, 0x0007)
    WaitForThreadExit(0x0018, 0x0000)

    @scena.Lambda('lambda_3BA3')
    def lambda_3BA3():
        SetChrDirection(0x00FE, 45, 80)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_3BA3)

    @scena.Lambda('lambda_3BB1')
    def lambda_3BB1():
        ChrMoveTo(0x00FE, 10000, 3000, 6800, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0000, lambda_3BB1)

    WaitForThreadExit(0x0019, 0x0000)

    @scena.Lambda('lambda_3BD1')
    def lambda_3BD1():
        SetChrDirection(0x00FE, 135, 80)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_3BD1)

    @scena.Lambda('lambda_3BDF')
    def lambda_3BDF():
        ChrMoveTo(0x00FE, 10000, 3000, -6800, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0000, lambda_3BDF)

    OP_72(0x000A, 0x0004)
    OP_72(0x000B, 0x0004)
    WaitForThreadExit(0x0017, 0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0xFF)
    Fade(1500)
    OP_66(0x0001)
    SetChrPos(0x0000, 3380, 0, 950, 90)
    SetChrPos(0x0001, 3480, 0, -870, 90)
    SetChrPos(0x0003, 1900, 0, 2270, 90)
    SetChrPos(0x0002, 2520, 0, -2190, 90)
    ClearMapFlags(0x00000010)
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
        'loc_3D4C',
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

    def _loc_3D4C(): pass

    label('loc_3D4C')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D90',
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

    def _loc_3D90(): pass

    label('loc_3D90')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DD4',
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

    def _loc_3DD4(): pass

    label('loc_3DD4')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E1E',
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

    def _loc_3E1E(): pass

    label('loc_3E1E')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E5C',
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

    def _loc_3E5C(): pass

    label('loc_3E5C')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3EA6',
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

    def _loc_3EA6(): pass

    label('loc_3EA6')

    WaitForThreadExit(0x0000, 0x0000)
    OP_72(0x0007, 0x0020)
    OP_73(0x0007)

    @scena.Lambda('lambda_3EB9')
    def lambda_3EB9():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3EB9)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('合成音')

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
    SetChrFlags(0x0017, 0x0004)

    @scena.Lambda('lambda_422F')
    def lambda_422F():
        ChrMoveToRelativeAsync(0x0017, -12000, -6000, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_422F)

    @scena.Lambda('lambda_424A')
    def lambda_424A():
        CameraMove(8900, 5600, 110, 500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_424A)

    @scena.Lambda('lambda_4262')
    def lambda_4262():
        CameraSetDistance(1380, 500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4262)

    @scena.Lambda('lambda_4272')
    def lambda_4272():
        OP_67(0, -130, -18290, 500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4272)

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

# id: 0x0007 offset: 0x42B2
@scena.Code('func_07_42B2')
def func_07_42B2():
    OP_B0(0x0007, 0x0B)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_42C0(): pass

    label('loc_42C0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_43E0',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_42DD')
    def lambda_42DD():
        ChrMoveTo(0x00FE, 16100, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_42DD)

    OP_B0(0x0007, 0x0A)
    OP_6F(0x0007, 141)
    OP_70(0x0007, 146)
    OP_73(0x0007)

    @scena.Lambda('lambda_430D')
    def lambda_430D():
        ChrMoveTo(0x00FE, 16100, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_430D)

    OP_B0(0x0007, 0x0F)
    OP_6F(0x0007, 147)
    OP_70(0x0007, 150)
    OP_73(0x0007)
    PlaySE(236, 0x00, 0x64)
    OP_7C(0, 300, 3000, 100)
    OP_4A(0x0017, 0)
    Sleep(100)

    OP_4B(0x0017, 0)

    @scena.Lambda('lambda_4360')
    def lambda_4360():
        ChrMoveTo(0x00FE, 16100, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_4360)

    OP_B0(0x0007, 0x0A)
    OP_6F(0x0007, 151)
    OP_70(0x0007, 156)
    OP_73(0x0007)

    @scena.Lambda('lambda_4390')
    def lambda_4390():
        ChrMoveTo(0x00FE, 16100, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_4390)

    OP_B0(0x0007, 0x0F)
    OP_6F(0x0007, 157)
    OP_70(0x0007, 159)
    OP_73(0x0007)
    PlaySE(236, 0x00, 0x64)
    OP_7C(0, 300, 3000, 100)
    OP_4A(0x0017, 0)
    Sleep(100)

    OP_4B(0x0017, 0)

    Jump('loc_42C0')

    def _loc_43E0(): pass

    label('loc_43E0')

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

# id: 0x0008 offset: 0x4416
@scena.Code('func_08_4416')
def func_08_4416():
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
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_44E5',
    )

    SetChrChipByIndex(0x0103, 14)

    def _loc_44E5(): pass

    label('loc_44E5')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_44F8',
    )

    SetChrChipByIndex(0x0104, 16)

    def _loc_44F8(): pass

    label('loc_44F8')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_450B',
    )

    SetChrChipByIndex(0x0106, 20)

    def _loc_450B(): pass

    label('loc_450B')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_451E',
    )

    SetChrChipByIndex(0x0105, 18)

    def _loc_451E(): pass

    label('loc_451E')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4531',
    )

    SetChrChipByIndex(0x0107, 22)

    def _loc_4531(): pass

    label('loc_4531')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4544',
    )

    SetChrChipByIndex(0x0108, 24)

    def _loc_4544(): pass

    label('loc_4544')

    SetChrPos(0x0017, 5900, 0, -30, 90)
    SetChrPos(0x0000, -6050, 0, -660, 90)
    SetChrPos(0x0001, -6050, 0, 660, 90)
    SetChrPos(0x0002, -4270, 0, -2020, 90)
    SetChrPos(0x0003, -4270, 0, 2020, 90)
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

    @scena.Lambda('lambda_4641')
    def lambda_4641():
        OP_6C(90000, 11000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4641)

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

    @scena.Lambda('lambda_46D0')
    def lambda_46D0():
        CameraMove(5470, 3000, -180, 5500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_46D0)

    @scena.Lambda('lambda_46E8')
    def lambda_46E8():
        CameraSetDistance(3390, 600)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_46E8)

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

    @scena.Lambda('lambda_4755')
    def lambda_4755():
        CameraSetDistance(1870, 3500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4755)

    OP_6F(0x0008, 112)
    OP_70(0x0008, 151)
    OP_73(0x0008)
    OP_7C(0, 600, 3000, 100)
    TerminateThread(0x0000, 0x03)

    @scena.Lambda('lambda_478B')
    def lambda_478B():
        OP_67(0, 160, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_478B)

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

    @scena.Lambda('lambda_47D8')
    def lambda_47D8():
        CameraSetDistance(1870, 2600)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_47D8)

    OP_6F(0x0008, 175)
    OP_70(0x0008, 206)
    OP_73(0x0008)
    PlaySE(242, 0x00, 0x64)

    @scena.Lambda('lambda_47FE')
    def lambda_47FE():
        OP_6E(651, 300)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_47FE)

    @scena.Lambda('lambda_480E')
    def lambda_480E():
        CameraSetDistance(3200, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_480E)

    OP_7C(0, 300, 3000, 100)
    OP_6F(0x0008, 207)
    OP_70(0x0008, 250)
    Sleep(300)

    @scena.Lambda('lambda_4842')
    def lambda_4842():
        OP_6E(409, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4842)

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
    SetChrName('合成音')

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

    @scena.Lambda('lambda_49B0')
    def lambda_49B0():
        OP_67(0, 4190, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_49B0)

    @scena.Lambda('lambda_49C8')
    def lambda_49C8():
        CameraSetDistance(2400, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_49C8)

    OP_6F(0x0008, 320)
    OP_70(0x0008, 334)
    OP_73(0x0008)
    LoadEffect(0x04, 'map\\\\mp021_04.eff')
    PlayEffect(0x04, 0xFF, 0x00FF, 5470, 3000, -180, 0, 90, 0, 7000, 7000, 7000, 0x00FF, 0, 0, 0, 0)
    PlaySE(243, 0x00, 0x64)

    @scena.Lambda('lambda_4A37')
    def lambda_4A37():
        CameraSetDistance(6000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4A37)

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
        (0x00000001, 'loc_4A8B'),
        (-1, 'loc_4A8E'),
    )

    def _loc_4A8B(): pass

    label('loc_4A8B')

    OP_B4(0x00)

    Return()

    def _loc_4A8E(): pass

    label('loc_4A8E')

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0x4),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_4A9D',
    )

    WaitEffect(0x19, 0x01)

    def _loc_4A9D(): pass

    label('loc_4A9D')

    OP_71(0x0008, 0x0004)
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0x4AA7
@scena.Code('func_09_4AA7')
def func_09_4AA7():
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
    SetChrPos(0x0017, 5900, 0, -30, 75)
    SetChrPos(0x0010, -4780, 0, 6090, 137)
    SetChrFlags(0x0010, 0x0080)

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0010, 29)
    FormationDelMember(0x00, 0xFF)
    FormationDelMember(0x01, 0xFF)
    FormationAddMember(0x00, 0xFF)
    FormationAddMember(0x01, 0xFF)
    SetChrPos(0x0101, -2910, 0, -3850, 47)
    SetChrPos(0x0102, -1740, 0, -6390, 6)
    SetChrPos(0x0000, -4710, 0, 610, 127)
    SetChrPos(0x0001, -5270, 0, -1970, 111)
    SetChrChipByIndex(0x0101, 37)
    SetChrChipByIndex(0x0102, 38)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C0B',
    )

    SetChrChipByIndex(0x0103, 39)

    def _loc_4C0B(): pass

    label('loc_4C0B')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C1E',
    )

    SetChrChipByIndex(0x0104, 40)

    def _loc_4C1E(): pass

    label('loc_4C1E')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C31',
    )

    SetChrChipByIndex(0x0106, 42)

    def _loc_4C31(): pass

    label('loc_4C31')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C44',
    )

    SetChrChipByIndex(0x0105, 41)

    def _loc_4C44(): pass

    label('loc_4C44')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C57',
    )

    SetChrChipByIndex(0x0107, 43)

    def _loc_4C57(): pass

    label('loc_4C57')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C6A',
    )

    SetChrChipByIndex(0x0108, 44)

    def _loc_4C6A(): pass

    label('loc_4C6A')

    SetChrSubChip(0x0000, 3)
    SetChrSubChip(0x0001, 3)
    SetChrSubChip(0x0002, 3)
    SetChrSubChip(0x0003, 3)
    LoadEffect(0x00, 'monster\\\\ms10000.eff')
    LoadEffect(0x01, 'monster\\\\ms10001.eff')
    LoadEffect(0x02, 'monster\\\\ms10002.eff')
    LoadEffect(0x03, 'monster\\msc0270b.eff')

    @scena.Lambda('lambda_4CE0')
    def lambda_4CE0():
        CameraSetDistance(2530, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_4CE0)

    @scena.Lambda('lambda_4CF0')
    def lambda_4CF0():
        OP_6C(69000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4CF0)

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
    ClearChrFlags(0x0010, 0x0080)
    SetChrChipByIndex(0x0010, 36)
    SetChrSubChip(0x0010, 0)
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

    @scena.Lambda('lambda_5011')
    def lambda_5011():
        CameraMove(1630, 550, -840, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5011)

    CreateThread(0x0017, 0x01, 0x00, 0x000A)
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
        'loc_5076',
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

    Jump('loc_51C9')

    def _loc_5076(): pass

    label('loc_5076')

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
        'loc_50C2',
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

    Jump('loc_51C9')

    def _loc_50C2(): pass

    label('loc_50C2')

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
        'loc_5108',
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

    Jump('loc_51C9')

    def _loc_5108(): pass

    label('loc_5108')

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
        'loc_514B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070140326V#069F#5P啊，我已经站不起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51C9')

    def _loc_514B(): pass

    label('loc_514B')

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
        'loc_518A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140327V#077F#5P呜……还是不行吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51C9')

    def _loc_518A(): pass

    label('loc_518A')

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
        'loc_51C9',
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

    def _loc_51C9(): pass

    label('loc_51C9')

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

    @scena.Lambda('lambda_521F')
    def lambda_521F():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_521F')

    DispatchAsync2(0x0102, 0x0002, lambda_521F)

    SetChrChipByIndex(0x0102, 12)
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

    @scena.Lambda('lambda_5274')
    def lambda_5274():
        OP_6C(70000, 1700)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5274)

    @scena.Lambda('lambda_5284')
    def lambda_5284():
        OP_67(0, -1770, -30160, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_5284)

    @scena.Lambda('lambda_529C')
    def lambda_529C():
        CameraMove(2730, 3000, -2190, 1700)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_529C)

    @scena.Lambda('lambda_52B4')
    def lambda_52B4():
        CameraSetDistance(770, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_52B4)

    OP_73(0x0009)
    OP_B0(0x0009, 0x06)
    OP_6F(0x0009, 214)
    OP_70(0x0009, 221)
    OP_73(0x0009)
    WaitForThreadExit(0x0000, 0x0001)
    SetChrPos(0x001A, 1980, 5000, 1220, 0)
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

    SetChrChipByIndex(0x0010, 28)
    SetChrPos(0x0010, -440, 0, 4310, 119)
    SetChrPos(0x001B, -440, 0, 4310, 119)
    SetChrPos(0x001C, -440, 0, 4310, 119)
    SetChrPos(0x001D, -440, 0, 4310, 119)
    SetChrPos(0x001E, -440, 0, 4310, 119)

    @scena.Lambda('lambda_53BA')
    def lambda_53BA():
        CameraMove(1680, 1900, 600, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_53BA)

    @scena.Lambda('lambda_53D2')
    def lambda_53D2():
        OP_67(0, 12070, -30160, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_53D2)

    @scena.Lambda('lambda_53EA')
    def lambda_53EA():
        CameraSetDistance(740, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_53EA)

    @scena.Lambda('lambda_53FA')
    def lambda_53FA():
        OP_6C(18000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_53FA)

    @scena.Lambda('lambda_540A')
    def lambda_540A():
        OP_6E(512, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_540A)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_7C(0, 600, 3000, 100)

    @scena.Lambda('lambda_5434')
    def lambda_5434():
        SetChrDirection(0x00FE, 120, 50)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_5434)

    SetChrDirection(0x0017, 110, 0)
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
    SetChrFlags(0x001B, 0x0004)
    SetChrFlags(0x001C, 0x0004)
    SetChrFlags(0x001D, 0x0004)
    SetChrFlags(0x001E, 0x0004)
    SetChrFlags(0x0010, 0x0004)
    ChrSetRGBAMask(0x001B, 255, 255, 255, 200, 0)
    ChrSetRGBAMask(0x001C, 255, 255, 255, 150, 0)
    ChrSetRGBAMask(0x001D, 255, 255, 255, 100, 0)
    ChrSetRGBAMask(0x001E, 255, 255, 255, 50, 0)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001B, 0x0040)
    SetChrFlags(0x001C, 0x0040)
    SetChrFlags(0x001D, 0x0040)
    SetChrFlags(0x001E, 0x0040)
    SetChrFlags(0x0010, 0x0040)
    SetChrChipByIndex(0x0010, 8)
    SetChrChipByIndex(0x001B, 8)
    SetChrChipByIndex(0x001C, 8)
    SetChrChipByIndex(0x001D, 8)
    SetChrChipByIndex(0x001E, 8)

    @scena.Lambda('lambda_564D')
    def lambda_564D():
        ChrWalkTo(0x00FE, 3510, 0, 1230, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_564D)

    Sleep(50)

    @scena.Lambda('lambda_566D')
    def lambda_566D():
        ChrWalkTo(0x00FE, 3510, 0, 1230, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0000, lambda_566D)

    Sleep(50)

    @scena.Lambda('lambda_568D')
    def lambda_568D():
        ChrWalkTo(0x00FE, 3510, 0, 1230, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0000, lambda_568D)

    Sleep(50)

    @scena.Lambda('lambda_56AD')
    def lambda_56AD():
        ChrWalkTo(0x00FE, 3510, 0, 1230, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0000, lambda_56AD)

    Sleep(50)

    @scena.Lambda('lambda_56CD')
    def lambda_56CD():
        ChrWalkTo(0x00FE, 3510, 0, 1230, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0000, lambda_56CD)

    WaitForThreadExit(0x0010, 0x0000)
    Fade(1000)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CameraMove(6200, 3370, 160, 0)
    OP_67(0, 12070, -30160, 0)
    CameraSetDistance(850, 0)
    OP_6C(152000, 0)
    OP_6E(512, 0)

    @scena.Lambda('lambda_5769')
    def lambda_5769():
        CameraMove(5750, 2370, -170, 15000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_5769)

    @scena.Lambda('lambda_5781')
    def lambda_5781():
        OP_67(0, 4050, -30160, 15000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5781)

    @scena.Lambda('lambda_5799')
    def lambda_5799():
        CameraSetDistance(970, 15000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_5799)

    @scena.Lambda('lambda_57A9')
    def lambda_57A9():
        OP_6C(97000, 15000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_57A9)

    @scena.Lambda('lambda_57B9')
    def lambda_57B9():
        OP_6E(561, 15000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_57B9)

    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x0010, 0xFF)
    SetChrChipByIndex(0x001B, 8)
    SetChrChipByIndex(0x001C, 8)
    SetChrChipByIndex(0x001D, 8)
    SetChrChipByIndex(0x001E, 8)
    SetChrChipByIndex(0x0010, 8)
    SetChrPos(0x001B, 5370, 0, 710, 139)
    SetChrPos(0x001C, 5370, 0, 710, 139)
    SetChrPos(0x001D, 5370, 0, 710, 139)
    SetChrPos(0x001E, 5370, 0, 710, 139)
    SetChrPos(0x0010, 5370, 0, 710, 139)
    OP_72(0x0009, 0x0020)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 126)
    CreateThread(0x0010, 0x00, 0x00, 0x000B)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, 0x000B)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, 0x000B)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, 0x000B)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, 0x000B)
    WaitForThreadExit(0x0010, 0x0000)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_B0(0x0009, 0x1E)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 126)
    CreateThread(0x0010, 0x00, 0x00, 0x000C)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, 0x000C)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, 0x000C)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, 0x000C)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, 0x000C)
    WaitForThreadExit(0x0010, 0x0000)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_B0(0x0009, 0x1E)
    OP_6F(0x0009, 105)
    OP_70(0x0009, 126)
    CreateThread(0x0010, 0x00, 0x00, 0x000D)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, 0x000D)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, 0x000D)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, 0x000D)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, 0x000D)
    WaitForThreadExit(0x0010, 0x0000)
    OP_73(0x0009)
    OP_B0(0x0009, 0x0F)
    OP_73(0x0009)
    OP_6F(0x0009, 510)
    OP_70(0x0009, 530)
    CreateThread(0x0010, 0x00, 0x00, 0x000E)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, 0x000E)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, 0x000E)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, 0x000E)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, 0x000E)
    Sleep(600)

    PlaySE(237, 0x00, 0x64)
    OP_73(0x0009)
    PlaySE(85, 0x00, 0x64)
    OP_7C(0, 1000, 3000, 100)
    CreateThread(0x0010, 0x00, 0x00, 0x000F)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, 0x000F)
    Sleep(50)

    OP_7C(0, 200, 3000, 3000)
    CreateThread(0x001C, 0x00, 0x00, 0x000F)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, 0x000F)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, 0x000F)
    WaitForThreadExit(0x0010, 0x0000)
    OP_7C(0, 1, 3000, 10)
    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 3900, 3300, 1120, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0009, 227)
    OP_70(0x0009, 254)
    CreateThread(0x0010, 0x00, 0x00, 0x0010)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, 0x0010)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, 0x0010)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, 0x0010)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, 0x0010)
    WaitForThreadExit(0x0010, 0x0000)
    OP_73(0x0009)
    CreateThread(0x0010, 0x00, 0x00, 0x0011)
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

    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)

    @scena.Lambda('lambda_5B82')
    def lambda_5B82():
        SetChrDirection(0x00FE, 46, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5B82)

    Sleep(650)

    PlaySE(237, 0x00, 0x64)
    OP_73(0x0009)
    OP_6F(0x0009, 227)
    OP_70(0x0009, 254)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_5BB0')
    def lambda_5BB0():
        ChrMoveTo(0x00FE, 740, 0, 1920, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5BB0)

    SetChrSubChip(0x0010, 7)
    Sleep(200)

    @scena.Lambda('lambda_5BD5')
    def lambda_5BD5():
        ChrMoveTo(0x00FE, 740, 0, 1920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5BD5)

    Sleep(200)

    @scena.Lambda('lambda_5BF5')
    def lambda_5BF5():
        ChrMoveTo(0x00FE, 740, 0, 1920, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5BF5)

    Sleep(200)

    @scena.Lambda('lambda_5C15')
    def lambda_5C15():
        ChrMoveTo(0x00FE, 740, 0, 1920, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5C15)

    @scena.Lambda('lambda_5C30')
    def lambda_5C30():
        OP_99(0x00FE, 0x07, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_5C30)

    Sleep(500)

    CreateThread(0x0010, 0x00, 0x00, 0x0012)
    Sleep(50)

    ClearChrFlags(0x001B, 0x0080)
    CreateThread(0x001B, 0x00, 0x00, 0x0012)
    Sleep(50)

    ClearChrFlags(0x001C, 0x0080)
    CreateThread(0x001C, 0x00, 0x00, 0x0012)
    Sleep(50)

    ClearChrFlags(0x001D, 0x0080)
    CreateThread(0x001D, 0x00, 0x00, 0x0012)
    Sleep(50)

    ClearChrFlags(0x001E, 0x0080)
    CreateThread(0x001E, 0x00, 0x00, 0x0012)
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
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
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

    @scena.Lambda('lambda_5EF9')
    def lambda_5EF9():
        CameraSetDistance(640, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_5EF9)

    @scena.Lambda('lambda_5F09')
    def lambda_5F09():
        OP_6C(139000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_5F09)

    @scena.Lambda('lambda_5F19')
    def lambda_5F19():
        CameraMove(390, 0, 1360, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_5F19)

    @scena.Lambda('lambda_5F31')
    def lambda_5F31():
        OP_6E(561, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_5F31)

    @scena.Lambda('lambda_5F41')
    def lambda_5F41():
        OP_67(0, 16200, -30160, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5F41)

    @scena.Lambda('lambda_5F59')
    def lambda_5F59():
        SetChrDirection(0x00FE, 90, 100)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_5F59)

    OP_B0(0x0009, 0x32)
    OP_6F(0x0009, 489)
    OP_70(0x0009, 444)
    OP_73(0x0009)
    OP_B0(0x0009, 0x1E)
    OP_6F(0x0009, 443)
    OP_70(0x0009, 421)
    Sleep(60)

    ChrJumpTo(0x0010, -80, 0, 2370, 500, 6000)
    SetChrDirection(0x0010, 14, 800)
    OP_73(0x0009)
    PlaySE(85, 0x00, 0x50)
    OP_7C(0, 600, 3000, 100)
    WaitForThreadExit(0x0010, 0x0001)
    Sleep(100)

    SetChrChipByIndex(0x0010, 33)
    PlaySE(504, 0x00, 0x64)
    OP_99(0x0010, 0x00, 0x01, 2000)

    @scena.Lambda('lambda_5FE7')
    def lambda_5FE7():
        CameraMove(0, 2800, -50, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_5FE7)

    @scena.Lambda('lambda_5FFF')
    def lambda_5FFF():
        OP_67(0, 15760, -30160, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_5FFF)

    @scena.Lambda('lambda_6017')
    def lambda_6017():
        OP_6C(130000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6017)

    OP_9E(0x0010, 80, 0, 250, 30000)
    LoadEffect(0x00, 'map\\\\mp009_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 100, 1000, 3150, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_6088')
    def lambda_6088():
        OP_99(0x00FE, 0x02, 0x05, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6088)

    OP_B0(0x0009, 0x96)
    OP_6F(0x0009, 421)
    OP_70(0x0009, 443)
    CreateThread(0x0020, 0x00, 0x00, 0x0013)
    Sleep(20)

    CreateThread(0x001B, 0x00, 0x00, 0x0013)
    Sleep(20)

    OP_7C(0, 100, 3000, 5000)
    CreateThread(0x001C, 0x00, 0x00, 0x0013)
    Sleep(20)

    CreateThread(0x001D, 0x00, 0x00, 0x0013)
    Sleep(20)

    CreateThread(0x001E, 0x00, 0x00, 0x0013)
    OP_73(0x0009)
    OP_B0(0x0009, 0x1E)
    OP_6F(0x0009, 444)
    OP_70(0x0009, 489)
    Sleep(400)

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_6123')
    def lambda_6123():
        ChrMoveTo(0x00FE, 830, 0, 1290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_6123)

    @scena.Lambda('lambda_613E')
    def lambda_613E():
        OP_99(0x00FE, 0x06, 0x0B, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_613E)

    @scena.Lambda('lambda_614E')
    def lambda_614E():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_614E')

    DispatchAsync2(0x0010, 0x0002, lambda_614E)

    Sleep(1300)

    Sleep(100)

    @scena.Lambda('lambda_6169')
    def lambda_6169():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_6169)

    OP_73(0x0009)

    @scena.Lambda('lambda_617A')
    def lambda_617A():
        CameraSetDistance(680, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_617A)

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
    SetChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 3160, 1480, 1320, 0)

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

    @scena.Lambda('lambda_6213')
    def lambda_6213():
        OP_67(0, 6790, -30160, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_6213)

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

    @scena.Lambda('lambda_6289')
    def lambda_6289():
        CameraMove(5700, 2800, 380, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6289)

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
    SetChrPos(0x0011, 260, 0, -8970, 154)

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
    SetChrFlags(0x0020, 0x0080)
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
        'loc_6F6F',
    )

    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001D, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001E, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001F, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_657C')
    def lambda_657C():
        ChrSetRGBAMask(0x001B, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_657C)

    @scena.Lambda('lambda_658E')
    def lambda_658E():
        ChrSetRGBAMask(0x001B, 255, 255, 255, 200, 700)

        ExitThread()

    DispatchAsync(0x001B, 0x0003, lambda_658E)

    @scena.Lambda('lambda_65A0')
    def lambda_65A0():
        ChrSetRGBAMask(0x001C, 255, 255, 255, 160, 900)

        ExitThread()

    DispatchAsync(0x001C, 0x0003, lambda_65A0)

    @scena.Lambda('lambda_65B2')
    def lambda_65B2():
        ChrSetRGBAMask(0x001D, 255, 255, 255, 120, 1100)

        ExitThread()

    DispatchAsync(0x001D, 0x0003, lambda_65B2)

    @scena.Lambda('lambda_65C4')
    def lambda_65C4():
        ChrSetRGBAMask(0x001E, 255, 255, 255, 80, 1300)

        ExitThread()

    DispatchAsync(0x001E, 0x0003, lambda_65C4)

    @scena.Lambda('lambda_65D6')
    def lambda_65D6():
        ChrSetRGBAMask(0x001F, 255, 255, 255, 40, 1500)

        ExitThread()

    DispatchAsync(0x001F, 0x0003, lambda_65D6)

    CreateThread(0x0011, 0x00, 0x00, 0x0015)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, 0x0015)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, 0x0015)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, 0x0015)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, 0x0015)
    Sleep(50)

    CreateThread(0x001F, 0x00, 0x00, 0x0015)

    @scena.Lambda('lambda_662B')
    def lambda_662B():
        CameraMove(5630, 2800, -60, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_662B)

    @scena.Lambda('lambda_6643')
    def lambda_6643():
        OP_67(0, 16840, -30160, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6643)

    @scena.Lambda('lambda_665B')
    def lambda_665B():
        CameraSetDistance(510, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_665B)

    @scena.Lambda('lambda_666B')
    def lambda_666B():
        OP_6C(73000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_666B)

    @scena.Lambda('lambda_667B')
    def lambda_667B():
        OP_6E(926, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_667B)

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
    CreateThread(0x0010, 0x00, 0x00, 0x0014)
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

    @scena.Lambda('lambda_6775')
    def lambda_6775():
        CameraMove(5610, 1150, -1750, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6775)

    @scena.Lambda('lambda_678D')
    def lambda_678D():
        OP_67(0, 26710, -30160, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_678D)

    @scena.Lambda('lambda_67A5')
    def lambda_67A5():
        CameraSetDistance(460, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_67A5)

    @scena.Lambda('lambda_67B5')
    def lambda_67B5():
        OP_6C(18000, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_67B5)

    @scena.Lambda('lambda_67C5')
    def lambda_67C5():
        OP_6E(698, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_67C5)

    CreateThread(0x0011, 0x00, 0x00, 0x0016)
    Sleep(35)

    CreateThread(0x001B, 0x00, 0x00, 0x0016)
    Sleep(35)

    CreateThread(0x001C, 0x00, 0x00, 0x0016)
    Sleep(35)

    CreateThread(0x001D, 0x00, 0x00, 0x0016)
    Sleep(35)

    CreateThread(0x001E, 0x00, 0x00, 0x0016)
    Sleep(35)

    CreateThread(0x001F, 0x00, 0x00, 0x0016)
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

    CreateThread(0x0011, 0x00, 0x00, 0x0017)
    Sleep(35)

    CreateThread(0x001B, 0x00, 0x00, 0x0017)
    Sleep(35)

    CreateThread(0x001C, 0x00, 0x00, 0x0017)
    Sleep(35)

    CreateThread(0x001D, 0x00, 0x00, 0x0017)
    Sleep(35)

    CreateThread(0x001E, 0x00, 0x00, 0x0017)
    Sleep(35)

    CreateThread(0x001F, 0x00, 0x00, 0x0017)
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

    @scena.Lambda('lambda_6A1E')
    def lambda_6A1E():
        CameraMove(6150, 850, -1670, 4500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_6A1E)

    @scena.Lambda('lambda_6A36')
    def lambda_6A36():
        OP_6C(135000, 4500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_6A36)

    @scena.Lambda('lambda_6A46')
    def lambda_6A46():
        OP_67(0, 11370, -30160, 4500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6A46)

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

    @scena.Lambda('lambda_6ABF')
    def lambda_6ABF():
        CameraSetDistance(590, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6ABF)

    @scena.Lambda('lambda_6ACF')
    def lambda_6ACF():
        CameraMove(7980, 1430, -610, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_6ACF)

    PlaySE(132, 0x00, 0x64)
    CreateThread(0x0011, 0x00, 0x00, 0x0018)
    Sleep(15)

    CreateThread(0x001B, 0x00, 0x00, 0x0018)
    Sleep(15)

    CreateThread(0x001C, 0x00, 0x00, 0x0018)
    Sleep(15)

    CreateThread(0x001D, 0x00, 0x00, 0x0018)
    Sleep(15)

    CreateThread(0x001E, 0x00, 0x00, 0x0018)
    Sleep(15)

    CreateThread(0x001F, 0x00, 0x00, 0x0018)
    PlaySE(521, 0x00, 0x64)
    OP_4A(0x0000, 255)
    OP_4A(0x001B, 0)
    OP_4A(0x001C, 0)
    OP_4A(0x001D, 0)
    OP_4A(0x001E, 0)
    OP_4A(0x0011, 0)
    SetChrSubChip(0x001B, 7)
    SetChrSubChip(0x001C, 7)
    SetChrSubChip(0x001D, 7)
    SetChrSubChip(0x001E, 7)
    SetChrSubChip(0x0011, 7)
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
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    TerminateThread(0x0011, 0xFF)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 255, 0)
    SetChrSubChip(0x0011, 13)
    OP_21()

    ChrTalk(
        0x0011,
        (
            '#0160140361V呼……这种东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0011, 270, 400)
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
    SetChrPos(0x0101, -1170, 0, 380, 0)
    SetChrPos(0x0102, -1160, 0, -890, 0)
    SetChrPos(0x0000, -400, 0, -2790, 0)
    SetChrPos(0x0001, 2090, 0, -3410, 0)
    SetChrChipByIndex(0x0000, 65535)
    SetChrChipByIndex(0x0001, 65535)
    SetChrChipByIndex(0x0002, 65535)
    SetChrChipByIndex(0x0003, 65535)
    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)

    @scena.Lambda('lambda_6DAC')
    def lambda_6DAC():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_6DAC')

    DispatchAsync2(0x0000, 0x0003, lambda_6DAC)

    @scena.Lambda('lambda_6DBD')
    def lambda_6DBD():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_6DBD')

    DispatchAsync2(0x0001, 0x0003, lambda_6DBD)

    @scena.Lambda('lambda_6DCE')
    def lambda_6DCE():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_6DCE')

    DispatchAsync2(0x0002, 0x0003, lambda_6DCE)

    @scena.Lambda('lambda_6DDF')
    def lambda_6DDF():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_6DDF')

    DispatchAsync2(0x0003, 0x0003, lambda_6DDF)

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

    @scena.Lambda('lambda_6E44')
    def lambda_6E44():
        CameraMove(190, 0, -590, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6E44)

    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0011, 2340, 0, -650, 2000, 6000)
    PlaySE(164, 0x00, 0x64)
    SetChrSubChip(0x0011, 10)
    Sleep(200)

    ClearChrFlags(0x0011, 0x0020)
    SetChrChipByIndex(0x0011, 9)
    SetChrSubChip(0x0011, 0)
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

    Jump('loc_79C8')

    def _loc_6F6F(): pass

    label('loc_6F6F')

    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001D, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001E, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001F, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_6FBA')
    def lambda_6FBA():
        ChrSetRGBAMask(0x001B, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_6FBA)

    @scena.Lambda('lambda_6FCC')
    def lambda_6FCC():
        ChrSetRGBAMask(0x001B, 255, 255, 255, 200, 700)

        ExitThread()

    DispatchAsync(0x001B, 0x0003, lambda_6FCC)

    @scena.Lambda('lambda_6FDE')
    def lambda_6FDE():
        ChrSetRGBAMask(0x001C, 255, 255, 255, 160, 900)

        ExitThread()

    DispatchAsync(0x001C, 0x0003, lambda_6FDE)

    @scena.Lambda('lambda_6FF0')
    def lambda_6FF0():
        ChrSetRGBAMask(0x001D, 255, 255, 255, 120, 1100)

        ExitThread()

    DispatchAsync(0x001D, 0x0003, lambda_6FF0)

    @scena.Lambda('lambda_7002')
    def lambda_7002():
        ChrSetRGBAMask(0x001E, 255, 255, 255, 80, 1300)

        ExitThread()

    DispatchAsync(0x001E, 0x0003, lambda_7002)

    @scena.Lambda('lambda_7014')
    def lambda_7014():
        ChrSetRGBAMask(0x001F, 255, 255, 255, 40, 1500)

        ExitThread()

    DispatchAsync(0x001F, 0x0003, lambda_7014)

    CreateThread(0x0011, 0x00, 0x00, 0x0019)
    Sleep(50)

    CreateThread(0x001B, 0x00, 0x00, 0x0019)
    Sleep(50)

    CreateThread(0x001C, 0x00, 0x00, 0x0019)
    Sleep(50)

    CreateThread(0x001D, 0x00, 0x00, 0x0019)
    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, 0x0019)
    Sleep(50)

    CreateThread(0x001F, 0x00, 0x00, 0x0019)

    @scena.Lambda('lambda_7069')
    def lambda_7069():
        CameraMove(2340, 1150, 10, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_7069)

    @scena.Lambda('lambda_7081')
    def lambda_7081():
        OP_67(0, 8830, -30160, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_7081)

    @scena.Lambda('lambda_7099')
    def lambda_7099():
        CameraSetDistance(640, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_7099)

    @scena.Lambda('lambda_70A9')
    def lambda_70A9():
        OP_6C(82000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_70A9)

    @scena.Lambda('lambda_70B9')
    def lambda_70B9():
        OP_6E(602, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_70B9)

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
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)
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
        'loc_715B',
    )

    SetChrChipByIndex(0x0103, 14)
    ChrTurnDirection(0x0103, 0x0017, 0)

    def _loc_715B(): pass

    label('loc_715B')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7175',
    )

    SetChrChipByIndex(0x0104, 16)
    ChrTurnDirection(0x0104, 0x0017, 0)

    def _loc_7175(): pass

    label('loc_7175')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_718F',
    )

    SetChrChipByIndex(0x0106, 20)
    ChrTurnDirection(0x0106, 0x0017, 0)

    def _loc_718F(): pass

    label('loc_718F')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_71A9',
    )

    SetChrChipByIndex(0x0105, 18)
    ChrTurnDirection(0x0105, 0x0017, 0)

    def _loc_71A9(): pass

    label('loc_71A9')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_71C3',
    )

    SetChrChipByIndex(0x0107, 22)
    ChrTurnDirection(0x0107, 0x0017, 0)

    def _loc_71C3(): pass

    label('loc_71C3')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_71DD',
    )

    SetChrChipByIndex(0x0108, 24)
    ChrTurnDirection(0x0108, 0x0017, 0)

    def _loc_71DD(): pass

    label('loc_71DD')

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
    CreateThread(0x0010, 0x00, 0x00, 0x0014)
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
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    TerminateThread(0x0011, 0xFF)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 255, 0)
    SetChrSubChip(0x0011, 13)
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

    SetChrStatus(0x0000, 0xFA, 1)
    SetChrStatus(0x0001, 0xFA, 1)
    SetChrStatus(0x0002, 0xFA, 1)
    SetChrStatus(0x0003, 0xFA, 1)
    SetChrStatus(0x0004, 0xFA, 1)
    SetChrStatus(0x0005, 0xFA, 1)
    SetChrStatus(0x0006, 0xFA, 1)
    SetChrStatus(0x0007, 0xFA, 1)
    SetChrStatus(0x0000, 0x05, 200)
    SetChrStatus(0x0001, 0x05, 200)
    SetChrStatus(0x0002, 0x05, 200)
    SetChrStatus(0x0003, 0x05, 200)
    SetChrStatus(0x0004, 0x05, 200)
    SetChrStatus(0x0005, 0x05, 200)
    SetChrStatus(0x0006, 0x05, 200)
    SetChrStatus(0x0007, 0x05, 200)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7338',
    )

    FormationDelMember(0x02, 0xFF)
    FormationAddMember(0x02, 0xFF)

    def _loc_7338(): pass

    label('loc_7338')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_734C',
    )

    FormationDelMember(0x03, 0xFF)
    FormationAddMember(0x03, 0xFF)

    def _loc_734C(): pass

    label('loc_734C')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7360',
    )

    FormationDelMember(0x05, 0xFF)
    FormationAddMember(0x05, 0xFF)

    def _loc_7360(): pass

    label('loc_7360')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7374',
    )

    FormationDelMember(0x04, 0xFF)
    FormationAddMember(0x04, 0xFF)

    def _loc_7374(): pass

    label('loc_7374')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7388',
    )

    FormationDelMember(0x06, 0xFF)
    FormationAddMember(0x06, 0xFF)

    def _loc_7388(): pass

    label('loc_7388')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_739C',
    )

    FormationDelMember(0x07, 0xFF)
    FormationAddMember(0x07, 0xFF)

    def _loc_739C(): pass

    label('loc_739C')

    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_73B9',
    )

    SetChrChipByIndex(0x0103, 14)

    def _loc_73B9(): pass

    label('loc_73B9')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_73CF',
    )

    SetChrChipByIndex(0x0104, 16)
    SetScenaFlags(ScenaFlag(0x00DE, 5, 0x6F5))

    def _loc_73CF(): pass

    label('loc_73CF')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_73E2',
    )

    SetChrChipByIndex(0x0106, 20)

    def _loc_73E2(): pass

    label('loc_73E2')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_73F5',
    )

    SetChrChipByIndex(0x0105, 18)

    def _loc_73F5(): pass

    label('loc_73F5')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7408',
    )

    SetChrChipByIndex(0x0107, 22)

    def _loc_7408(): pass

    label('loc_7408')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_741B',
    )

    SetChrChipByIndex(0x0108, 24)

    def _loc_741B(): pass

    label('loc_741B')

    SetChrPos(0x0101, -2910, 0, -3850, 47)
    SetChrPos(0x0102, -1510, 0, -3240, 47)
    SetChrPos(0x0002, -4710, 0, 610, 127)
    SetChrPos(0x0003, -5270, 0, -1970, 111)
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
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    TerminateThread(0x0011, 0xFF)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 255, 0)
    ClearChrFlags(0x0011, 0x0020)
    SetChrChipByIndex(0x0011, 9)
    SetChrSubChip(0x0011, 0)
    SetChrPos(0x0011, 3450, 0, 6350, 209)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 3590, 1600, 5110, 0)
    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x0010, 32)
    SetChrPos(0x0010, 4790, 0, 6510, 0)
    CameraMove(21280, 0, -530, 0)
    OP_67(0, 7990, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1170, 0, 380, 0)
    SetChrPos(0x0102, -1160, 0, -890, 0)
    SetChrPos(0x0000, -400, 0, -2790, 0)
    SetChrPos(0x0001, 2090, 0, -3410, 0)
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7637',
    )

    SetChrChipByIndex(0x0103, 14)

    def _loc_7637(): pass

    label('loc_7637')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_764D',
    )

    SetChrChipByIndex(0x0104, 16)
    SetScenaFlags(ScenaFlag(0x00DE, 5, 0x6F5))

    def _loc_764D(): pass

    label('loc_764D')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7660',
    )

    SetChrChipByIndex(0x0106, 20)

    def _loc_7660(): pass

    label('loc_7660')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7673',
    )

    SetChrChipByIndex(0x0105, 18)

    def _loc_7673(): pass

    label('loc_7673')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7686',
    )

    SetChrChipByIndex(0x0107, 22)

    def _loc_7686(): pass

    label('loc_7686')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7699',
    )

    SetChrChipByIndex(0x0108, 24)

    def _loc_7699(): pass

    label('loc_7699')

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
    SetChrChipByIndex(0x0000, 65535)
    SetChrChipByIndex(0x0001, 65535)
    SetChrChipByIndex(0x0002, 65535)
    SetChrChipByIndex(0x0003, 65535)
    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)

    @scena.Lambda('lambda_778F')
    def lambda_778F():
        CameraMove(190, 0, -590, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_778F)

    @scena.Lambda('lambda_77A7')
    def lambda_77A7():
        CameraSetDistance(3300, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_77A7)

    @scena.Lambda('lambda_77B7')
    def lambda_77B7():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_77B7)

    @scena.Lambda('lambda_77C5')
    def lambda_77C5():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_77C5)

    @scena.Lambda('lambda_77D3')
    def lambda_77D3():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0003, lambda_77D3)

    @scena.Lambda('lambda_77E1')
    def lambda_77E1():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0003, lambda_77E1)

    Sleep(1500)

    @scena.Lambda('lambda_77F4')
    def lambda_77F4():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_77F4')

    DispatchAsync2(0x0000, 0x0003, lambda_77F4)

    @scena.Lambda('lambda_7805')
    def lambda_7805():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_7805')

    DispatchAsync2(0x0001, 0x0003, lambda_7805)

    @scena.Lambda('lambda_7816')
    def lambda_7816():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_7816')

    DispatchAsync2(0x0002, 0x0003, lambda_7816)

    @scena.Lambda('lambda_7827')
    def lambda_7827():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_7827')

    DispatchAsync2(0x0003, 0x0003, lambda_7827)

    @scena.Lambda('lambda_7838')
    def lambda_7838():
        ChrWalkTo(0x0011, 700, 0, -750, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7838)

    WaitForThreadExit(0x0011, 0x0001)
    SetChrDirection(0x0011, 270, 400)
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

    def _loc_79C8(): pass

    label('loc_79C8')

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

    @scena.Lambda('lambda_7BDD')
    def lambda_7BDD():
        CameraMove(720, 0, -2650, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_7BDD)

    WaitForThreadExit(0x0000, 0x0000)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7DCA',
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

    def _loc_7DCA(): pass

    label('loc_7DCA')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7FD7',
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

    def _loc_7FD7(): pass

    label('loc_7FD7')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_81B1',
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

    def _loc_81B1(): pass

    label('loc_81B1')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8333',
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

    def _loc_8333(): pass

    label('loc_8333')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_84FB',
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

    def _loc_84FB(): pass

    label('loc_84FB')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_86ED',
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

    def _loc_86ED(): pass

    label('loc_86ED')

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
    SetChrChipByIndex(0x0010, 31)
    SetChrSubChip(0x0010, 0)
    SetChrPos(0x0010, 2670, 0, 6490, 180)
    SetChrPos(0x000E, -1860, 0, -15040, 0)

    ChrTalk(
        0x000E,
        (
            '#0540140450V#3P哎呀呀……\n',
            '看来总算是把危机解决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_87C8')
    def lambda_87C8():
        CameraMove(1200, 0, -3730, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_87C8)

    ClearChrFlags(0x000E, 0x0080)

    @scena.Lambda('lambda_87E5')
    def lambda_87E5():
        ChrWalkTo(0x00FE, 1030, 0, -4810, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_87E5)

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8851',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_881B',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetChrChipByIndex(0x000D, 5)

    Jump('loc_8851')

    def _loc_881B(): pass

    label('loc_881B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_882E',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    SetChrChipByIndex(0x0008, 5)

    Jump('loc_8851')

    def _loc_882E(): pass

    label('loc_882E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8841',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    SetChrChipByIndex(0x0009, 5)

    Jump('loc_8851')

    def _loc_8841(): pass

    label('loc_8841')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8851',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetChrChipByIndex(0x000A, 5)

    def _loc_8851(): pass

    label('loc_8851')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8872',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetChrChipByIndex(0x000D, 1)

    Jump('loc_88A8')

    def _loc_8872(): pass

    label('loc_8872')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8885',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    SetChrChipByIndex(0x0008, 1)

    Jump('loc_88A8')

    def _loc_8885(): pass

    label('loc_8885')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8898',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    SetChrChipByIndex(0x0009, 1)

    Jump('loc_88A8')

    def _loc_8898(): pass

    label('loc_8898')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_88A8',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetChrChipByIndex(0x000A, 1)

    def _loc_88A8(): pass

    label('loc_88A8')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_88C9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetChrChipByIndex(0x000D, 0)

    Jump('loc_88FF')

    def _loc_88C9(): pass

    label('loc_88C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_88DC',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    SetChrChipByIndex(0x0008, 0)

    Jump('loc_88FF')

    def _loc_88DC(): pass

    label('loc_88DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_88EF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    SetChrChipByIndex(0x0009, 0)

    Jump('loc_88FF')

    def _loc_88EF(): pass

    label('loc_88EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_88FF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetChrChipByIndex(0x000A, 0)

    def _loc_88FF(): pass

    label('loc_88FF')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8956',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8920',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetChrChipByIndex(0x000D, 2)

    Jump('loc_8956')

    def _loc_8920(): pass

    label('loc_8920')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8933',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    SetChrChipByIndex(0x0008, 2)

    Jump('loc_8956')

    def _loc_8933(): pass

    label('loc_8933')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8946',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    SetChrChipByIndex(0x0009, 2)

    Jump('loc_8956')

    def _loc_8946(): pass

    label('loc_8946')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8956',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetChrChipByIndex(0x000A, 2)

    def _loc_8956(): pass

    label('loc_8956')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_89AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8977',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetChrChipByIndex(0x000D, 3)

    Jump('loc_89AD')

    def _loc_8977(): pass

    label('loc_8977')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_898A',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    SetChrChipByIndex(0x0008, 3)

    Jump('loc_89AD')

    def _loc_898A(): pass

    label('loc_898A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_899D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    SetChrChipByIndex(0x0009, 3)

    Jump('loc_89AD')

    def _loc_899D(): pass

    label('loc_899D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_89AD',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetChrChipByIndex(0x000A, 3)

    def _loc_89AD(): pass

    label('loc_89AD')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8A04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_89CE',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetChrChipByIndex(0x000D, 4)

    Jump('loc_8A04')

    def _loc_89CE(): pass

    label('loc_89CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_89E1',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    SetChrChipByIndex(0x0008, 4)

    Jump('loc_8A04')

    def _loc_89E1(): pass

    label('loc_89E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_89F4',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    SetChrChipByIndex(0x0009, 4)

    Jump('loc_8A04')

    def _loc_89F4(): pass

    label('loc_89F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8A04',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetChrChipByIndex(0x000A, 4)

    def _loc_8A04(): pass

    label('loc_8A04')

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 110, 0, -17400, 0)

    @scena.Lambda('lambda_8A20')
    def lambda_8A20():
        ChrWalkTo(0x00FE, 2700, 0, -7520, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_8A20)

    Sleep(200)

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -2180, 0, -17210, 0)

    @scena.Lambda('lambda_8A56')
    def lambda_8A56():
        ChrWalkTo(0x00FE, -1170, 0, -7620, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_8A56)

    Sleep(200)

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -1530, 0, -17240, 0)

    @scena.Lambda('lambda_8A8C')
    def lambda_8A8C():
        ChrWalkTo(0x00FE, 240, 0, -8890, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_8A8C)

    Sleep(200)

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -720, 0, -17320, 0)

    @scena.Lambda('lambda_8AC2')
    def lambda_8AC2():
        ChrWalkTo(0x00FE, 1370, 0, -8690, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_8AC2)

    Sleep(1000)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)

    @scena.Lambda('lambda_8AF2')
    def lambda_8AF2():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_8AF2)

    @scena.Lambda('lambda_8B00')
    def lambda_8B00():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_8B00)

    @scena.Lambda('lambda_8B0E')
    def lambda_8B0E():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_8B0E)

    @scena.Lambda('lambda_8B1C')
    def lambda_8B1C():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0003, lambda_8B1C)

    @scena.Lambda('lambda_8B2A')
    def lambda_8B2A():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0003, lambda_8B2A)

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
    SetChrDirection(0x0011, 315, 400)

    @scena.Lambda('lambda_8D37')
    def lambda_8D37():
        SetChrDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_8D37)

    @scena.Lambda('lambda_8D45')
    def lambda_8D45():
        SetChrDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_8D45)

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

    @scena.Lambda('lambda_8E8D')
    def lambda_8E8D():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_8E8D)

    @scena.Lambda('lambda_8E9B')
    def lambda_8E9B():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_8E9B)

    @scena.Lambda('lambda_8EA9')
    def lambda_8EA9():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_8EA9)

    @scena.Lambda('lambda_8EB7')
    def lambda_8EB7():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0003, lambda_8EB7)

    @scena.Lambda('lambda_8EC5')
    def lambda_8EC5():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0003, lambda_8EC5)

    OP_20(0x000005DC)

    @scena.Lambda('lambda_8ED8')
    def lambda_8ED8():
        CameraMove(2300, 0, 2700, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_8ED8)

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

    @scena.Lambda('lambda_91E6')
    def lambda_91E6():
        CameraMove(3460, 0, 7840, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_91E6)

    @scena.Lambda('lambda_91FE')
    def lambda_91FE():
        CameraSetDistance(2800, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_91FE)

    ChrWalkTo(0x0011, 2200, 0, 3860, 2000, 0x00)
    Sleep(500)

    SetChrFlags(0x0011, 0x0020)
    SetChrChipByIndex(0x0011, 35)
    SetChrSubChip(0x0011, 0)
    ChrWalkTo(0x0011, 2440, 0, 5480, 10000, 0x00)
    SetChrSubChip(0x0011, 1)

    @scena.Lambda('lambda_924F')
    def lambda_924F():
        ChrWalkTo(0x0011, 2600, 0, 6440, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_924F)

    PlaySE(507, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_9274')
    def lambda_9274():
        ChrWalkTo(0x0011, 2600, 0, 6440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_9274)

    PlaySE(553, 0x00, 0x64)
    SetChrChipByIndex(0x0010, 7)
    SetChrSubChip(0x0010, 0)
    ChrJumpTo(0x0010, 2780, 0, 9350, 600, 3000)
    PlaySE(554, 0x00, 0x64)
    SetChrChipByIndex(0x0010, 32)
    ChrJumpTo(0x0010, 2780, 0, 10330, 300, 1000)
    Sleep(1000)

    SetChrChipByIndex(0x0011, 9)
    SetChrSubChip(0x0011, 0)
    Sleep(300)

    @scena.Lambda('lambda_92EA')
    def lambda_92EA():
        OP_99(0x0010, 0x00, 0x02, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_92EA)

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

    SetChrName('')
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
    ClearMapFlags(0x02000000)
    OP_20(0x000007D0)
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x9710
@scena.Code('func_0A_9710')
def func_0A_9710():
    OP_66(0x0001)

    @scena.Lambda('lambda_9719')
    def lambda_9719():
        CameraMove(4690, 2000, -1350, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9719)

    @scena.Lambda('lambda_9731')
    def lambda_9731():
        OP_67(0, 2630, -27100, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9731)

    @scena.Lambda('lambda_9749')
    def lambda_9749():
        OP_6C(85000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9749)

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

    @scena.Lambda('lambda_97AC')
    def lambda_97AC():
        CameraSetDistance(1110, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_97AC)

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

    @scena.Lambda('lambda_97FE')
    def lambda_97FE():
        CameraSetDistance(1300, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_97FE)

    OP_71(0x0009, 0x0020)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 50)
    OP_70(0x0009, 69)

    Return()

# id: 0x000B offset: 0x9820
@scena.Code('func_0B_9820')
def func_0B_9820():
    ChrMoveTo(0x00FE, 2720, 0, 2110, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0020)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 28)
    Sleep(100)

    @scena.Lambda('lambda_984E')
    def lambda_984E():
        OP_99(0x00FE, 0x00, 0x01, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_984E)

    ChrMoveTo(0x00FE, 4820, 2000, 790, 10000, 0x00)

    Return()

# id: 0x000C offset: 0x986D
@scena.Code('func_0C_986D')
def func_0C_986D():
    @scena.Lambda('lambda_9873')
    def lambda_9873():
        OP_99(0x00FE, 0x05, 0x0B, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9873)

    ChrJumpTo(0x00FE, 4260, 0, 2930, 300, 10000)

    @scena.Lambda('lambda_989A')
    def lambda_989A():
        OP_99(0x00FE, 0x00, 0x01, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_989A)

    ChrMoveTo(0x00FE, 4820, 2000, 790, 10000, 0x00)

    Return()

# id: 0x000D offset: 0x98B9
@scena.Code('func_0D_98B9')
def func_0D_98B9():
    @scena.Lambda('lambda_98BF')
    def lambda_98BF():
        OP_99(0x00FE, 0x05, 0x0B, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_98BF)

    ChrJumpTo(0x00FE, 3310, 0, 1740, 300, 8000)

    Return()

# id: 0x000E offset: 0x98E1
@scena.Code('func_0E_98E1')
def func_0E_98E1():
    Sleep(250)

    @scena.Lambda('lambda_98EC')
    def lambda_98EC():
        ChrJumpTo(0x00FE, 1410, 0, 3720, 500, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_98EC)

    Sleep(600)

    @scena.Lambda('lambda_990F')
    def lambda_990F():
        ChrJumpTo(0x00FE, 2570, 0, 4370, 300, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_990F)

    Sleep(300)

    @scena.Lambda('lambda_9932')
    def lambda_9932():
        ChrJumpTo(0x00FE, 3330, 2890, 3960, 4000, 10000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9932)

    Return()

# id: 0x000F offset: 0x994B
@scena.Code('func_0F_994B')
def func_0F_994B():
    SetChrFlags(0x00FE, 0x0004)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_995B')
    def lambda_995B():
        OP_99(0x00FE, 0x00, 0x01, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_995B)

    ChrJumpTo(0x00FE, 3350, 2450, 1360, 1000, 6000)

    Return()

# id: 0x0010 offset: 0x997D
@scena.Code('func_10_997D')
def func_10_997D():
    @scena.Lambda('lambda_9983')
    def lambda_9983():
        OP_99(0x00FE, 0x05, 0x0B, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9983)

    ChrJumpTo(0x00FE, 2300, 0, 3430, 300, 6000)

    Return()

# id: 0x0011 offset: 0x99A5
@scena.Code('func_11_99A5')
def func_11_99A5():
    SetChrPos(0x001A, 5140, 2450, 340, 0)
    PlayEffect(0x03, 0xFF, 0x0010, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)
    Sleep(200)

    SetChrPos(0x001A, 5140, 2450, 340, 0)
    PlayEffect(0x03, 0xFF, 0x0010, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)
    Sleep(200)

    SetChrPos(0x001A, 5140, 2450, 340, 0)
    PlayEffect(0x03, 0xFF, 0x0010, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)

    Return()

# id: 0x0012 offset: 0x9A82
@scena.Code('func_12_9A82')
def func_12_9A82():
    SetChrSubChip(0x00FE, 11)
    SetChrPos(0x00FE, 740, 0, 1920, 46)
    ChrTurnDirection(0x00FE, 0x0017, 400)
    ChrJumpTo(0x00FE, 4480, 0, 730, 500, 4000)
    Sleep(50)

    @scena.Lambda('lambda_9AC1')
    def lambda_9AC1():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 3000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9AC1)

    OP_99(0x00FE, 0x00, 0x02, 2000)
    SetChrFlags(0x00FE, 0x0002)

    @scena.Lambda('lambda_9AED')
    def lambda_9AED():
        OP_99(0x00FE, 0x20, 0x31, 3500)
        Yield()

        Jump('lambda_9AED')

    DispatchAsync2(0x00FE, 0x0002, lambda_9AED)

    WaitForThreadExit(0x00FE, 0x0001)
    TerminateThread(0x00FE, 0x02)
    ClearChrFlags(0x00FE, 0x0002)
    ChrTurnDirection(0x00FE, 0x0017, 0)

    @scena.Lambda('lambda_9B15')
    def lambda_9B15():
        OP_99(0x00FE, 0x05, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_9B15)

    Sleep(1000)

    ChrJumpTo(0x00FE, 780, 0, 4600, 500, 6000)
    ChrTurnDirection(0x00FE, 0x0017, 0)

    Return()

# id: 0x0013 offset: 0x9B43
@scena.Code('func_13_9B43')
def func_13_9B43():
    SetChrChipByIndex(0x00FE, 45)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0004)
    SetChrPos(0x00FE, 100, -600, 3150, 0)

    @scena.Lambda('lambda_9B78')
    def lambda_9B78():
        OP_99(0x00FE, 0x00, 0x07, 3000)
        Yield()

        Jump('lambda_9B78')

    DispatchAsync2(0x00FE, 0x0001, lambda_9B78)

    ChrJumpTo(0x00FE, -4070, -600, 4059, 4000, 4000)
    TerminateThread(0x00FE, 0x01)
    SetChrSubChip(0x00FE, 8)

    Return()

# id: 0x0014 offset: 0x9BA6
@scena.Code('func_14_9BA6')
def func_14_9BA6():
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 3590, 1600, 5110, 0)
    SetChrChipByIndex(0x0010, 7)
    SetChrSubChip(0x0010, 0)
    ChrJumpTo(0x0010, 4520, 0, 6090, 2000, 4000)
    SetChrChipByIndex(0x0010, 32)
    ChrJumpTo(0x0010, 4790, 0, 6510, 400, 4000)
    ChrJumpToRelative(0x0010, 0, 0, 0, 200, 4000)

    Return()

# id: 0x0015 offset: 0x9C11
@scena.Code('func_15_9C11')
def func_15_9C11():
    SetChrChipByIndex(0x00FE, 34)
    SetChrSubChip(0x00FE, 1)
    SetChrPos(0x00FE, 260, 0, -8970, 154)
    ClearChrFlags(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0004)
    SetChrFlags(0x00FE, 0x0040)
    SetChrSubChip(0x00FE, 1)
    ChrWalkTo(0x00FE, 2320, 0, -1770, 10000, 0x00)
    SetChrSubChip(0x00FE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9C73',
    )

    PlaySE(163, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    def _loc_9C73(): pass

    label('loc_9C73')

    ChrJumpTo(0x00FE, 4480, 1820, 3340, 1900, 1000)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    SetChrSubChip(0x00FE, 1)

    @scena.Lambda('lambda_9C98')
    def lambda_9C98():
        SetChrDirection(0x00FE, 77, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_9C98)

    ChrJumpTo(0x00FE, 1760, 0, -980, 200, 3000)
    WaitForThreadExit(0x00FE, 0x0001)
    SetChrSubChip(0x00FE, 10)

    Return()

# id: 0x0016 offset: 0x9CC2
@scena.Code('func_16_9CC2')
def func_16_9CC2():
    SetChrSubChip(0x00FE, 4)

    @scena.Lambda('lambda_9CCD')
    def lambda_9CCD():
        SetChrDirection(0x00FE, 170, 1200)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_9CCD)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9CE5',
    )

    PlaySE(163, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    def _loc_9CE5(): pass

    label('loc_9CE5')

    ChrJumpTo(0x00FE, 3710, 0, -2700, 500, 7000)
    TerminateThread(0x00FE, 0x03)
    SetChrDirection(0x00FE, 90, 1200)
    SetChrDirection(0x00FE, 180, 0)
    SetChrSubChip(0x00FE, 5)
    SetChrDirection(0x00FE, 135, 1200)
    Sleep(100)

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    SetChrDirection(0x00FE, 0, 1200)
    SetChrDirection(0x00FE, 90, 400)
    SetChrSubChip(0x00FE, 6)

    Return()

# id: 0x0017 offset: 0x9D36
@scena.Code('func_17_9D36')
def func_17_9D36():
    SetChrSubChip(0x00FE, 11)

    @scena.Lambda('lambda_9D41')
    def lambda_9D41():
        SetChrDirection(0x00FE, 90, 800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_9D41)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9D59',
    )

    PlaySE(163, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    def _loc_9D59(): pass

    label('loc_9D59')

    ChrJumpTo(0x00FE, 5690, 4600, -2090, 6000, 7000)
    SetChrSubChip(0x00FE, 12)
    OP_A6(0x0007)
    Sleep(250)

    ChrMoveTo(0x00FE, 5420, 2230, -2530, 15000, 0x00)
    Sleep(500)

    SetChrSubChip(0x00FE, 11)
    ChrJumpTo(0x00FE, 1380, 0, -990, 500, 4000)
    SetChrSubChip(0x00FE, 6)

    Return()

# id: 0x0018 offset: 0x9DB8
@scena.Code('func_18_9DB8')
def func_18_9DB8():
    SetChrSubChip(0x00FE, 7)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9DCD',
    )

    PlaySE(163, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    def _loc_9DCD(): pass

    label('loc_9DCD')

    ChrJumpTo(0x00FE, 7600, 1730, -590, 3000, 12000)
    SetChrSubChip(0x00FE, 6)

    Return()

# id: 0x0019 offset: 0x9DEA
@scena.Code('func_19_9DEA')
def func_19_9DEA():
    SetChrChipByIndex(0x00FE, 34)
    SetChrSubChip(0x00FE, 1)
    SetChrPos(0x00FE, 260, 0, -8970, 154)
    ClearChrFlags(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0004)
    SetChrFlags(0x00FE, 0x0040)
    SetChrSubChip(0x00FE, 1)
    ChrWalkTo(0x00FE, 2320, 0, -1770, 10000, 0x00)
    SetChrSubChip(0x00FE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9E4C',
    )

    PlaySE(163, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    def _loc_9E4C(): pass

    label('loc_9E4C')

    ChrJumpTo(0x00FE, 4480, 1820, 3340, 1900, 1000)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    SetChrSubChip(0x00FE, 1)

    @scena.Lambda('lambda_9E71')
    def lambda_9E71():
        SetChrDirection(0x00FE, 77, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_9E71)

    ChrJumpTo(0x00FE, 2900, 0, 5660, 200, 3000)
    WaitForThreadExit(0x00FE, 0x0001)
    SetChrSubChip(0x00FE, 10)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
