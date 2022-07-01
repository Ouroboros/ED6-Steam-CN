import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1120_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1120   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '赛恩'),
    TXT(0x02, '科梅尔斯'),
    TXT(0x03, '卡莉娅'),
    TXT(0x04, '斯丁克'),
    TXT(0x05, '阿尔丹'),
    TXT(0x06, '库瓦诺老人'),
    TXT(0x07, '罗亚'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1120.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0x000C
    header.importTable    = ['ED6_DT21/T1120._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2D11
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
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT27/CH03790._CH', 'ED6_DT27/CH03790P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 500,
            z                   = 0,
            y                   = 7400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -24500,
            z                   = 0,
            y                   = 4690,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -28800,
            z                   = 0,
            y                   = 24200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -2460,
            z                   = 0,
            y                   = 2950,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -26270,
            z                   = 0,
            y                   = 2690,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -22750,
            z                   = 0,
            y                   = 4660,
            direction           = 266,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -28810,
            z                   = 0,
            y                   = 1020,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
    )

# id: 0x10003 offset: 0x1BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1BA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1BA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -24000,
            triggerZ            = 0,
            triggerY            = 3580,
            triggerRange        = 700,
            actorX              = -24500,
            actorZ              = 1500,
            actorY              = 4690,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 920,
            triggerZ            = 0,
            triggerY            = 6280,
            triggerRange        = 700,
            actorX              = 500,
            actorZ              = 1500,
            actorY              = 7400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x202
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_235',
    )

    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_223',
    )

    ClearChrFlags(0x000E, 0x0080)

    Jump('loc_232')

    def _loc_223(): pass

    label('loc_223')

    SetChrFlags(0x0009, 0x0010)
    ClearChrFlags(0x000D, 0x0010)
    ClearChrFlags(0x000C, 0x0010)

    def _loc_232(): pass

    label('loc_232')

    Jump('loc_246')

    def _loc_235(): pass

    label('loc_235')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_246',
    )

    SetChrFlags(0x000A, 0x0010)

    def _loc_246(): pass

    label('loc_246')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_264',
    )

    ClearChrFlags(0x000B, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_264',
    )

    SetChrFlags(0x000B, 0x0010)

    def _loc_264(): pass

    label('loc_264')

    Return()

# id: 0x0001 offset: 0x265
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x266
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
        'loc_28B',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_3CD')

    def _loc_28B(): pass

    label('loc_28B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A4',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_3CD')

    def _loc_2A4(): pass

    label('loc_2A4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BD',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_3CD')

    def _loc_2BD(): pass

    label('loc_2BD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D6',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_3CD')

    def _loc_2D6(): pass

    label('loc_2D6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EF',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_3CD')

    def _loc_2EF(): pass

    label('loc_2EF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_308',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_3CD')

    def _loc_308(): pass

    label('loc_308')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_321',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_3CD')

    def _loc_321(): pass

    label('loc_321')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33A',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_3CD')

    def _loc_33A(): pass

    label('loc_33A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_353',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_3CD')

    def _loc_353(): pass

    label('loc_353')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36C',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_3CD')

    def _loc_36C(): pass

    label('loc_36C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_385',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_3CD')

    def _loc_385(): pass

    label('loc_385')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39E',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_3CD')

    def _loc_39E(): pass

    label('loc_39E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B7',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_3CD')

    def _loc_3B7(): pass

    label('loc_3B7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CD',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_3CD(): pass

    label('loc_3CD')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3E2',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_3CD')

    def _loc_3E2(): pass

    label('loc_3E2')

    Return()

# id: 0x0003 offset: 0x3E3
@scena.Code('func_03_3E3')
def func_03_3E3():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x3E8
@scena.Code('func_04_3E8')
def func_04_3E8():
    TalkBegin(0x0008)
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
        'loc_457',
    )

    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_44F',
    )

    OP_A9(0x53)

    Jump('loc_451')

    def _loc_44F(): pass

    label('loc_44F')

    OP_A9(0x33)

    def _loc_451(): pass

    label('loc_451')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_457(): pass

    label('loc_457')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_468',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_468(): pass

    label('loc_468')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_54F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F4',
    )

    ChrTalk(
        0x0008,
        (
            '真头痛。\n',
            '几乎都没什么客人来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '人气很旺的护身用导力枪\n',
            '很多人都用不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '一般人对剑和棍\n',
            '根本就不会有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_54C')

    def _loc_4F4(): pass

    label('loc_4F4')

    ChrTalk(
        0x0008,
        (
            '平时的话普通的客人\n',
            '可是会陆续上门的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '主力商品导力枪\n',
            '无法使用影响果然巨大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_54C(): pass

    label('loc_54C')

    Jump('loc_B73')

    def _loc_54F(): pass

    label('loc_54F')

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
        'loc_5CC',
    )

    ChrTalk(
        0x0008,
        (
            '虽然隔壁忙得一塌糊涂，\n',
            '但正如你所见，我这里生意很差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '非导力兵器也大量到货了，\n',
            '请慢慢挑选吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_5F7')

    def _loc_5CC(): pass

    label('loc_5CC')

    ChrTalk(
        0x0008,
        (
            '如你所见我们这里很空闲。\n',
            '慢慢挑选喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F7(): pass

    label('loc_5F7')

    Jump('loc_B73')

    def _loc_5FA(): pass

    label('loc_5FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_6BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_655',
    )

    ChrTalk(
        0x0008,
        (
            '龙的事件解决了，\n',
            '真的是只差一步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这样一来\n',
            '终于可以当商人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B8')

    def _loc_655(): pass

    label('loc_655')

    ChrTalk(
        0x0008,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '龙的事件解决了，\n',
            '真的是只差一步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，这样一来\n',
            '终于可以当商人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_6B8(): pass

    label('loc_6B8')

    Jump('loc_B73')

    def _loc_6BB(): pass

    label('loc_6BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_961',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0348, 7, 0x1A47)),
            Expr.Return,
        ),
        'loc_7D1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_778',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_718',
    )

    ChrTalk(
        0x0008,
        (
            '王国军的作战\n',
            '不知道怎么样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '怎么几乎没有音讯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_775')

    def _loc_718(): pass

    label('loc_718')

    ChrTalk(
        0x0008,
        (
            '说来王国军的作战\n',
            '不知道怎么样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好像连飞行舰队也投入了，\n',
            '怎么几乎没有音讯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_775(): pass

    label('loc_775')

    Jump('loc_7CE')

    def _loc_778(): pass

    label('loc_778')

    ChrTurnDirection(0x0008, 0x0106, 0)

    ChrTalk(
        0x0008,
        (
            '但是不知道要消灭什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这剑制造得相当坚固。\n',
            '别担心，尽管放手用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_7CE(): pass

    label('loc_7CE')

    Jump('loc_95E')

    def _loc_7D1(): pass

    label('loc_7D1')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0106, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '嘿，是你啊。\n',
            '剑的情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F目前没什么问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '部件的结合部位也\n',
            '也非常地密实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这样啊。\n',
            '那真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '毕竟是把造的很结实的剑啊。\n',
            '尽情挥舞吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F是，不用说\n',
            '我也会马上这么做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#552F即使只能用２，３下，\n',
            '那也就够了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '嗯，虽然不是很清楚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总之有什么事就来吧。\n',
            '调整什么的我都会帮你做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A47)
    OP_A2(0x0001)
    def _loc_95E(): pass

    label('loc_95E')

    Jump('loc_B73')

    def _loc_961(): pass

    label('loc_961')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_A5E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9CA',
    )

    ChrTalk(
        0x0008,
        (
            '超市的商人们\n',
            '好像改到餐厅和酒店做生意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因此市民的生活\n',
            '暂时没有太大的混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5B')

    def _loc_9CA(): pass

    label('loc_9CA')

    ChrTalk(
        0x0008,
        (
            '超市的商人们\n',
            '好像改到餐厅和酒店做生意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '听说梅贝尔市长请求\n',
            '各店铺协力，\n',
            '真是佩服市长她的果断啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因此市民的生活\n',
            '也有所好转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_A5B(): pass

    label('loc_A5B')

    Jump('loc_B73')

    def _loc_A5E(): pass

    label('loc_A5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_B31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AB8',
    )

    ChrTalk(
        0x0008,
        (
            '超市没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那里假如不能营业的话，\n',
            '市民的生活会非常混乱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B2E')

    def _loc_AB8(): pass

    label('loc_AB8')

    ChrTalk(
        0x0008,
        (
            '感觉好像\n',
            '出大事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然有人受伤，但\n',
            '超市没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那里假如不能营业的话，\n',
            '市民的生活会非常混乱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_B2E(): pass

    label('loc_B2E')

    Jump('loc_B73')

    def _loc_B31(): pass

    label('loc_B31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_B73',
    )

    ChrTalk(
        0x0008,
        (
            '噢，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '新进了一批好东西噢。\n',
            '好好看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B73(): pass

    label('loc_B73')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xB77
@scena.Code('func_05_B77')
def func_05_B77():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0xB7C
@scena.Code('func_06_B7C')
def func_06_B7C():
    TalkBegin(0x0009)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_BCE',
    )

    Call(6, 0x0003)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BBA',
    )

    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_BB2',
    )

    OP_A9(0x52)

    Jump('loc_BB4')

    def _loc_BB2(): pass

    label('loc_BB2')

    OP_A9(0x32)

    def _loc_BB4(): pass

    label('loc_BB4')

    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_BBA(): pass

    label('loc_BBA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BCB',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_BCB(): pass

    label('loc_BCB')

    Jump('loc_14FF')

    def _loc_BCE(): pass

    label('loc_BCE')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14FF',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -23800, 0, 2400, 0)
    SetChrPos(0x0102, -24600, 0, 2200, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C35',
    )

    SetChrPos(0x00F9, -24200, 0, 1200, 0)
    SetChrPos(0x00F8, -25100, 0, 1000, 0)

    Jump('loc_C57')

    def _loc_C35(): pass

    label('loc_C35')

    SetChrPos(0x00F8, -24200, 0, 1200, 0)
    SetChrPos(0x00F9, -25100, 0, 1000, 0)

    def _loc_C57(): pass

    label('loc_C57')

    OP_8C(0x0009, 180, 0)
    OP_6D(-24840, 0, 3030, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '啊，欢迎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '让你们大老远跑来真的很抱歉，\n',
            '不过工房暂时无法使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '工作中用到的器材\n',
            '全部无法使用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 6, 0x20E6)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_D4A',
    )

    ChrTalk(
        0x0101,
        (
            '#1018F#4P啊，那个不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们带了好东西来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好东西……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1199')

    def _loc_D4A(): pass

    label('loc_D4A')

    ChrTalk(
        0x0101,
        (
            '#1026F#4P啊，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯……不过真伤脑筋啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '结晶回路的合成和结晶孔的强化\n',
            '都完全不能进行……',
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
        'loc_DF9',
    )

    ChrTalk(
        0x0103,
        (
            '#025F嗯嗯，难得有了这的发生器，\n',
            '真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E94')

    def _loc_DF9(): pass

    label('loc_DF9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E3C',
    )

    ChrTalk(
        0x0108,
        (
            '#072F唔，难得有了这的发生器，\n',
            '真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E94')

    def _loc_E3C(): pass

    label('loc_E3C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E94',
    )

    ChrTalk(
        0x0106,
        (
            '#552F啊啊，难得有了这的发生器，\n',
            '恢复导力魔法了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E94(): pass

    label('loc_E94')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EE9',
    )

    ChrTalk(
        0x0107,
        (
            '#064F啊，不过姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果只是一小会儿，\n',
            '那我或许有点办法喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F36')

    def _loc_EE9(): pass

    label('loc_EE9')

    ChrTalk(
        0x0102,
        (
            '#1043F的确是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1040F不过，如果只是一小会儿\n',
            '那我或许有点办法喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F36(): pass

    label('loc_F36')

    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FB3',
    )

    @scena.Lambda('lambda_0F66')
    def lambda_0F66():
        ChrTurnDirection(0x0000, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0F66)

    Sleep(120)

    @scena.Lambda('lambda_0F79')
    def lambda_0F79():
        ChrTurnDirection(0x0001, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0F79)

    @scena.Lambda('lambda_0F87')
    def lambda_0F87():
        ChrTurnDirection(0x0002, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0F87)

    Sleep(120)

    @scena.Lambda('lambda_0F9A')
    def lambda_0F9A():
        ChrTurnDirection(0x0003, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0F9A)

    @scena.Lambda('lambda_0FA8')
    def lambda_0FA8():
        ChrTurnDirection(0x0009, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0FA8)

    Jump('loc_FBA')

    def _loc_FB3(): pass

    label('loc_FB3')

    ChrTurnDirection(0x0101, 0x0102, 400)

    def _loc_FBA(): pass

    label('loc_FBA')

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#1004F#4P啊……！？',
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
        'loc_1017',
    )

    ChrTalk(
        0x0106,
        (
            '#052F能让工房运作起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1072')

    def _loc_1017(): pass

    label('loc_1017')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1045',
    )

    ChrTalk(
        0x0103,
        (
            '#023F能让工房运作起来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1072')

    def _loc_1045(): pass

    label('loc_1045')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1072',
    )

    ChrTalk(
        0x0108,
        (
            '#073F能让工房运作起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1072(): pass

    label('loc_1072')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10B6',
    )

    ChrTalk(
        0x0107,
        (
            '#060F是，是，大概……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '使用那个发生器的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10FC')

    def _loc_10B6(): pass

    label('loc_10B6')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P是，我想……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果使用那个发生器\n',
            '应该能在短时间内复原。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10FC(): pass

    label('loc_10FC')

    ChrTalk(
        0x0101,
        (
            '#1018F#4P啊，原来如此！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '到底在说些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1149')
    def lambda_1149():
        ChrTurnDirection(0x0000, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1149)

    Sleep(120)

    @scena.Lambda('lambda_115C')
    def lambda_115C():
        ChrTurnDirection(0x0001, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_115C)

    @scena.Lambda('lambda_116A')
    def lambda_116A():
        ChrTurnDirection(0x0002, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_116A)

    Sleep(120)

    @scena.Lambda('lambda_117D')
    def lambda_117D():
        ChrTurnDirection(0x0003, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_117D)

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    def _loc_1199(): pass

    label('loc_1199')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P那个，是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了使用『零力场发生器』\n',
            '可暂时恢复工房机能的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '啊～～～很厉害的装置啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，全拜托你了。\n',
            '快点来试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#4P嗯，那我们就开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12AB',
    )

    ChrTalk(
        0x0107,
        (
            '#560F那么～\n',
            '请稍等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12DB')

    def _loc_12AB(): pass

    label('loc_12AB')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P那么，稍等片刻。\n',
            '借用一下机械了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12DB(): pass

    label('loc_12DB')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_22(0x009D, 0x00, 0x64)
    OP_8C(0x0009, 270, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '使用『零力场发生器』将工房机能恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '噢，机械确实动起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 6, 0x20E6)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1377',
    )

    ChrTurnDirection(0x0009, 0x0000, 400)

    Jump('loc_1467')

    def _loc_1377(): pass

    label('loc_1377')

    ChrTalk(
        0x0101,
        (
            '#1000F#4P太好了……看来是成功了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13F6',
    )

    ChrTalk(
        0x0107,
        (
            '#063F嗯，不过这\n',
            '只是暂时能动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#561F马上又会回到不动的状态的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1444')

    def _loc_13F6(): pass

    label('loc_13F6')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P嗯，确实很顺利……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但并不是真的修好了。\n',
            '过一段时间又会停止的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1444(): pass

    label('loc_1444')

    ChrTurnDirection(0x0009, 0x0000, 400)

    ChrTalk(
        0x0009,
        (
            '这样的话必须要赶紧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1467(): pass

    label('loc_1467')

    ChrTalk(
        0x0009,
        (
            '来，要调整导力器的话\n',
            '就趁现在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x52)
    OP_56(0x00)
    OP_0D()
    Sleep(30)

    ChrTalk(
        0x0009,
        (
            '今后要使用工房时\n',
            '也请把那个装置带来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样的话就能\n',
            '一直的使用工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)
    OP_A2(0x20E2)
    EventEnd(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_14FF(): pass

    label('loc_14FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_15AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1587',
    )

    ChrTalk(
        0x0009,
        (
            '修理什么的\n',
            '本来就是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为各位的导力器\n',
            '并没有发生故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唉哟哟……\n',
            '这样说明到底是第几次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_15A8')

    def _loc_1587(): pass

    label('loc_1587')

    ChrTalk(
        0x0009,
        (
            '都说了……\n',
            '并不是出故障了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A8(): pass

    label('loc_15A8')

    Jump('loc_1AA7')

    def _loc_15AB(): pass

    label('loc_15AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_167B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1630',
    )

    ChrTalk(
        0x0009,
        (
            '从早上开始就不断\n',
            '有要求修理的顾客前来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '就算说明了\n',
            '不是出故障了也不肯回去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '啊～谁来救救我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_1678')

    def _loc_1630(): pass

    label('loc_1630')

    ChrTalk(
        0x0009,
        (
            '要求修理的\n',
            '客人可真多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不管怎么说\n',
            '都会有人源源不断的赶来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1678(): pass

    label('loc_1678')

    Jump('loc_1AA7')

    def _loc_167B(): pass

    label('loc_167B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1777',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_16E6',
    )

    ChrTalk(
        0x0009,
        (
            '超市的硬件设施\n',
            '已经完全恢复到原来的模样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '没有超市的话\n',
            '果然没有柏斯的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1774')

    def _loc_16E6(): pass

    label('loc_16E6')

    ChrTalk(
        0x0009,
        (
            '呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '来看超市的吗？\n',
            '已经完全恢复了原貌哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那里果然是\n',
            '柏斯市的象征啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '超市一开门，\n',
            '好像整个城市就又恢复了活力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1774(): pass

    label('loc_1774')

    Jump('loc_1AA7')

    def _loc_1777(): pass

    label('loc_1777')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_18CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_17E4',
    )

    ChrTalk(
        0x0009,
        (
            '感觉在超市做事\n',
            '是最快乐的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '将来若是有一天能再次\n',
            '怀着那样的心情做生意就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C9')

    def _loc_17E4(): pass

    label('loc_17E4')

    ChrTalk(
        0x0009,
        (
            '为了超市的修复\n',
            '稍微出了一点力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我也以那里\n',
            '作为人生的起点的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '现在回想起来\n',
            '那个超市时代\n',
            '才是最开心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '和尼冈德那家伙一起\n',
            '为了追求梦想已经尽了全力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哈哈，要是时光可以倒流的话，\n',
            '真想回到那个时代啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_18C9(): pass

    label('loc_18C9')

    Jump('loc_1AA7')

    def _loc_18CC(): pass

    label('loc_18CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_192B',
    )

    ChrTalk(
        0x0009,
        (
            '古代龙什么的\n',
            '真的活着啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '以前在酒馆里\n',
            '听说过这些事、\n',
            '当时完全不当一回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA7')

    def _loc_192B(): pass

    label('loc_192B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1999',
    )

    ChrTalk(
        0x0009,
        (
            '北街区的超市似乎\n',
            '好像出什么事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '大家正在议论，\n',
            '巨大的怪物什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '到底出什么事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA7')

    def _loc_1999(): pass

    label('loc_1999')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1AA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_19FA',
    )

    ChrTalk(
        0x0009,
        (
            '霸占我店铺的那个\n',
            '尼冈德还在服刑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '倒是和他通过信，\n',
            '监狱生活相当苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA7')

    def _loc_19FA(): pass

    label('loc_19FA')

    ChrTalk(
        0x0009,
        (
            '以前，霸占我店铺的那个\n',
            '叫尼冈德的家伙还在服刑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '倒是和他通过信，\n',
            '监狱生活相当苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我当上店主之后，\n',
            '商店的经营变得有条不紊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '所以请务必\n',
            '放心购物吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1AA7(): pass

    label('loc_1AA7')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x1AAB
@scena.Code('func_07_1AAB')
def func_07_1AAB():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1BA5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B51',
    )

    ChrTalk(
        0x00FE,
        (
            '客人们好像还在坚持啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器不是外行能搞懂的。\n',
            '说明不被理解是自然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，做出说明是店主的责任。\n',
            '虽然有点同情，但没有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_1BA2')

    def _loc_1B51(): pass

    label('loc_1B51')

    ChrTalk(
        0x00FE,
        (
            '客人们好像还在坚持啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器不是外行能搞懂的。\n',
            '说明不被理解是自然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BA2(): pass

    label('loc_1BA2')

    Jump('loc_2168')

    def _loc_1BA5(): pass

    label('loc_1BA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C5F',
    )

    ChrTalk(
        0x00FE,
        (
            '是什么原因让客人们一大早\n',
            '就气冲冲的冲进来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，接待客人是店主的职责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自己的工作\n',
            '只能自己承担。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '包括导力器无法工作在内，\n',
            '要做的事有一大堆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_1C9C')

    def _loc_1C5F(): pass

    label('loc_1C5F')

    ChrTalk(
        0x00FE,
        (
            '接待客人是店主的职责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自己的工作，\n',
            '只能自己承担。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C9C(): pass

    label('loc_1C9C')

    Jump('loc_2168')

    def _loc_1C9F(): pass

    label('loc_1C9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1DD8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1D12',
    )

    ChrTalk(
        0x00FE,
        (
            '市长官邸好像收到了\n',
            '一块极品金耀石结晶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是某人赠送的，\n',
            '世上竟然有出手这么阔绰的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD5')

    def _loc_1D12(): pass

    label('loc_1D12')

    ChrTalk(
        0x00FE,
        (
            '市长官邸好像收到了\n',
            '一块特大号的金耀石。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是某人赠送的，\n',
            '世上竟然有出手这么阔绰的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，如此巨大的结晶\n',
            '是无法在城里的工房进行换钱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恐怕会被转交王城，\n',
            '收归国库吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1DD5(): pass

    label('loc_1DD5')

    Jump('loc_2168')

    def _loc_1DD8(): pass

    label('loc_1DD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1EC0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1E3D',
    )

    ChrTalk(
        0x00FE,
        (
            '买家虽然曾经表示要来验货，\n',
            '但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于定期船停运，\n',
            '验货事宜延期的下周。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EBD')

    def _loc_1E3D(): pass

    label('loc_1E3D')

    ChrTalk(
        0x00FE,
        (
            '买家虽然曾经表示要来验货，\n',
            '但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于定期船停运，\n',
            '验货事宜延期的下周。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，请务必为我们的商品\n',
            '做一个评价。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1EBD(): pass

    label('loc_1EBD')

    Jump('loc_2168')

    def _loc_1EC0(): pass

    label('loc_1EC0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1FCF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1F23',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，若是有机会的话\n',
            '真想亲眼看一看龙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '会成为导力器工艺品的\n',
            '良好动机吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FCC')

    def _loc_1F23(): pass

    label('loc_1F23')

    ChrTalk(
        0x00FE,
        (
            '前几天的骚乱……\n',
            '是龙引起的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '传说中从『大崩坏』时代\n',
            '就存在的神兽吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，若是有机会的话\n',
            '真想亲眼看一次啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '会成为导力器工艺品的\n',
            '良好动机吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1FCC(): pass

    label('loc_1FCC')

    Jump('loc_2168')

    def _loc_1FCF(): pass

    label('loc_1FCF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2032',
    )

    ChrTalk(
        0x00FE,
        (
            '外面好像很吵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但不要分心，专心做好自己的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_2168')

    def _loc_2032(): pass

    label('loc_2032')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2168',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_20A7',
    )

    ChrTalk(
        0x00FE,
        (
            '现在的店主科梅尔斯\n',
            '是这间工房的创业者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前的店主被逮捕了。\n',
            '然后他就回来重新主持大局了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2168')

    def _loc_20A7(): pass

    label('loc_20A7')

    ChrTalk(
        0x00FE,
        (
            '现在的店主科梅尔斯\n',
            '是这间工房的创业者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然临时请了别人担当店主，\n',
            '但被王国军逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '于是创业者科梅尔斯才\n',
            '重新担当起店主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '详细的事情虽然不太清楚，\n',
            '真是个复杂的故事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_2168(): pass

    label('loc_2168')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x216C
@scena.Code('func_08_216C')
def func_08_216C():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Return,
        ),
        'loc_2179',
    )

    OP_A2(0x0004)

    def _loc_2179(): pass

    label('loc_2179')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21F5',
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
        100,
        0,
        (
            TXT(0x00, '【◇在前篇遇到过斯丁克】\n'),
            TXT(0x01, '【◇在前篇没遇到过斯丁克】\n'),
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
        (0x00000000, 'loc_21E9'),
        (0x00000001, 'loc_21EF'),
        (-1, 'loc_21F5'),
    )

    def _loc_21E9(): pass

    label('loc_21E9')

    OP_A2(0x0004)

    Jump('loc_21F5')

    def _loc_21EF(): pass

    label('loc_21EF')

    OP_A3(0x0004)

    Jump('loc_21F5')

    def _loc_21F5(): pass

    label('loc_21F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2753',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Return,
        ),
        'loc_22D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2295',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2250',
    )

    ChrTalk(
        0x00FE,
        (
            '琐碎的事\n',
            '就由我来做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……龙的事情就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2292')

    def _loc_2250(): pass

    label('loc_2250')

    ChrTalk(
        0x00FE,
        (
            '前些天在超市\n',
            '协助我们救助的人是你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_2292(): pass

    label('loc_2292')

    Jump('loc_22D0')

    def _loc_2295(): pass

    label('loc_2295')

    ChrTalk(
        0x00FE,
        (
            '琐碎的事\n',
            '就由我来做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……龙的事情就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_22D0(): pass

    label('loc_22D0')

    Jump('loc_2753')

    def _loc_22D3(): pass

    label('loc_22D3')

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_24C4',
    )

    ChrTalk(
        0x0101,
        (
            '#1011F啊、你是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '斯丁克……对吧？\n',
            '柏斯支部的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '你是……\n',
            '那时的准游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，看样子已经升任正游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，是啊。',
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
        'loc_2464',
    )

    ChrTalk(
        0x0103,
        (
            '#027F好久不见了，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x00FE)
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '雪拉扎德吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前些天在超市\n',
            '协助我们救助的人是你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#026F哪里，那是应该做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24C1')

    def _loc_2464(): pass

    label('loc_2464')

    ChrTalk(
        0x00FE,
        (
            '前些天在超市\n',
            '协助我们救助的人是你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯，那是应该的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24C1(): pass

    label('loc_24C1')

    Jump('loc_2712')

    def _loc_24C4(): pass

    label('loc_24C4')

    ChrTalk(
        0x0101,
        (
            '#1015F（啊？这个人……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（仔细看看的话，\n',
            '　竟然也戴着游击士的徽章啊？）',
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
        'loc_25D9',
    )

    ChrTalk(
        0x0103,
        (
            '#027F好久不见了，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x00FE)
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '雪拉扎德吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前些天在超市\n',
            '协助我们救助的人是你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#026F哪里，那是应该做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2712')

    def _loc_25D9(): pass

    label('loc_25D9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_260F',
    )

    ChrTalk(
        0x0108,
        (
            '#070F（嗯，看来他也是游击士。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2644')

    def _loc_260F(): pass

    label('loc_260F')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2644',
    )

    ChrTalk(
        0x0104,
        (
            '#030F（嗯，看来也是个游击士啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2644(): pass

    label('loc_2644')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢格兰老爷子提到的那个\n',
            '新人正游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，嗯。\n',
            '大概是我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前些天在超市\n',
            '协助我们救助的人是你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯，那是应该的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2712(): pass

    label('loc_2712')

    ChrTalk(
        0x00FE,
        (
            '琐碎的事\n',
            '就由我来做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……龙的事情就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A53)
    OP_A2(0x0005)

    def _loc_2753(): pass

    label('loc_2753')

    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0x2757
@scena.Code('func_09_2757')
def func_09_2757():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_281B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27E3',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '紧追不舍的我们也\n',
            '渐渐感到疲劳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从一大早开始\n',
            '就一直是这样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以实在是累死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_2818')

    def _loc_27E3(): pass

    label('loc_27E3')

    ChrTalk(
        0x00FE,
        (
            '嗯，唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们好像也开始\n',
            '渐渐感到疲劳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2818(): pass

    label('loc_2818')

    Jump('loc_28B7')

    def _loc_281B(): pass

    label('loc_281B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_28B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_287A',
    )

    ChrTalk(
        0x00FE,
        (
            '修，修不了……\n',
            '这到底什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道就那么想\n',
            '让我们买新的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_28B7')

    def _loc_287A(): pass

    label('loc_287A')

    ChrTalk(
        0x00FE,
        (
            '喂，店主！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除非把相机修好，\n',
            '否则我们是不会走的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28B7(): pass

    label('loc_28B7')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x28BB
@scena.Code('func_0A_28BB')
def func_0A_28BB():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_292C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2919',
    )

    ChrTalk(
        0x00FE,
        (
            '你们的解释\n',
            '我不管听几次都听不懂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～唉……\n',
            '真是太糟糕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_2929')

    def _loc_2919(): pass

    label('loc_2919')

    ChrTalk(
        0x00FE,
        (
            '唉～唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2929(): pass

    label('loc_2929')

    Jump('loc_29CF')

    def _loc_292C(): pass

    label('loc_292C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_29CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2985',
    )

    ChrTalk(
        0x00FE,
        (
            '辩解我们听够了，\n',
            '快点给我们修好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去钓鱼\n',
            '这是我计划好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_29CF')

    def _loc_2985(): pass

    label('loc_2985')

    ChrTalk(
        0x00FE,
        (
            '辩解我听够了，\n',
            '快点给我修好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们跟我家那老太婆\n',
            '串通一气了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29CF(): pass

    label('loc_29CF')

    TalkEnd(0x000D)

    Return()

# id: 0x000B offset: 0x29D3
@scena.Code('func_0B_29D3')
def func_0B_29D3():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A40',
    )

    ChrTalk(
        0x00FE,
        (
            '柜台那两个人……\n',
            '真是剑拔弩张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里的店主\n',
            '也真可怜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可真是如坐针毡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_2A8A')

    def _loc_2A40(): pass

    label('loc_2A40')

    ChrTalk(
        0x00FE,
        (
            '其实我也是\n',
            '来请求修理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是还不至于\n',
            '会像那个人那样不顾一切。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A8A(): pass

    label('loc_2A8A')

    TalkEnd(0x000E)

    Return()

# id: 0x000C offset: 0x2A8E
@scena.Code('func_0C_2A8E')
def func_0C_2A8E():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A9B',
    )

    Return()

    def _loc_2A9B(): pass

    label('loc_2A9B')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2AAD',
    )

    Return()

    def _loc_2AAD(): pass

    label('loc_2AAD')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x0009)"),
            Expr.Return,
        ),
        'loc_2AE8',
    )

    Call(0, 0x000D)

    Jump('loc_2BAB')

    def _loc_2AE8(): pass

    label('loc_2AE8')

    If(
        (
            (Expr.Eval, "OP_CD(0x0008)"),
            Expr.Return,
        ),
        'loc_2AF7',
    )

    Call(0, 0x000E)

    Jump('loc_2BAB')

    def _loc_2AF7(): pass

    label('loc_2AF7')

    If(
        (
            (Expr.Eval, "OP_CD(0x03E8)"),
            Expr.Return,
        ),
        'loc_2B06',
    )

    Call(0, 0x000D)

    Jump('loc_2BAB')

    def _loc_2B06(): pass

    label('loc_2B06')

    If(
        (
            (Expr.Eval, "OP_CD(0x03E9)"),
            Expr.Return,
        ),
        'loc_2B15',
    )

    Call(0, 0x000E)

    Jump('loc_2BAB')

    def _loc_2B15(): pass

    label('loc_2B15')

    If(
        (
            (Expr.Eval, "OP_CD(0x00FF)"),
            Expr.Return,
        ),
        'loc_2B6D',
    )

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '试着出示了照片，\n',
            '但似乎没有见过的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_2BAB')

    def _loc_2B6D(): pass

    label('loc_2B6D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近没有人可以确认照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_2BAB(): pass

    label('loc_2BAB')

    OP_0D()
    ClearMapFlags(0x00000080)

    Return()

# id: 0x000D offset: 0x2BB2
@scena.Code('func_0D_2BB2')
def func_0D_2BB2():
    TalkBegin(0x0009)

    ChrTalk(
        0x0009,
        (
            '#3780490548V真可怜，\n',
            '10年前走失的孩子吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3780490549V我们的客人里\n',
            '没有像这个孩子的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3780490550V很遗憾，\n',
            '去别的地方看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x000E offset: 0x2C4C
@scena.Code('func_0E_2C4C')
def func_0E_2C4C():
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#3770490551V嗯……不记得见过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3770490552V女性客人很少，\n',
            '假如来过的话应该会有印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3770490553V就算是１０年前的照片，\n',
            '气质上还是有所相似的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
