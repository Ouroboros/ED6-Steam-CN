import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1300.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T1300._SN', 'ED6_DT01/T1300_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFF5AC4,
            dword_04        = 0xFFFFFE0C,
            dword_08        = 0x00007148,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 225,
            word_32         = 180,
            word_34         = 270,
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵卡多尔斯',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '斯丁克',
            x                   = -42500,
            z                   = -50,
            y                   = 16500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '哈尔德',
            x                   = 99500,
            z                   = -50,
            y                   = 99500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '梅尔茨',
            x                   = -42500,
            z                   = -50,
            y                   = 16500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '照相机',
            x                   = -42500,
            z                   = -50,
            y                   = 16500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵阿萨',
            x                   = -48000,
            z                   = -50,
            y                   = -10000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '士兵迈奇',
            x                   = -47600,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '玛诺利亚海岸方向',
            x                   = -50220,
            z                   = -500,
            y                   = -35780,
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
            name                = '西柏斯街道方向',
            x                   = -40370,
            z                   = -500,
            y                   = 36990,
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

# id: 0x10002 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1EA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -51360,
            y           = -2000,
            z           = 11340,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000008,
        ),
    )

# id: 0x10004 offset: 0x20A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -51690,
            triggerZ            = -470,
            triggerY            = 23510,
            triggerRange        = 1500,
            actorX              = -51690,
            actorZ              = 1800,
            actorY              = 23510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -53780,
            triggerZ            = -510,
            triggerY            = -19530,
            triggerRange        = 1500,
            actorX              = -53780,
            actorZ              = 1900,
            actorY              = -19530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x252
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_26B',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)
    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_2B8')

    def _loc_26B(): pass

    label('loc_26B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_284',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)
    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_2B8')

    def _loc_284(): pass

    label('loc_284')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_293',
    )

    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_2B8')

    def _loc_293(): pass

    label('loc_293')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Return,
        ),
        'loc_2A2',
    )

    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_2B8')

    def _loc_2A2(): pass

    label('loc_2A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_2AC',
    )

    Jump('loc_2B8')

    def _loc_2AC(): pass

    label('loc_2AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2B8',
    )

    ChrClearFlags(0x0009, 0x0080)

    def _loc_2B8(): pass

    label('loc_2B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_30D',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_30D',
    )

    FormationDelMember(0x34, 0xFF)
    MapSetFlags(0x00400000)
    ChrClearFlags(0x000A, 0x0080)
    OP_6C(270000, 0)
    CameraSetDistance(3400, 0)
    CameraMove(-44000, 0, 24400, 0)
    Event(1, 0x0000)

    def _loc_30D(): pass

    label('loc_30D')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_319'),
        (-1, 'loc_335'),
    )

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 2, 0x402)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 0, 0x400)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_332',
    )

    OP_B1('t1300_y')
    Event(0, func_07_12DB)

    def _loc_332(): pass

    label('loc_332')

    Jump('loc_335')

    def _loc_335(): pass

    label('loc_335')

    Return()

# id: 0x0001 offset: 0x336
@scena.Code('func_01_336')
def func_01_336():
    OP_16(0x02, 4000, -178000, -125000, 196676)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 2, 0x402)),
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_360',
    )

    OP_B1('t1300_y')

    Jump('loc_369')

    def _loc_360(): pass

    label('loc_360')

    OP_B1('t1300_n')

    def _loc_369(): pass

    label('loc_369')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 2, 0x402)),
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_37A',
    )

    OP_1B(0x03, 0x00, 0x0009)

    def _loc_37A(): pass

    label('loc_37A')

    OP_71(0x0000, 0x0010)
    OP_1C(0x00, 0x00, 0x000C)
    OP_1C(0x01, 0x00, 0x000C)

    Return()

# id: 0x0002 offset: 0x38A
@scena.Code('func_02_38A')
def func_02_38A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_39F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_38A')

    def _loc_39F(): pass

    label('loc_39F')

    Return()

# id: 0x0003 offset: 0x3A0
@scena.Code('func_03_3A0')
def func_03_3A0():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_3E8',
    )

    ChrTalk(
        0x00FE,
        (
            '离值勤还有段时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是先\n',
            '稍微小睡一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EA')

    def _loc_3E8(): pass

    label('loc_3E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_4DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '这里是深山老林，\n',
            '食物的供应非常不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然也有很多东西\n',
            '从柏斯和卢安那里运送过来，\n',
            '不过毕竟是山路啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经常需要去迎接送货的人，\n',
            '并且给他们顺便但当护卫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D8')

    def _loc_4A5(): pass

    label('loc_4A5')

    ChrTalk(
        0x00FE,
        (
            '这里一到冬天，\n',
            '大雪就会堆积起来，特别不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D8(): pass

    label('loc_4D8')

    Jump('loc_8EA')

    def _loc_4DB(): pass

    label('loc_4DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_532',
    )

    ChrTalk(
        0x00FE,
        (
            '差不多到训练的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为发生过魔兽袭击事件，\n',
            '大家要提高警惕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EA')

    def _loc_532(): pass

    label('loc_532')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_5E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '早上好，昨天谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然看上去挺年轻，\n',
            '但真不愧是游击士呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干得真棒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E3')

    def _loc_5A2(): pass

    label('loc_5A2')

    ChrTalk(
        0x00FE,
        (
            '虽然看上去挺年轻，\n',
            '但真不愧是游击士呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天干得真棒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E3(): pass

    label('loc_5E3')

    Jump('loc_8EA')

    def _loc_5E6(): pass

    label('loc_5E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_689',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_653',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '有什么事吗？\n',
            '你们可以随便进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要使用休息室的话，\n',
            '和我们队长打声招呼就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_686')

    def _loc_653(): pass

    label('loc_653')

    ChrTalk(
        0x00FE,
        (
            '要使用休息室的话，\n',
            '和我们队长打声招呼就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_686(): pass

    label('loc_686')

    Jump('loc_8EA')

    def _loc_689(): pass

    label('loc_689')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_79B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_748',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '好像还是找不到\n',
            '空贼团的所在之处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '国境守备队的那伙人\n',
            '也经常到这里来进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯这个地方\n',
            '就是山岳比较多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '犯人要是隐藏在这里，\n',
            '可是最难发现的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_798')

    def _loc_748(): pass

    label('loc_748')

    ChrTalk(
        0x00FE,
        (
            '柏斯这个地方\n',
            '就是山岳比较多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '犯人要是隐藏在这里，\n',
            '可是最难发现的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_798(): pass

    label('loc_798')

    Jump('loc_8EA')

    def _loc_79B(): pass

    label('loc_79B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_804',
    )

    ChrTalk(
        0x00FE,
        (
            '消失的定期船\n',
            '好像被找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为犯人还没有被抓住，\n',
            '所以关所还要继续\n',
            '维持盘查的制度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EA')

    def _loc_804(): pass

    label('loc_804')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_88C',
    )

    ChrTalk(
        0x00FE,
        (
            '是空贼团吗……\n',
            '真是一群不容易对付的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，这次是由那位\n',
            '摩尔根将军亲临指挥呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定马上就会抓到他们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EA')

    def _loc_88C(): pass

    label('loc_88C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_8EA',
    )

    ChrTalk(
        0x00FE,
        (
            '要去卢安吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是的话，\n',
            '必须要先办通行手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为现在正处于戒严状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8EA(): pass

    label('loc_8EA')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x8EE
@scena.Code('func_04_8EE')
def func_04_8EE():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B8C',
    )

    SetScenaFlags(ScenaFlag(0x006B, 7, 0x35F))

    ChrTalk(
        0x0101,
        (
            '#006F（咦……\n',
            '　这个人莫非是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯，\n',
            '　好像和我们一样都是游击士呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F喂，打扰一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F你还是那样不讨人喜欢呢，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '你是……\n',
            '以前的那个见习游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F没错呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '托你的福，\n',
            '现在我已经是正游击士啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……看起来的确成熟了不少。\n',
            '在柏斯支部有工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，现在就正在工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近发生了很多事情，\n',
            '游击士的人手远远不够呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那就靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 90, 0)

    ChrTalk(
        0x0101,
        (
            '#002F（是雪拉姐的熟人吧。\n',
            '　感觉有点恐怖的人呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（但是那走路的动作……\n',
            '　看起来应该很厉害吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C48')

    def _loc_B8C(): pass

    label('loc_B8C')

    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x0103,
        (
            '#020F斯丁克，\n',
            '这附近是不是出什么事情了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是雪拉扎德啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我接到通报说在这一带\n',
            '有人看到了没见过的魔兽，\n',
            '所以前来调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F辛苦你了。\n',
            '我们彼此加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 90, 0)

    def _loc_C48(): pass

    label('loc_C48')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0xC4C
@scena.Code('func_05_C4C')
def func_05_C4C():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_C86',
    )

    ChrTalk(
        0x00FE,
        (
            '堡垒的人最近\n',
            '总是谈论市长被捕这个话题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1105')

    def _loc_C86(): pass

    label('loc_C86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_D53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D08',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '今天该轮到\n',
            '我来炒菜做饭了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过刚才副长来，\n',
            '说要代替我做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人，\n',
            '真的非常喜欢烹饪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D50')

    def _loc_D08(): pass

    label('loc_D08')

    ChrTalk(
        0x00FE,
        (
            '刚才副长来了，\n',
            '说要代替我做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人，\n',
            '真的非常喜欢烹饪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D50(): pass

    label('loc_D50')

    Jump('loc_1105')

    def _loc_D53(): pass

    label('loc_D53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_DFA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DC8',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '自从空贼被逮捕以来，\n',
            '柏斯地区就非常和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，要是接连不断发生事件\n',
            '那真是很难办啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF7')

    def _loc_DC8(): pass

    label('loc_DC8')

    ChrTalk(
        0x00FE,
        (
            '自从空贼被逮捕以来，\n',
            '柏斯地区就非常和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DF7(): pass

    label('loc_DF7')

    Jump('loc_1105')

    def _loc_DFA(): pass

    label('loc_DFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_E4C',
    )

    ChrTalk(
        0x00FE,
        (
            '之前来的魔兽\n',
            '比想象中的要厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也必须\n',
            '加紧训练才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1105')

    def _loc_E4C(): pass

    label('loc_E4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_E9A',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天的袭击\n',
            '真是个很好的教训。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来平时\n',
            '就要做好充分准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1105')

    def _loc_E9A(): pass

    label('loc_E9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_EFB',
    )

    ChrTalk(
        0x00FE,
        (
            '搜索这样持续下去，\n',
            '国境师团的家伙们也相当累吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有什么新的进展就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1105')

    def _loc_EFB(): pass

    label('loc_EFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_F6B',
    )

    ChrTalk(
        0x00FE,
        (
            '这一带\n',
            '越往山中走魔兽越多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且被通缉的魔兽\n',
            '也越来越多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每天的训练是必不可少的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1105')

    def _loc_F6B(): pass

    label('loc_F6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1018',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FDD',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '这座古罗尼连峰的地形\n',
            '也是起伏频繁的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难不成……\n',
            '空贼团那些家伙们\n',
            '都隐藏在这一带？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1015')

    def _loc_FDD(): pass

    label('loc_FDD')

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '国境师团的搜查队\n',
            '已经在这里调查好几次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1015(): pass

    label('loc_1015')

    Jump('loc_1105')

    def _loc_1018(): pass

    label('loc_1018')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1105',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10AB',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '这么险峻的山道，\n',
            '一般来说旅行的人\n',
            '是根本不会走的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为现在飞艇还在停航，\n',
            '急着去卢安和柏斯的人们\n',
            '不得不从这里通过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1105')

    def _loc_10AB(): pass

    label('loc_10AB')

    ChrTalk(
        0x00FE,
        (
            '但是不管怎么说，\n',
            '还是应该尽量避免\n',
            '在晚上翻越这座山峰啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对一般人来说太危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1105(): pass

    label('loc_1105')

    TalkEnd(0x000D)

    Return()

# id: 0x0006 offset: 0x1109
@scena.Code('func_06_1109')
def func_06_1109():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_114B',
    )

    ChrTalk(
        0x00FE,
        (
            '听说卢安的市长\n',
            '被逮捕了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然有这种事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D7')

    def _loc_114B(): pass

    label('loc_114B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_11AD',
    )

    ChrTalk(
        0x00FE,
        (
            '被魔兽打伤的地方\n',
            '终于痊愈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要尽量避免以后再发生这类事情，\n',
            '所以要加紧训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D7')

    def _loc_11AD(): pass

    label('loc_11AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1204',
    )

    ChrTalk(
        0x00FE,
        (
            '副长还真是喜欢烹饪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时候明明不是他当班，\n',
            '但是他却在厨房做饭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D7')

    def _loc_1204(): pass

    label('loc_1204')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_1257',
    )

    ChrTalk(
        0x00FE,
        (
            '柴火差不多要用完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '训练结束后去报告一下，\n',
            '然后就去砍些柴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D7')

    def _loc_1257(): pass

    label('loc_1257')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_129C',
    )

    ChrTalk(
        0x00FE,
        (
            '痛痛痛痛痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是失策。\n',
            '被魔兽打伤的地方好痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D7')

    def _loc_129C(): pass

    label('loc_129C')

    ChrTalk(
        0x00FE,
        (
            '一会儿就轮到我值班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '趁现在赶快吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12D7(): pass

    label('loc_12D7')

    TalkEnd(0x000E)

    Return()

# id: 0x0007 offset: 0x12DB
@scena.Code('func_07_12DB')
def func_07_12DB():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetPos(0x0101, -43430, -550, 25300, 225)
    ChrSetPos(0x0102, -43600, -600, 26890, 225)
    CameraMove(-46560, -50, -15120, 0)
    OP_67(0, 5210, -10000, 0)
    CameraSetDistance(5140, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    CameraMove(-48090, -50, 16940, 8000)
    Fade(500)
    CameraMove(-44280, -480, 24940, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 3, 0x36B)),
            Expr.Return,
        ),
        'loc_1492',
    )

    ChrTalk(
        0x0101,
        (
            '#0010040107V#501F#1P呼～～总算到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040108V只要过了这个关所，\n',
            '就可以进入卢安地区了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040109V#010F嗯，应该是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040110V#013F不过不好办啊……太阳快要下山了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040111V今天我们还是\n',
            '在这里借宿一晚吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1574')

    def _loc_1492(): pass

    label('loc_1492')

    ChrTalk(
        0x0101,
        (
            '#0010040095V#501F#1P呼～～总算到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040096V那就是关所吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040097V#010F好像是。\n',
            '只要过了这里就是卢安地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040098V#013F不过不好办啊……太阳快要下山了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040099V今天我们还是\n',
            '在这里借宿一晚吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1574(): pass

    label('loc_1574')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040100V#000F#1P我倒没意见……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040101V不过，我们赶路下山，\n',
            '然后找家旅馆落脚不也行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040102V#015F晚上下山很危险的。\n',
            '光线暗，走起路来也很麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040103V要是被夜行性的魔兽袭击的话，\n',
            '可能会从山崖上掉下去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040104V#010F所以还是不要这样比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040105V#007F#1P呜啊啊～听起来真的好危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040106V总之还是先问问\n',
            '关所的士兵能不能借宿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    MapSetFlags(0x00000001)
    Fade(1000)
    CameraMove(-43600, -554, 24000, 0)
    ChrSetPos(0x0000, -43600, -550, 26890, 180)
    ChrSetPos(0x0001, -43600, -550, 26890, 180)
    OP_0D()
    EventEnd(0x02)
    SetScenaFlags(ScenaFlag(0x0080, 2, 0x402))
    OP_1B(0x03, 0x00, 0x0009)

    Return()

# id: 0x0008 offset: 0x176C
@scena.Code('func_08_176C')
def func_08_176C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 3, 0x403)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 0, 0x400)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C30',
    )

    SetScenaFlags(ScenaFlag(0x0080, 3, 0x403))
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x0008, 0)
    ChrTurnDirection(0x0001, 0x0008, 0)
    OP_4A(0x0008, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000C, 1000)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#1420040112V哟，真少见。\n',
            '这么晚了还有客人来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040113V客人是来郊游的吧。\n',
            '难道你们迷了路？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040114V#000F呵呵，不是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040115V我们两个可是\n',
            '从洛连特来的游击士哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔向士兵出示准游击士的徽章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#1420040116V哎～这种年纪就当了游击士，\n',
            '真让人吃惊呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040117V那么你们是来工作的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040118V#010F也不是，其实我们是为了成为\n',
            '正游击士而打算到王国各地旅行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040119V#006F因此我们没乘坐定期船，\n',
            '一边修行一边走路过来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040120V绕着王国走一圈啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040121V哈哈～真不知该说你们太年轻呢，\n',
            '还是该称赞你们很有干劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040122V#006F嘿嘿～～这没什么啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040123V不过不管怎么说，\n',
            '现在下山是非常危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040124V而且最近这附近\n',
            '又发生过魔兽暴动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040125V关所里有旅行者专用的休息室，\n',
            '你们今晚还是在这里过夜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040126V#001F太好了，谢谢你啦☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040127V#010F真是帮了我们的大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040128V小意思小意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040129V要使用休息室的话，\n',
            '和我们队长打声招呼就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040130V他就在里面的值勤室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x01)

    def _loc_1C30(): pass

    label('loc_1C30')

    Return()

# id: 0x0009 offset: 0x1C31
@scena.Code('func_09_1C31')
def func_09_1C31():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D30',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 4, 0x404)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CEB',
    )

    ChrTalk(
        0x0102,
        (
            '#0020040131V#010F天色已经晚了，\n',
            '街道上会很危险的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040132V向关所的士兵说明情况，\n',
            '今天就在这里过夜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040133V#000F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D2D')

    def _loc_1CEB(): pass

    label('loc_1CEB')

    ChrTalk(
        0x0102,
        (
            '#0020040134V#010F天色已经晚了，\n',
            '今天就在关所的休息室过夜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D2D(): pass

    label('loc_1D2D')

    Jump('loc_1DF5')

    def _loc_1D30(): pass

    label('loc_1D30')

    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 4, 0x404)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DB3',
    )

    ChrTalk(
        0x0102,
        (
            '#0020040135V#010F天色已经晚了，\n',
            '街道上会很危险的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040136V向关所的士兵说明情况，\n',
            '今天就在这里过夜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF5')

    def _loc_1DB3(): pass

    label('loc_1DB3')

    ChrTalk(
        0x0102,
        (
            '#0020040137V#010F天色已经晚了，\n',
            '今天就在关所的休息室过夜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DF5(): pass

    label('loc_1DF5')

    Fade(1000)
    ChrSetPos(0x0000, -43600, -550, 26890, 180)
    ChrSetPos(0x0001, -43600, -550, 26890, 180)
    OP_0D()
    EventEnd(0x02)

    Return()

# id: 0x000A offset: 0x1E20
@scena.Code('func_0A_1E20')
def func_0A_1E20():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东北　柏斯市　　　４４１塞尔矩\n',
            '西南　卢安市　　　６６９塞尔矩\n',
            '　　　玛诺利亚村　３５７塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x1EAF
@scena.Code('func_0B_1EAF')
def func_0B_1EAF():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西南　卢安市　　　６６９塞尔矩\n',
            '　　　玛诺利亚村　３５７塞尔矩\n',
            '东北　柏斯市　　　４４１塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x1F3E
@scena.Code('func_0C_1F3E')
def func_0C_1F3E():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
