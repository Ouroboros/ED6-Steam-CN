import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '嗜杀巨蟹'),
    TXT(0x02, '嗜杀巨蟹'),
    TXT(0x03, '嗜杀巨蟹'),
    TXT(0x04, '嗜杀巨蟹'),
    TXT(0x05, '嗜杀巨蟹'),
    TXT(0x06, '嗜杀巨蟹'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0100.x'
    header.mapIndex       = 14
    header.bgm            = 30
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xD65
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x000061A8,
            dword_04        = 0x00000000,
            dword_08        = 0x00002328,
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
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 14,
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
        ('ED6_DT09/CH10000._CH', 'ED6_DT09/CH10000P._CP'),
        ('ED6_DT09/CH10001._CH', 'ED6_DT09/CH10001P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xBA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 114000,
            z           = -500,
            y           = 80000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 108000,
            z           = 0,
            y           = 54000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 105000,
            z           = 0,
            y           = 16000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 129090,
            z           = 1000,
            y           = 12770,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 93190,
            z           = 0,
            y           = 86160,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 84390,
            z           = 1000,
            y           = 32040,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x162
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x162
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 14000,
            triggerZ            = 1000,
            triggerY            = 31800,
            triggerRange        = 1000,
            actorX              = 14000,
            actorZ              = 1000,
            actorY              = 31800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x186
@scena.Code('PreInit')
def PreInit():
    OP_A2(0x0001)
    OP_A3(0x0002)
    OP_A3(0x0003)

    Return()

# id: 0x0001 offset: 0x190
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AC',
    )

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
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
    OP_71(0x0012, 0x0004)
    OP_71(0x0013, 0x0004)
    OP_71(0x0014, 0x0004)
    OP_71(0x0015, 0x0004)
    OP_71(0x0016, 0x0004)
    OP_71(0x0017, 0x0004)
    OP_71(0x0018, 0x0004)
    OP_71(0x0019, 0x0004)
    OP_71(0x001A, 0x0004)
    OP_71(0x001B, 0x0004)
    OP_71(0x001C, 0x0004)
    OP_71(0x001D, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x001F, 0x0004)
    OP_71(0x0020, 0x0004)
    OP_71(0x0021, 0x0004)
    OP_71(0x0022, 0x0004)
    OP_71(0x0023, 0x0004)
    OP_71(0x0024, 0x0004)
    OP_71(0x0025, 0x0004)
    OP_71(0x0026, 0x0004)
    OP_71(0x0027, 0x0004)
    OP_71(0x0028, 0x0004)
    OP_71(0x0029, 0x0004)
    OP_71(0x002A, 0x0004)
    OP_71(0x002B, 0x0004)
    OP_71(0x002C, 0x0004)
    OP_71(0x002D, 0x0004)
    OP_71(0x002E, 0x0004)
    OP_71(0x002F, 0x0004)
    OP_71(0x0030, 0x0004)
    OP_71(0x0031, 0x0004)
    OP_71(0x0032, 0x0004)
    OP_78(0x80, 0x80, 0x80)
    OP_79(0xFF, 0x0002)
    OP_7B()
    OP_77(0xFF, 0xFF, 0xFF, 0x01, 0x00000000)

    Jump('loc_2F5')

    def _loc_2AC(): pass

    label('loc_2AC')

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 104880, 1000, 39790, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_2F5(): pass

    label('loc_2F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_306',
    )

    OP_6F(0x0000, 0)

    Jump('loc_325')

    def _loc_306(): pass

    label('loc_306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_317',
    )

    OP_6F(0x0000, 330)

    Jump('loc_325')

    def _loc_317(): pass

    label('loc_317')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_325',
    )

    OP_6F(0x0000, 900)

    def _loc_325(): pass

    label('loc_325')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_336',
    )

    OP_6F(0x0003, 25)

    Jump('loc_33D')

    def _loc_336(): pass

    label('loc_336')

    OP_6F(0x0003, 0)

    def _loc_33D(): pass

    label('loc_33D')

    Return()

# id: 0x0002 offset: 0x33E
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
        'loc_363',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_4A5')

    def _loc_363(): pass

    label('loc_363')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37C',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_4A5')

    def _loc_37C(): pass

    label('loc_37C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_395',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_4A5')

    def _loc_395(): pass

    label('loc_395')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AE',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_4A5')

    def _loc_3AE(): pass

    label('loc_3AE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C7',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_4A5')

    def _loc_3C7(): pass

    label('loc_3C7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E0',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_4A5')

    def _loc_3E0(): pass

    label('loc_3E0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F9',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_4A5')

    def _loc_3F9(): pass

    label('loc_3F9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_412',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_4A5')

    def _loc_412(): pass

    label('loc_412')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42B',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_4A5')

    def _loc_42B(): pass

    label('loc_42B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_444',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_4A5')

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45D',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_4A5')

    def _loc_45D(): pass

    label('loc_45D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_476',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_4A5')

    def _loc_476(): pass

    label('loc_476')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48F',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_4A5')

    def _loc_48F(): pass

    label('loc_48F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A5',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4BA',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_4A5')

    def _loc_4BA(): pass

    label('loc_4BA')

    Return()

# id: 0x0003 offset: 0x4BB
@scena.Code('func_03_4BB')
def func_03_4BB():
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '升降机被锁住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x4F5
@scena.Code('func_04_4F5')
def func_04_4F5():
    EventBegin(0x00)
    SetMapFlags(0x08000000)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)

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
            TXT(0x00, '【乘升降机】\n'),
            TXT(0x01, '【不乘升降机】\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_563',
    )

    Sleep(300)

    EventEnd(0x01)

    Return()

    def _loc_563(): pass

    label('loc_563')

    Fade(1000)
    SetChrPos(0x0000, 128580, 50, 77550, 0)
    SetChrPos(0x0001, 129580, 50, 77550, 0)
    SetChrPos(0x0002, 128580, 50, 76780, 0)
    SetChrPos(0x0003, 129580, 50, 76780, 0)
    OP_6D(129020, 50, 77590, 1000)
    Sleep(120)

    OP_22(0x0066, 0x00, 0x64)
    OP_70(0x0002, 0x00000168)
    OP_73(0x0002)
    OP_6F(0x0002, 360)
    Fade(1000)
    OP_6F(0x0001, 120)
    Sleep(120)

    OP_6D(54110, 50, 57680, 0)
    SetChrPos(0x0000, 53570, -6000, 57550, 180)
    SetChrPos(0x0001, 54570, -6000, 57550, 180)
    SetChrPos(0x0002, 53570, -6000, 56780, 180)
    SetChrPos(0x0003, 54570, -6000, 56780, 180)
    OP_70(0x0001, 0x00000000)
    OP_73(0x0001)
    OP_6F(0x0001, 0)
    ClearMapFlags(0x00400000)
    EventEnd(0x00)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x65C
@scena.Code('func_05_65C')
def func_05_65C():
    EventBegin(0x00)
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
            TXT(0x00, '乘升降机\n'),
            TXT(0x01, '不乘升降机\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6BB',
    )

    Sleep(300)

    EventEnd(0x01)

    Return()

    def _loc_6BB(): pass

    label('loc_6BB')

    SetMapFlags(0x00000001)
    Fade(500)
    SetChrFlags(0x0001, 0x0008)
    SetChrFlags(0x0002, 0x0008)
    SetChrFlags(0x0003, 0x0008)
    SetChrPos(0x0000, 15900, 400, 32299, 0)
    SetChrPos(0x0001, 15900, 400, 32299, 0)
    SetChrPos(0x0002, 15900, 400, 32299, 0)
    SetChrPos(0x0003, 15900, 400, 32299, 0)
    Sleep(500)

    OP_22(0x0065, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7B2',
    )

    OP_A3(0x0001)
    OP_A2(0x0002)
    OP_A3(0x0003)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x0000014A)
    OP_73(0x0000)
    OP_6F(0x0000, 330)
    Sleep(500)

    Fade(500)
    OP_69(0x0000, 0x00000000)
    ClearChrFlags(0x0001, 0x0008)
    ClearChrFlags(0x0002, 0x0008)
    ClearChrFlags(0x0003, 0x0008)
    SetChrPos(0x0000, 34200, 100, 61400, 315)
    SetChrPos(0x0001, 34200, 100, 61400, 315)
    SetChrPos(0x0002, 34200, 100, 61400, 315)
    SetChrPos(0x0003, 34200, 100, 61400, 315)

    Jump('loc_837')

    def _loc_7B2(): pass

    label('loc_7B2')

    OP_A3(0x0001)
    OP_A3(0x0002)
    OP_A2(0x0003)
    OP_6F(0x0000, 500)
    OP_70(0x0000, 0x00000384)
    OP_73(0x0000)
    OP_6F(0x0000, 900)
    Sleep(500)

    Fade(500)
    OP_69(0x0000, 0x00000000)
    ClearChrFlags(0x0001, 0x0008)
    ClearChrFlags(0x0002, 0x0008)
    ClearChrFlags(0x0003, 0x0008)
    SetChrPos(0x0000, 50500, 0, 51900, 45)
    SetChrPos(0x0001, 50500, 0, 51900, 45)
    SetChrPos(0x0002, 50500, 0, 51900, 45)
    SetChrPos(0x0003, 50500, 0, 51900, 45)

    def _loc_837(): pass

    label('loc_837')

    Sleep(300)

    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x83F
@scena.Code('func_06_83F')
def func_06_83F():
    EventBegin(0x00)
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
            TXT(0x00, '乘升降机\n'),
            TXT(0x01, '不乘升降机\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_89E',
    )

    Sleep(300)

    EventEnd(0x01)

    Return()

    def _loc_89E(): pass

    label('loc_89E')

    OP_A2(0x0001)
    OP_A3(0x0002)
    OP_A3(0x0003)
    SetMapFlags(0x00000001)
    Fade(500)
    OP_69(0x0000, 0x00000000)
    SetChrFlags(0x0001, 0x0008)
    SetChrFlags(0x0002, 0x0008)
    SetChrFlags(0x0003, 0x0008)
    SetChrPos(0x0000, 34800, 400, 59200, 225)
    SetChrPos(0x0001, 34800, 400, 59200, 225)
    SetChrPos(0x0002, 34800, 400, 59200, 225)
    SetChrPos(0x0003, 34800, 400, 59200, 225)
    Sleep(500)

    OP_22(0x0065, 0x00, 0x64)
    OP_6F(0x0000, 330)
    OP_70(0x0000, 0x00000000)
    OP_73(0x0000)
    OP_6F(0x0000, 0)
    Sleep(500)

    Fade(500)
    OP_69(0x0000, 0x00000000)
    ClearChrFlags(0x0001, 0x0008)
    ClearChrFlags(0x0002, 0x0008)
    ClearChrFlags(0x0003, 0x0008)
    SetChrPos(0x0000, 16000, 50, 29700, 180)
    SetChrPos(0x0001, 16000, 50, 29700, 180)
    SetChrPos(0x0002, 16000, 50, 29700, 180)
    SetChrPos(0x0003, 16000, 50, 29700, 180)
    Sleep(300)

    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x999
@scena.Code('func_07_999')
def func_07_999():
    EventBegin(0x00)
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
            TXT(0x00, '乘升降机\n'),
            TXT(0x01, '不乘升降机\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9F8',
    )

    Sleep(300)

    EventEnd(0x01)

    Return()

    def _loc_9F8(): pass

    label('loc_9F8')

    OP_A2(0x0001)
    OP_A3(0x0002)
    OP_A3(0x0003)
    SetMapFlags(0x00000001)
    Fade(500)
    SetChrFlags(0x0001, 0x0008)
    SetChrFlags(0x0002, 0x0008)
    SetChrFlags(0x0003, 0x0008)
    SetChrPos(0x0000, 50200, 400, 49900, 270)
    SetChrPos(0x0001, 50200, 400, 49900, 270)
    SetChrPos(0x0002, 50200, 400, 49900, 270)
    SetChrPos(0x0003, 50200, 400, 49900, 270)
    Sleep(500)

    OP_22(0x0065, 0x00, 0x64)
    OP_6F(0x0000, 900)
    OP_70(0x0000, 0x000001F4)
    OP_73(0x0000)
    OP_6F(0x0000, 500)
    Sleep(500)

    Fade(500)
    OP_69(0x0000, 0x00000000)
    SetChrPos(0x0000, 16000, 50, 29700, 180)
    SetChrPos(0x0001, 16000, 50, 29700, 180)
    SetChrPos(0x0002, 16000, 50, 29700, 180)
    SetChrPos(0x0003, 16000, 50, 29700, 180)
    ClearChrFlags(0x0001, 0x0008)
    ClearChrFlags(0x0002, 0x0008)
    ClearChrFlags(0x0003, 0x0008)
    Sleep(300)

    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0xAEC
@scena.Code('func_08_AEC')
def func_08_AEC():
    SetMapFlags(0x00000080)
    Sleep(30)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '拉杆被锁住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xB42
@scena.Code('func_09_B42')
def func_09_B42():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B95',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '好像是导力停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_D50')

    def _loc_B95(): pass

    label('loc_B95')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
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

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D35',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_82(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 104880, 1000, 39790, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0033, 0)
    OP_70(0x0033, 0x00000032)
    OP_73(0x0033)
    OP_20(0x00000BB8)
    OP_22(0x000C, 0x00, 0x64)
    OP_82(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 104880, 1000, 39790, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_82(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 104880, 1000, 39790, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0033, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_D35(): pass

    label('loc_D35')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D4F',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_D4F(): pass

    label('loc_D4F')

    Return()

    def _loc_D50(): pass

    label('loc_D50')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
