import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0600_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0600   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '士兵亚多罗瓦'),
    TXT(0x02, '士兵洛克思'),
    TXT(0x03, '士兵托马斯'),
    TXT(0x04, '古利乌副队长'),
    TXT(0x05, '士兵舒托尔'),
    TXT(0x06, '士兵巴兰克'),
    TXT(0x07, '雾调整'),
    TXT(0x08, '艾利兹街道方向'),
    TXT(0x09, '庭园大道方向'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0600.x'
    header.mapIndex       = 17
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x23B3
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -10690,
            z                   = 0,
            y                   = -3640,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -10660,
            z                   = 0,
            y                   = 3600,
            direction           = 90,
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
            x                   = -21590,
            z                   = 11750,
            y                   = 150,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -7840,
            z                   = 0,
            y                   = -4840,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -35300,
            z                   = 0,
            y                   = 3650,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -35300,
            z                   = 0,
            y                   = -3560,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0189,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 37180,
            z                   = 0,
            y                   = -1450,
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
        ScenaNpcData(
            x                   = -83430,
            z                   = 0,
            y                   = -1170,
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

# id: 0x10003 offset: 0x1DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1DA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -75400,
            y           = -2000,
            z           = -8100,
            range       = -74400,
            dword_10    = 0x000007D0,
            dword_14    = 0x00001FA4,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
    )

# id: 0x10005 offset: 0x1FA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1FA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_213',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_224')

    def _loc_213(): pass

    label('loc_213')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_224',
    )

    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_224(): pass

    label('loc_224')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006B, 'loc_230'),
        (-1, 'loc_248'),
    )

    def _loc_230(): pass

    label('loc_230')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 7, 0x1637)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_245',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000B)

    def _loc_245(): pass

    label('loc_245')

    Jump('loc_248')

    def _loc_248(): pass

    label('loc_248')

    Return()

# id: 0x0001 offset: 0x249
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFDB610, 0xFFFE0430, 0x00230006)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_273',
    )

    OP_B1('t0600_y')

    Jump('loc_285')

    def _loc_273(): pass

    label('loc_273')

    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_B1('t0600_n')

    def _loc_285(): pass

    label('loc_285')

    OP_1C(0x02, 0x00, 0x000D)
    OP_1C(0x03, 0x00, 0x000D)
    OP_1C(0x04, 0x00, 0x000D)
    OP_82(0x80, 0x00)
    OP_82(0x81, 0x00)
    OP_82(0x82, 0x00)
    OP_82(0x83, 0x00)
    OP_82(0x84, 0x00)
    OP_82(0x85, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_40E',
    )

    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x00013880, 0x00000000)
    CreateThread(0x000E, 0x00, 0x00, 0x0004)

    def _loc_40E(): pass

    label('loc_40E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43E',
    )

    OP_6F(0x0002, 100)
    OP_72(0x0002, 0x0010)
    OP_6F(0x0003, 100)
    OP_72(0x0003, 0x0010)
    OP_6F(0x0004, 100)
    OP_72(0x0004, 0x0010)

    def _loc_43E(): pass

    label('loc_43E')

    OP_6F(0x0000, 160)
    OP_6F(0x0001, 160)
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)

    Return()

# id: 0x0002 offset: 0x457
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
        'loc_47C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_5BE')

    def _loc_47C(): pass

    label('loc_47C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_495',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_5BE')

    def _loc_495(): pass

    label('loc_495')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AE',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_5BE')

    def _loc_4AE(): pass

    label('loc_4AE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C7',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_5BE')

    def _loc_4C7(): pass

    label('loc_4C7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E0',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_5BE')

    def _loc_4E0(): pass

    label('loc_4E0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F9',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_5BE')

    def _loc_4F9(): pass

    label('loc_4F9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_512',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_5BE')

    def _loc_512(): pass

    label('loc_512')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52B',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_5BE')

    def _loc_52B(): pass

    label('loc_52B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_544',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_5BE')

    def _loc_544(): pass

    label('loc_544')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55D',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_5BE')

    def _loc_55D(): pass

    label('loc_55D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_576',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_5BE')

    def _loc_576(): pass

    label('loc_576')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58F',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_5BE')

    def _loc_58F(): pass

    label('loc_58F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A8',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_5BE')

    def _loc_5A8(): pass

    label('loc_5A8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BE',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_5BE(): pass

    label('loc_5BE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5D3',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5BE')

    def _loc_5D3(): pass

    label('loc_5D3')

    Return()

# id: 0x0003 offset: 0x5D4
@scena.Code('func_03_5D4')
def func_03_5D4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5F7',
    )

    OP_8D(0x00FE, -28070, -8920, -16500, 6400, 3000)

    Jump('func_03_5D4')

    def _loc_5F7(): pass

    label('loc_5F7')

    Return()

# id: 0x0004 offset: 0x5F8
@scena.Code('func_04_5F8')
def func_04_5F8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_68D',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x5DC0),
            (Expr.PushValueByIndex, 0x65),
            Expr.Sub,
            (Expr.PushLong, 0xF),
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x37),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_62B',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_640')

    def _loc_62B(): pass

    label('loc_62B')

    If(
        (
            (Expr.PushValueByIndex, 0x37),
            (Expr.PushLong, 0x7D00),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_640',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x7D00),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_640(): pass

    label('loc_640')

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x5DC0),
            (Expr.PushValueByIndex, 0x65),
            Expr.Sub,
            (Expr.PushLong, 0xF),
            Expr.Mul,
            (Expr.PushLong, 0x13880),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x38),
            (Expr.PushLong, 0x13880),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_670',
    )

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x13880),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_685')

    def _loc_670(): pass

    label('loc_670')

    If(
        (
            (Expr.PushValueByIndex, 0x38),
            (Expr.PushLong, 0x222E0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_685',
    )

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x222E0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_685(): pass

    label('loc_685')

    Sleep(10)

    Jump('func_04_5F8')

    def _loc_68D(): pass

    label('loc_68D')

    Return()

# id: 0x0005 offset: 0x68E
@scena.Code('func_05_68E')
def func_05_68E():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_6F0',
    )

    ChrTalk(
        0x00FE,
        (
            '大门的机能好像\n',
            '还是没有恢复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，又要这样\n',
            '渡过一夜，\n',
            '真是无法想象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A9B')

    def _loc_6F0(): pass

    label('loc_6F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_78B',
    )

    ChrTalk(
        0x00FE,
        (
            '现在不管哪个关所\n',
            '都处在很困扰的境地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '武器方面是个问题，\n',
            '补给问题更是让人头疼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '搬运车和飞船都不能用了，\n',
            '食品的运送现在非常麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A9B')

    def _loc_78B(): pass

    label('loc_78B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_7F9',
    )

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约的签字仪式\n',
            '好像顺利结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为王都关所的门卫，\n',
            '我肩上的担子一下就轻了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A9B')

    def _loc_7F9(): pass

    label('loc_7F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Return,
        ),
        'loc_88A',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天经过这里的游击士\n',
            '刚才又回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，不知为何…\n',
            '看起来好像很疲倦的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，从王都那里往返一趟，\n',
            '疲劳也是正常的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A9B')

    def _loc_88A(): pass

    label('loc_88A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_96C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8EF',
    )

    ChrTalk(
        0x00FE,
        (
            '今天早上看见了一位\n',
            '打扮很奇特的神父呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近神父们还背着\n',
            '护身用的武器啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_969')

    def _loc_8EF(): pass

    label('loc_8EF')

    ChrTalk(
        0x00FE,
        (
            '今天早上看见了一位\n',
            '打扮很奇特的神父呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '背上还背着\n',
            '弓箭一样的武器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近神父们还背着\n',
            '护身用的武器啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_969(): pass

    label('loc_969')

    Jump('loc_A9B')

    def _loc_96C(): pass

    label('loc_96C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_9DA',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天从关所来的游击士\n',
            '今天早上向王都出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏好好休息了一个晚上，\n',
            '旅行者们都很有精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A9B')

    def _loc_9DA(): pass

    label('loc_9DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_A9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 1, 0x1811)),
            Expr.Return,
        ),
        'loc_A39',
    )

    ChrTalk(
        0x00FE,
        (
            '被游击士护送的旅行商人\n',
            '刚才已经到达了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛连特的雾有\n',
            '那么厉害的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A9B')

    def _loc_A39(): pass

    label('loc_A39')

    ChrTalk(
        0x00FE,
        (
            '明天要在艾尔贝离宫\n',
            '进行互不侵犯条约的签字仪式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以通行时的审查也会\n',
            '比平时更加严格哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A9B(): pass

    label('loc_A9B')

    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0xA9F
@scena.Code('func_06_A9F')
def func_06_A9F():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_BCC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B75',
    )

    ChrTalk(
        0x00FE,
        (
            '飞船无法飞行\n',
            '对王国军来说非常致命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟我们军队的主要战力\n',
            '就是飞行舰队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帝国也有飞行舰队，\n',
            '但他们还是以地面部队为主力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然也会受到一些影响，\n',
            '不过显然不如我们严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_BC9')

    def _loc_B75(): pass

    label('loc_B75')

    ChrTalk(
        0x00FE,
        (
            '飞船无法飞行\n',
            '对王国军来说非常致命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟我们军队的主要战力\n',
            '就是飞行舰队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BC9(): pass

    label('loc_BC9')

    Jump('loc_FBA')

    def _loc_BCC(): pass

    label('loc_BCC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C4A',
    )

    ChrTalk(
        0x00FE,
        (
            '不但关卡大门无法关闭，\n',
            '连导力枪都无法使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情况真是恶劣到极点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在只能祈祷\n',
            '别发生什么意外了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FBA')

    def _loc_C4A(): pass

    label('loc_C4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_C9F',
    )

    ChrTalk(
        0x00FE,
        (
            '雾终于散去了啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '签字仪式也顺利结束了。\n',
            '真是个令人高兴的早晨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FBA')

    def _loc_C9F(): pass

    label('loc_C9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_D8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_D14',
    )

    ChrTalk(
        0x00FE,
        (
            '听说威尔特桥的守备队\n',
            '进入洛连特镇中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每次一想到那种浓雾\n',
            '就不由对大自然之力感到恐惧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D88')

    def _loc_D14(): pass

    label('loc_D14')

    ChrTalk(
        0x00FE,
        (
            '听说威尔特桥的守备队\n',
            '进入洛连特镇中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '浓雾原来是\n',
            '这么恐怖的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大自然的力量\n',
            '真是令人畏惧呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_D88(): pass

    label('loc_D88')

    Jump('loc_FBA')

    def _loc_D8B(): pass

    label('loc_D8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_E68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_DE5',
    )

    ChrTalk(
        0x00FE,
        (
            '今天终于要进行\n',
            '互不侵犯条约的签字仪式了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一天终于来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E65')

    def _loc_DE5(): pass

    label('loc_DE5')

    ChrTalk(
        0x00FE,
        (
            '今天终于要进行\n',
            '互不侵犯条约的签字仪式了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对王国来说，\n',
            '这也是很有纪念意义的一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很好！\n',
            '我也要努力才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_E65(): pass

    label('loc_E65')

    Jump('loc_FBA')

    def _loc_E68(): pass

    label('loc_E68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_FBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_EE7',
    )

    ChrTalk(
        0x00FE,
        (
            '现在王都中除了各国要人之外，\n',
            '还有很多关联人员也来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为士兵，我们也很希望\n',
            '这次的活动能顺利结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FBA')

    def _loc_EE7(): pass

    label('loc_EE7')

    ChrTalk(
        0x00FE,
        (
            '明天就是条约的签字仪式了啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在王都中除了各国要人之外，\n',
            '还有很多关联人员也来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '十年前侵略王国的\n',
            '埃雷波尼亚帝国，如今却\n',
            '要和我们签署互不侵犯条约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话，引起各国关注\n',
            '也是不奇怪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_FBA(): pass

    label('loc_FBA')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0xFBE
@scena.Code('func_07_FBE')
def func_07_FBE():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1066',
    )

    ChrTalk(
        0x00FE,
        (
            '听说哈肯大门那边\n',
            '处于严格的警备状态…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道帝国方面对这次的事件\n',
            '有什么准备对策…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果只是签署互不侵犯条约的话，\n',
            '我想也不会有什么事，可是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1806')

    def _loc_1066(): pass

    label('loc_1066')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_11A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1141',
    )

    ChrTalk(
        0x00FE,
        (
            '从这里的城墙上可以很清楚地\n',
            '看见那个浮游岛屿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使不刻意去注意\n',
            '也非常显眼…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之让人很难不在意那个岛屿，\n',
            '我没事的时候也经常眺望它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，不过在警备的时候\n',
            '总是分散注意力可不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_119D')

    def _loc_1141(): pass

    label('loc_1141')

    ChrTalk(
        0x00FE,
        (
            '可是、那座岛……\n',
            '究竟是什么东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看起来虽然很漂亮，\n',
            '但不知为何总让人觉得不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_119D(): pass

    label('loc_119D')

    Jump('loc_1806')

    def _loc_11A0(): pass

    label('loc_11A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_12A3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1217',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的警备工作\n',
            '终于也恢复到普通的状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '国家典礼也好，异常气象也好，\n',
            '应该都只是暂时的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A0')

    def _loc_1217(): pass

    label('loc_1217')

    ChrTalk(
        0x00FE,
        (
            '这里的警备工作\n',
            '终于也恢复到普通的状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能的话，真希望什么也别发生了，\n',
            '不管是国家典礼还是异常气象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～累死了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_12A0(): pass

    label('loc_12A0')

    Jump('loc_1806')

    def _loc_12A3(): pass

    label('loc_12A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_13F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1337',
    )

    ChrTalk(
        0x00FE,
        (
            '最近食堂的亚米丽\n',
            '新做了一些东方料理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吃虽然是好吃，\n',
            '但总是卖光，真讨厌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～如果今天没意外的话\n',
            '应该能吃到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13F4')

    def _loc_1337(): pass

    label('loc_1337')

    ChrTalk(
        0x00FE,
        (
            '马上就是接班的时间了吧……\n',
            '今天的午饭吃什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近食堂的亚米丽\n',
            '新做了一些东方料理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吃虽然是好吃，\n',
            '但总是卖光，真讨厌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咕、咕噜……（吞口水）\n',
            '今天该去哪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_13F4(): pass

    label('loc_13F4')

    Jump('loc_1806')

    def _loc_13F7(): pass

    label('loc_13F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_14E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1451',
    )

    ChrTalk(
        0x00FE,
        (
            '签字仪式结束后…\n',
            '又是浓雾吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是让人一口气都不能松下来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14DE')

    def _loc_1451(): pass

    label('loc_1451')

    ChrTalk(
        0x00FE,
        (
            '因签字仪式而实施的临时强化警备，\n',
            '今天好不容易才结束…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还没来得及松口气，\n',
            '又到处浓雾弥漫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～真是让人一分钟都不能休息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_14DE(): pass

    label('loc_14DE')

    Jump('loc_1806')

    def _loc_14E1(): pass

    label('loc_14E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_154B',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，洛连特那边的状况\n',
            '因为雾太浓很难确认。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还魔兽没有出现，\n',
            '但还是要仔细巡查才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1806')

    def _loc_154B(): pass

    label('loc_154B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_15A0',
    )

    ChrTalk(
        0x00FE,
        (
            '似乎将王都的受害情况\n',
            '压制到了最低呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真不愧是尤莉亚中尉她们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1806')

    def _loc_15A0(): pass

    label('loc_15A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_1611',
    )

    ChrTalk(
        0x00FE,
        (
            '我、我在这里也看见了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和奇怪的飞行物体战斗的\n',
            '就是你们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那究竟是什么东西啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1806')

    def _loc_1611(): pass

    label('loc_1611')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_16B7',
    )

    ChrTalk(
        0x00FE,
        (
            '……黑发的男孩吗？\n',
            '没有来过这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果来了的话应该在\n',
            '南边的城墙上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游客一般\n',
            '都会去那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该是从南边的台阶下去，\n',
            '然后从南门出去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1806')

    def _loc_16B7(): pass

    label('loc_16B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_172D',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然签字仪式已经临近了，\n',
            '但我们的工作还是和平时一样，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是全力守卫格鲁纳门而已……\n',
            '嗯，仅此而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1806')

    def _loc_172D(): pass

    label('loc_172D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_17CD',
    )

    ChrTalk(
        0x00FE,
        (
            '政变之后，\n',
            '部队进行了重编，\n',
            '上层的首脑们好像很忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然这里是镇守王都的要道，\n',
            '但大概是因为全部配备了精英人员。\n',
            '似乎没有发生任何异常状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1806')

    def _loc_17CD(): pass

    label('loc_17CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1806',
    )

    ChrTalk(
        0x00FE,
        (
            '没有异常状况！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，今天的天气也不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1806(): pass

    label('loc_1806')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x180A
@scena.Code('func_08_180A')
def func_08_180A():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_186D',
    )

    ChrTalk(
        0x00FE,
        (
            '亚宁堡的防线自建国以来\n',
            '从未被敌人突破过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了维护这荣耀\n',
            '我也会死守在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_196E')

    def _loc_186D(): pass

    label('loc_186D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_196E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1906',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，你们是游击士吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们格鲁纳门的守备队\n',
            '也开始加强警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在大门无法控制的状态下，\n',
            '必须要加强警备，防患于未然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_196E')

    def _loc_1906(): pass

    label('loc_1906')

    ChrTalk(
        0x00FE,
        (
            '我们格鲁纳门的守备队\n',
            '也开始加强警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在大门无法控制的状态下，\n',
            '必须要加强警备，防患于未然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_196E(): pass

    label('loc_196E')

    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0x1972
@scena.Code('func_09_1972')
def func_09_1972():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1A95',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A44',
    )

    ChrTalk(
        0x00FE,
        (
            '空中浮岛的出现、\n',
            '导力机能的停止……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国内最近一直\n',
            '发生不可思议的事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这样下去的话，\n',
            '就算女神降临也不觉得奇怪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……噢，失礼了。\n',
            '这样说话太冒犯女神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_1A92')

    def _loc_1A44(): pass

    label('loc_1A44')

    ChrTalk(
        0x00FE,
        (
            '空中浮岛的出现、\n',
            '导力机能的停止……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得像是神话中\n',
            '的世界一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A92(): pass

    label('loc_1A92')

    Jump('loc_1DBB')

    def _loc_1A95(): pass

    label('loc_1A95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1B7B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B1C',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到格鲁纳门，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '进入警备状态之后\n',
            '通行管理也比以前更严了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以自由通行的\n',
            '只有游击士和军队的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_1B78')

    def _loc_1B1C(): pass

    label('loc_1B1C')

    ChrTalk(
        0x00FE,
        (
            '现在处于非常状况，\n',
            '通行管理也比以前更严了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以自由通行的\n',
            '只有游击士和军队的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B78(): pass

    label('loc_1B78')

    Jump('loc_1DBB')

    def _loc_1B7B(): pass

    label('loc_1B7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1BF5',
    )

    ChrTalk(
        0x00FE,
        (
            '听说在格兰赛尔\n',
            '好像出了什么事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和出现在周游道的那些特务兵\n',
            '有什么关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总有种不好的预感……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBB')

    def _loc_1BF5(): pass

    label('loc_1BF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_1C5F',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，话是那么说，\n',
            '不过周游道现在已经被封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要去格兰赛尔的话，\n',
            '走庭园大道就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBB')

    def _loc_1C5F(): pass

    label('loc_1C5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_1CCF',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到格鲁纳门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么慌慌张张的，\n',
            '是有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要参观的话不用着急，\n',
            '还有的是时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBB')

    def _loc_1CCF(): pass

    label('loc_1CCF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_1D24',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到格鲁纳门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '马上就是条约的签字仪式了，\n',
            '警备工作也要加强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBB')

    def _loc_1D24(): pass

    label('loc_1D24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1D67',
    )

    ChrTalk(
        0x00FE,
        (
            '条约的签字仪式吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望不要有人\n',
            '暗中捣乱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBB')

    def _loc_1D67(): pass

    label('loc_1D67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1DBB',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到格鲁纳门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里是格兰赛尔地区和\n',
            '洛连特地区之间交接的关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DBB(): pass

    label('loc_1DBB')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x1DBF
@scena.Code('func_0A_1DBF')
def func_0A_1DBF():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1E12',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，奇怪的事件\n',
            '一直层出不穷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前的政变事件\n',
            '就够受了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2196')

    def _loc_1E12(): pass

    label('loc_1E12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1F39',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EBA',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器瘫痪的时候\n',
            '这里也发生了很大的骚乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不但灯全都熄灭了，\n',
            '连大门也关不上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然通信器已经修好了，\n',
            '但严峻的状况仍然没有得到好转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_1F36')

    def _loc_1EBA(): pass

    label('loc_1EBA')

    ChrTalk(
        0x00FE,
        (
            '虽然通信器已经修好了，\n',
            '但严峻的状况仍然没有得到好转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在还没发生什么太严重的事情。\n',
            '但无论如何也不能松懈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F36(): pass

    label('loc_1F36')

    Jump('loc_2196')

    def _loc_1F39(): pass

    label('loc_1F39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1FA5',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部就此解散了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然让人松了口气，\n',
            '但那飞走的巨大人形机器人…\n',
            '究竟是什么东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2196')

    def _loc_1FA5(): pass

    label('loc_1FA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_200F',
    )

    ChrTalk(
        0x00FE,
        (
            '结社……\n',
            '到底是怎样的一群家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我对那东西实在放不下心，\n',
            '今后必须要继续加强警备啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2196')

    def _loc_200F(): pass

    label('loc_200F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_206F',
    )

    ChrTalk(
        0x00FE,
        (
            '队长说要集合开会，\n',
            '好像是有什么事情要说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是那件事吗……\n',
            '柏斯发生的事件',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2196')

    def _loc_206F(): pass

    label('loc_206F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_20DA',
    )

    ChrTalk(
        0x00FE,
        (
            '听说离宫中安置了警备本部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从卡西乌斯准将回到军队以后，\n',
            '军队的办事效率迅速了很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2196')

    def _loc_20DA(): pass

    label('loc_20DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2131',
    )

    ChrTalk(
        0x00FE,
        (
            '马上就是签字仪式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各界要人都会来到这里，\n',
            '必须要加强警备才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2196')

    def _loc_2131(): pass

    label('loc_2131')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2196',
    )

    ChrTalk(
        0x00FE,
        (
            '听说卢安和蔡斯好像都\n',
            '发生了奇妙的事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔和城墙那面的\n',
            '洛连特倒还是很安稳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2196(): pass

    label('loc_2196')

    TalkEnd(0x000D)

    Return()

# id: 0x000B offset: 0x219A
@scena.Code('func_0B_219A')
def func_0B_219A():
    EventBegin(0x00)
    OP_6D(-16830, 0, 1620, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(8000, 0)
    OP_6C(74000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -82890, 0, 20, 90)
    OP_12(0x00007D00, 0x0003D090, 0x00000000)
    FadeIn(2000, 0)
    OP_12(0x00007D00, 0x0001FBD0, 0x00002EE0)

    @scena.Lambda('lambda_2213')
    def lambda_2213():
        OP_6B(3250, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2213)

    @scena.Lambda('lambda_2223')
    def lambda_2223():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2223)

    @scena.Lambda('lambda_2233')
    def lambda_2233():
        OP_6D(-72030, 0, 20, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2233)

    Sleep(8000)

    OP_8E(0x0101, -74030, 0, -20, 5000, 0x00)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010260969V#1020F#5P已经是黄昏了……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260970V#1015F亚宁堡的上面……\n',
            '也就是城墙上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260964V#1002F必须要赶快过去……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1637)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x22F8
@scena.Code('func_0C_22F8')
def func_0C_22F8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 7, 0x1637)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_238A',
    )

    EventBegin(0x02)

    ChrTalk(
        0x0101,
        (
            '#0010260972V#1003F（我在做什么啊！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260973V#1002F（约修亚……\n',
            '  约修亚不是还在等着我吗！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_238A(): pass

    label('loc_238A')

    Return()

# id: 0x000D offset: 0x238B
@scena.Code('func_0D_238B')
def func_0D_238B():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
