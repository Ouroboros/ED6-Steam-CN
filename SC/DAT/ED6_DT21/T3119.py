import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3119_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3119   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '拉赛尔博士'),
    TXT(0x02, '玛多克工房长'),
    TXT(0x03, '特莱斯主任'),
    TXT(0x04, '接待处小姐海泽尔'),
    TXT(0x05, '威尔姆'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3119.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T3119._SN', 'ED6_DT21/T3119_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x63B7
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
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
    ]

# id: 0x10002 offset: 0xD2
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            x                   = -440,
            z                   = 0,
            y                   = 10490,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
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
            x                   = 4650,
            z                   = 1000,
            y                   = 6180,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10003 offset: 0x172
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x172
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -106990,
            y           = 0,
            z           = -550,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000011,
        ),
    )

# id: 0x10005 offset: 0x192
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -540,
            triggerZ            = 0,
            triggerY            = 6300,
            triggerRange        = 800,
            actorX              = -540,
            actorZ              = 900,
            actorY              = 6300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1B6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C0',
    )

    Jump('loc_204')

    def _loc_1C0(): pass

    label('loc_1C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_204',
    )

    SetChrPos(0x0008, -480, 0, 10270, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x000A, 4650, 1000, 6340, 90)
    SetChrPos(0x000C, 2300, 0, 7700, 90)

    def _loc_204(): pass

    label('loc_204')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_21E',
    )

    OP_A3(0x10F0)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x000B)

    Jump('loc_242')

    def _loc_21E(): pass

    label('loc_21E')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_242',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_242',
    )

    Event(0, 0x0006)

    def _loc_242(): pass

    label('loc_242')

    Return()

# id: 0x0001 offset: 0x243
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EC',
    )

    OP_6F(0x0008, 0)
    OP_72(0x0008, 0x0010)
    OP_6F(0x0005, 29)
    OP_72(0x0005, 0x0010)
    OP_6F(0x0006, 29)
    OP_72(0x0006, 0x0010)
    OP_6F(0x0007, 29)
    OP_72(0x0007, 0x0010)
    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_71(0x0011, 0x0004)
    OP_79(0xFF, 0x0002)
    OP_7A(0x1F, 0x0002)
    OP_7B()
    OP_72(0x0013, 0x0004)
    OP_72(0x0014, 0x0004)
    OP_10(0x00, 0x00)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_64(0x00, 0x0001)
    OP_71(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_71(0x0012, 0x0004)
    OP_71(0x0012, 0x0004)

    Jump('loc_373')

    def _loc_2EC(): pass

    label('loc_2EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_30F',
    )

    OP_72(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_71(0x0012, 0x0004)

    Jump('loc_373')

    def _loc_30F(): pass

    label('loc_30F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_332',
    )

    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_72(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0012, 0x0004)

    Jump('loc_373')

    def _loc_332(): pass

    label('loc_332')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_35A',
    )

    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_72(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0012, 0x0004)

    Jump('loc_373')

    def _loc_35A(): pass

    label('loc_35A')

    OP_72(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_71(0x0012, 0x0004)

    def _loc_373(): pass

    label('loc_373')

    Return()

# id: 0x0002 offset: 0x374
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_3A5'),
        (0x00000001, 'loc_3B1'),
        (0x00000002, 'loc_3BD'),
        (0x00000003, 'loc_3C9'),
        (0x00000004, 'loc_3D5'),
        (0x00000005, 'loc_3E1'),
        (0x00000006, 'loc_3ED'),
        (-1, 'loc_3F9'),
    )

    def _loc_3A5(): pass

    label('loc_3A5')

    OP_99(0x00FE, 0x00, 0x07, 0x000005AA)

    Jump('loc_405')

    def _loc_3B1(): pass

    label('loc_3B1')

    OP_99(0x00FE, 0x00, 0x07, 0x0000060E)

    Jump('loc_405')

    def _loc_3BD(): pass

    label('loc_3BD')

    OP_99(0x00FE, 0x00, 0x07, 0x00000640)

    Jump('loc_405')

    def _loc_3C9(): pass

    label('loc_3C9')

    OP_99(0x00FE, 0x00, 0x07, 0x00000578)

    Jump('loc_405')

    def _loc_3D5(): pass

    label('loc_3D5')

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_405')

    def _loc_3E1(): pass

    label('loc_3E1')

    OP_99(0x00FE, 0x00, 0x07, 0x00000546)

    Jump('loc_405')

    def _loc_3ED(): pass

    label('loc_3ED')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_405')

    def _loc_3F9(): pass

    label('loc_3F9')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_405')

    def _loc_405(): pass

    label('loc_405')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_41A',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_405')

    def _loc_41A(): pass

    label('loc_41A')

    Return()

# id: 0x0003 offset: 0x41B
@scena.Code('func_03_41B')
def func_03_41B():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_53A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4EB',
    )

    ChrTalk(
        0x00FE,
        (
            '博士去出差了，\n',
            '我也不知道他在哪里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过他一定在忘我地\n',
            '研究着这种现象吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，我们也不能懈怠，\n',
            '一定要努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不能做得跟博士一样，\n',
            '不过应该还是有很多事可以做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_537')

    def _loc_4EB(): pass

    label('loc_4EB')

    ChrTalk(
        0x00FE,
        (
            '博士也一定在忘我地\n',
            '研究着现象吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也不能懈怠，\n',
            '一定要努力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_537(): pass

    label('loc_537')

    Jump('loc_C29')

    def _loc_53A(): pass

    label('loc_53A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_617',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5C6',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，受不了了……\n',
            '到底是怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和工房长说的一样，\n',
            '机械材料都不动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候\n',
            '拉赛尔博士要是在的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_614')

    def _loc_5C6(): pass

    label('loc_5C6')

    ChrTalk(
        0x00FE,
        (
            '和工房长说的一样，\n',
            '机械材料都不动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，拉赛尔博士\n',
            '要是在的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_614(): pass

    label('loc_614')

    Jump('loc_C29')

    def _loc_617(): pass

    label('loc_617')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 7, 0x142F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_A4D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_984',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_707',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_682',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然能操纵七耀脉，\n',
            '真是了不起的技术啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们连想都不敢想啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_704')

    def _loc_682(): pass

    label('loc_682')

    ChrTalk(
        0x00FE,
        (
            '哟，各位辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '震源的调查\n',
            '很麻烦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话虽如此……\n',
            '竟然能操纵七耀脉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以我们的知识水平\n',
            '是无法想象得到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_704(): pass

    label('loc_704')

    Jump('loc_981')

    def _loc_707(): pass

    label('loc_707')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_75B',
    )

    ChrTalk(
        0x00FE,
        (
            '七耀脉的运动\n',
            '好象还没停止呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但到底是什么\n',
            '引发了这样的现象呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_981')

    def _loc_75B(): pass

    label('loc_75B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_85D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7DE',
    )

    ChrTalk(
        0x00FE,
        (
            '问题是数据的交接啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之得抓紧\n',
            '进行测试……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真不愧是拉赛尔博士啊。\n',
            '一下子就出了这么一个难题啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_85A')

    def _loc_7DE(): pass

    label('loc_7DE')

    ChrTalk(
        0x00FE,
        (
            '从外部接收数据，\n',
            '并且进行即时处理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不是做不到，\n',
            '不过也是非常困难的工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之得抓紧\n',
            '进行测试……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_85A(): pass

    label('loc_85A')

    Jump('loc_981')

    def _loc_85D(): pass

    label('loc_85D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_918',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_8C4',
    )

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士……\n',
            '这次又会怎么样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一半兴趣、一半恐惧……\n',
            '现在就是这种心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_915')

    def _loc_8C4(): pass

    label('loc_8C4')

    ChrTalk(
        0x00FE,
        (
            '说起来，拉赛尔博士\n',
            '好像很忙的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯、嗯～总觉得\n',
            '有不好的预感……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_915(): pass

    label('loc_915')

    Jump('loc_981')

    def _loc_918(): pass

    label('loc_918')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_981',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然刚才有地震……\n',
            '不过好象对『卡佩尔』没有影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们有需要的话随时\n',
            '可以用它进行搜索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_981(): pass

    label('loc_981')

    Jump('loc_A4A')

    def _loc_984(): pass

    label('loc_984')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_9E1',
    )

    ChrTalk(
        0x00FE,
        (
            '托你们的福，『卡佩尔』状态也很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们有需要的话随时\n',
            '可以用它进行搜索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4A')

    def _loc_9E1(): pass

    label('loc_9E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_A4A',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然刚才有地震……\n',
            '不过好象对『卡佩尔』没有影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们有需要的话随时\n',
            '可以用它进行搜索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A4A(): pass

    label('loc_A4A')

    Jump('loc_C29')

    def _loc_A4D(): pass

    label('loc_A4D')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A98',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊。\n',
            '哟～好久不见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AB9')

    def _loc_A98(): pass

    label('loc_A98')

    ChrTalk(
        0x00FE,
        (
            '哟，是你啊？\n',
            '哟～好久不见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AB9(): pass

    label('loc_AB9')

    ChrTalk(
        0x0101,
        (
            '#1001F嘿嘿，好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F『卡佩尔』的状态如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，托你们的福，状态很好。\n',
            '现在看来也没有受到地震的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你们有需要的话随时\n',
            '可以用它进行搜索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样你们是\n',
            '『卡佩尔』的恩人啊。',
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
        'loc_BB3',
    )

    ChrTalk(
        0x0107,
        (
            '#061F啊 ，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BCE')

    def _loc_BB3(): pass

    label('loc_BB3')

    ChrTalk(
        0x00FE,
        (
            '你们太有\n',
            '这个资格了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BCE(): pass

    label('loc_BCE')

    ChrTalk(
        0x0101,
        (
            '#1017F嗯、嗯，谢谢你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，有需要的话\n',
            '请再让我们使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，我们期待着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x142F)
    OP_A2(0x0000)
    def _loc_C29(): pass

    label('loc_C29')

    TalkEnd(0x000A)

    Return()

# id: 0x0004 offset: 0xC2D
@scena.Code('func_04_C2D')
def func_04_C2D():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_D3B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_CB0',
    )

    ChrTalk(
        0x0008,
        (
            '#0541270017V#100F你们赶快去\n',
            '亚尔摩村吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270018V我呆在这里继续分析。\n',
            '了解到什么的话就赶快联系旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D38')

    def _loc_CB0(): pass

    label('loc_CB0')

    ChrTalk(
        0x0008,
        (
            '#0541270017V#100F你们赶快去\n',
            '亚尔摩村吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270019V我在这里继续\n',
            '解析『卡佩尔』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230813V了解到什么的话就赶快联系旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_D38(): pass

    label('loc_D38')

    Jump('loc_E1D')

    def _loc_D3B(): pass

    label('loc_D3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_E1D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_DA3',
    )

    ChrTalk(
        0x0008,
        (
            '#0541270020V#100F我们在这里\n',
            '准备接收数据。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270021V就拜托你们去\n',
            '设置测量仪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E1D')

    def _loc_DA3(): pass

    label('loc_DA3')

    ChrTalk(
        0x0008,
        (
            '#0541270022V#100F哟，怎么样？\n',
            '测量仪的设置还顺利吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270023V今天『卡佩尔』状态不错。\n',
            '这边的准备也非常顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_E1D(): pass

    label('loc_E1D')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xE21
@scena.Code('func_05_E21')
def func_05_E21():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_F67',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F22',
    )

    ChrTalk(
        0x00FE,
        (
            '说不定对这个事件博士\n',
            '也要负责任呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定是他偷偷做的实验失败了，\n',
            '使整个王国的导力停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈……\n',
            '不、不会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就、就算是那个人也不会\n',
            '做这么危险的实验吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不、不过也不能这么断言，\n',
            '这正是可怕的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_F64')

    def _loc_F22(): pass

    label('loc_F22')

    ChrTalk(
        0x00FE,
        (
            '拉、拉赛尔博士\n',
            '不会与此有关吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈……\n',
            '不、不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F64(): pass

    label('loc_F64')

    Jump('loc_14E7')

    def _loc_F67(): pass

    label('loc_F67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_106F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1008',
    )

    ChrTalk(
        0x00FE,
        (
            '现在发生的现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像以前拉赛尔博士\n',
            '也搞出来过吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是说现象持续的过程中\n',
            '我们是无可奈何的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……今天就早点回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_106C')

    def _loc_1008(): pass

    label('loc_1008')

    ChrTalk(
        0x00FE,
        (
            '好像以前拉赛尔博士\n',
            '也搞出来过现在的这个现象吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是说现象持续的过程中\n',
            '我们是无可奈何的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_106C(): pass

    label('loc_106C')

    Jump('loc_14E7')

    def _loc_106F(): pass

    label('loc_106F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1137',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_10DB',
    )

    ChrTalk(
        0x00FE,
        (
            '地震已经好象平息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么样，\n',
            '希望地面能够稳住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是为了『卡佩尔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1134')

    def _loc_10DB(): pass

    label('loc_10DB')

    ChrTalk(
        0x00FE,
        (
            '虽然工房长已经发表了说法\n',
            '地震已经好象平息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，那个测量\n',
            '好像起作用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1134(): pass

    label('loc_1134')

    Jump('loc_14E7')

    def _loc_1137(): pass

    label('loc_1137')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_11EE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_118A',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～工作总算\n',
            '收拾完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那～接下来就\n',
            '交给特莱斯主任吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11EB')

    def _loc_118A(): pass

    label('loc_118A')

    ChrTalk(
        0x00FE,
        (
            '呼～工作总算\n',
            '开始进行处理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过博士很厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在短期内能构筑起\n',
            '这样的系统。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_11EB(): pass

    label('loc_11EB')

    Jump('loc_14E7')

    def _loc_11EE(): pass

    label('loc_11EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_1285',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1251',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，博士真是每每\n',
            '有惊人之举。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是早点说的话，\n',
            '我们就能再轻松一点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1282')

    def _loc_1251(): pass

    label('loc_1251')

    ChrTalk(
        0x00FE,
        (
            '抱歉，现在有点忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有话一会儿再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1282(): pass

    label('loc_1282')

    Jump('loc_14E7')

    def _loc_1285(): pass

    label('loc_1285')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_148A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_13C4',
    )

    ChrTalk(
        0x00FE,
        (
            '『卡佩尔』与其他的机械不同\n',
            '好像必须休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是我个人的想法，不过我觉得\n',
            '这恐怕和有没有『记忆』有关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『卡佩尔』在活动中\n',
            '会不断更新自己的记忆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过没有在工作中重新构成\n',
            '那些记忆并储存的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以整理记忆就只能\n',
            '在停止的状态下进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我现在就在写\n',
            '有关这方面的论文。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1487')

    def _loc_13C4(): pass

    label('loc_13C4')

    ChrTalk(
        0x00FE,
        (
            '『卡佩尔』的状态很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为最近让它避开连续\n',
            '工作而进行定期的休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『卡佩尔』与其他的机械不同\n',
            '好像必须休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期休息的话状态\n',
            '就不容易下降。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真有趣。\n',
            '就好像生物一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1487(): pass

    label('loc_1487')

    Jump('loc_14E7')

    def _loc_148A(): pass

    label('loc_148A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_14E7',
    )

    ChrTalk(
        0x00FE,
        (
            '这个房间在５层，\n',
            '地震时还是有点摇晃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望『卡佩尔』不要\n',
            '又因此而闹别扭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14E7(): pass

    label('loc_14E7')

    TalkEnd(0x000C)

    Return()

# id: 0x0006 offset: 0x14EB
@scena.Code('func_06_14EB')
def func_06_14EB():
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
        'loc_1502',
    )

    Call(0, 0x000F)
    Call(0, 0x0010)

    def _loc_1502(): pass

    label('loc_1502')

    OP_4A(0x0008, 255)
    OP_72(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_72(0x0012, 0x0004)
    OP_76(0x0012, 0x00000000, 0x0002, 0x00000004, 0x00000008, 0x00000064, 0x03, 0x03)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0107, 0x0080)
    SetChrFlags(0x00F7, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    OP_6D(2120, 0, 13780, 0)
    OP_67(0, 7040, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0008, -510, 0, 10500, 0)
    SetChrPos(0x000A, 4420, 1000, 4220, 90)
    SetChrPos(0x0009, 460, 0, 7640, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_15CF')
    def lambda_15CF():
        OP_6D(1900, 0, 8220, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_15CF)

    @scena.Lambda('lambda_15E7')
    def lambda_15E7():
        OP_67(0, 7040, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15E7)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    Fade(250)
    OP_76(0x0012, 0x00000000, 0x0002, 0x00000004, 0x00000008, 0x00000064, 0x04, 0x07)
    OP_0D()
    Sleep(500)

    OP_4A(0x000A, 255)
    Sleep(500)

    OP_8C(0x000A, 270, 400)

    ChrTalk(
        0x000A,
        (
            '#1960230631V拉赛尔博士，\n',
            '１号连接成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230632V#100F#5P看来是的。\n',
            '情报很快就有了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230633V#104F嗯嗯……\n',
            '好象还算稳定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230634V#102F接着开始进行２号、３号的连接。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1960230635V明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 90, 400)
    OP_4B(0x000A, 255)

    @scena.Lambda('lambda_172C')
    def lambda_172C():
        OP_6D(710, 0, 3390, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_172C)

    OP_22(0x006D, 0x00, 0x64)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, 0x0007)
    Sleep(500)

    CreateThread(0x0107, 0x01, 0x00, 0x0008)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, 0x0009)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, 0x000A)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0107, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010230636V#1006F#5P干得不错，干得不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1804',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230637V#552F#2P真是的……\n',
            '仍旧是个稀奇古怪的房间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184B')

    def _loc_1804(): pass

    label('loc_1804')

    ChrTalk(
        0x0103,
        (
            '#0030230638V#023F#2P怎么说好呢……\n',
            '这个房间用这一句话就能概括了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_184B(): pass

    label('loc_184B')

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_186D')
    def lambda_186D():
        OP_6D(710, 0, 5300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_186D)

    ChrTurnDirection(0x0009, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1924',
    )

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
            TXT(0x00, '【◇已经和玛多克重逢的情况下】\n'),
            TXT(0x01, '【◇还没和玛多克重逢的情况下】\n'),
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
        (0x00000000, 'loc_190F'),
        (0x00000001, 'loc_1915'),
        (-1, 'loc_191B'),
    )

    def _loc_190F(): pass

    label('loc_190F')

    OP_A2(0x1481)

    Jump('loc_191B')

    def _loc_1915(): pass

    label('loc_1915')

    OP_A3(0x1481)

    Jump('loc_191B')

    def _loc_191B(): pass

    label('loc_191B')

    FadeIn(300, 0)

    def _loc_1924(): pass

    label('loc_1924')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 1, 0x1481)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B74',
    )

    ChrTalk(
        0x0009,
        (
            '#0550230639V#802F#5P哟……\n',
            '艾丝蒂尔，你来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230640V#1004F#6P啊，玛多克工房长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1994')
    def lambda_1994():
        OP_6D(710, 0, 6300, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1994)

    @scena.Lambda('lambda_19AC')
    def lambda_19AC():
        OP_8E(0x00FE, -290, 0, 4300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_19AC)

    Sleep(200)

    SetChrFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_19D1')
    def lambda_19D1():
        OP_8E(0x00FE, 500, 0, 6630, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_19D1)

    @scena.Lambda('lambda_19EC')
    def lambda_19EC():
        OP_8E(0x00FE, -1430, 0, 4330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_19EC)

    Sleep(100)

    @scena.Lambda('lambda_1A0C')
    def lambda_1A0C():
        OP_8E(0x00FE, -380, 0, 2970, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_1A0C)

    Sleep(200)

    @scena.Lambda('lambda_1A2C')
    def lambda_1A2C():
        OP_8E(0x00FE, -1470, 0, 3020, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_1A2C)

    WaitForThreadExit(0x00F9, 0x0000)
    WaitForThreadExit(0x0009, 0x0001)
    ClearChrFlags(0x0009, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010230641V#1025F#6P好久不见。\n',
            '好像是从诞辰庆典以来就没见过了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550230642V#803F#5P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550230643V#800F听说你遇到了一些事……\n',
            '还能这么打起精神来真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230644V#1016F#6P啊哈哈……\n',
            '谢谢你，工房长先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230645V#1011F我们受博士的委托\n',
            '安放了测量仪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CD1')

    def _loc_1B74(): pass

    label('loc_1B74')

    ChrTalk(
        0x0009,
        (
            '#0550230646V#802F#5P哟，艾丝蒂尔，你们来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230647V#1011F#6P嗯，工房长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1BD9')
    def lambda_1BD9():
        OP_6D(710, 0, 6300, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1BD9)

    @scena.Lambda('lambda_1BF1')
    def lambda_1BF1():
        OP_8E(0x00FE, -290, 0, 4300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1BF1)

    Sleep(200)

    SetChrFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_1C16')
    def lambda_1C16():
        OP_8E(0x00FE, 500, 0, 6630, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1C16)

    @scena.Lambda('lambda_1C31')
    def lambda_1C31():
        OP_8E(0x00FE, -1430, 0, 4330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_1C31)

    Sleep(100)

    @scena.Lambda('lambda_1C51')
    def lambda_1C51():
        OP_8E(0x00FE, -380, 0, 2970, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_1C51)

    Sleep(200)

    @scena.Lambda('lambda_1C71')
    def lambda_1C71():
        OP_8E(0x00FE, -1470, 0, 3020, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_1C71)

    WaitForThreadExit(0x00F9, 0x0000)
    WaitForThreadExit(0x0009, 0x0001)
    ClearChrFlags(0x0009, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010230648V#1011F#6P我们受博士的委托\n',
            '安放了测量仪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CD1(): pass

    label('loc_1CD1')

    ChrTalk(
        0x0009,
        (
            '#0550230649V#800F#5P嗯，看来是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550230650V好像正好刚从各地的\n',
            '测量仪传来了情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230651V#064F#6P那就是说『卡佩尔』的\n',
            '调整也结束了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0107, 400)

    ChrTalk(
        0x0009,
        (
            '#0550230652V#801F#5P嗯，博士刚让它\n',
            '运行了专用程序。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_76(0x0012, 0x00000000, 0x0002, 0x00000004, 0x00000008, 0x00000064, 0x08, 0x0B)
    OP_4A(0x000A, 255)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x000A, 270, 400)

    ChrTalk(
        0x000A,
        (
            '#1960230653V#5P２号、３号的连接也成功了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1E1C')
    def lambda_1E1C():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1E1C)

    Sleep(50)

    @scena.Lambda('lambda_1E2F')
    def lambda_1E2F():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1E2F)

    Sleep(50)

    @scena.Lambda('lambda_1E42')
    def lambda_1E42():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E42)

    Sleep(50)

    @scena.Lambda('lambda_1E55')
    def lambda_1E55():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1E55)

    Sleep(50)

    @scena.Lambda('lambda_1E68')
    def lambda_1E68():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1E68)

    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0540230654V#100F嗯，我们这边也确认好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 90, 400)
    OP_4B(0x000A, 255)

    ChrTalk(
        0x0008,
        (
            '#0540230655V#101F好好……\n',
            '哪边都很稳定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230656V这样一来从１号到３号的\n',
            '所有测量仪都传来了情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_1F3C')
    def lambda_1F3C():
        OP_6D(710, 0, 7300, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1F3C)

    ChrTurnDirection(0x0008, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0540230657V#103F哟，总算回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F89')
    def lambda_1F89():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1F89)

    Sleep(50)

    @scena.Lambda('lambda_1F9C')
    def lambda_1F9C():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F9C)

    Sleep(50)

    @scena.Lambda('lambda_1FAF')
    def lambda_1FAF():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1FAF)

    Sleep(50)

    @scena.Lambda('lambda_1FC2')
    def lambda_1FC2():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1FC2)

    Sleep(50)

    @scena.Lambda('lambda_1FD5')
    def lambda_1FD5():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1FD5)

    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0540230658V#101F看，托你们的福\n',
            '顺利地得到了情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230659V真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230660V#1016F#2P哈哈，我们只是\n',
            '运送了测量仪的零件而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_20FD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230661V#051F而且这件事也是\n',
            '我们这边请求的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230662V应该慰劳一下你那个连装置的\n',
            '启动都负责到底了的孙女啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2176')

    def _loc_20FD(): pass

    label('loc_20FD')

    ChrTalk(
        0x0103,
        (
            '#0030230663V#027F而且这件事也是\n',
            '我们这边请求的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230664V应该慰劳一下你那个连装置的\n',
            '启动都负责到底了的孙女啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2176(): pass

    label('loc_2176')

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    OP_8C(0x0107, 90, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230665V#560F#5P没、没什么的～\n',
            '也不是什么了不起的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230666V#101F不不，\n',
            '你也很努力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230667V传送器的设定也没问题。\n',
            '情报发送很正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0107, 0, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230668V#067F#6P嘿嘿，太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230669V#560F那就是说\n',
            '准备都完成了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230670V还有什么需要我帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230671V#104F没有了，准备已经完成。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230672V#100F我已经给『卡佩尔』设计了程序，\n',
            '如果七耀脉的运动发生紊乱的话\n',
            '它会自动开始解析的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230673V接下来，就只要等待\n',
            '什么地方再发生地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230674V#1007F#2P是吗……\n',
            '现在可以算是告一段落了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230675V#1015F不过干等什么地方发生地震\n',
            '还是让人感觉不自在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2465',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230676V#035F#6P呵呵，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230677V#030F说不定蔡斯还会发生\n',
            '大规模的地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24BA')

    def _loc_2465(): pass

    label('loc_2465')

    ChrTalk(
        0x0105,
        (
            '#0060230678V#043F#6P确实是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230679V说不定蔡斯还会发生\n',
            '大规模的地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24BA(): pass

    label('loc_24BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_24F2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230680V#050F对此你们\n',
            '有什么对策吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2520')

    def _loc_24F2(): pass

    label('loc_24F2')

    ChrTalk(
        0x0103,
        (
            '#0030230681V#020F对此你们\n',
            '有什么对策吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2520(): pass

    label('loc_2520')

    OP_8C(0x0009, 225, 400)

    ChrTalk(
        0x0009,
        (
            '#0550230682V#800F#5P我们姑且已经把\n',
            '容易倒塌的装置进行了固定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550230683V#803F不过即便如此，要是发生比\n',
            '上次更厉害的地震就不好办了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550230684V设备的损坏应该是不能避免了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230685V#100F就是说，这台\n',
            '『卡佩尔』也是一样的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230686V因为摇晃而引起误操作\n',
            '致使实验失败的可能性也很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230687V#101F大家都向女神祈祷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230688V#1007F#2P啊……\n',
            '感觉有点不安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2707',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230689V#035F#6P呼，就算是最新技术也\n',
            '仍然很需要祈求神灵保佑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2750')

    def _loc_2707(): pass

    label('loc_2707')

    ChrTalk(
        0x0105,
        (
            '#0060230690V#045F#6P呼，就算是最新技术也\n',
            '仍然很需要祈求神灵保佑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2750(): pass

    label('loc_2750')

    OP_8C(0x0107, 180, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230691V#560F#5P嘿嘿，技术人员可是\n',
            '出奇地有信仰心哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230692V我在进行困难的作业时\n',
            '也经常向女神祈祷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550230693V#806F#5P确实有点道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550230694V我在博士首次开发\n',
            '导力飞船的时候\n',
            '一天要去三次教会哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230695V#102F什么啊，你真是个失礼的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550230696V#803F#5P经历过３９次实验失败的话\n',
            '当然会这么做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230697V#1016F#2P啊哈哈……\n',
            '从以前开始就有这种感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0107, 90, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230698V#067F#6P嗯……确实如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_299C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230699V#051F不过既然这样的话，\n',
            '我们去找个地方打发时间吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230700V先回一次协会\n',
            '报告一下也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A0B')

    def _loc_299C(): pass

    label('loc_299C')

    ChrTalk(
        0x0103,
        (
            '#0030230701V#027F不过既然这样的话，\n',
            '我们去找个地方打发时间吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230702V先回一次协会\n',
            '报告一下也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A0B(): pass

    label('loc_2A0B')

    ChrTalk(
        0x0008,
        (
            '#0540230703V#101F嗯，你们就这么办吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230704V有什么动向的话\n',
            '我们会联络协会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x009D, 0x00, 0x64)
    OP_76(0x0012, 0x00000000, 0x0002, 0x00000004, 0x00000008, 0x00000064, 0x0C, 0x0F)
    Sleep(1500)

    OP_20(0x000007D0)
    OP_22(0x009E, 0x00, 0x64)
    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_76(0x0012, 0x00000000, 0x0002, 0x00000004, 0x00000008, 0x00000064, 0x10, 0x17)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0009, 0, 600)
    OP_8C(0x0008, 0, 600)
    OP_8C(0x0101, 0, 600)
    OP_8C(0x0107, 0, 600)

    ChrTalk(
        0x0101,
        (
            '#0010230705V#1020F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230706V#065F#6P莫、莫非……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230707V#104F……看来没必要\n',
            '回协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x000A, 255)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x000A, 270, 600)

    ChrTalk(
        0x000A,
        (
            '#1960230708V#5P从１号到３号的所有\n',
            '测量仪都有了变化！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1960230709V#5P地下的七耀脉的\n',
            '运动好像变得活跃了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230710V#102F嗯，继续\n',
            '监视屏幕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230711V如果通讯被阻断就报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1960230712V#5P明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 90, 600)
    OP_4B(0x000A, 255)
    OP_8C(0x0008, 225, 600)

    @scena.Lambda('lambda_2CCD')
    def lambda_2CCD():
        ChrTurnDirection(0x0009, 0x0008, 400)
        Yield()

        Jump('lambda_2CCD')

    DispatchAsync2(0x0009, 0x0001, lambda_2CCD)

    @scena.Lambda('lambda_2CDE')
    def lambda_2CDE():
        OP_6D(-590, 0, 6000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2CDE)

    OP_8E(0x0008, -1700, 0, 9650, 3000, 0x00)
    OP_8E(0x0008, -1700, 0, 5790, 3000, 0x00)
    OP_8E(0x0008, -480, 0, 5790, 3000, 0x00)
    OP_8C(0x0008, 0, 400)
    TerminateThread(0x0009, 0x01)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0540230713V#102F#5P即时开始解析\n',
            '3处的情报……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230714V搜索目前集合了\n',
            '最大地震波的地点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230715V#104F座标【12.73，378.02】\n',
            '哟……原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230716V#1026F#2P怎、怎样啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230717V#102F#5P现在已经知道\n',
            '哪儿在发生地震了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230718V是雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230719V#1020F#2P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2EB1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230720V#055F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED0')

    def _loc_2EB1(): pass

    label('loc_2EB1')

    ChrTalk(
        0x0103,
        (
            '#0030230721V#024F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2ED0(): pass

    label('loc_2ED0')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_4B(0x000A, 255)
    OP_4B(0x0008, 255)
    OP_4B(0x000C, 255)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/C3101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x2EF4
@scena.Code('func_07_2EF4')
def func_07_2EF4():
    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x0101, -1120, 0, -1250, 0)
    ClearChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_2F1B')
    def lambda_2F1B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2F1B)

    OP_8E(0x0101, -360, 0, 2350, 2000, 0x00)
    OP_8C(0x0101, 0, 400)

    Return()

# id: 0x0008 offset: 0x2F43
@scena.Code('func_08_2F43')
def func_08_2F43():
    OP_9F(0x0107, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x0107, -1120, 0, -1250, 0)
    ClearChrFlags(0x0107, 0x0080)

    @scena.Lambda('lambda_2F6A')
    def lambda_2F6A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_2F6A)

    OP_8E(0x0107, -1600, 0, 2130, 2000, 0x00)
    OP_8C(0x0107, 0, 400)

    Return()

# id: 0x0009 offset: 0x2F92
@scena.Code('func_09_2F92')
def func_09_2F92():
    OP_9F(0x00F7, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00F7, -1120, 0, -1250, 0)
    ClearChrFlags(0x00F7, 0x0080)

    @scena.Lambda('lambda_2FB9')
    def lambda_2FB9():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_2FB9)

    OP_8E(0x00F7, -510, 0, 910, 2000, 0x00)
    OP_8C(0x00F7, 0, 400)

    Return()

# id: 0x000A offset: 0x2FE1
@scena.Code('func_0A_2FE1')
def func_0A_2FE1():
    OP_9F(0x00F9, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00F9, -1120, 0, -1250, 0)
    ClearChrFlags(0x00F9, 0x0080)

    @scena.Lambda('lambda_3008')
    def lambda_3008():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_3008)

    OP_8E(0x00F9, -1710, 0, 740, 2000, 0x00)
    OP_8C(0x00F9, 0, 400)

    Return()

# id: 0x000B offset: 0x3030
@scena.Code('func_0B_3030')
def func_0B_3030():
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
        'loc_3047',
    )

    Call(0, 0x000F)
    Call(0, 0x0010)

    def _loc_3047(): pass

    label('loc_3047')

    OP_22(0x009E, 0x00, 0x64)
    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_72(0x0012, 0x0004)
    OP_76(0x0012, 0x00000000, 0x0002, 0x00000004, 0x00000008, 0x00000064, 0x10, 0x17)
    OP_4A(0x0008, 255)
    OP_6D(-840, 0, 2850, 0)
    OP_67(0, 7040, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -290, 0, 4300, 0)
    SetChrPos(0x0107, -1430, 0, 4330, 0)
    SetChrPos(0x00F7, -380, 0, 2970, 0)
    SetChrPos(0x00F9, -1470, 0, 3020, 0)
    SetChrPos(0x0008, -480, 0, 5780, 0)
    SetChrPos(0x000A, 4420, 1000, 4220, 90)
    SetChrPos(0x0009, 500, 0, 6630, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    FadeIn(1000, 0)
    Sleep(500)

    OP_22(0x006D, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_3166')
    def lambda_3166():
        OP_6D(-800, 0, 5130, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_3166)

    OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x000B, -1080, 0, -1380, 0)
    ClearChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_319F')
    def lambda_319F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_319F)

    OP_8E(0x000B, -950, 0, 1450, 3000, 0x00)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#1950230733V工房长！\n',
            '从雷斯顿要塞收到联络！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1950230734V说是就在刚才\n',
            '发生了中等规模的地震！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000B, 400)

    ChrTalk(
        0x0009,
        (
            '#0550230735V#805F#5P果然如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3259')
    def lambda_3259():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3259)

    Sleep(100)

    @scena.Lambda('lambda_326C')
    def lambda_326C():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_326C)

    Sleep(50)

    @scena.Lambda('lambda_327F')
    def lambda_327F():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_327F)

    Sleep(50)

    @scena.Lambda('lambda_3292')
    def lambda_3292():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3292)

    Sleep(50)

    @scena.Lambda('lambda_32A5')
    def lambda_32A5():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_32A5)

    WaitForThreadExit(0x0107, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010230736V#1020F#5P受、受害情况怎样！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1950230737V幸好\n',
            '没人受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1950230738V好像是事先\n',
            '做好了对地震的防范。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230739V#1007F#5P太、太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230740V#101F#5P不愧是卡西乌斯。\n',
            '有着万全的危机对策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_24(0x009D, 0x46)
    OP_22(0x009D, 0x00, 0x64)
    OP_23(0x009E)
    OP_76(0x0012, 0x00000000, 0x0002, 0x00000004, 0x00000008, 0x00000064, 0x18, 0x1B)

    @scena.Lambda('lambda_33C4')
    def lambda_33C4():
        OP_6D(-800, 0, 6500, 800)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_33C4)

    OP_8C(0x0008, 0, 500)
    WaitForThreadExit(0x0000, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0540230741V#102F#6P那么……\n',
            '这边的解析也完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_341F')
    def lambda_341F():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_341F)

    Sleep(50)

    @scena.Lambda('lambda_3432')
    def lambda_3432():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3432)

    Sleep(100)

    @scena.Lambda('lambda_3445')
    def lambda_3445():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3445)

    Sleep(50)

    @scena.Lambda('lambda_3458')
    def lambda_3458():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3458)

    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '拉赛尔博士确认了\n',
            '显示屏上的解析结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0540230742V#102F#6P嗯……让我看看……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230743V#103F哦哦……\n',
            '这真有意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230744V#1002F#2P发、发现什么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0540230745V#100F#5P嗯，别着急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230746V根据这个解析，地震发生之前，\n',
            '七耀脉的运动出现了异常。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230747V然后，由于扭曲的运动\n',
            '集合到要塞地下，\n',
            '发生了局部性的地震。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230748V因为发生在相当浅的地下，\n',
            '所以没影响到其他地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_366B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230749V#057F这就是地震的真正原因吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_369C')

    def _loc_366B(): pass

    label('loc_366B')

    ChrTalk(
        0x0103,
        (
            '#0030230750V#022F这就是地震的真正原因呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_369C(): pass

    label('loc_369C')

    ChrTalk(
        0x0101,
        (
            '#0010230751V#1020F#2P就、就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230752V有人通过操纵七耀脉\n',
            '引发地震！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_373D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230753V#032F#6P呼……\n',
            '可以称之为『地震兵器』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_377E')

    def _loc_373D(): pass

    label('loc_373D')

    ChrTalk(
        0x0105,
        (
            '#0060230754V#042F#6P『地震兵器』……\n',
            '说不定可以这么称呼它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_377E(): pass

    label('loc_377E')

    ChrTalk(
        0x0008,
        (
            '#0540230755V#102F#5P嗯。\n',
            '你说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230756V#065F#6P可、可是爷爷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230757V操纵七耀脉的运动这种事\n',
            '真的有可能做到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550230758V#805F#5P唔，就算利用最新的土木技术\n',
            '也应该是不可能做到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230759V#104F#5P对此我也有同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230760V#102F不过，虽然不愿意承认……\n',
            '可似乎是有人已经做到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230761V#1022F#2P好一个挑衅行为……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230762V#1005F博士，你还能推断出一些什么吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230763V比如那个『地震兵器』\n',
            '被放在哪里什么的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230764V#560F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_39A2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230765V#051F对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39BD')

    def _loc_39A2(): pass

    label('loc_39A2')

    ChrTalk(
        0x0103,
        (
            '#0030230766V#021F对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39BD(): pass

    label('loc_39BD')

    ChrTalk(
        0x0008,
        (
            '#0540230767V#103F#5P原来如此……\n',
            '这可真是个盲点呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 0, 600)
    OP_8C(0x0009, 225, 400)

    ChrTalk(
        0x0008,
        (
            '#0540230768V#102F#6P解析３处七耀脉\n',
            '运动的扭曲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230769V如果用逆算的形式\n',
            '算出扭曲的源头的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230770V出来了……\n',
            '坐标【165.88，-228.35】……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070230771V#065F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230772V#1002F#2P提妲，你认识这地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0107, 90, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230773V#065F#6P嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲取出了地图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    FadeOut(500, 0, -1)
    OP_0D()
    OP_C5(0x00, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS134._CH')
    OP_C5(0x01, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS207._CH')
    OP_C5(0x02, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS208._CH')
    OP_C5(0x03, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS209._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(1500)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('提妲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0070230774V#062F座标中心为\n',
            '蔡斯，单位塞尔矩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('提妲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0070230775V#062F从这里往东１２塞尔矩、\n',
            '往北３７８塞尔矩的地点\n',
            '是雷斯顿要塞的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('提妲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0070230776V#062F往东１６５塞尔矩、\n',
            '往南２２８塞尔矩的地点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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

    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '从蔡斯往东１６５塞尔矩、\n',
            '往南２２８塞尔矩的地点是？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【卡鲁迪亚钟乳洞】\n'),
            TXT(0x01, '【红莲之塔】\n'),
            TXT(0x02, '【亚尔摩温泉】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3E5F'),
        (0x00000001, 'loc_3EB5'),
        (0x00000002, 'loc_3F0B'),
        (-1, 'loc_3F64'),
    )

    def _loc_3E5F(): pass

    label('loc_3E5F')

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('提妲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0070230777V#063F啊，不对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230778V大概是在\n',
            '这附近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_3F64')

    def _loc_3EB5(): pass

    label('loc_3EB5')

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('提妲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0070230777V#063F啊，不对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230778V大概是在\n',
            '这附近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_3F64')

    def _loc_3F0B(): pass

    label('loc_3F0B')

    OP_2B(0x0088, 0x0002)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('提妲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0070230781V#063F嗯、嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230778V大概是在\n',
            '这附近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_3F64')

    def _loc_3F64(): pass

    label('loc_3F64')

    OP_AE(0x000001F4)
    Sleep(500)

    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(300, 50, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010230783V#1020F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4013',
    )

    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName('阿加特')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0050230784V#555F完全成为盲点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_4051')

    def _loc_4013(): pass

    label('loc_4013')

    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0030230785V#025F完全成为盲点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4051(): pass

    label('loc_4051')

    ChrTurnDirection(0x0008, 0x0101, 0)
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x03, 0x03, 16777215, 1000, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4153',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230786V#035F#6P亚尔摩村……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230787V#030F看来那个温泉胜地里面\n',
            '才是真正的『震源』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41B7')

    def _loc_4153(): pass

    label('loc_4153')

    ChrTalk(
        0x0105,
        (
            '#0060230788V#047F#6P亚尔摩村……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230789V#042F看来那个温泉胜地里面\n',
            '才是真正的『震源』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41B7(): pass

    label('loc_41B7')

    ChrTalk(
        0x0008,
        (
            '#0540230790V#102F#5P虽然不敢断言，\n',
            '不过那个可能性看来很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230791V你们准备怎么做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)
    OP_8C(0x0107, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230792V#1005F#2P那还用问！\n',
            '必须马上去调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4290',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230793V#057F嗯……\n',
            '看来要抓紧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42BC')

    def _loc_4290(): pass

    label('loc_4290')

    ChrTalk(
        0x0103,
        (
            '#0030230794V#022F嗯……\n',
            '看来要抓紧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42BC(): pass

    label('loc_42BC')

    ChrTalk(
        0x0008,
        (
            '#0540230795V#104F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230796V#102F那你们就把\n',
            '提妲也带去好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230797V这孩子的知识和技术\n',
            '一定会对调查有帮助的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0107, 0, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230798V#560F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0107, 90, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230799V#062F#6P嗯，我一定能帮忙的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230800V#1007F#2P唔……\n',
            '虽然可能有危险……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230801V#1006F不过有我们保护你的话\n',
            '应该没问题的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_447A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230802V#053F真是的……拿你没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230803V#050F喂，小不点。\n',
            '绝对不要勉强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44C3')

    def _loc_447A(): pass

    label('loc_447A')

    ChrTalk(
        0x0103,
        (
            '#0030230804V#026F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230805V#020F提妲。\n',
            '千万不能勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44C3(): pass

    label('loc_44C3')

    OP_8C(0x0107, 180, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230806V#062F#5P好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550230807V#800F#5P那么就由我来\n',
            '联系亚尔摩村吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550230808V如果请麻绪婆婆帮忙的话\n',
            '你们的调查也会更加顺利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)
    OP_8C(0x0107, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230809V#1006F#6P嗯，那真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550230810V#800F#5P海泽尔。\n',
            '准备通讯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1950230811V遵命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_45E4')
    def lambda_45E4():
        OP_6D(-840, 0, 2850, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_45E4)

    @scena.Lambda('lambda_45FC')
    def lambda_45FC():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_45FC')

    DispatchAsync2(0x0101, 0x0002, lambda_45FC)

    @scena.Lambda('lambda_460D')
    def lambda_460D():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_460D')

    DispatchAsync2(0x0107, 0x0002, lambda_460D)

    @scena.Lambda('lambda_461E')
    def lambda_461E():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_461E')

    DispatchAsync2(0x00F7, 0x0002, lambda_461E)

    @scena.Lambda('lambda_462F')
    def lambda_462F():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_462F')

    DispatchAsync2(0x00F9, 0x0002, lambda_462F)

    CreateThread(0x0009, 0x01, 0x00, 0x000C)
    Sleep(200)

    CreateThread(0x000B, 0x01, 0x00, 0x000D)
    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0107, 0x02)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x00F9, 0x02)

    @scena.Lambda('lambda_466D')
    def lambda_466D():
        OP_6D(-840, 0, 5130, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_466D)

    @scena.Lambda('lambda_4685')
    def lambda_4685():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_4685)

    Sleep(50)

    @scena.Lambda('lambda_4698')
    def lambda_4698():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4698)

    Sleep(50)

    @scena.Lambda('lambda_46AB')
    def lambda_46AB():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_46AB)

    Sleep(50)

    @scena.Lambda('lambda_46BE')
    def lambda_46BE():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_46BE)

    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0000, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0540230812V#102F#5P我在这里\n',
            '解析『卡佩尔』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230813V了解到什么的话就会尽快联系旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230814V#1002F#2P嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230815V我们如果发现了什么\n',
            '也会联络中央工房的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540230816V#102F#5P嗯，交给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_47F9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230817V#054F好……\n',
            '那么我们这就去亚尔摩村吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4831')

    def _loc_47F9(): pass

    label('loc_47F9')

    ChrTalk(
        0x0103,
        (
            '#0030230818V#024F那么……\n',
            '我们就这就去亚尔摩村吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4831(): pass

    label('loc_4831')

    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(-1230, 0, 3450, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0000, -1230, 0, 3450, 17)
    SetChrPos(0x0001, -1230, 0, 3450, 17)
    SetChrPos(0x0002, -1230, 0, 3450, 17)
    SetChrPos(0x0003, -1230, 0, 3450, 17)
    SetChrPos(0x0008, -480, 0, 10270, 0)
    OP_0D()
    OP_8C(0x0008, 0, 0)
    OP_4B(0x0008, 255)
    OP_4B(0x000A, 255)
    OP_4B(0x000C, 255)
    OP_72(0x0002, 0x0004)
    OP_71(0x0012, 0x0004)
    OP_A2(0x1420)
    OP_28(0x0088, 0x04, 0x02)
    OP_28(0x0088, 0x04, 0x08)
    OP_28(0x0088, 0x01, 0x0001)
    OP_28(0x0085, 0x04, 0x10)
    OP_28(0x0086, 0x04, 0x10)
    OP_28(0x0087, 0x04, 0x10)
    OP_28(0x0070, 0x04, 0x40)
    Sleep(500)

    OP_1D(0x0D)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x02000000)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x4939
@scena.Code('func_0C_4939')
def func_0C_4939():
    OP_8E(0x0009, 950, 0, 6090, 2500, 0x00)
    OP_8E(0x0009, 600, 0, 2650, 2500, 0x00)
    OP_8E(0x0009, -1090, 0, 740, 2500, 0x00)
    OP_8E(0x0009, -1230, 0, -370, 2500, 0x00)
    OP_20(0x00000BB8)

    @scena.Lambda('lambda_4994')
    def lambda_4994():
        OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4994)

    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x0009, -1200, 0, -1830, 2500, 0x00)
    SetChrFlags(0x0009, 0x0080)

    Return()

# id: 0x000D offset: 0x49BF
@scena.Code('func_0D_49BF')
def func_0D_49BF():
    OP_8C(0x00FE, 180, 500)
    OP_8E(0x00FE, -1230, 0, -370, 2500, 0x00)

    @scena.Lambda('lambda_49E0')
    def lambda_49E0():
        OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_49E0)

    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, -1200, 0, -1830, 2500, 0x00)
    SetChrFlags(0x000B, 0x0080)

    Return()

# id: 0x000E offset: 0x4A0B
@scena.Code('func_0E_4A0B')
def func_0E_4A0B():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    OP_6D(-200, 0, 7100, 1000)
    FadeOut(300, 0, 100)
    OP_22(0x009D, 0x00, 0x64)
    SetChrName('CAPEL')
    SetMessageWindowPos(250, 78, 36, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1SThe Orbal Calculator\n',
            'CAPEL SYSTEM Ver.7.0\n',
            'Copyright(C) Z.C.F. 1197-1202\n',
            'MODE:Information Retrieval\n',
            '#200W　#20W\n',
            'MEMORY_CHECK#100W..........#20WＯＫ!\n',
            '#200W　#20W\n',
            '#1S已连接到数据库。\n',
            '请选择要搜索的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4B1D(): pass

    label('loc_4B1D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_625F',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        6,
        28,
        1,
        (
            TXT(0x00, '【中央工房关联】　　\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4B6B'),
        (-1, 'loc_624F'),
    )

    def _loc_4B6B(): pass

    label('loc_4B6B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_623F',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        6,
        116,
        1,
        (
            TXT(0x00, '【设立·沿革】\n'),
            TXT(0x01, '【技术一览】\n'),
            TXT(0x02, '【关联信息搜索】　　\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4BD4'),
        (0x00000001, 'loc_5239'),
        (0x00000002, 'loc_5F5D'),
        (-1, 'loc_622F'),
    )

    def _loc_4BD4(): pass

    label('loc_4BD4')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１５４】（Ｓ…七耀历）\n',
            'Ｃ·爱普斯泰恩博士于列曼自治州去世。\n',
            '【Ｓ１１５５】\n',
            'Ａ·拉赛尔博士回到利贝尔王国。\n',
            '回国后提倡普及导力器技术，\n',
            '但是没得到世人的认可和支持。\n',
            '【Ｓ１１５７】\n',
            '拉赛尔博士带领蔡斯的钟表工匠普及导力器。\n',
            '同年，『蔡斯技术工房』（即之后的中央工房）设立。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１６０】\n',
            '埃德佳Ⅲ世在视察蔡斯技术工房后提供巨额资金建设工\n',
            '房。拉赛尔博士出任首任工房长。\n',
            '【Ｓ１１６２】\n',
            '埃德佳Ⅲ世去世。艾莉茜雅Ⅱ世即位。\n',
            '【Ｓ１１６４】\n',
            '『伦格兰德大桥』落成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１６８】\n',
            '首部导力飞船『加拉托拉巴号』诞生。\n',
            '（经过３９次飞行实验失败后的产物）\n',
            '【Ｓ１１７３】\n',
            '蔡斯技术工房开始对共和国乌尔努社和帝国莱恩福尔特\n',
            '社输出导力器技术。工房改名为『中央工房』。\n',
            '【Ｓ１１７５】\n',
            '飞船公社设立。定期船『林德号』开始服役。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１７７】\n',
            '定期船『赛希莉亚号』开始服役。\n',
            '【Ｓ１１７８】\n',
            '移动工房船『莱普尼兹号』开始服役。\n',
            '【Ｓ１１８０】\n',
            '中央工房搬迁（即现在的建筑物）。\n',
            '开掘卡鲁迪亚平原丘陵的一角，地下工房建成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１８２】\n',
            '拉赛尔工房长退休。\n',
            '玛多克技术主任出任第二任工房长。\n',
            '【Ｓ１１８５】\n',
            '自然科学和医学研究部门设立。\n',
            '【Ｓ１１８７】\n',
            '客船『埃迪鲁那号』在卡尔瓦德领海沉没。\n',
            '尤迪斯王太子夫妇去世。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１９０】\n',
            '与爱普斯泰恩财团合作，\n',
            '发表了『导力网络』的构想。\n',
            '【Ｓ１１９２】\n',
            '『百日战役』爆发。\n',
            '中央工房被埃雷波尼亚帝国接管。\n',
            '拉赛尔博士在雷斯顿要塞开发出警备飞艇，\n',
            '并将其用于反攻作战中，取得了显赫的战功，\n',
            '从此警备飞艇作为王国军的主力兵器而被使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１９３】\n',
            '利贝尔王国和埃雷波尼亚帝国缔结和平条约。\n',
            '战后，王国再次向帝国输出导力器。\n',
            '【Ｓ１１９７】\n',
            '导力演算器『卡佩尔』Ver.1完成。\n',
            '【Ｓ１１９９】\n',
            '高速巡洋舰『埃尔赛尤』开发工程开始。\n',
            '【Ｓ１２０２】\n',
            '高速巡洋舰『埃尔赛尤』竣工，进入试飞阶段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_623C')

    def _loc_5239(): pass

    label('loc_5239')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F4D',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_52ED',
    )

    Menu(
        2,
        6,
        116,
        1,
        (
            TXT(0x00, '【导力器】\n'),
            TXT(0x01, '【结晶回路】\n'),
            TXT(0x02, '【七耀石】\n'),
            TXT(0x03, '【导力飞船】\n'),
            TXT(0x04, '【导力兵器】\n'),
            TXT(0x05, '【战术导力器】\n'),
            TXT(0x06, '【新型战术导力器】\n'),
            TXT(0x07, '【游击士协会招牌】\n'),
        ),
    )

    Jump('loc_5355')

    def _loc_52ED(): pass

    label('loc_52ED')

    Menu(
        2,
        6,
        116,
        1,
        (
            TXT(0x00, '【导力器】\n'),
            TXT(0x01, '【结晶回路】\n'),
            TXT(0x02, '【七耀石】\n'),
            TXT(0x03, '【导力飞船】\n'),
            TXT(0x04, '【导力兵器】\n'),
            TXT(0x05, '【战术导力器】\n'),
            TXT(0x06, '【新型战术导力器】\n'),
        ),
    )

    def _loc_5355(): pass

    label('loc_5355')

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5381'),
        (0x00000001, 'loc_550A'),
        (0x00000002, 'loc_55D4'),
        (0x00000003, 'loc_56EC'),
        (0x00000004, 'loc_5821'),
        (0x00000005, 'loc_5993'),
        (0x00000006, 'loc_5B22'),
        (0x00000007, 'loc_5CCB'),
        (-1, 'loc_5F3D'),
    )

    def _loc_5381(): pass

    label('loc_5381')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：导力器（Orbment）\n',
            '在半世纪前由Ｃ·爱普斯泰恩博士所发明，是能从七耀\n',
            '石中提取导力，从而引发各种各样现象的机械装置的总\n',
            '称。导力器内部的构造和齿轮的运动，使加工七耀石而\n',
            '成的结晶回路相互干涉，可以引发丰富多彩的现象。导\n',
            '力器的实用性，除了能产生丰富现象以外，还在于拥有\n',
            '『经过一段时间内部的导力可以自然恢复』这种特异的\n',
            '便利性。另外，经济效率也要远远地领先于各种外燃、\n',
            '内燃引擎设备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F4A')

    def _loc_550A(): pass

    label('loc_550A')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：结晶回路（Quartz）\n',
            '将七耀石的碎片（耀晶片，Sepith）精制、加工而成的\n',
            '具有结晶构造的回路。作为能量源的同时，本身还是引\n',
            '起各种各样现象的装置。但结晶回路必须安装在导力器\n',
            '内才可以发挥作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F4A')

    def _loc_55D4(): pass

    label('loc_55D4')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：七耀石（Septium）\n',
            '是在大陆全土分布的７种贵重矿石的总称。因被人们称\n',
            '为『古代的宝石』、『神秘的象征』而变得珍重。近代\n',
            '一种将体积过小不能成为宝石的碎片（耀晶片）精制加\n',
            '工制作出结晶回路的技术被发明出来，因此导致七耀石\n',
            '资源的重要性在大陆诸国之间一夜之间变得十分重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F4A')

    def _loc_56EC(): pass

    label('loc_56EC')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：导力飞船\n',
            '导力飞船可以称得上是导力技术精华凝聚而成的结晶。\n',
            '集合了用于重力制御的大型飞翔装置和供给大量能量的\n',
            '导力引擎两大技术，使得如此大的飞船在空中飞行成为\n',
            '可能。\n',
            '为了实现高效率的导力传送和十分复杂的船体控制，最\n',
            '新的飞船大多搭载了高性能的导力演算器。２０亚矩以\n',
            '下的小型飞船又被称为『飞艇』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F4A')

    def _loc_5821(): pass

    label('loc_5821')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：导力兵器\n',
            '即以导力枪、导力炮作为代表，使用导力技术的兵器体\n',
            '系。现在已成为大多数国家军队的主力装备。\n',
            '导力枪枪管内具有能将能量按照螺旋线聚集并高速射出\n',
            '豆粒大小的金属子弹的构造，与发射火药的枪相比，填\n',
            '弹量大幅增加，而且还能够调节枪的威力。\n',
            '导力炮则可以发射封装了能量的炮弹（导力弹）并产生\n',
            '爆炸，与发射火药的炮相比，其后坐力小，而且也可以\n',
            '自由调节威力大小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F4A')

    def _loc_5993(): pass

    label('loc_5993')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：战术导力器\n',
            '可以发动导力魔法的导力器。大小和怀表差不多，内部\n',
            '构造则相当精致优雅。\n',
            '战术导力器具有安装结晶回路后能够提高持有者能力的\n',
            '设计，使内部结晶回路与持有者达到同步，引发出『共\n',
            '鸣现象』，以代替传统释放魔法所需的复杂的齿轮和驱\n',
            '动装置，使持有者能够发动各种导力魔法。\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S　\n',
            '而且，根据复数结晶回路属性和势能的组合不同，持有\n',
            '者能够使用的导力魔法也会发生变化，具有相当的灵活\n',
            '性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F4A')

    def _loc_5B22(): pass

    label('loc_5B22')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：新型战术导力器\n',
            '作为战术导力器的开发者，爱普斯泰恩财团对过去的型号进\n',
            '行大幅改良，并且成功投入实用的新规格战术导力器。和过\n',
            '去只有六个结晶回路插槽的旧型号相比，这种新型号则具备\n',
            '了七个结晶回路插槽，可以实现更为灵活的结晶回路组合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S　\n',
            '新型号不仅使可以使用的魔法变得多元化，而且使其威力也\n',
            '得到了飞跃性的提升。但是，由于新型号和过去型号的基本\n',
            '构造有很大的不同，新型战术导力器也有着无法互换结晶回\n',
            '路的缺陷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F4A')

    def _loc_5CCB(): pass

    label('loc_5CCB')

    OP_A2(0x0004)
    OP_28(0x006C, 0x01, 0x0008)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#0170450843V#1S内容：游击士协会招牌\n',
            '这就是英俊潇洒的怪盗绅士布卢布兰凭借其天才般的超级无\n',
            '敌手腕从傻瓜般的超级无能游击士协会之一的蔡斯支部的檐\n',
            '头偷走的金属招牌。虽然没什么经济价值，不过给予协会相\n',
            '关人员的打击是无穷的，正在读此文的诸位想必也强烈地感\n',
            '受到了屈辱吧。好了，闲话到此为止。该是时候给出下一个\n',
            '提示了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#0170450844V#1S　\n',
            '　　┌──────────────────┐　　\n',
            '　　│　　　　第３把钥匙再次位于市内。　　│　\n',
            '　　│      抬头看那『尖帽子三兄弟』吧。  │　　\n',
            '　　└──────────────────┘\n',
            '　※另外，这个记录会自动删除。　　　　\n',
            '　　所以再次极力推荐诸位赶快做好应做的笔记！　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F4A')

    def _loc_5F3D(): pass

    label('loc_5F3D')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5F4A')

    def _loc_5F4A(): pass

    label('loc_5F4A')

    Jump('loc_5239')

    def _loc_5F4D(): pass

    label('loc_5F4D')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0002)

    Jump('loc_623C')

    def _loc_5F5D(): pass

    label('loc_5F5D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_621F',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        2,
        6,
        264,
        1,
        (
            TXT(0x00, '【内燃引擎设备】\n'),
            TXT(0x01, '【汽油】\n'),
            TXT(0x02, '【运输车】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5FBA'),
        (0x00000001, 'loc_6093'),
        (0x00000002, 'loc_6132'),
        (-1, 'loc_620F'),
    )

    def _loc_5FBA(): pass

    label('loc_5FBA')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：内燃引擎设备\n',
            '在机关装置内燃烧燃料以获得能量的动力源。与导力机\n',
            '关相比经济效率低下，而且还会产生噪音、废气等各种\n',
            '问题，因此已经停止开发和生产。\n',
            '\n',
            '『内燃引擎设备』\n',
            '库存量：１台\n',
            '管理责任人：格斯塔夫维修长',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_621C')

    def _loc_6093(): pass

    label('loc_6093')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：汽油\n',
            '将天然产生的液态碳氢化合物（石油）分馏、精制而成\n',
            '的液体。常作为内燃引擎设备的燃料以及工业生产的溶\n',
            '剂使用。\n',
            '\n',
            '储备量：无（已向共和国订购）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_621C')

    def _loc_6132(): pass

    label('loc_6132')

    OP_28(0x0029, 0x01, 0x8000)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：运输车\n',
            '使用导力引擎驱动的各种车辆的总称。因为乘坐的舒适\n',
            '度较差，速度也很慢，所以基本不用于客运方面，而主\n',
            '要用来进行中短距离的货物运输。\n',
            '\n',
            '『运输车用驱动导力器』\n',
            '库存量：不明\n',
            '保管地点：地下工场搬入口',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_621C')

    def _loc_620F(): pass

    label('loc_620F')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_621C')

    def _loc_621C(): pass

    label('loc_621C')

    Jump('loc_5F5D')

    def _loc_621F(): pass

    label('loc_621F')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0002)

    Jump('loc_623C')

    def _loc_622F(): pass

    label('loc_622F')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_623C')

    def _loc_623C(): pass

    label('loc_623C')

    Jump('loc_4B6B')

    def _loc_623F(): pass

    label('loc_623F')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0001)

    Jump('loc_625C')

    def _loc_624F(): pass

    label('loc_624F')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_625C')

    def _loc_625C(): pass

    label('loc_625C')

    Jump('loc_4B1D')

    def _loc_625F(): pass

    label('loc_625F')

    SetMessageWindowPos(72, 320, 56, 3)

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

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_628D',
    )

    Call(1, 0x0000)
    OP_A3(0x0004)

    def _loc_628D(): pass

    label('loc_628D')

    EventEnd(0x01)

    Return()

# id: 0x000F offset: 0x6290
@scena.Code('func_0F_6290')
def func_0F_6290():
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
        (0x00000000, 'loc_630A'),
        (0x00000001, 'loc_6310'),
        (-1, 'loc_6316'),
    )

    def _loc_630A(): pass

    label('loc_630A')

    OP_A2(0x1200)

    Jump('loc_6316')

    def _loc_6310(): pass

    label('loc_6310')

    OP_A2(0x1201)

    Jump('loc_6316')

    def _loc_6316(): pass

    label('loc_6316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_6324',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_6328')

    def _loc_6324(): pass

    label('loc_6324')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_6328(): pass

    label('loc_6328')

    Return()

# id: 0x0010 offset: 0x6329
@scena.Code('func_10_6329')
def func_10_6329():
    ClearMapFlags(0x00000001)
    OP_6D(0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_6363',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x0006,
            0x00FF,
        ),
        (
            0x0003,
            0x0004,
            0xFFFF,
        ),
    )

    Jump('loc_637D')

    def _loc_6363(): pass

    label('loc_6363')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0005,
            0x0006,
            0x00FF,
        ),
        (
            0x0003,
            0x0004,
            0xFFFF,
        ),
    )

    def _loc_637D(): pass

    label('loc_637D')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0011 offset: 0x638F
@scena.Code('func_11_638F')
def func_11_638F():
    SetPlaceName(0x009A)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
