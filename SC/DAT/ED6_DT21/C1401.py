import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1401   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, '士兵拉凯尔'),
    TXT(0x03, '士兵古特'),
    TXT(0x04, ''),
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
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1401.x'
    header.mapIndex       = 60
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xDBC
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
    ]

# id: 0x10002 offset: 0x102
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
            x                   = 860,
            z                   = -1910,
            y                   = 188180,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 4130,
            z                   = -1910,
            y                   = 188050,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x162
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
            x           = -21980,
            z           = -30,
            y           = 47990,
            word_0C     = 0x0026,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -2600,
            z           = 10,
            y           = 79910,
            word_0C     = 0x00DB,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 7230,
            z           = -1190,
            y           = 93200,
            word_0C     = 0x011D,
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
            x           = 4790,
            z           = -1950,
            y           = 141270,
            word_0C     = 0x00FC,
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
            x           = 8460,
            z           = -2020,
            y           = 79300,
            word_0C     = 0x0118,
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

# id: 0x10004 offset: 0x27A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 920,
            y           = -3000,
            z           = 189170,
            range       = 4030,
            dword_10    = 0x000007D0,
            dword_14    = 0x0002E180,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10005 offset: 0x29A
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
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2BE
@scena.Code('PreInit')
def PreInit():
    OP_11(0xFF, 0xFF, 0xFF, 0x000080E8, 0x0000E290, 0x00000000)

    Return()

# id: 0x0001 offset: 0x2CF
@scena.Code('Init')
def Init():
    OP_C4(0x00, 0x00000004)

    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x24,
        (
            (Expr.PushLong, 0xB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0000, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 6, 0x1B16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_302',
    )

    OP_6F(0x0002, 0)

    Jump('loc_309')

    def _loc_302(): pass

    label('loc_302')

    OP_6F(0x0002, 60)

    def _loc_309(): pass

    label('loc_309')

    OP_71(0x0001, 0x0004)

    Return()

# id: 0x0002 offset: 0x30F
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
        'loc_334',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_476')

    def _loc_334(): pass

    label('loc_334')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34D',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_476')

    def _loc_34D(): pass

    label('loc_34D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_366',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_476')

    def _loc_366(): pass

    label('loc_366')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37F',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_476')

    def _loc_37F(): pass

    label('loc_37F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_398',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_476')

    def _loc_398(): pass

    label('loc_398')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B1',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_476')

    def _loc_3B1(): pass

    label('loc_3B1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CA',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_476')

    def _loc_3CA(): pass

    label('loc_3CA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E3',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_476')

    def _loc_3E3(): pass

    label('loc_3E3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FC',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_476')

    def _loc_3FC(): pass

    label('loc_3FC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_415',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_476')

    def _loc_415(): pass

    label('loc_415')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42E',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_476')

    def _loc_42E(): pass

    label('loc_42E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_447',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_476')

    def _loc_447(): pass

    label('loc_447')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_460',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_476')

    def _loc_460(): pass

    label('loc_460')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_476',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_476(): pass

    label('loc_476')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_48B',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_476')

    def _loc_48B(): pass

    label('loc_48B')

    Return()

# id: 0x0003 offset: 0x48C
@scena.Code('func_03_48C')
def func_03_48C():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_588',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_52B',
    )

    ChrTalk(
        0x00FE,
        (
            '听说哈肯大门那边\n',
            '现在的情况非常紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是国境的大门一直开着，\n',
            '没有办法关上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '国、国境师团的士兵们\n',
            '这下可不得了了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_585')

    def _loc_52B(): pass

    label('loc_52B')

    ChrTalk(
        0x00FE,
        (
            '听说哈肯大门那边\n',
            '现在的情况非常紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是国境的大门一直开着，\n',
            '没有办法关上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_585(): pass

    label('loc_585')

    Jump('loc_784')

    def _loc_588(): pass

    label('loc_588')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_5FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5D8',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，不好意思，这里\n',
            '现在还是禁止进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_5F7')

    def _loc_5D8(): pass

    label('loc_5D8')

    ChrTalk(
        0x00FE,
        (
            '这里禁止入内。\n',
            '请回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F7(): pass

    label('loc_5F7')

    Jump('loc_784')

    def _loc_5FA(): pass

    label('loc_5FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_66B',
    )

    ChrTalk(
        0x00FE,
        (
            '结果最后好像还是无法将\n',
            '那条龙捕获呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然要倾尽王国军\n',
            '的全部力量来围剿，\n',
            '真是可怕的生物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_784')

    def _loc_66B(): pass

    label('loc_66B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_6B3',
    )

    ChrTalk(
        0x00FE,
        (
            '总觉得龙还潜藏在\n',
            '附近呢，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜、拜托了\n',
            '不要来这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_784')

    def _loc_6B3(): pass

    label('loc_6B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_784',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6EF',
    )

    ChrTalk(
        0x00FE,
        (
            '这里禁止入内的。\n',
            '请老老实实地回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_784')

    def _loc_6EF(): pass

    label('loc_6EF')

    ChrTalk(
        0x00FE,
        (
            '啊，你们是旅行者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，这里\n',
            '现在禁止通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从空贼艇被抢走之后，\n',
            '这里的警备就\n',
            '更加森严了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不要给我们\n',
            '添太多麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_784(): pass

    label('loc_784')

    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0x788
@scena.Code('func_04_788')
def func_04_788():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_8A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_839',
    )

    ChrTalk(
        0x00FE,
        (
            '哈肯大门那边的情况\n',
            '好像也不太好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟才刚签署完互不侵犯条约，\n',
            '我想帝国应该不会乱来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话虽然是这么说，\n',
            '但是战争这种事情谁也说不准的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_89D')

    def _loc_839(): pass

    label('loc_839')

    ChrTalk(
        0x00FE,
        (
            '哈肯大门那边的情况\n',
            '好像也不太好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟才刚签署完互不侵犯条约，\n',
            '我想帝国应该不会乱来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_89D(): pass

    label('loc_89D')

    Jump('loc_B6A')

    def _loc_8A0(): pass

    label('loc_8A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_93B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_90D',
    )

    ChrTalk(
        0x00FE,
        (
            '再往前就是王国军的训练设施，\n',
            '禁止民间人士入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，\n',
            '还是请你们离开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_938')

    def _loc_90D(): pass

    label('loc_90D')

    ChrTalk(
        0x00FE,
        (
            '禁止民间人士入内。\n',
            '还是请你们离开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_938(): pass

    label('loc_938')

    Jump('loc_B6A')

    def _loc_93B(): pass

    label('loc_93B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_A22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_9A6',
    )

    ChrTalk(
        0x00FE,
        (
            '这里几乎没有人\n',
            '会来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以最主要的工作\n',
            '就是别让自己睡着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼啊啊～啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A1F')

    def _loc_9A6(): pass

    label('loc_9A6')

    ChrTalk(
        0x00FE,
        (
            '哎呀呀、龙的骚乱事件\n',
            '似乎也已经平息了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恢复和平固然是很好，\n',
            '但日子又开始变得无聊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼啊啊～啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_A1F(): pass

    label('loc_A1F')

    Jump('loc_B6A')

    def _loc_A22(): pass

    label('loc_A22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_A88',
    )

    ChrTalk(
        0x00FE,
        (
            '迷雾峡谷的西部\n',
            '在地图中也都没有标识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '误闯进去的话非常危险，\n',
            '所以平时都把桥撤掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6A')

    def _loc_A88(): pass

    label('loc_A88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_B6A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_AD2',
    )

    ChrTalk(
        0x00FE,
        (
            '前面禁止民间人士\n',
            '进入了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，请回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6A')

    def _loc_AD2(): pass

    label('loc_AD2')

    ChrTalk(
        0x00FE,
        (
            '自从遭到空贼团的入侵之后，\n',
            '这里的警备就更加森严了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以说，\n',
            '现在这里禁止民间人士入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连猫也不能放进去一只，\n',
            '这是队长下达的死命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_B6A(): pass

    label('loc_B6A')

    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0xB6E
@scena.Code('func_05_B6E')
def func_05_B6E():
    UnlockAchievement(0x02, 0x02, 0x02, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 6, 0x1B16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D06',
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
        'loc_C52',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0BC5')
    def lambda_0BC5():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BC5)

    @scena.Lambda('lambda_0BE0')
    def lambda_0BE0():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0BE0)

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
        (0x00000000, 'loc_C2D'),
        (0x00000002, 'loc_C3F'),
        (0x00000001, 'loc_C4F'),
        (-1, 'loc_C52'),
    )

    def _loc_C2D(): pass

    label('loc_C2D')

    OP_A2(0x1B17)
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_C52')

    def _loc_C3F(): pass

    label('loc_C3F')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_C4F(): pass

    label('loc_C4F')

    OP_B4(0x00)

    Return()

    def _loc_C52(): pass

    label('loc_C52')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['回避４'], 1)"),
            Expr.Return,
        ),
        'loc_CA1',
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

    Jump('loc_D03')

    def _loc_CA1(): pass

    label('loc_CA1')

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

    def _loc_D03(): pass

    label('loc_D03')

    Jump('loc_D35')

    def _loc_D06(): pass

    label('loc_D06')

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
    def _loc_D35(): pass

    label('loc_D35')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xD43
@scena.Code('func_06_D43')
def func_06_D43():
    EventBegin(0x01)
    ChrTurnDirection(0x000A, 0x0000, 400)

    ChrTalk(
        0x000A,
        (
            '这里禁止\n',
            '民间人士进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不好意思，请回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 0, 0, -1200, 2000, 0x00)
    OP_8C(0x000A, 180, 400)
    Fade(500)
    OP_30(0x01)
    SetMapFlags(0x00000001)
    OP_0D()
    EventEnd(0x03)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
