import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4210   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '索蕾拉'),
    TXT(0x02, '亲卫队队员'),
    TXT(0x03, '亲卫队队员'),
    TXT(0x04, '希尔丹夫人'),
    TXT(0x05, '杜南公爵'),
    TXT(0x06, '科洛蒂娅公主'),
    TXT(0x07, '艾莉茜雅女王'),
    TXT(0x08, '管家菲利普'),
    TXT(0x09, '幻惑之铃露茜奥拉'),
    TXT(0x0A, '瘦狼瓦鲁特'),
    TXT(0x0B, '怪盗布卢布兰'),
    TXT(0x0C, '歼灭天使玲'),
    TXT(0x0D, '亲卫队队员'),
    TXT(0x0E, '亲卫队队员'),
    TXT(0x0F, '亲卫队队员'),
    TXT(0x10, '亲卫队队员'),
    TXT(0x11, '亲卫队队员'),
    TXT(0x12, '亲卫队队员'),
    TXT(0x13, '亲卫队队员'),
    TXT(0x14, '亲卫队队员'),
    TXT(0x15, '亲卫队队员'),
    TXT(0x16, '亲卫队队员'),
    TXT(0x17, '亲卫队队员'),
    TXT(0x18, '亲卫队队员'),
    TXT(0x19, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4210.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x38DB
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
        ('ED6_DT26/CH20447._CH', 'ED6_DT26/CH20447P._CP'),
        ('ED6_DT26/CH20448._CH', 'ED6_DT26/CH20448P._CP'),
        ('ED6_DT26/CH20449._CH', 'ED6_DT26/CH20449P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT26/CH20421._CH', 'ED6_DT26/CH20421P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -170,
            z                   = 1000,
            y                   = 4390,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 5000,
            z                   = 0,
            y                   = -5000,
            direction           = 182,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -5000,
            z                   = 0,
            y                   = -5000,
            direction           = 182,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 20,
            z                   = 9000,
            y                   = 29200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
    )

# id: 0x10003 offset: 0x3E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x3E2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -1880,
            y           = 8000,
            z           = 29100,
            range       = 1580,
            dword_10    = 0x00002AF8,
            dword_14    = 0x0000760C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000014,
        ),
    )

# id: 0x10005 offset: 0x402
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x402
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_41B',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)

    Jump('loc_427')

    def _loc_41B(): pass

    label('loc_41B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_427',
    )

    ClearChrFlags(0x000B, 0x0080)

    def _loc_427(): pass

    label('loc_427')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 5, 0x203D)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_43B',
    )

    Call(0, 0x000C)

    def _loc_43B(): pass

    label('loc_43B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_44C',
    )

    OP_A3(0x10F0)
    Event(0, 0x0008)

    Jump('loc_499')

    def _loc_44C(): pass

    label('loc_44C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_45D',
    )

    OP_A3(0x10F1)
    Event(0, 0x000E)

    Jump('loc_499')

    def _loc_45D(): pass

    label('loc_45D')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_469'),
        (-1, 'loc_499'),
    )

    def _loc_469(): pass

    label('loc_469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 5, 0x203D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 6, 0x203E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_481',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000D)

    Jump('loc_496')

    def _loc_481(): pass

    label('loc_481')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 3, 0x1623)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 4, 0x1624)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_496',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0007)

    def _loc_496(): pass

    label('loc_496')

    Jump('loc_499')

    def _loc_499(): pass

    label('loc_499')

    Return()

# id: 0x0001 offset: 0x49A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B6',
    )

    OP_B1('t4210_y')

    Jump('loc_4BF')

    def _loc_4B6(): pass

    label('loc_4B6')

    OP_B1('t4210_n')

    def _loc_4BF(): pass

    label('loc_4BF')

    OP_71(0x0000, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_4F1',
    )

    OP_22(0x0087, 0x01, 0x1E)
    OP_22(0x00AE, 0x01, 0x1E)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x02000000)
    OP_77(0xFF, 0xBF, 0xB7, 0x00, 0x00000000)
    OP_72(0x0006, 0x0004)

    def _loc_4F1(): pass

    label('loc_4F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 6, 0x203E)),
            Expr.Return,
        ),
        'loc_51B',
    )

    OP_1B(0x01, 0x00, 0x0011)
    OP_1B(0x02, 0x00, 0x0012)
    OP_1B(0x08, 0x00, 0x0012)
    OP_1B(0x03, 0x00, 0x0013)
    OP_1B(0x04, 0x00, 0x0013)
    OP_1B(0x05, 0x00, 0x0013)
    OP_1B(0x06, 0x00, 0x0013)

    def _loc_51B(): pass

    label('loc_51B')

    Return()

# id: 0x0002 offset: 0x51C
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_53F',
    )

    OP_8D(0x00FE, -1790, 6330, 1580, 2190, 2000)

    Jump('ReInit')

    def _loc_53F(): pass

    label('loc_53F')

    Return()

# id: 0x0003 offset: 0x540
@scena.Code('func_03_540')
def func_03_540():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_57B',
    )

    ChrTalk(
        0x00FE,
        (
            '那位公爵大人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还真不明事理呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BD')

    def _loc_57B(): pass

    label('loc_57B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_614',
    )

    ChrTalk(
        0x00FE,
        (
            '听说情报部的凯诺娜小姐\n',
            '在昨天的事件中被捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他说头头都一网打尽了，\n',
            '一副很高兴的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，特务部队的队长\n',
            '好像还没被捉住？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BD')

    def _loc_614(): pass

    label('loc_614')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 1, 0x1629)),
            Expr.Return,
        ),
        'loc_634',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，好忙好忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BD')

    def _loc_634(): pass

    label('loc_634')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_6BD',
    )

    ChrTalk(
        0x00FE,
        (
            '咦，你问女佣室？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00FE, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '从这里正面的会客室一直走，\n',
            '能看到一个很大的入口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00FE, 45, 400)

    ChrTalk(
        0x00FE,
        (
            '入口右侧的门进去\n',
            '就是女佣室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6BD(): pass

    label('loc_6BD')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x6C1
@scena.Code('func_04_6C1')
def func_04_6C1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_73B',
    )

    ChrTalk(
        0x00FE,
        (
            '尤莉亚上尉\n',
            '乘上了『埃尔赛尤』，\n',
            '所以不在城堡内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在上尉不在的这段时间，\n',
            '我们一定会好好保卫这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AF')

    def _loc_73B(): pass

    label('loc_73B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_78E',
    )

    ChrTalk(
        0x00FE,
        (
            '好痛，伤口还没好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过能阻止那辆坦克\n',
            '进入市区真是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AF')

    def _loc_78E(): pass

    label('loc_78E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_7AF',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到格兰赛尔城！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7AF(): pass

    label('loc_7AF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x7B3
@scena.Code('func_05_7B3')
def func_05_7B3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_81C',
    )

    ChrTalk(
        0x00FE,
        (
            '前几天科洛蒂娅殿下带着\n',
            '一副奇怪的表情回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她最近好像一直在和\n',
            '女王陛下说话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_889')

    def _loc_81C(): pass

    label('loc_81C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_851',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部还真是开发了个\n',
            '了不起的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_889')

    def _loc_851(): pass

    label('loc_851')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_889',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎回来，亲卫队的尤莉亚上尉\n',
            '现在不在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_889(): pass

    label('loc_889')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x88D
@scena.Code('func_06_88D')
def func_06_88D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_BCC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041B, 4, 0x20DC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B2E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0650371094V#712F艾丝蒂尔小姐，还有约修亚先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371095V#1040F好久不见了，希尔丹夫人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0650371096V#711F嗯，你能回来真好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371097V#1011F希尔丹夫人，科洛丝\n',
            '在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0650371098V#710F……科洛蒂娅殿下\n',
            '在前面的谒见室里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650371099V不过她现在正和女王陛下\n',
            '进行着重要的谈话，\n',
            '能不能请你们先不要进去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371100V#1004F啊，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0650371101V#710F嗯，现在还不知道\n',
            '她们何时会结束谈话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650371102V#713F你们难得来一次，\n',
            '真不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371103V#1006F不，没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010371104V我们只是因为到了王都\n',
            '顺路过来看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010371105V#1001F很抱歉，打扰了，\n',
            '那我们就先走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371106V#1040F再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20DC)

    Jump('loc_BCC')

    def _loc_B2E(): pass

    label('loc_B2E')

    ChrTalk(
        0x00FE,
        (
            '#0650371107V#710F科洛蒂娅殿下在前面的\n',
            '谒见室里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650371108V不过她现在正和女王陛下\n',
            '进行着重要的谈话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650371109V实在抱歉，\n',
            '能不能请你们先不要进去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BCC(): pass

    label('loc_BCC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xBD0
@scena.Code('func_07_BD0')
def func_07_BD0():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_C8(0x0200, 0x0046, 'C_PLAC00._CH', 0x00, 0x07D0)
    ShowPlaceName('格兰赛尔城')
    OP_6D(350, 500, -3260, 0)
    OP_67(0, 7380, -10000, 0)
    OP_6B(4350, 0)
    OP_6C(45000, 0)
    OP_6E(513, 0)
    SetChrPos(0x0101, 500, 0, -23600, 360)
    SetChrPos(0x0105, -500, 0, -23650, 360)
    SetChrPos(0x0104, -610, 0, -24600, 360)
    SetChrPos(0x0108, 650, 0, -24680, 360)
    Sleep(500)

    FadeIn(2000, 0)

    @scena.Lambda('lambda_0C92')
    def lambda_0C92():
        OP_8E(0x00FE, 600, 0, -18300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C92)

    Sleep(300)

    @scena.Lambda('lambda_0CB2')
    def lambda_0CB2():
        OP_8E(0x00FE, -600, 0, -18300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0CB2)

    @scena.Lambda('lambda_0CCD')
    def lambda_0CCD():
        OP_8E(0x00FE, 600, 0, -19600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0CCD)

    Sleep(300)

    @scena.Lambda('lambda_0CED')
    def lambda_0CED():
        OP_8E(0x00FE, -600, 0, -19600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0CED)

    WaitForThreadExit(0x0108, 0x0001)
    Fade(1000)
    OP_6D(500, 0, -18600, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    ChrTurnDirection(0x0101, 0x0104, 400)

    @scena.Lambda('lambda_0D57')
    def lambda_0D57():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0D57)

    Sleep(50)

    @scena.Lambda('lambda_0D6A')
    def lambda_0D6A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0D6A)

    Sleep(50)

    @scena.Lambda('lambda_0D7D')
    def lambda_0D7D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0D7D)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010250922V#1006F好了……\n',
            '既然要在城里进行调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250923V那就先去和女王陛下\n',
            '打个招呼，然后谈一谈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250924V#1015F那个，我记得尤莉亚上尉\n',
            '应该不在吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250925V#542F嗯，她参加了埃尔赛尤的试飞，\n',
            '现在去雷斯顿要塞出差了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250926V#073F那可真遗憾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250927V如果那位大姐在的话\n',
            '一定能帮上忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250928V#030F那还有没有其他\n',
            '可以谈话的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250929V#040F我觉得也应该找\n',
            '希尔丹夫人聊聊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250930V如果玲的父母\n',
            '去过格兰赛尔城堡的话\n',
            '她一定会知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250931V#1006F确实，城堡里的事\n',
            '没有希尔丹夫人不知道的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250932V那么我们赶紧去找女王陛下\n',
            '和希尔丹夫人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250933V#040F这种时间的话，我想祖母大人\n',
            '应该在女王宫里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250934V#047F希尔丹夫人嘛……让我想想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250935V#542F到那边的女佣室问问的话\n',
            '就能知道她在不在了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250936V#1001F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250937V#1011F那么我们就去女佣室和\n',
            '女王宫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1624)
    OP_28(0x008B, 0x01, 0x0200)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x1107
@scena.Code('func_08_1107')
def func_08_1107():
    EventBegin(0x00)
    OP_D2(0x000600E8, 0x000600ED, 0x07)
    OP_D2(0x002701C8, 0x002701CD, 0x08)
    OP_D2(0x002701C6, 0x002701CB, 0x09)
    OP_D2(0x002701C9, 0x002701CE, 0x0A)
    OP_D2(0x00260003, 0x00260008, 0x0B)
    OP_D2(0x0007035B, 0x00070360, 0x0C)
    OP_D2(0x0007015A, 0x0007015E, 0x0D)
    OP_D2(0x0006011B, 0x00060120, 0x0E)
    OP_D2(0x00070141, 0x00070145, 0x0F)
    OP_D2(0x0007035C, 0x00070361, 0x10)
    OP_D2(0x002601BB, 0x002601C0, 0x11)
    OP_D2(0x002600A0, 0x002600A5, 0x12)
    OP_4A(0x000B, 255)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrPos(0x0014, -5310, 0, -18490, 135)
    SetChrPos(0x0015, -4080, 0, -17010, 180)
    SetChrPos(0x0016, -5390, 0, -16770, 135)
    SetChrPos(0x0017, -3760, 0, -15580, 180)
    SetChrPos(0x0018, -2220, 0, -15380, 180)
    SetChrPos(0x0019, -850, 0, -14430, 180)
    SetChrPos(0x001A, 1210, 0, -14490, 180)
    SetChrPos(0x001B, 2410, 0, -15390, 180)
    SetChrPos(0x001C, 3840, 0, -15090, 225)
    SetChrPos(0x001D, 4030, 0, -16540, 225)
    SetChrPos(0x001E, 5190, 0, -16930, 225)
    SetChrPos(0x001F, 5180, 0, -18310, 225)
    SetChrSubChip(0x0014, 1)
    SetChrSubChip(0x0015, 1)
    SetChrSubChip(0x0016, 1)
    SetChrSubChip(0x0017, 1)
    SetChrSubChip(0x0018, 1)
    SetChrSubChip(0x0019, 1)
    SetChrSubChip(0x001A, 1)
    SetChrSubChip(0x001B, 1)
    SetChrSubChip(0x001C, 1)
    SetChrSubChip(0x001D, 1)
    SetChrSubChip(0x001E, 1)
    SetChrSubChip(0x001F, 1)
    SetChrChipByIndex(0x0014, 7)
    SetChrChipByIndex(0x0015, 7)
    SetChrChipByIndex(0x0016, 7)
    SetChrChipByIndex(0x0017, 7)
    SetChrChipByIndex(0x0018, 7)
    SetChrChipByIndex(0x0019, 7)
    SetChrChipByIndex(0x001A, 7)
    SetChrChipByIndex(0x001B, 7)
    SetChrChipByIndex(0x001C, 7)
    SetChrChipByIndex(0x001D, 7)
    SetChrChipByIndex(0x001E, 7)
    SetChrChipByIndex(0x001F, 7)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x000C, -590, 9000, 10940, 180)
    SetChrPos(0x000F, 810, 9000, 10940, 180)
    SetChrPos(0x000D, -790, 9000, 12400, 180)
    SetChrPos(0x000E, 350, 9000, 12440, 180)
    SetChrPos(0x000B, 1460, 9000, 12700, 180)
    SetChrChipByIndex(0x000C, 13)
    SetChrChipByIndex(0x000F, 16)
    SetChrChipByIndex(0x000B, 12)
    SetChrChipByIndex(0x000E, 15)
    SetChrChipByIndex(0x000D, 14)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    OP_6D(660, 0, -17440, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    OP_71(0x0006, 0x0004)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_23(0x0087)
    OP_23(0x00AE)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_1400')
    def lambda_1400():
        OP_6D(540, 9000, 12460, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1400)

    @scena.Lambda('lambda_1418')
    def lambda_1418():
        OP_67(0, 7060, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1418)

    @scena.Lambda('lambda_1430')
    def lambda_1430():
        OP_6B(2670, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1430)

    @scena.Lambda('lambda_1440')
    def lambda_1440():
        OP_6C(31000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1440)

    OP_6E(280, 5000)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0650380224V#712F#5P难道城门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0640380225V#226F#5P可恶，守不住了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 0, 600)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0640380226V#222F#6P科洛蒂娅！　希尔丹夫人！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640380227V你们马、马上陪同陛下\n',
            '前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_151F')
    def lambda_151F():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_151F)

    Sleep(50)

    @scena.Lambda('lambda_1532')
    def lambda_1532():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1532)

    Sleep(50)

    @scena.Lambda('lambda_1545')
    def lambda_1545():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1545)

    Sleep(50)

    @scena.Lambda('lambda_1558')
    def lambda_1558():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1558)

    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0060380228V#409F#5P叔、叔叔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0630380229V#093F#5P杜南，你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0640380230V#226F#6P我、我也是\n',
            '利贝尔王室的一员！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640380231V像这种公然侵犯王族权威之辈，\n',
            '我又怎么可以视若不见！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640380232V现在尤莉亚不在，\n',
            '我来负责这里的指挥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060380233V#403F#5P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0640380234V#224F#6P哎呀！真讨厌！别磨磨蹭蹭的了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640380235V那些家伙的目的就是将\n',
            '陛下和你劫持！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640380236V他们要劫持利贝尔的女王和公主啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060380237V#402F#5P！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0640380238V#224F#6P你现在最重要的责任\n',
            '就是保护好陛下和自己！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640380239V不要忘记自己的使命，小丫头！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060380240V#406F#5P叔叔……谨遵吩咐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 90, 400)

    @scena.Lambda('lambda_17DD')
    def lambda_17DD():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_17DD)

    @scena.Lambda('lambda_17EB')
    def lambda_17EB():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_17EB)

    Sleep(300)

    ChrTalk(
        0x000D,
        (
            '#0060380241V#402F#6P祖母大人、希尔丹夫人！\n',
            '我们赶快去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0630380242V#094F#5P嗯……好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380243V#092F杜南……\n',
            '请你一定要保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0640380244V#221F#6P哈哈！我会让那些冒犯王族天威\n',
            '的亡命之徒尝到苦头的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0650380245V#713F#5P……祝你们旗开得胜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650380246V#714F菲利普也要\n',
            '多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x000B, 400)
    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#0660380247V#720F#6P多谢关心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000E, 45, 600)

    @scena.Lambda('lambda_196D')
    def lambda_196D():
        OP_6D(2750, 9000, 17440, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_196D)

    CreateThread(0x000E, 0x00, 0x00, 0x0009)
    Sleep(200)

    OP_8C(0x000D, 45, 600)
    CreateThread(0x000D, 0x00, 0x00, 0x000A)
    Sleep(300)

    OP_8C(0x000B, 45, 600)
    CreateThread(0x000B, 0x00, 0x00, 0x000B)

    @scena.Lambda('lambda_19B2')
    def lambda_19B2():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_19B2')

    DispatchAsync2(0x000F, 0x0001, lambda_19B2)

    @scena.Lambda('lambda_19C3')
    def lambda_19C3():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_19C3')

    DispatchAsync2(0x000C, 0x0001, lambda_19C3)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1500)

    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000C, 0x01)

    @scena.Lambda('lambda_19E6')
    def lambda_19E6():
        OP_6D(430, 9000, 11240, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_19E6)

    OP_6B(2550, 1500)
    ChrTurnDirection(0x000F, 0x000C, 400)
    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#0660380248V#720F#2P……阁下，您真是太了不起了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660380249V我菲利普，此时此刻第一次\n',
            '发自内心地感受到…能够侍奉阁下\n',
            '真是我的幸运和荣耀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000F, 400)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0640380250V#222F#6P咳咳、哼，别那么正经。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_22(0x0088, 0x00, 0x50)
    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x000001F4)
    OP_72(0x0006, 0x0004)
    Sleep(500)

    OP_77(0xFF, 0xBF, 0xB7, 0x00, 0x00001388)
    OP_22(0x0087, 0x01, 0x0A)
    OP_22(0x00AE, 0x01, 0x0A)
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_22(0x013C, 0x00, 0x50)
    Sleep(1000)

    OP_22(0x00F6, 0x00, 0x50)
    OP_24(0x0087, 0x14)
    OP_24(0x00AE, 0x14)

    @scena.Lambda('lambda_1B61')
    def lambda_1B61():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1B61)

    Sleep(50)

    @scena.Lambda('lambda_1B74')
    def lambda_1B74():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B74)

    Sleep(2000)

    SetChrChipByIndex(0x0010, 8)
    SetChrChipByIndex(0x0011, 9)
    SetChrChipByIndex(0x0012, 10)
    SetChrChipByIndex(0x0013, 11)
    SetChrPos(0x0012, -100, 0, -32200, 0)
    SetChrPos(0x0011, -160, 0, -34300, 0)
    SetChrPos(0x0013, -1250, 0, -32860, 0)
    SetChrPos(0x0010, 1220, 0, -33660, 0)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    Fade(1000)
    OP_6D(410, 0, -21270, 0)
    OP_67(0, 5250, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(148000, 0)
    OP_6E(331, 0)
    OP_24(0x0087, 0x1E)
    OP_24(0x00AE, 0x1E)

    @scena.Lambda('lambda_1C3D')
    def lambda_1C3D():
        OP_8E(0x00FE, -100, 0, -21260, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1C3D)

    Sleep(120)

    @scena.Lambda('lambda_1C5D')
    def lambda_1C5D():
        OP_8E(0x00FE, -1250, 0, -22860, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_1C5D)

    Sleep(180)

    @scena.Lambda('lambda_1C7D')
    def lambda_1C7D():
        OP_8E(0x00FE, 1220, 0, -22460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1C7D)

    Sleep(100)

    @scena.Lambda('lambda_1C9D')
    def lambda_1C9D():
        OP_8E(0x00FE, -160, 0, -23620, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1C9D)

    WaitForThreadExit(0x0011, 0x0001)
    SetChrChipByIndex(0x0011, 18)
    SetChrSubChip(0x0011, 0)
    Fade(500)
    OP_6D(130, 9000, 11060, 0)
    OP_67(0, 7350, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(31000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0640380251V#226F#5P他、他们来了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0660380252V#720F#5P呼，好强烈的杀气……\n',
            '简直就是些鬼气逼人的魔人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660380253V阁下…如果我被打倒的话，\n',
            '请不要犹豫，马上逃走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1DC5')
    def lambda_1DC5():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_1DC5')

    DispatchAsync2(0x000C, 0x0001, lambda_1DC5)

    ChrTalk(
        0x000C,
        (
            '#0640380254V#223F#6P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8F(0x000F, 1040, 9000, 13590, 2000, 0x00)
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrFlags(0x000F, 0x0002)
    SetChrFlags(0x000F, 0x0040)
    SetChrFlags(0x000F, 0x0020)
    SetChrSubChip(0x000F, 0)
    SetChrChipByIndex(0x000F, 17)
    OP_0D()
    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1E42')
    def lambda_1E42():
        OP_99(0x00FE, 0x01, 0x08, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1E42)

    OP_8F(0x000F, 1040, 9000, 11400, 7000, 0x00)

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    SetChrSubChip(0x000F, 10)

    @scena.Lambda('lambda_1E7B')
    def lambda_1E7B():
        OP_6D(980, 1000, 3340, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1E7B)

    @scena.Lambda('lambda_1E93')
    def lambda_1E93():
        OP_67(0, 5250, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E93)

    @scena.Lambda('lambda_1EAB')
    def lambda_1EAB():
        OP_6B(2560, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EAB)

    @scena.Lambda('lambda_1EBB')
    def lambda_1EBB():
        OP_6C(33000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1EBB)

    @scena.Lambda('lambda_1ECB')
    def lambda_1ECB():
        OP_6E(331, 1000)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_1ECB)

    OP_22(0x023B, 0x00, 0x64)
    OP_96(0x000F, 0x000000D2, 0x000003E8, 0x00000B04, 0x000003E8, 0x00000FA0)
    OP_22(0x00A4, 0x00, 0x64)
    OP_99(0x000F, 0x0B, 0x0F, 0x000005DC)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    @scena.Lambda('lambda_1F13')
    def lambda_1F13():
        OP_6D(1040, 0, -17600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1F13)

    @scena.Lambda('lambda_1F2B')
    def lambda_1F2B():
        OP_67(0, 4560, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F2B)

    @scena.Lambda('lambda_1F43')
    def lambda_1F43():
        OP_6B(2590, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1F43)

    @scena.Lambda('lambda_1F53')
    def lambda_1F53():
        OP_6E(390, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1F53)

    @scena.Lambda('lambda_1F63')
    def lambda_1F63():
        OP_99(0x00FE, 0x01, 0x08, 0x000009C4)
        Yield()

        Jump('lambda_1F63')

    DispatchAsync2(0x000F, 0x0002, lambda_1F63)

    OP_8F(0x000F, 190, 0, -15890, 8000, 0x00)
    TerminateThread(0x000F, 0x02)
    SetChrSubChip(0x000F, 0)
    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0018, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0019, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x001D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x001E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x001A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x001B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0016, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x001C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x001F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrFlags(0x001A, 0x0020)
    SetChrFlags(0x001B, 0x0020)

    @scena.Lambda('lambda_20C5')
    def lambda_20C5():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_20C5)

    Sleep(100)

    @scena.Lambda('lambda_20D8')
    def lambda_20D8():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_20D8)

    WaitForThreadExit(0x001A, 0x0001)

    ChrTalk(
        0x001A,
        (
            '#4290380255V#5P菲、菲利普先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0220380256V#264F#6P咦？这不是细眼睛的爷爷吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0200380257V#254F#4P老家伙，你是干什么的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0660380258V#720F#5P杜南公爵阁下的管家，\n',
            '原·王室亲卫队大队长，\n',
            '菲利普·雷纳尔参见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x01F5, 0x00, 0x64)
    OP_99(0x000F, 0x10, 0x17, 0x000004B0)
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0660380259V#721F当年的本领……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660380260V如今不知还剩下几成……\n',
            '不如就在你们身上证实一下吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0200380261V#252F#4P喔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0170380262V#231F#6P哈哈……这可有趣了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0210380263V#241F#4P呵呵……\n',
            '看来你能给我们带来一点乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x203C)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4200._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x22EF
@scena.Code('func_09_22EF')
def func_09_22EF():
    OP_8E(0x00FE, 5180, 9000, 25190, 4000, 0x00)
    OP_8E(0x00FE, 13370, 9000, 27080, 4000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x000A offset: 0x231D
@scena.Code('func_0A_231D')
def func_0A_231D():
    OP_8E(0x00FE, 5180, 9000, 25190, 4000, 0x00)
    OP_8E(0x00FE, 13370, 9000, 27080, 4000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x000B offset: 0x234B
@scena.Code('func_0B_234B')
def func_0B_234B():
    OP_8E(0x00FE, 4960, 9000, 23750, 4000, 0x00)
    OP_8E(0x00FE, 13370, 9000, 27080, 4000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x000C offset: 0x2379
@scena.Code('func_0C_2379')
def func_0C_2379():
    SetChrPos(0x0014, 4280, 0, -19910, 45)
    SetChrPos(0x0015, 5060, 0, -18690, 315)
    SetChrPos(0x0016, 3940, 0, -17900, 225)
    SetChrPos(0x0017, 3150, 0, -16390, 315)
    SetChrPos(0x0018, 5220, 0, -14920, 180)
    SetChrPos(0x0019, 3700, 0, -13350, 135)
    SetChrPos(0x001A, -3770, 0, -14210, 45)
    SetChrPos(0x001B, -5950, 0, -16070, 315)
    SetChrPos(0x001C, -4320, 0, -21290, 225)
    SetChrPos(0x001D, -5730, 0, -18970, 180)
    SetChrPos(0x001E, -3430, 0, -18480, 90)
    SetChrPos(0x001F, -4480, 0, -17140, 45)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0014, 0x0001)
    ClearChrFlags(0x0015, 0x0001)
    ClearChrFlags(0x0016, 0x0001)
    ClearChrFlags(0x0017, 0x0001)
    ClearChrFlags(0x0018, 0x0001)
    ClearChrFlags(0x0019, 0x0001)
    ClearChrFlags(0x001A, 0x0001)
    ClearChrFlags(0x001B, 0x0001)
    ClearChrFlags(0x001C, 0x0001)
    ClearChrFlags(0x001D, 0x0001)
    ClearChrFlags(0x001E, 0x0001)
    ClearChrFlags(0x001F, 0x0001)
    SetChrFlags(0x0014, 0x0020)
    SetChrFlags(0x0015, 0x0020)
    SetChrFlags(0x0016, 0x0020)
    SetChrFlags(0x0017, 0x0020)
    SetChrFlags(0x0018, 0x0020)
    SetChrFlags(0x0019, 0x0020)
    SetChrFlags(0x001A, 0x0020)
    SetChrFlags(0x001B, 0x0020)
    SetChrFlags(0x001C, 0x0020)
    SetChrFlags(0x001D, 0x0020)
    SetChrFlags(0x001E, 0x0020)
    SetChrFlags(0x001F, 0x0020)
    SetChrPos(0x000F, -1100, 0, -7300, 0)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000F, 0x0002)
    ClearChrFlags(0x000F, 0x0001)
    SetChrChipByIndex(0x000F, 6)
    SetChrSubChip(0x000F, 5)
    SetChrPos(0x000C, 940, 0, -6690, 180)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000C, 0x0001)
    SetChrFlags(0x000C, 0x0020)

    Return()

# id: 0x000D offset: 0x2544
@scena.Code('func_0D_2544')
def func_0D_2544():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2565',
    )

    Call(0, 0x000F)
    Call(0, 0x0010)

    def _loc_2565(): pass

    label('loc_2565')

    SetChrPos(0x0101, -380, 0, -33500, 0)
    SetChrPos(0x0102, 480, 0, -33500, 0)
    SetChrPos(0x00F8, -1190, 0, -34000, 0)
    SetChrPos(0x00F9, 1290, 0, -34000, 0)
    SetChrPos(0x000F, -750, 0, -6900, 0)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000F, 0x0002)
    SetChrChipByIndex(0x000F, 1)
    SetChrSubChip(0x000F, 7)
    SetChrFlags(0x000F, 0x0001)
    OP_6D(400, 0, -28320, 0)
    OP_67(0, 7130, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_72(0x0006, 0x0004)

    @scena.Lambda('lambda_261B')
    def lambda_261B():
        OP_8E(0x00FE, -380, 0, -21700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_261B)

    Sleep(80)

    @scena.Lambda('lambda_263B')
    def lambda_263B():
        OP_8E(0x00FE, 880, 0, -21810, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_263B)

    Sleep(80)

    @scena.Lambda('lambda_265B')
    def lambda_265B():
        OP_8E(0x00FE, -910, 0, -23200, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_265B)

    Sleep(80)

    @scena.Lambda('lambda_267B')
    def lambda_267B():
        OP_8E(0x00FE, 900, 0, -23220, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_267B)

    FadeIn(1000, 0)

    @scena.Lambda('lambda_269F')
    def lambda_269F():
        OP_6D(810, 0, -20120, 2200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_269F)

    @scena.Lambda('lambda_26B7')
    def lambda_26B7():
        OP_6E(293, 2200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_26B7)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_272A',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2768')

    def _loc_272A(): pass

    label('loc_272A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2751',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2768')

    def _loc_2751(): pass

    label('loc_2751')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2768(): pass

    label('loc_2768')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2794',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_27D2')

    def _loc_2794(): pass

    label('loc_2794')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27BB',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_27D2')

    def _loc_27BB(): pass

    label('loc_27BB')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_27D2(): pass

    label('loc_27D2')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380281V#1020F#6P这、这是……',
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
        'loc_283A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380282V#065F大、大家\n',
            '都被打倒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_283A(): pass

    label('loc_283A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_287F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380283V#057F连王国军最强的\n',
            '精锐部队也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2906')

    def _loc_287F(): pass

    label('loc_287F')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28C4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380284V#022F连王国军最强的\n',
            '精锐部队也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2906')

    def _loc_28C4(): pass

    label('loc_28C4')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2906',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380285V#072F连王国军最强的\n',
            '精锐部队也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2906(): pass

    label('loc_2906')

    NpcTalk(
        0x000F,
        '男性的声音',
        (
            '#0660380286V#4P艾、艾丝蒂尔小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2994',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_29D2')

    def _loc_2994(): pass

    label('loc_2994')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29BB',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_29D2')

    def _loc_29BB(): pass

    label('loc_29BB')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_29D2(): pass

    label('loc_29D2')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29F9',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2A37')

    def _loc_29F9(): pass

    label('loc_29F9')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A20',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2A37')

    def _loc_2A20(): pass

    label('loc_2A20')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2A37(): pass

    label('loc_2A37')

    Sleep(1000)

    @scena.Lambda('lambda_2A42')
    def lambda_2A42():
        OP_6B(2830, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A42)

    OP_6D(280, 0, -6850, 2000)
    SetChrFlags(0x0018, 0x0040)
    SetChrFlags(0x0019, 0x0040)
    SetChrFlags(0x001A, 0x0040)
    SetChrFlags(0x001B, 0x0040)

    @scena.Lambda('lambda_2A77')
    def lambda_2A77():
        OP_6D(640, 0, -7360, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A77)

    @scena.Lambda('lambda_2A8F')
    def lambda_2A8F():
        OP_67(0, 6310, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2A8F)

    @scena.Lambda('lambda_2AA7')
    def lambda_2AA7():
        OP_8E(0x00FE, -640, 0, -8640, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AA7)

    Sleep(80)

    @scena.Lambda('lambda_2AC7')
    def lambda_2AC7():
        OP_8E(0x00FE, 500, 0, -8660, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2AC7)

    Sleep(80)

    @scena.Lambda('lambda_2AE7')
    def lambda_2AE7():
        OP_8E(0x00FE, -1050, 0, -10240, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2AE7)

    Sleep(80)

    @scena.Lambda('lambda_2B07')
    def lambda_2B07():
        OP_8E(0x00FE, 400, 0, -10240, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2B07)

    WaitForThreadExit(0x0101, 0x0001)
    OP_8C(0x0101, 0, 400)
    WaitForThreadExit(0x0102, 0x0001)
    OP_8C(0x0102, 0, 400)
    WaitForThreadExit(0x00F8, 0x0001)
    OP_8C(0x00F8, 0, 400)
    WaitForThreadExit(0x00F9, 0x0001)
    OP_8C(0x00F9, 0, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010380287V#1020F#6P菲、菲利普先生！？\n',
            '还有杜南公爵也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380288V#1042F莫非……\n',
            '你们是打算拖住他们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0660380289V#722F#5P真、真惭愧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660380290V看来我还是老了……\n',
            '没能拖久一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660380291V#721F公、公爵阁下怎么样了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C91',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380292V#070F不必担心。\n',
            '看来只是被击晕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D18')

    def _loc_2C91(): pass

    label('loc_2C91')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CD8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380293V#524F他不要紧……\n',
            '看来只是被击晕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D18')

    def _loc_2CD8(): pass

    label('loc_2CD8')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D18',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380294V#051F别担心。\n',
            '看来只是被击晕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D18(): pass

    label('loc_2D18')

    ChrTalk(
        0x000F,
        (
            '#0660380295V#722F#5P那、那我就放心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660380296V陛下她们去了女王宫……\n',
            '请、请你们快点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(250)
    OP_22(0x020C, 0x00, 0x64)
    ClearChrFlags(0x000F, 0x0001)
    SetChrChipByIndex(0x000F, 6)
    SetChrSubChip(0x000F, 5)
    SetChrPos(0x000F, -1100, 0, -7300, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010380297V#1020F#6P菲、菲利普先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380298V#1035F没事的，只是晕过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 270, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020380299V#1042F#2P要赶快……\n',
            '科洛丝她们很危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 500)

    ChrTalk(
        0x0101,
        (
            '#0010380300V#1002F#6P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T4201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x2E93
@scena.Code('func_0E_2E93')
def func_0E_2E93():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    SetChrPos(0x0000, 50, 0, -8940, 0)
    SetChrPos(0x0001, 50, 0, -8940, 0)
    SetChrPos(0x0002, 50, 0, -8940, 0)
    SetChrPos(0x0003, 50, 0, -8940, 0)
    OP_69(0x0000, 0x00000000)
    OP_A2(0x203E)
    Sleep(200)

    FadeIn(1000, 0)
    OP_1B(0x01, 0x00, 0x0011)
    OP_1B(0x02, 0x00, 0x0012)
    OP_1B(0x08, 0x00, 0x0012)
    OP_1B(0x03, 0x00, 0x0013)
    OP_1B(0x04, 0x00, 0x0013)
    OP_1B(0x05, 0x00, 0x0013)
    OP_1B(0x06, 0x00, 0x0013)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x000F offset: 0x2F26
@scena.Code('func_0F_2F26')
def func_0F_2F26():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0x00000000, 'loc_2FA0'),
        (0x00000001, 'loc_2FA6'),
        (-1, 'loc_2FAC'),
    )

    def _loc_2FA0(): pass

    label('loc_2FA0')

    OP_A2(0x1200)

    Jump('loc_2FAC')

    def _loc_2FA6(): pass

    label('loc_2FA6')

    OP_A2(0x1201)

    Jump('loc_2FAC')

    def _loc_2FAC(): pass

    label('loc_2FAC')

    Return()

# id: 0x0010 offset: 0x2FAD
@scena.Code('func_10_2FAD')
def func_10_2FAD():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0007,
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
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

# id: 0x0011 offset: 0x3006
@scena.Code('func_11_3006')
def func_11_3006():
    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_3028'),
        (0x00000001, 'loc_3068'),
        (0x00000002, 'loc_30A6'),
        (0x00000005, 'loc_30DF'),
        (0x00000007, 'loc_3118'),
        (0x00000006, 'loc_3155'),
        (-1, 'loc_3194'),
    )

    def _loc_3028(): pass

    label('loc_3028')

    ChrTalk(
        0x0101,
        (
            '#0010380301V#1002F不，不是这边。\n',
            '……得抓紧前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3194')

    def _loc_3068(): pass

    label('loc_3068')

    ChrTalk(
        0x0102,
        (
            '#0020380302V#1042F不对，不是这边。\n',
            '……赶紧去女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3194')

    def _loc_30A6(): pass

    label('loc_30A6')

    ChrTalk(
        0x0103,
        (
            '#0030380303V#022F这边不对。\n',
            '……赶紧去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3194')

    def _loc_30DF(): pass

    label('loc_30DF')

    ChrTalk(
        0x0106,
        (
            '#0050380304V#057F没时间磨蹭了，\n',
            '赶快去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3194')

    def _loc_3118(): pass

    label('loc_3118')

    ChrTalk(
        0x0108,
        (
            '#0080380305V#072F没空去别处了。\n',
            '……抓紧去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3194')

    def _loc_3155(): pass

    label('loc_3155')

    ChrTalk(
        0x0107,
        (
            '#0070380306V#062F不、不是这边。\n',
            '……得抓紧前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3194')

    def _loc_3194(): pass

    label('loc_3194')

    OP_90(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0012 offset: 0x31B5
@scena.Code('func_12_31B5')
def func_12_31B5():
    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_31D7'),
        (0x00000001, 'loc_3217'),
        (0x00000002, 'loc_3255'),
        (0x00000005, 'loc_328E'),
        (0x00000007, 'loc_32C7'),
        (0x00000006, 'loc_3304'),
        (-1, 'loc_3343'),
    )

    def _loc_31D7(): pass

    label('loc_31D7')

    ChrTalk(
        0x0101,
        (
            '#0010380301V#1002F不，不是这边。\n',
            '……得抓紧前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3343')

    def _loc_3217(): pass

    label('loc_3217')

    ChrTalk(
        0x0102,
        (
            '#0020380302V#1042F不对，不是这边。\n',
            '……赶紧去女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3343')

    def _loc_3255(): pass

    label('loc_3255')

    ChrTalk(
        0x0103,
        (
            '#0030380303V#022F这边不对。\n',
            '……赶紧去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3343')

    def _loc_328E(): pass

    label('loc_328E')

    ChrTalk(
        0x0106,
        (
            '#0050380304V#057F没时间磨蹭了，\n',
            '赶快去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3343')

    def _loc_32C7(): pass

    label('loc_32C7')

    ChrTalk(
        0x0108,
        (
            '#0080380305V#072F没空去别处了。\n',
            '……抓紧去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3343')

    def _loc_3304(): pass

    label('loc_3304')

    ChrTalk(
        0x0107,
        (
            '#0070380306V#062F不、不是这边。\n',
            '……得抓紧前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3343')

    def _loc_3343(): pass

    label('loc_3343')

    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0013 offset: 0x3364
@scena.Code('func_13_3364')
def func_13_3364():
    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_3386'),
        (0x00000001, 'loc_33C6'),
        (0x00000002, 'loc_3404'),
        (0x00000005, 'loc_343D'),
        (0x00000007, 'loc_3476'),
        (0x00000006, 'loc_34B3'),
        (-1, 'loc_34F2'),
    )

    def _loc_3386(): pass

    label('loc_3386')

    ChrTalk(
        0x0101,
        (
            '#0010380301V#1002F不，不是这边。\n',
            '……得抓紧前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34F2')

    def _loc_33C6(): pass

    label('loc_33C6')

    ChrTalk(
        0x0102,
        (
            '#0020380302V#1042F不对，不是这边。\n',
            '……赶紧去女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34F2')

    def _loc_3404(): pass

    label('loc_3404')

    ChrTalk(
        0x0103,
        (
            '#0030380303V#022F这边不对。\n',
            '……赶紧去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34F2')

    def _loc_343D(): pass

    label('loc_343D')

    ChrTalk(
        0x0106,
        (
            '#0050380304V#057F没时间磨蹭了，\n',
            '赶快去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34F2')

    def _loc_3476(): pass

    label('loc_3476')

    ChrTalk(
        0x0108,
        (
            '#0080380305V#072F没空去别处了。\n',
            '……抓紧去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34F2')

    def _loc_34B3(): pass

    label('loc_34B3')

    ChrTalk(
        0x0107,
        (
            '#0070380306V#062F不、不是这边。\n',
            '……得抓紧前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34F2')

    def _loc_34F2(): pass

    label('loc_34F2')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0014 offset: 0x3513
@scena.Code('func_14_3513')
def func_14_3513():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_38B0',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x000B, 0x0000, 400)
    ChrTurnDirection(0x0000, 0x000B, 0)
    ChrTurnDirection(0x0001, 0x000B, 0)
    ChrTurnDirection(0x0002, 0x000B, 0)
    ChrTurnDirection(0x0003, 0x000B, 0)
    OP_4A(0x000B, 255)
    SetChrFlags(0x000B, 0x0040)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041B, 4, 0x20DC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37E4',
    )

    ChrTalk(
        0x000B,
        (
            '#0650371094V#712F艾丝蒂尔小姐，还有约修亚先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371095V#1040F好久不见了，希尔丹夫人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0650371096V#711F嗯，你能回来真好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371097V#1011F希尔丹夫人，科洛丝\n',
            '在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0650371098V#710F……科洛蒂娅殿下\n',
            '在前面的谒见室里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650371099V不过她现在在和女王陛下\n',
            '进行着重要的谈话，\n',
            '能不能请你们先不要进去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371100V#1004F啊，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0650371101V#710F嗯，现在还不知道\n',
            '她们何时会结束谈话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650371102V#713F你们难得来一次，\n',
            '真不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371103V#1006F不，没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010371104V我们只是因为到了王都\n',
            '顺路过来看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010371105V#1001F很抱歉，打扰了，\n',
            '那我们就先走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371106V#1040F再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20DC)

    Jump('loc_3882')

    def _loc_37E4(): pass

    label('loc_37E4')

    ChrTalk(
        0x000B,
        (
            '#0650371107V#710F科洛蒂娅殿下在前面的\n',
            '谒见室里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650371108V不过她现在在和女王陛下\n',
            '进行着重要的谈话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650371109V实在抱歉，\n',
            '能不能请你们先不要进去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3882(): pass

    label('loc_3882')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    OP_8C(0x000B, 180, 400)
    Sleep(50)

    EventEnd(0x04)
    OP_4B(0x000B, 255)
    ClearChrFlags(0x000B, 0x0040)

    Jump('loc_38B0')

    def _loc_38B0(): pass

    label('loc_38B0')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
