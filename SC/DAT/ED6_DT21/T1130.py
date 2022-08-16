import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1130_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1130   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1130.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0001
    header.entryFunction  = 0x0001
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1130_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '豪尔斯教区长',
            x                   = 59100,
            z                   = 1000,
            y                   = 52100,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '修女萝萨',
            x                   = 63070,
            z                   = 0,
            y                   = 48320,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '哈尔德',
            x                   = 56670,
            z                   = 0,
            y                   = 43550,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '丽露露',
            x                   = 60350,
            z                   = 0,
            y                   = 45170,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '格蕾娅',
            x                   = 58930,
            z                   = 0,
            y                   = 44670,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '科尔娜',
            x                   = 59980,
            z                   = 0,
            y                   = 46900,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '雅哈多老人',
            x                   = 58180,
            z                   = 0,
            y                   = 45750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '萨拉',
            x                   = 61740,
            z                   = 0,
            y                   = 46550,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = 57200,
            z                   = 0,
            y                   = 47070,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
    )

# id: 0x10002 offset: 0x212
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x212
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x212
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 58950,
            triggerZ            = 1000,
            triggerY            = 50250,
            triggerRange        = 400,
            actorX              = 59100,
            actorZ              = 2500,
            actorY              = 52100,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 16410,
            triggerZ            = 4000,
            triggerY            = 43010,
            triggerRange        = 800,
            actorX              = 16410,
            actorZ              = 5200,
            actorY              = 43010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x25A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_269',
    )

    ChrClearFlags(0x0010, 0x0080)

    Jump('loc_2F0')

    def _loc_269(): pass

    label('loc_269')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_278',
    )

    ChrClearFlags(0x000C, 0x0080)

    Jump('loc_2F0')

    def _loc_278(): pass

    label('loc_278')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_282',
    )

    Jump('loc_2F0')

    def _loc_282(): pass

    label('loc_282')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_291',
    )

    ChrSetFlags(0x0009, 0x0080)

    Jump('loc_2F0')

    def _loc_291(): pass

    label('loc_291')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2A5',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x0009, 0x0080)

    Jump('loc_2F0')

    def _loc_2A5(): pass

    label('loc_2A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2DD',
    )

    OP_64(0x00, 0x0001)
    ChrSetPos(0x0008, 59100, 0, 48100, 180)
    ChrSetFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_2F0')

    def _loc_2DD(): pass

    label('loc_2DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2F0',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrTurnDirection(0x0009, 0x000A, 0)

    def _loc_2F0(): pass

    label('loc_2F0')

    Return()

# id: 0x0001 offset: 0x2F1
@scena.Code('func_01_2F1')
def func_01_2F1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 2, 0x1A12)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_303',
    )

    OP_10(0x00, 0x00)
    OP_10(0x03, 0x01)

    def _loc_303(): pass

    label('loc_303')

    OP_64(0x01, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0078, 0x01, 0x0080)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0078, 0x01, 0x0100)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_32E',
    )

    OP_65(0x01, 0x0001)

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_338',
    )

    Jump('loc_343')

    def _loc_338(): pass

    label('loc_338')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_343',
    )

    OP_64(0x00, 0x0001)

    def _loc_343(): pass

    label('loc_343')

    Return()

# id: 0x0002 offset: 0x344
@scena.Code('func_02_344')
def func_02_344():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x349
@scena.Code('func_03_349')
def func_03_349():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_434',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FA',
    )

    ChrTalk(
        0x0008,
        (
            '人们的脸上稍微\n',
            '有了点光彩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '行走在道路上的人们，脚步\n',
            '也轻快了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯嗯，这是个好兆头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '状态恢复的快，\n',
            '这正是这柏斯市的长处所在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_431')

    def _loc_3FA(): pass

    label('loc_3FA')

    ChrTalk(
        0x0008,
        (
            '人们的脸上稍微\n',
            '有了点光彩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，是个好兆头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_431(): pass

    label('loc_431')

    Jump('loc_AFB')

    def _loc_434(): pass

    label('loc_434')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_593',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_530',
    )

    ChrTalk(
        0x0008,
        (
            '哎呀哎呀，\n',
            '昨天晚上那是场很严重的骚乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '情绪激动的市民们\n',
            '包围了协会和市长官邸，\n',
            '吵闹了整整一个晚上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然梅贝尔小姐的劝说取得了效果，\n',
            '事态在变得严重前得到了控制……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但导力器所带来的影响\n',
            '需要我们重新认识一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_590')

    def _loc_530(): pass

    label('loc_530')

    ChrTalk(
        0x0008,
        (
            '哎呀哎呀，\n',
            '昨天晚上那是场很严重的骚乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但导力器所带来的影响\n',
            '需要我们重新认识一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_590(): pass

    label('loc_590')

    Jump('loc_AFB')

    def _loc_593(): pass

    label('loc_593')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_6B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_5EE',
    )

    ChrTalk(
        0x0008,
        (
            '柏斯一带终于\n',
            '恢复了平静啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '拉文努村的果树园也\n',
            '有了复苏的迹象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B6')

    def _loc_5EE(): pass

    label('loc_5EE')

    ChrTalk(
        0x0008,
        (
            '柏斯一带终于\n',
            '恢复了平静啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '超市顺利恢复营业，\n',
            '拉文努村的果树园\n',
            '也有了复苏的迹象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '复兴虽然需要时间，\n',
            '但是，一定能够实现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '毕竟柏斯市是从那场战争中\n',
            '奇迹般的迅速恢复过来的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_6B6(): pass

    label('loc_6B6')

    Jump('loc_AFB')

    def _loc_6B9(): pass

    label('loc_6B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_80F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_75B',
    )

    ChrTalk(
        0x0008,
        (
            '梅贝尔市长\n',
            '相当努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但几乎不顾自己的身体这点\n',
            '让我有点担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '人在年轻的时候谁都是这样的吧。\n',
            '我年轻的时候也是这么不顾一切的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_80C')

    def _loc_75B(): pass

    label('loc_75B')

    ChrTalk(
        0x0008,
        (
            '梅贝尔市长\n',
            '相当努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可以说她工作的风采已经不输给\n',
            '身为前市长的父亲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但几乎不顾自己的身体这点\n',
            '让我有点担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，人在年轻的时候\n',
            '谁都是这样的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_80C(): pass

    label('loc_80C')

    Jump('loc_AFB')

    def _loc_80F(): pass

    label('loc_80F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_906',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_876',
    )

    ChrTalk(
        0x0008,
        (
            '市长官邸的女佣\n',
            '好像还没有恢复意识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我已经把我所知道的\n',
            '药的处方都用过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_903')

    def _loc_876(): pass

    label('loc_876')

    ChrTalk(
        0x0008,
        (
            '很遗憾，\n',
            '市长官邸的女佣\n',
            '好像还没有恢复意识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我已经把我所知道的\n',
            '药的处方都用过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '剩下的就只有等待\n',
            '看护修女的好消息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_903(): pass

    label('loc_903')

    Jump('loc_AFB')

    def _loc_906(): pass

    label('loc_906')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_9A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_954',
    )

    ChrTalk(
        0x0008,
        (
            '请大家冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '直到王国军赶来前，\n',
            '女神会保佑我们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A5')

    def _loc_954(): pass

    label('loc_954')

    ChrTalk(
        0x0008,
        (
            '请大家冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '很快\n',
            '王国军就会赶到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在这之前女神会\n',
            '保佑大家的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_9A5(): pass

    label('loc_9A5')

    Jump('loc_AFB')

    def _loc_9A8(): pass

    label('loc_9A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_AFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_A2E',
    )

    ChrTalk(
        0x0008,
        (
            '多亏了超市，\n',
            '只要得到许可，谁都可以开一家\n',
            '在市场里的商店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，也难怪这些初出茅庐\n',
            '的商人们会聚集在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AFB')

    def _loc_A2E(): pass

    label('loc_A2E')

    ChrTalk(
        0x0008,
        (
            '作为商人之城的柏斯市，\n',
            '一直以来就对商业有所保护。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '位于市中心的超市\n',
            '可以说是其象征吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总之只要得到许可的话，\n',
            '就可以在里面开一家店铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，也难怪这些初出茅庐\n',
            '的商人们会聚集在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_AFB(): pass

    label('loc_AFB')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0xAFF
@scena.Code('func_04_AFF')
def func_04_AFF():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_C7D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BF4',
    )

    ChrTalk(
        0x00FE,
        (
            '超市已经完全恢复\n',
            '到以前的样子了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一靠近，\n',
            '就听到很有气势的叫卖声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必定是梅贝尔市长的视察\n',
            '把超市的能量都发挥出来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，这是理所当然的事情吧。\n',
            '本来计划要去教堂做礼拜的，\n',
            '却偏偏临时说有事要办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_C7A')

    def _loc_BF4(): pass

    label('loc_BF4')

    ChrTalk(
        0x00FE,
        (
            '而且还常在礼拜做到一半的时候跑掉，\n',
            '这种态度的确有点难以容忍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得身为市长，\n',
            '不可以在市民面前做出这种不虔诚的举止啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C7A(): pass

    label('loc_C7A')

    Jump('loc_FDA')

    def _loc_C7D(): pass

    label('loc_C7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_DE1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D6A',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到只是因为导力器无法使用\n',
            '就造成了这样的混乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为信奉女神的人来说\n',
            '真是件羞耻的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正是因为过于依赖导力器\n',
            '才会导致这种事情发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望人们可以通过这次女神给予的启示和教训，\n',
            '从中觉醒过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_DDE')

    def _loc_D6A(): pass

    label('loc_D6A')

    ChrTalk(
        0x00FE,
        (
            '正是因为过于依赖导力器\n',
            '才会导致这种事情发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望人们可以通过这次女神给予的启示和教训，\n',
            '从中觉醒过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DDE(): pass

    label('loc_DDE')

    Jump('loc_FDA')

    def _loc_DE1(): pass

    label('loc_DE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_F18',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E5C',
    )

    ChrTalk(
        0x00FE,
        (
            '今天起超市将恢复营业，\n',
            '这样一来柏斯也将恢复原貌了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '购物的乐趣\n',
            '只有在和平的时候才体会得到呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F15')

    def _loc_E5C(): pass

    label('loc_E5C')

    ChrTalk(
        0x00FE,
        (
            '今天起超市将恢复营业，\n',
            '这样一来柏斯也将恢复原貌了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来教堂做礼拜的人\n',
            '总感觉还是很少的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '购物的乐趣\n',
            '只有在和平的时候才体会得到呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天一天\n',
            '不打算计较了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_F15(): pass

    label('loc_F15')

    Jump('loc_FDA')

    def _loc_F18(): pass

    label('loc_F18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_FDA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_F79',
    )

    ChrTalk(
        0x00FE,
        (
            '有很多祈求生意兴隆的\n',
            '人来教堂礼拜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，面对创造女神\n',
            '就不觉得失礼吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FDA')

    def _loc_F79(): pass

    label('loc_F79')

    ChrTalk(
        0x00FE,
        (
            '在那边祈祷的几位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是来\n',
            '祈求生意兴隆的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为这种俗事祈祷，\n',
            '不觉得失礼吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_FDA(): pass

    label('loc_FDA')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0xFDE
@scena.Code('func_05_FDE')
def func_05_FDE():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_10DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1050',
    )

    ChrTalk(
        0x00FE,
        (
            '我是为商业洽谈的\n',
            '成功来祈祷的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '从刚才起修女就\n',
            '一直盯着这边看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是我干了什么坏事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10DF')

    def _loc_1050(): pass

    label('loc_1050')

    ChrTalk(
        0x00FE,
        (
            '我将要去超市\n',
            '开门营业。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '为了祈求商业洽谈成功，\n',
            '就来这里祈祷了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，从刚才起修女就\n',
            '一直盯着这里看……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '怎么回事？\n',
            '我并没做坏事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_10DF(): pass

    label('loc_10DF')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x10E3
@scena.Code('func_06_10E3')
def func_06_10E3():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_113F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1101',
    )

    ChrTalk(
        0x00FE,
        (
            '呜～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_113F')

    def _loc_1101(): pass

    label('loc_1101')

    ChrTalk(
        0x00FE,
        (
            '超市里\n',
            '一下子暗了下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '使我好害怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_113F(): pass

    label('loc_113F')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x1143
@scena.Code('func_07_1143')
def func_07_1143():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1200',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11C2',
    )

    ChrTalk(
        0x00FE,
        (
            '很久没有来\n',
            '向女神祈祷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为超市那边\n',
            '实在脱不开身……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在去买东西\n',
            '一点乐趣都没有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_11FD')

    def _loc_11C2(): pass

    label('loc_11C2')

    ChrTalk(
        0x00FE,
        (
            '很久没有来\n',
            '向女神祈祷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能把心静下来的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11FD(): pass

    label('loc_11FD')

    Jump('loc_12B7')

    def _loc_1200(): pass

    label('loc_1200')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_12B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_124E',
    )

    ChrTalk(
        0x00FE,
        (
            '袭击超市的好像是\n',
            '巨大的怪物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是件可怕的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B7')

    def _loc_124E(): pass

    label('loc_124E')

    ChrTalk(
        0x00FE,
        (
            '袭击超市的好像是\n',
            '巨大的怪物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且那头怪物现在\n',
            '还正在某处飞着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是件可怕的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_12B7(): pass

    label('loc_12B7')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x12BB
@scena.Code('func_08_12BB')
def func_08_12BB():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1307',
    )

    ChrTalk(
        0x00FE,
        (
            '超市被那么巨大的\n',
            '怪物袭击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，但愿\n',
            '那个女孩没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1307(): pass

    label('loc_1307')

    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0x130B
@scena.Code('func_09_130B')
def func_09_130B():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_142B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_137B',
    )

    ChrTalk(
        0x00FE,
        (
            '话虽如此……\n',
            '那到底是什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就好像是\n',
            '传说中的龙一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真不敢相信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_142B')

    def _loc_137B(): pass

    label('loc_137B')

    ChrTalk(
        0x00FE,
        (
            '那怪物是从东面飞过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '开始还只是隐约可见呢，\n',
            '但一下子就飞到超市上空了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后就刮起了强风。\n',
            '我都以为自己要被吹走了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，但愿市长\n',
            '的下属没事就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_142B(): pass

    label('loc_142B')

    TalkEnd(0x000E)

    Return()

# id: 0x000A offset: 0x142F
@scena.Code('func_0A_142F')
def func_0A_142F():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_14F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1487',
    )

    ChrTalk(
        0x00FE,
        (
            '我出来买东西，\n',
            '顺便就过来做祷告了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '祈祷莉拉能\n',
            '早日醒来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F5')

    def _loc_1487(): pass

    label('loc_1487')

    ChrTalk(
        0x00FE,
        (
            '我出来买东西，\n',
            '顺便就过来做祷告了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '祈祷莉拉能\n',
            '早日醒来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，希望女神能够\n',
            '倾听我的祈求……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_14F5(): pass

    label('loc_14F5')

    TalkEnd(0x000F)

    Return()

# id: 0x000B offset: 0x14F9
@scena.Code('func_0B_14F9')
def func_0B_14F9():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15E7',
    )

    ChrTalk(
        0x0010,
        (
            '#0370350346V#620F梅贝尔小姐\n',
            '正在视察超市。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370350347V也就是说\n',
            '这次祈祷她又偷懒了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370350348V因为现在这种情况，\n',
            '我就先不说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370350349V等城里所有的事情都安定下来之后，\n',
            '一定要让小姐老老实实地做祈祷才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_1642')

    def _loc_15E7(): pass

    label('loc_15E7')

    ChrTalk(
        0x0010,
        (
            '#0370350346V#620F梅贝尔小姐\n',
            '正在视察超市。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370350351V也就是说\n',
            '这次祈祷她又偷懒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1642(): pass

    label('loc_1642')

    TalkEnd(0x0010)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
