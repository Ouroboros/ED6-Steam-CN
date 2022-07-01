import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1402   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, '士兵古特'),
    TXT(0x03, '士兵拉凯尔'),
    TXT(0x04, '守备队长'),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
    TXT(0x0D, ''),
    TXT(0x0E, ''),
    TXT(0x0F, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1402.x'
    header.mapIndex       = 60
    header.bgm            = 89
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1E01
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
        ('ED6_DT09/CH11170._CH', 'ED6_DT09/CH11170P._CP'),
        ('ED6_DT09/CH11171._CH', 'ED6_DT09/CH11171P._CP'),
        ('ED6_DT09/CH11180._CH', 'ED6_DT09/CH11180P._CP'),
        ('ED6_DT09/CH11181._CH', 'ED6_DT09/CH11181P._CP'),
        ('ED6_DT09/CH11190._CH', 'ED6_DT09/CH11190P._CP'),
        ('ED6_DT09/CH11191._CH', 'ED6_DT09/CH11191P._CP'),
        ('ED6_DT09/CH10170._CH', 'ED6_DT09/CH10170P._CP'),
        ('ED6_DT09/CH10171._CH', 'ED6_DT09/CH10171P._CP'),
        ('ED6_DT09/CH10840._CH', 'ED6_DT09/CH10840P._CP'),
        ('ED6_DT09/CH10841._CH', 'ED6_DT09/CH10841P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH00322._CH', 'ED6_DT07/CH00322P._CP'),
        ('ED6_DT07/CH00324._CH', 'ED6_DT07/CH00324P._CP'),
        ('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP'),
        ('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT26/CH20327._CH', 'ED6_DT26/CH20327P._CP'),
        ('ED6_DT26/CH20310._CH', 'ED6_DT26/CH20310P._CP'),
    ]

# id: 0x10002 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 19810,
            z                   = 0,
            y                   = 166800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -31230,
            z           = -30,
            y           = 76720,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -22600,
            z           = 0,
            y           = 45730,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -1980,
            z           = 40,
            y           = 82660,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 8330,
            z           = -1840,
            y           = 91320,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 2350,
            z           = -1960,
            y           = 58080,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -31080,
            z           = -1990,
            y           = 103160,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5530,
            z           = -1920,
            y           = 140390,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 10740,
            z           = -2009,
            y           = 162000,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 10420,
            z           = -1910,
            y           = 77510,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -21780,
            z           = -2050,
            y           = 78280,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x2DA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 30,
            y           = -2100,
            z           = 179370,
            range       = 4750,
            dword_10    = 0xFFFFFBB4,
            dword_14    = 0x0002C31C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
    )

# id: 0x10005 offset: 0x2FA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 19360,
            triggerZ            = -1990,
            triggerY            = 166110,
            triggerRange        = 1000,
            actorX              = 19810,
            actorZ              = -490,
            actorY              = 166800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x31E
@scena.Code('PreInit')
def PreInit():
    OP_11(0x30, 0x78, 0xC8, 0x000061A8, 0x000109A0, 0x00000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 0, 0x1800)),
            Expr.Return,
        ),
        'loc_387',
    )

    OP_4A(0x000A, 255)
    SetChrPos(0x000A, 4880, -1940, 187950, 180)
    SetChrChipByIndex(0x000A, 15)
    ClearChrFlags(0x000A, 0x0040)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000A, 0x0001)
    OP_4A(0x0009, 255)
    SetChrPos(0x0009, 470, -1910, 187800, 45)
    SetChrChipByIndex(0x0009, 15)
    ClearChrFlags(0x0009, 0x0001)
    ClearChrFlags(0x0009, 0x0040)
    ClearChrFlags(0x0009, 0x0080)

    def _loc_387(): pass

    label('loc_387')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_3A3',
    )

    OP_20(0x00000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0004)

    Jump('loc_3BA')

    def _loc_3A3(): pass

    label('loc_3A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_3BA',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F1)
    Event(0, 0x0005)

    def _loc_3BA(): pass

    label('loc_3BA')

    Return()

# id: 0x0001 offset: 0x3BB
@scena.Code('Init')
def Init():
    ExecExpressionWithValue(
        0x000F,
        0x24,
        (
            (Expr.PushLong, 0xB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x24,
        (
            (Expr.PushLong, 0xB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 6, 0x1B16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E3',
    )

    OP_6F(0x0002, 0)

    Jump('loc_3EA')

    def _loc_3E3(): pass

    label('loc_3E3')

    OP_6F(0x0002, 60)

    def _loc_3EA(): pass

    label('loc_3EA')

    OP_71(0x0000, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_404',
    )

    OP_20(0x00000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_404(): pass

    label('loc_404')

    Return()

# id: 0x0002 offset: 0x405
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
        'loc_42A',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_56C')

    def _loc_42A(): pass

    label('loc_42A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_443',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_56C')

    def _loc_443(): pass

    label('loc_443')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45C',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_56C')

    def _loc_45C(): pass

    label('loc_45C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_475',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_56C')

    def _loc_475(): pass

    label('loc_475')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48E',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_56C')

    def _loc_48E(): pass

    label('loc_48E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A7',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_56C')

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C0',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_56C')

    def _loc_4C0(): pass

    label('loc_4C0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D9',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_56C')

    def _loc_4D9(): pass

    label('loc_4D9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F2',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_56C')

    def _loc_4F2(): pass

    label('loc_4F2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_50B',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_56C')

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_524',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_56C')

    def _loc_524(): pass

    label('loc_524')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53D',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_56C')

    def _loc_53D(): pass

    label('loc_53D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_556',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_56C')

    def _loc_556(): pass

    label('loc_556')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_56C',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_56C(): pass

    label('loc_56C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_581',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_56C')

    def _loc_581(): pass

    label('loc_581')

    Return()

# id: 0x0003 offset: 0x582
@scena.Code('func_03_582')
def func_03_582():
    UnlockAchievement(0x02, 0x02, 0x02, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 6, 0x1B16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_71A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 7, 0x1B17)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_666',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_05D9')
    def lambda_05D9():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_05D9)

    @scena.Lambda('lambda_05F4')
    def lambda_05F4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_05F4)

    ClearChrFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000000BA, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_641'),
        (0x00000002, 'loc_653'),
        (0x00000001, 'loc_663'),
        (-1, 'loc_666'),
    )

    def _loc_641(): pass

    label('loc_641')

    OP_A2(0x1B17)
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_666')

    def _loc_653(): pass

    label('loc_653')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_663(): pass

    label('loc_663')

    OP_B4(0x00)

    Return()

    def _loc_666(): pass

    label('loc_666')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['回避４'], 1)"),
            Expr.Return,
        ),
        'loc_6B5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['回避４']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B16)

    Jump('loc_717')

    def _loc_6B5(): pass

    label('loc_6B5')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['回避４']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['回避４']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_717(): pass

    label('loc_717')

    Jump('loc_749')

    def _loc_71A(): pass

    label('loc_71A')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_749(): pass

    label('loc_749')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x757
@scena.Code('func_04_757')
def func_04_757():
    EventBegin(0x00)
    SetChrPos(0x0009, 780, -1950, 187800, 177)
    SetChrPos(0x000A, 4330, -1940, 187800, 177)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-9890, 2120, 60910, 0)
    OP_67(0, 9310, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(36000, 0)
    OP_6E(564, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC13._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_07FA')
    def lambda_07FA():
        OP_6D(1860, -30, 185090, 13000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_07FA)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    @scena.Lambda('lambda_0826')
    def lambda_0826():
        OP_67(0, 6570, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0826)

    @scena.Lambda('lambda_083E')
    def lambda_083E():
        OP_6C(20000, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_083E)

    @scena.Lambda('lambda_084E')
    def lambda_084E():
        OP_6E(362, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_084E)

    WaitForThreadExit(0x0001, 0x0002)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0000, 0x0080)
    ClearChrFlags(0x0001, 0x0080)
    ClearChrFlags(0x0002, 0x0080)
    ClearChrFlags(0x0003, 0x0080)
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C1301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x894
@scena.Code('func_05_894')
def func_05_894():
    EventBegin(0x00)
    FormationReset()
    OP_BB(0x01, 0x01, 0x00000001)
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['乔丝特2'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['吉尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['多伦'], 0xF9, 0xFF)
    SetChrStatus(ChrTable['约修亚'], 0x00, 72)
    SetChrStatus(ChrTable['约修亚'], 0xFE, 0)
    EquipCmd(ChrTable['约修亚'], ItemTable['暗杀小刀'], 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['纤维大衣'], 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['斯托雷加Ｆ'], 0xFF)
    AddCraft(ChrTable['约修亚'], 0x0000)
    OP_37(0x01, 0x7F, 0x02)
    EquipCmd(ChrTable['约修亚'], ItemTable['行动力４'], 0x00)
    EquipCmd(ChrTable['约修亚'], ItemTable['回避４'], 0x01)
    EquipCmd(ChrTable['约修亚'], ItemTable['省ＥＰ４'], 0x02)
    EquipCmd(ChrTable['约修亚'], ItemTable['驱动２'], 0x03)
    EquipCmd(ChrTable['约修亚'], ItemTable['ＥＰ３'], 0x04)
    EquipCmd(ChrTable['约修亚'], ItemTable['精神３'], 0x05)
    EquipCmd(ChrTable['约修亚'], ItemTable['情报'], 0x06)
    OP_BB(0x01, 0x06, 0x000000EE)
    OP_D6(0x00)
    AddItem(ItemTable['回复药'], 5)
    AddItem(ItemTable['中回复药'], 2)
    AddItem(ItemTable['棕榈之药'], 2)
    AddItem(ItemTable['痊愈之药'], 1)
    AddItem(ItemTable['复苏药'], 2)
    AddItem(ItemTable['EP填充剂Ⅰ'], 1)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrPos(0x0009, 780, -1950, 187800, 177)
    SetChrPos(0x000A, 4330, -1940, 187800, 177)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_6D(2490, -1980, 188410, 0)
    OP_67(0, 5880, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(0, 0)
    OP_6E(263, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#3300280066V啊～好困。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280067V交班时间快点到吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280068V想不到都进入第二级警戒状态了，\n',
            '居然还是如此空闲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280069V刚才的小妹妹\n',
            '能再来就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280070V那个戴眼镜的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280071V你的兴趣可真古怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280072V个性确实有点独特，\n',
            '不过也很可爱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280073V想跟她认识认识～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280074V哈哈，那么你就趁\n',
            '休息时间去跟她打个招呼好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280075V不过……\n',
            '不知道情报部的那些余党\n',
            '到底在想什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280076V不管怎么看，他们似乎都\n',
            '藏在拉文努的废坑里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280077V谁知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280078V这些原精英部队份子考虑的事情\n',
            '我们怎么搞得清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x000B, 2440, -2040, 192000, 177)
    ClearChrFlags(0x000B, 0x0080)

    ChrTalk(
        0x000B,
        (
            '#3290280079V#6P……你们两个辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0C9C')
    def lambda_0C9C():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_0C9C)

    @scena.Lambda('lambda_0CAE')
    def lambda_0CAE():
        OP_8E(0x00FE, 2440, -2000, 189270, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0CAE)

    OP_8C(0x0009, 45, 400)
    OP_8C(0x000A, 315, 400)
    WaitForThreadExit(0x000B, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#3300280080V队、队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280081V您巡视辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3290280082V嗯，你们听着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3290280083V情报部的余党好像\n',
            '在格兰赛尔出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3290280084V以凯诺娜原上尉为首的\n',
            '全部成员都被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280085V是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280086V那么这样一来\n',
            '警戒体制就可以结束了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3290280087V不，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3290280088V听说王都出现了\n',
            '『会飞的巨大机器人』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3290280089V目前好像正在搜寻那个东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280090V会、会飞的巨大机器人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280091V那是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3290280092V我也不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3290280093V总而言之上头指示要\n',
            '持续警戒体制到天亮为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3290280094V不好意思，麻烦你们继续辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280095V呜呜……是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280096V……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 0, 400)
    OP_8E(0x000B, 2440, -2040, 192000, 2000, 0x00)
    OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x00, 0x000000C8)
    SetChrFlags(0x000B, 0x0080)
    Sleep(1000)

    ChrTurnDirection(0x0009, 0x000A, 400)

    ChrTalk(
        0x0009,
        (
            '#3300280097V哈……\n',
            '真是了不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280098V『会飞的巨大机器人』\n',
            '到底是什么啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0009, 400)

    ChrTalk(
        0x000A,
        (
            '#3310280099V谁知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280100V反正，不管怎样\n',
            '都已经没有被袭击的危险了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3310280101V接下来只要随便站到\n',
            '交班的时间就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280102V是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x00F8, 0x00, 0x32)
    Sleep(800)

    OP_62(0x0009, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0009, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#3300280103V……咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 270, 400)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#3310280104V什么，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3300280105V等等，好像有什么声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1168')
    def lambda_1168():
        OP_6D(2410, -2029, 186190, 3000)

        ExitThread()

    DispatchAsync(0x0129, 0x0000, lambda_1168)

    @scena.Lambda('lambda_1180')
    def lambda_1180():
        OP_6C(315000, 3000)

        ExitThread()

    DispatchAsync(0x0129, 0x0001, lambda_1180)

    CreateThread(0x0009, 0x00, 0x00, 0x0006)
    Sleep(300)

    OP_8C(0x000A, 225, 400)
    Sleep(2000)

    CreateThread(0x000A, 0x00, 0x00, 0x0007)
    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x000A, 0x0000)
    OP_20(0x00000BB8)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    WaitForThreadExit(0x0129, 0x0000)
    WaitForThreadExit(0x0129, 0x0001)
    ClearChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0102, 0x0004)
    SetChrPos(0x0102, 3800, 10000, 187900, 180)
    SetChrChipByIndex(0x0102, 17)
    SetChrSubChip(0x0102, 0)
    OP_7D(0x00, 0x0102, 0x0032, 0x01F4)
    OP_96(0x0102, 0x00000ED8, 0xFFFFF844, 0x0002DDFC, 0x00000064, 0x000005DC)
    OP_7D(0x01, 0x0102, 0x0000, 0x0000)
    OP_22(0x00A4, 0x00, 0x32)
    ClearChrFlags(0x0102, 0x0004)
    SetChrSubChip(0x0102, 1)
    Sleep(800)

    Fade(250)
    SetChrPos(0x0102, 3720, -1980, 187090, 180)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0102, 0x0002)
    SetChrChipByIndex(0x0102, 18)
    SetChrSubChip(0x0102, 0)
    OP_0D()

    @scena.Lambda('lambda_125D')
    def lambda_125D():
        OP_99(0x0102, 0x01, 0x03, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_125D)

    Sleep(300)

    OP_22(0x008F, 0x00, 0x64)

    ChrTalk(
        0x000A,
        (
            '#3310280106V啊……',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0102, 0x0000)
    CloseMessageWindow()

    @scena.Lambda('lambda_1294')
    def lambda_1294():
        OP_99(0x0102, 0x04, 0x06, 0x00000320)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1294)

    WaitForThreadExit(0x0102, 0x0000)
    Fade(250)
    OP_22(0x020C, 0x00, 0x64)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 15)
    SetChrPos(0x000A, 4000, -1980, 185970, 180)
    ClearChrFlags(0x0102, 0x0002)
    SetChrPos(0x0102, 3800, -1980, 187600, 180)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    OP_0D()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrFlags(0x0102, 0x0040)
    OP_7D(0x00, 0x0102, 0x0032, 0x01F4)
    SetChrChipByIndex(0x0102, 17)
    SetChrSubChip(0x0102, 0)

    @scena.Lambda('lambda_1322')
    def lambda_1322():
        OP_96(0x0102, 0x00000B54, 0xFFFFF7CC, 0x0002CA10, 0x000009C4, 0x00001770)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1322)

    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_1345')
    def lambda_1345():
        OP_8C(0x0009, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1345)

    Sleep(300)

    OP_22(0x00A4, 0x00, 0x64)
    OP_8C(0x0102, 0, 0)
    Sleep(300)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrSubChip(0x0102, 1)
    ClearChrFlags(0x0102, 0x0040)
    OP_7D(0x01, 0x0102, 0x0000, 0x0000)

    ChrTalk(
        0x0009,
        (
            '#3300280107V#5P喂、喂喂！\n',
            '怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(250)
    SetChrPos(0x0102, 2920, -2100, 183720, 0)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0102, 0x0002)
    SetChrFlags(0x0102, 0x0800)
    SetChrChipByIndex(0x0102, 18)
    SetChrSubChip(0x0102, 8)
    OP_0D()
    Sleep(300)

    @scena.Lambda('lambda_13E4')
    def lambda_13E4():
        OP_99(0x0102, 0x09, 0x0B, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_13E4)

    Sleep(300)

    OP_22(0x008F, 0x00, 0x64)

    ChrTalk(
        0x0009,
        (
            '#3300280108V#5P唔……',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0102, 0x0000)
    CloseMessageWindow()

    @scena.Lambda('lambda_141E')
    def lambda_141E():
        OP_99(0x0102, 0x0C, 0x0E, 0x00000320)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_141E)

    WaitForThreadExit(0x0102, 0x0000)
    Fade(250)
    OP_22(0x020C, 0x00, 0x64)
    ClearChrFlags(0x0009, 0x0080)
    SetChrChipByIndex(0x0009, 15)
    SetChrPos(0x0009, 3280, -2080, 183670, 0)
    ClearChrFlags(0x0102, 0x0002)
    ClearChrFlags(0x0102, 0x0800)
    SetChrPos(0x0102, 2880, -2100, 183230, 0)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020280109V#1033F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x012A, 0x0080)
    ClearChrFlags(0x0146, 0x0080)
    ClearChrFlags(0x0129, 0x0080)
    OP_9F(0x012A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0146, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0129, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x012A, 3250, -2100, 176180, 0)
    SetChrPos(0x0146, 2080, -2140, 176150, 0)
    SetChrPos(0x0129, 2740, -2130, 175160, 0)

    NpcTalk(
        0x012A,
        '男人的声音',
        (
            '#0290280110V#2P嘿嘿，挺厉害的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x012A, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)
    OP_9F(0x0146, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)
    OP_9F(0x0129, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

    @scena.Lambda('lambda_1569')
    def lambda_1569():
        OP_6D(2100, -2040, 182000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1569)

    @scena.Lambda('lambda_1581')
    def lambda_1581():
        OP_67(0, 6600, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1581)

    @scena.Lambda('lambda_1599')
    def lambda_1599():
        OP_6B(3510, 3000)

        ExitThread()

    DispatchAsync(0x012A, 0x0003, lambda_1599)

    @scena.Lambda('lambda_15A9')
    def lambda_15A9():
        OP_6E(242, 3000)

        ExitThread()

    DispatchAsync(0x0129, 0x0003, lambda_15A9)

    @scena.Lambda('lambda_15B9')
    def lambda_15B9():
        OP_8C(0x0102, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_15B9)

    Sleep(500)

    @scena.Lambda('lambda_15CC')
    def lambda_15CC():
        OP_8E(0x012A, 3400, -2009, 179780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0146, 0x0001, lambda_15CC)

    Sleep(200)

    @scena.Lambda('lambda_15EC')
    def lambda_15EC():
        OP_8E(0x0146, 2220, -2000, 179960, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x012A, 0x0001, lambda_15EC)

    Sleep(200)

    @scena.Lambda('lambda_160C')
    def lambda_160C():
        OP_8E(0x0129, 2880, -1990, 178560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0129, 0x0001, lambda_160C)

    Sleep(2000)

    WaitForThreadExit(0x012A, 0x0001)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x012A,
        (
            '#0290280111V#200F#6P了不起。\n',
            '一转眼就搞定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280112V#210F#5P嗯，嗯……\n',
            '挺有一手的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280113V#1035F……这不算什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280114V让松懈的士兵\n',
            '睡一觉可谓轻而易举。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280115V#413F#5P嗯，知道了知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280116V是我自己太傻，\n',
            '老是希望你的个性会可爱一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0129,
        (
            '#0300280117V#197F不过『山猫号』确实\n',
            '在这里吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300280118V我还以为被运到\n',
            '那个要塞去了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280119V#1030F据我的调查是没有错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280120V而且还被作为飞行训练使用过，\n',
            '应该已经进行了整备才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280121V#200F#6P嘿嘿，那就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290280122V只不过要起动机体的话，\n',
            '必须有『山猫号』的启动钥匙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290280123V可以弄得到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280124V#1035F刚才那个守备队长\n',
            '身上应该有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280125V大概准备在交付帝国军飞艇时\n',
            '一并交给对方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280126V#210F#5P也就是要强行抢回是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280127V#1030F不过不可以用杀人的方式。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280128V没有必要的话，\n',
            '最好不要与王国军为敌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280129V也尽量不要让那些\n',
            '巡逻的卫兵发现我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280130V#413F#5P真是的……\n',
            '好乱来的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280131V#210F不过我也确实\n',
            '反对杀人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0129,
        (
            '#0300280132V#490F嘿嘿，当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300280133V谁让我们『卡普亚一家』\n',
            '是禁止杀人和施暴的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280134V#203F#6P唉，我们其实\n',
            '没法彻底成为恶人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290280135V可能就像那个少尉说的那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280136V#1031F……呵呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280137V#216F#5P有、有什么好笑的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280138V#1035F不是……\n',
            '我们的时间不多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280139V快点开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280140V#212F#5P嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280141V#200F#6P终于要开始了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0129,
        (
            '#0300280142V#196F好～……\n',
            '加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_1D(0x59)
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(2830, -1970, 185370, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_4A(0x000A, 255)
    SetChrPos(0x000A, 4880, -1940, 188000, 180)
    SetChrChipByIndex(0x000A, 15)
    ClearChrFlags(0x000A, 0x0040)
    ClearChrFlags(0x000A, 0x0080)
    OP_4A(0x0009, 255)
    SetChrPos(0x0009, 470, -1910, 187870, 45)
    SetChrChipByIndex(0x0009, 15)
    ClearChrFlags(0x0009, 0x0040)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0000, 2830, -1970, 185370, 0)
    SetChrPos(0x0001, 2830, -1970, 185370, 0)
    SetChrPos(0x0002, 2830, -1970, 185370, 0)
    SetChrPos(0x0003, 2830, -1970, 185370, 0)
    OP_69(0x0000, 0x00000000)
    OP_A2(0x1800)
    AddItem(ItemTable['魔兽手册'], 1)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x1D10
@scena.Code('func_06_1D10')
def func_06_1D10():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 16)
    OP_8E(0x00FE, 2510, -1980, 187040, 2000, 0x00)
    OP_8E(0x00FE, 2870, -2080, 183660, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    OP_22(0x00D8, 0x00, 0x46)
    SetChrChipByIndex(0x00FE, 12)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0007 offset: 0x1D59
@scena.Code('func_07_1D59')
def func_07_1D59():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 16)
    OP_8E(0x00FE, 3690, -1980, 187270, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    OP_22(0x00D8, 0x00, 0x46)
    SetChrChipByIndex(0x00FE, 12)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0008 offset: 0x1D8E
@scena.Code('func_08_1D8E')
def func_08_1D8E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 0, 0x1800)),
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 6, 0x1806)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DEE',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0102,
        (
            '#0020280143V#1030F（时间并不宽裕。\n',
            '赶快进去吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_1DEE(): pass

    label('loc_1DEE')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
