import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0122_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0122   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '佛莱迪'),
    TXT(0x02, '梅尔达斯'),
    TXT(0x03, '埃尔格'),
    TXT(0x04, '斯蒂娜'),
    TXT(0x05, '乘务员库因特'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0122.x'
    header.mapIndex       = 4
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T0122._SN', 'ED6_DT21/T0122_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1936
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
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
    ]

# id: 0x10002 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -38180,
            z                   = 0,
            y                   = -500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -36560,
            z                   = 0,
            y                   = 1550,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -36680,
            z                   = 0,
            y                   = 73750,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -86130,
            z                   = 0,
            y                   = 71210,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -42050,
            z                   = 0,
            y                   = -4160,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
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
    )

# id: 0x10005 offset: 0x172
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -38537,
            triggerZ            = 0,
            triggerY            = -1845,
            triggerRange        = 400,
            actorX              = -38180,
            actorZ              = 1500,
            actorY              = -497,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -36170,
            triggerZ            = 0,
            triggerY            = 71651,
            triggerRange        = 1000,
            actorX              = -36678,
            actorZ              = 1500,
            actorY              = 73751,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1BA
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1BB
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x1BC
@scena.Code('ReInit')
def ReInit():
    Call(0, 0x0004)

    Return()

# id: 0x0003 offset: 0x1C1
@scena.Code('func_03_1C1')
def func_03_1C1():
    Call(0, 0x0005)

    Return()

# id: 0x0004 offset: 0x1C6
@scena.Code('func_04_1C6')
def func_04_1C6():
    TalkBegin(0x0008)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_204',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 2, 0x188A)),
            Expr.Return,
        ),
        'loc_204',
    )

    Call(6, 0x0003)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F3',
    )

    OP_A9(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_1F3(): pass

    label('loc_1F3')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_204',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_204(): pass

    label('loc_204')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_706',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 3, 0x188B)),
            Expr.Return,
        ),
        'loc_303',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_255',
    )

    ChrTalk(
        0x0008,
        (
            '那么，巡逻就拜托了。\n',
            '有什么事的话我们会联系协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_300')

    def _loc_255(): pass

    label('loc_255')

    ChrTalk(
        0x0008,
        (
            '老爸对新型导力器\n',
            '看来很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '最近他就像那样，一个人\n',
            '进行调整之类的练习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果在导力器方面有什么问题，\n',
            '可以随时来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么，就有劳\n',
            '你们巡逻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_300(): pass

    label('loc_300')

    Jump('loc_706')

    def _loc_303(): pass

    label('loc_303')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 2, 0x188A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_545',
    )

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '呀，艾丝蒂尔和雪拉扎德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好久不见呢。\n',
            '你们看起来精神很不错，太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 2, 0x142A)),
            Expr.Return,
        ),
        'loc_3DD',
    )

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，佛莱迪先生也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '蔡斯的研修，\n',
            '看来圆满结束了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊啊，真是受益匪浅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_503')

    def _loc_3DD(): pass

    label('loc_3DD')

    ChrTalk(
        0x0101,
        (
            '#1000F晚上好，佛莱迪先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F你看来\n',
            '气色不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '嗯，我最近\n',
            '刚从蔡斯回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因为中央工房的新型引擎\n',
            '开始开发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F咦，佛莱迪先生\n',
            '也去了蔡斯！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯……刚好错过，\n',
            '没能遇见真有点遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F看来我们和你没有缘分啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈，可能算是错过了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_503(): pass

    label('loc_503')

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '对了，这么晚\n',
            '还在到处走动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是不是在巡逻？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188A)

    Jump('loc_586')

    def _loc_545(): pass

    label('loc_545')

    ChrTalk(
        0x0008,
        (
            '呀，艾丝蒂尔你们啊。\n',
            '这么晚了真不容易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是不是在巡逻？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_586(): pass

    label('loc_586')

    ChrTalk(
        0x0101,
        (
            '#1015F嗯……\n',
            '嗯，算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F我们在巡视市内的各处\n',
            '兼调查雾的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这附近\n',
            '没什么异常吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，没什么特别的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '……是吧，老爸，\n',
            '没什么异常吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)
    OP_4A(0x0009, 255)

    ChrTalk(
        0x0009,
        (
            '#3P嗯，很安静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F……嗯，那就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0000, 400)
    OP_8C(0x0009, 90, 400)
    OP_4B(0x0009, 255)

    ChrTalk(
        0x0103,
        (
            '#026F打扰你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#020F那我们继续\n',
            '去巡视了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '啊啊，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '有什么事的话，\n',
            '我会马上通知协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188B)

    def _loc_706(): pass

    label('loc_706')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x70A
@scena.Code('func_05_70A')
def func_05_70A():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 4, 0x188C)),
            Expr.Return,
        ),
        'loc_74D',
    )

    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_73C',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_736',
    )

    OP_A9(0x08)

    Jump('loc_738')

    def _loc_736(): pass

    label('loc_736')

    OP_A9(0x01)

    def _loc_738(): pass

    label('loc_738')

    TalkEnd(0x000A)

    Return()

    def _loc_73C(): pass

    label('loc_73C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_74D',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_74D(): pass

    label('loc_74D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_F12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 4, 0x188C)),
            Expr.Return,
        ),
        'loc_8C2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_882',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7B1',
    )

    ChrTalk(
        0x000A,
        (
            '看来这次的雾\n',
            '用常识无法解释。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔你们\n',
            '巡逻要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_87F')

    def _loc_7B1(): pass

    label('loc_7B1')

    ChrTalk(
        0x000A,
        (
            '哦，是艾丝蒂尔你们啊。\n',
            '巡逻辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '到了晚上雾还是\n',
            '没有变化呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '本来在夜风的吹拂下…\n',
            '第二天早上就会是个大晴天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '……看来这次的雾\n',
            '用常识无法解释。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们这些市民也该\n',
            '提高警戒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_87F(): pass

    label('loc_87F')

    Jump('loc_8BF')

    def _loc_882(): pass

    label('loc_882')

    ChrTalk(
        0x000A,
        (
            '鲁克他们确实令人担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔你们\n',
            '巡逻要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_8BF(): pass

    label('loc_8BF')

    Jump('loc_F12')

    def _loc_8C2(): pass

    label('loc_8C2')

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000A, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '哦，这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好久不见啦。\n',
            '从你去了训练场以后头一次见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F埃尔格先生，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊啊，终于回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '雪拉扎德也在一起，\n',
            '是不是又在执行协会的什么任务啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#026F嗯，我们正在\n',
            '城里巡逻。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#022F你们可能已经听说了，\n',
            '发生了一些让人有点在意的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0103, 400)

    ChrTalk(
        0x000A,
        (
            '嗯，我也是刚听说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '确实挺令人担心的……\n',
            '有你们巡逻真是太好了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '真是的，才这么一会儿不见，\n',
            '艾丝蒂尔你也成长了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '当年你那么讨厌考试，\n',
            '在研修中发牢骚，真令人怀念啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1008F我、我说埃尔格先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B06')
    def lambda_0B06():
        ChrTurnDirection(0x0000, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0B06)

    @scena.Lambda('lambda_0B14')
    def lambda_0B14():
        ChrTurnDirection(0x0001, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0B14)

    @scena.Lambda('lambda_0B22')
    def lambda_0B22():
        ChrTurnDirection(0x0002, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0B22)

    ChrTurnDirection(0x0003, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#021F哎呀，有什么好隐瞒的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '考试确实是很惨，\n',
            '但实技不是学的很好吗。',
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
        'loc_BC2',
    )

    ChrTalk(
        0x0106,
        (
            '#051F哈哈，果然是这样吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真像你的风格啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C76')

    def _loc_BC2(): pass

    label('loc_BC2')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF8',
    )

    ChrTalk(
        0x0107,
        (
            '#560F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哎～姐姐真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C76')

    def _loc_BF8(): pass

    label('loc_BF8')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C35',
    )

    ChrTalk(
        0x0104,
        (
            '#031F呵，感觉\n',
            '真像是艾丝蒂尔的过去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C76')

    def _loc_C35(): pass

    label('loc_C35')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C76',
    )

    ChrTalk(
        0x0108,
        (
            '#070F哈哈，别害羞嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '人有缺点才显得可爱嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C76(): pass

    label('loc_C76')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C97',
    )

    ChrTalk(
        0x0105,
        (
            '#041F嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C97(): pass

    label('loc_C97')

    ChrTalk(
        0x000A,
        (
            '呀，抱歉抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '老爱说过去的事，\n',
            '大概是因为上了年纪啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '话说回来，艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '关于约修亚\n',
            '有什么消息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D19')
    def lambda_0D19():
        ChrTurnDirection(0x0000, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0D19)

    @scena.Lambda('lambda_0D27')
    def lambda_0D27():
        ChrTurnDirection(0x0001, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0D27)

    @scena.Lambda('lambda_0D35')
    def lambda_0D35():
        ChrTurnDirection(0x0002, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0D35)

    ChrTurnDirection(0x0003, 0x000A, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1003F嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F调查了不少，\n',
            '但没什么发现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是吗……\n',
            '果然没那么简单吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '听卡西乌斯说起的时候，\n',
            '担心的不得了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样看来……艾丝蒂尔。\n',
            '你是没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是，觉得难过的时候\n',
            '随时都可以来这里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不介意的话，我和斯蒂娜\n',
            '都可以听你倾诉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F埃尔格先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F……嗯，谢谢。\n',
            '我一定会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊啊，常来逛逛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那么，小心巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们这边如果有什么异常\n',
            '也会马上联络协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    OP_A2(0x0001)

    def _loc_F12(): pass

    label('loc_F12')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0xF16
@scena.Code('func_06_F16')
def func_06_F16():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_1793',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 6, 0x188E)),
            Expr.Return,
        ),
        'loc_1267',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 7, 0x188F)),
            Expr.Return,
        ),
        'loc_F8C',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '虽然很担心这次的事，不过\n',
            '艾丝蒂尔你也要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听我说，一定\n',
            '不能勉强自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1264')

    def _loc_F8C(): pass

    label('loc_F8C')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_FDE',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你这么晚在干什么呢？\n',
            '有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1023')

    def _loc_FDE(): pass

    label('loc_FDE')

    ChrTalk(
        0x00FE,
        (
            '哎呀，是艾丝蒂尔～～\n',
            '还有雪拉也来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你这么晚在干什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1023(): pass

    label('loc_1023')

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，我们在\n',
            '城里巡逻一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F协会为了以防万一，\n',
            '也提高警惕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生了的那些事\n',
            '阿姨也听说了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '醒不过来的鲁克他们\n',
            '真令人担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，你们\n',
            '你们也要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听我说，\n',
            '一定不能勉强自己哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1013F真、真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '阿姨你每次\n',
            '都把我当小孩子看。',
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
        'loc_1176',
    )

    ChrTalk(
        0x0107,
        (
            '#061F嘿嘿……\n',
            '就像我妈妈一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1212')

    def _loc_1176(): pass

    label('loc_1176')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11A7',
    )

    ChrTalk(
        0x0105,
        (
            '#045F呵呵……\n',
            '你真是幸运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1212')

    def _loc_11A7(): pass

    label('loc_11A7')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11DD',
    )

    ChrTalk(
        0x0104,
        (
            '#031F呵呵，就像母亲一般的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1212')

    def _loc_11DD(): pass

    label('loc_11DD')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1212',
    )

    ChrTalk(
        0x0106,
        (
            '#051F哈哈，看来这就叫一物降一物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1212(): pass

    label('loc_1212')

    ChrTalk(
        0x0103,
        (
            '#020F嗯，不过阿姨\n',
            '没说错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们也\n',
            '小心一点为好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188F)

    def _loc_1264(): pass

    label('loc_1264')

    Jump('loc_1793')

    def _loc_1267(): pass

    label('loc_1267')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哎呀…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '呀～怎么办呀。\n',
            '这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，仔细一看…\n',
            '连雪拉也在一起呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的～真是好久不见哦！\n',
            '阿姨都急死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '昨天就听到传闻，\n',
            '但去碰你却一直没碰上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈，对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F不过，艾丝蒂尔\n',
            '也有很多事情啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就原谅她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没问题，这点事\n',
            '阿姨还是明白的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说约修亚的事时…\n',
            '还有点担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，看来艾丝蒂尔\n',
            '也很努力的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯、嗯……算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，别提了，\n',
            '艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（盯……………………\n',
            '　……………………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F什、什么？\n',
            '突然盯着我看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我、我刷了牙，\n',
            '脸也洗了才来的呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3S真是的，多漂亮呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1004F哇哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么回事，穿这裙子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有种活跃女孩子的感觉哦～～\n',
            '很适合你哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿……是、是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这个，是雪拉姐\n',
            '在王都给我买的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '作为当上正游击士的祝贺哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦～到底是雪拉。\n',
            '很有品味嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，阿姨\n',
            '喜欢就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '注意仪容\n',
            '可是有心思的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，即使成为正游击士\n',
            '看来也能做得很出色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前那么邋遢的艾丝蒂尔\n',
            '打扮得这么有模有样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜……\n',
            '阿、阿姨都快流眼泪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F哈，哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1013F（没，没想到\n',
            '  穿条裙子她都会哭啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F（要是看到艾丝蒂尔穿婚纱\n',
            '那还不得昏倒了啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188E)
    OP_A2(0x0002)

    def _loc_1793(): pass

    label('loc_1793')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x1797
@scena.Code('func_07_1797')
def func_07_1797():
    TalkBegin(0x000C)

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_1818',
    )

    ChrTalk(
        0x00FE,
        (
            '#3330461112V呼哼哼哼～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461141V嘿嘿，难得\n',
            '到了城里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461142V不去购物\n',
            '真是损失太大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1922')

    def _loc_1818(): pass

    label('loc_1818')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_18A0',
    )

    ChrTalk(
        0x00FE,
        (
            '#3330461143V索斯摩夫说他在工作中\n',
            '看到了一只猫哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461144V总之，详细情况可以去问他本人。\n',
            '他应该还在飞船坪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1922')

    def _loc_18A0(): pass

    label('loc_18A0')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_18B2',
    )

    Call(1, 0x0000)

    Jump('loc_1922')

    def _loc_18B2(): pass

    label('loc_18B2')

    ChrTalk(
        0x00FE,
        (
            '#3330461112V哼哼哼哼～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461141V嘿嘿，难得\n',
            '到了城里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461142V不去购物\n',
            '真是损失太大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1922(): pass

    label('loc_1922')

    TalkEnd(0x000C)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
