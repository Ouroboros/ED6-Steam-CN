import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0700_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0700   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '斯库拉特'),
    TXT(0x02, '法布利'),
    TXT(0x03, '雪拉扎德'),
    TXT(0x04, '卡西乌斯'),
    TXT(0x05, '阿兰'),
    TXT(0x06, '奥维德'),
    TXT(0x07, '目标用摄像机'),
    TXT(0x08, '洛连特市街道'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0700.x'
    header.mapIndex       = 9
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5587
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x000088B8,
            dword_04        = 0x00000000,
            dword_08        = 0x00003E80,
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
            word_3A         = 9,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x000088B8,
            dword_04        = 0x00000000,
            dword_08        = 0x00003E80,
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
            word_3A         = 9,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
    ]

# id: 0x10002 offset: 0x116
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 45064,
            z                   = 4200,
            y                   = 30855,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 31837,
            z                   = 0,
            y                   = 51534,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 43018,
            z                   = 4000,
            y                   = 33475,
            direction           = 205,
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
            x                   = 42909,
            z                   = 4000,
            y                   = 30908,
            direction           = 282,
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
            x                   = 36095,
            z                   = 0,
            y                   = 35619,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 38020,
            z                   = 0,
            y                   = 28750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 35320,
            z                   = 0,
            y                   = -13920,
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

# id: 0x10003 offset: 0x216
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x216
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x216
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 38000,
            triggerZ            = 0,
            triggerY            = 30000,
            triggerRange        = 800,
            actorX              = 38000,
            actorZ              = 2200,
            actorY              = 30000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 40000,
            triggerZ            = 4000,
            triggerY            = 41300,
            triggerRange        = 800,
            actorX              = 40000,
            actorZ              = 5500,
            actorY              = 41800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 34500,
            triggerZ            = 0,
            triggerY            = 46570,
            triggerRange        = 800,
            actorX              = 35000,
            actorZ              = 1500,
            actorY              = 46570,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 36142,
            triggerZ            = 0,
            triggerY            = 34342,
            triggerRange        = 1000,
            actorX              = 36095,
            actorZ              = 1500,
            actorY              = 35619,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2A6
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_2B2'),
        (-1, 'loc_354'),
    )

    def _loc_2B2(): pass

    label('loc_2B2')

    ClearMapFlags(0x00000001)
    OP_B1('t0700_0')
    CameraMove(55210, -3070, 40180, 0)
    CameraSetDistance(5870, 0)
    OP_6C(201000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x0101, 41736, 4000, 31654, 118)
    SetChrPos(0x0102, 41716, 4000, 32539, 129)
    SetChrPos(0x000A, 43018, 4000, 33475, 205)
    SetChrPos(0x000B, 42909, 4000, 30908, 282)
    ClearMapFlags(0x00000010)
    FadeIn(2000, 0)
    Event(0, 0x000B)

    Jump('loc_354')

    def _loc_354(): pass

    label('loc_354')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_36B',
    )

    SetChrFlags(0x000D, 0x0080)

    Jump('loc_38F')

    def _loc_36B(): pass

    label('loc_36B')

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_37D',
    )

    SetChrFlags(0x000D, 0x0010)

    Jump('loc_38F')

    def _loc_37D(): pass

    label('loc_37D')

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_38F',
    )

    ClearChrFlags(0x000D, 0x0010)

    Jump('loc_38F')

    def _loc_38F(): pass

    label('loc_38F')

    Return()

# id: 0x0001 offset: 0x390
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B7',
    )

    OP_B1('t0700_1')
    OP_72(0x000B, 0x0004)
    OP_72(0x000C, 0x0004)
    OP_72(0x000D, 0x0004)

    Jump('loc_3F6')

    def _loc_3B7(): pass

    label('loc_3B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3DE',
    )

    OP_B1('t0700_y')
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)

    Jump('loc_3F6')

    def _loc_3DE(): pass

    label('loc_3DE')

    OP_B1('t0700_0')
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)

    def _loc_3F6(): pass

    label('loc_3F6')

    OP_16(0x02, 4000, -92000, -97000, 196615)
    OP_71(0x000E, 0x0004)
    OP_71(0x000E, 0x0002)
    OP_72(0x000E, 0x0400)
    OP_72(0x000E, 0x0040)

    Return()

# id: 0x0002 offset: 0x41D
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_432',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_432(): pass

    label('loc_432')

    Return()

# id: 0x0003 offset: 0x433
@scena.Code('func_03_433')
def func_03_433():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_456',
    )

    OP_8D(0x00FE, 29021, 54795, 33637, 48557, 4000)

    Jump('func_03_433')

    def _loc_456(): pass

    label('loc_456')

    Return()

# id: 0x0004 offset: 0x457
@scena.Code('func_04_457')
def func_04_457():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船起降坪\n',
            '≡　开往王都格兰赛尔\n',
            '≡　开往柏斯市',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　　利贝尔飞艇公社',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0005 offset: 0x4F1
@scena.Code('func_05_4F1')
def func_05_4F1():
    ChrTalk(
        0x0102,
        (
            '#0020011193V#010F这里是控制塔的入口呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011194V#010F照明装置和搭乘用的船桥\n',
            '都是由这里来控制的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x556
@scena.Code('func_06_556')
def func_06_556():
    ChrTalk(
        0x0102,
        (
            '#0020011195V#010F这里面好像\n',
            '不许无关人员进入呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011196V#509F越是说不许进入，\n',
            '我就越是想进去看看～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x5C2
@scena.Code('func_07_5C2')
def func_07_5C2():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_643',
    )

    ChrTalk(
        0x00FE,
        (
            '听说从柏斯出发的定期船\n',
            '突然失去了行踪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公社还没有收到来自定期船的联络，\n',
            '真是担心是不是发生了什么意外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF6')

    def _loc_643(): pass

    label('loc_643')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_6F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6BB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '好慢啊……\n',
            '怎么了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从柏斯起飞的定期船\n',
            '到现在还没到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我这边的准备\n',
            '都已经做好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F4')

    def _loc_6BB(): pass

    label('loc_6BB')

    ChrTalk(
        0x0008,
        (
            '好慢啊……\n',
            '怎么了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不会是发生事故了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F4(): pass

    label('loc_6F4')

    Jump('loc_EF6')

    def _loc_6F7(): pass

    label('loc_6F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_83A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7C8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '你们知道王家的专用高速巡洋舰\n',
            '『埃尔赛尤号』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是艘拥有纯白流线型的高级飞艇，\n',
            '无论是外形还是气质都极具王家气派。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '而且它还凝聚了\n',
            '导力技术的精华，\n',
            '号称拥有世界第一的性能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_837')

    def _loc_7C8(): pass

    label('loc_7C8')

    ChrTalk(
        0x0008,
        (
            '你们知道王家的专用高速巡洋舰\n',
            '『埃尔赛尤号』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '它凝聚了\n',
            '导力技术的精华，\n',
            '号称拥有世界第一的性能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_837(): pass

    label('loc_837')

    Jump('loc_EF6')

    def _loc_83A(): pass

    label('loc_83A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_96F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_92D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '这一艘是西向航线的\n',
            '定期船『赛希莉亚号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '马上就要起飞\n',
            '开往柏斯地区了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '目前国内还没有\n',
            '发生过什么严重的\n',
            '定期船事故呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因为飞艇公社\n',
            '在安全上花了很多的功夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从来不发生事故\n',
            '也是我们维修员的骄傲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_96C')

    def _loc_92D(): pass

    label('loc_92D')

    ChrTalk(
        0x0008,
        (
            '好，\n',
            '导力引擎和机体的检查完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '随时都能起飞了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_96C(): pass

    label('loc_96C')

    Jump('loc_EF6')

    def _loc_96F(): pass

    label('loc_96F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_A8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A20',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '每一艘飞艇上\n',
            '都配备有一台\n',
            '相当强力的导力引擎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '听说引擎开发的费用\n',
            '非常的昂贵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过，正因为有了王家的出资，\n',
            '定期船才能够这么广泛投入实用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A88')

    def _loc_A20(): pass

    label('loc_A20')

    ChrTalk(
        0x0008,
        (
            '听说引擎开发的费用\n',
            '非常的昂贵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过，正因为有了王家的出资，\n',
            '定期船才能够这么广泛投入实用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A88(): pass

    label('loc_A88')

    Jump('loc_EF6')

    def _loc_A8B(): pass

    label('loc_A8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_ADE',
    )

    ChrTalk(
        0x0008,
        (
            '呼，终于忙完一阵了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今天风和日丽，\n',
            '遨游蓝天一定是心旷神怡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF6')

    def _loc_ADE(): pass

    label('loc_ADE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_CF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C7F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '说起来我们王国的五大都市\n',
            '都有各自的魅力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '首先，我们这里就是\n',
            '风光明媚的地方都市洛连特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在我们西边的是\n',
            '和帝国贸易往来十分频繁的\n',
            '商业都市柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '再往西的就是\n',
            '利贝尔的外洋窗口，\n',
            '美丽的海港都市卢安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '而王国的南部就是\n',
            '以导力器研究而闻名的\n',
            '工房都市蔡斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '而在瓦雷利亚湖东岸的就是\n',
            '华丽宏伟的王都格兰赛尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '每一个城市都很有地方特色，\n',
            '乘坐定期船到各地旅游也非常有趣哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF4')

    def _loc_C7F(): pass

    label('loc_C7F')

    ChrTalk(
        0x0008,
        (
            '王国的五大都市\n',
            '每一个都很有地方特色，\n',
            '坐着定期船环游各地是非常有趣的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '有机会一定要\n',
            '乘坐飞艇去四处旅行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CF4(): pass

    label('loc_CF4')

    Jump('loc_EF6')

    def _loc_CF7(): pass

    label('loc_CF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_E74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DF0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '在五大都市之间\n',
            '往返的定期船分为\n',
            '东向航线和西向航线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '西向航线是从格兰赛尔起飞，\n',
            '途中经过洛连特、柏斯、卢安，\n',
            '最后到蔡斯的顺序……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '而东向航线就刚刚相反了，\n',
            '从格兰赛尔起飞后，途径蔡斯、\n',
            '卢安、柏斯，最后达到洛连特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E71')

    def _loc_DF0(): pass

    label('loc_DF0')

    ChrTalk(
        0x0008,
        (
            '而且不相邻的地区之间\n',
            '是没有直航飞行的航线的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '除了王国军和王家专用的飞艇，\n',
            '也只有非法航行的飞艇\n',
            '才会这样偏离航线飞行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E71(): pass

    label('loc_E71')

    Jump('loc_EF6')

    def _loc_E74(): pass

    label('loc_E74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EC9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '从格兰赛尔来的定期船\n',
            '很快就要到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '必须准备进行着陆导航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF6')

    def _loc_EC9(): pass

    label('loc_EC9')

    ChrTalk(
        0x0008,
        (
            '到了下午，\n',
            '从柏斯来的航班也会抵达这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EF6(): pass

    label('loc_EF6')

    TalkEnd(0x0008)

    Return()

# id: 0x0008 offset: 0xEFA
@scena.Code('func_08_EFA')
def func_08_EFA():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_F67',
    )

    ChrTalk(
        0x00FE,
        (
            '公社的定期船突然失踪，\n',
            '这可是前所未闻的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望乘客和定期船\n',
            '都平安无事就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1497')

    def _loc_F67(): pass

    label('loc_F67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_FAA',
    )

    ChrTalk(
        0x0009,
        (
            '……怎么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '迟到这么久，\n',
            '肯定是出什么事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1497')

    def _loc_FAA(): pass

    label('loc_FAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_10F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1091',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0009,
        (
            '自从飞艇发明以来，\n',
            '洛连特也出现了许多\n',
            '各种各样的来访者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '过去基本就只有\n',
            '来收购七耀石、\n',
            '木材和野菜的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '今时今日徒步旅行的人\n',
            '也相应减少了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为坐飞艇比较舒服，\n',
            '而且更重要的是速度快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10EF')

    def _loc_1091(): pass

    label('loc_1091')

    ChrTalk(
        0x0009,
        (
            '今时今日徒步旅行的人\n',
            '也相应减少了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为坐飞艇比较舒服，\n',
            '而且更重要的是速度快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10EF(): pass

    label('loc_10EF')

    Jump('loc_1497')

    def _loc_10F2(): pass

    label('loc_10F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_11E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1195',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0009,
        (
            '有没有哪种味道是\n',
            '别人没什么感觉\n',
            '但你自己却十分喜欢的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我很喜欢\n',
            '引擎发动时独特的焦糊味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '还有飞艇跑道\n',
            '被雨水打湿时的味道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E5')

    def _loc_1195(): pass

    label('loc_1195')

    ChrTalk(
        0x0009,
        (
            '我很喜欢\n',
            '引擎发动时独特的焦糊味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '还有飞艇跑道\n',
            '被雨水打湿时的味道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11E5(): pass

    label('loc_11E5')

    Jump('loc_1497')

    def _loc_11E8(): pass

    label('loc_11E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_125A',
    )

    ChrTalk(
        0x0009,
        (
            '从这里运出去的货物\n',
            '果然还是七耀石最多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '自从导力器产业迅速发展以来，\n',
            '矿山好像就一直很景气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1497')

    def _loc_125A(): pass

    label('loc_125A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_12CA',
    )

    ChrTalk(
        0x0009,
        (
            '刚才飞走的那班定期船\n',
            '是卡西乌斯先生乘的那艘吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '又是上哪里出差去了吧。\n',
            '他可真是大忙人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1497')

    def _loc_12CA(): pass

    label('loc_12CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1361',
    )

    ChrTalk(
        0x0009,
        (
            '今天的飞艇航运终于结束了，\n',
            '为了让明天的航运继续正常运作，\n',
            '安全检查一定要做到准确无误才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '『有备无患』，\n',
            '这是我的行为准则之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1497')

    def _loc_1361(): pass

    label('loc_1361')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_141B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13C8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0009,
        (
            '对于我这份工作，\n',
            '我感到很自豪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '原本我就想做\n',
            '调整导力引擎这样的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1418')

    def _loc_13C8(): pass

    label('loc_13C8')

    ChrTalk(
        0x0009,
        (
            '虽然我现在还是个维修员，\n',
            '但是我的梦想是将来\n',
            '成为一名设计飞艇的技术人员哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1418(): pass

    label('loc_1418')

    Jump('loc_1497')

    def _loc_141B(): pass

    label('loc_141B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1462',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0009,
        (
            '哼哼，\n',
            '今天果然睡过头了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '昨天喝得太多了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1497')

    def _loc_1462(): pass

    label('loc_1462')

    ChrTalk(
        0x0009,
        (
            '糟糕，\n',
            '要快点开始检点货物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '打起精神来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1497(): pass

    label('loc_1497')

    TalkEnd(0x0009)

    Return()

# id: 0x0009 offset: 0x149B
@scena.Code('func_09_149B')
def func_09_149B():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x14A0
@scena.Code('func_0A_14A0')
def func_0A_14A0():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_15E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1584',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '王国军正在搜索\n',
            '行踪不明的定期船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '而且，根据公社的消息，\n',
            '暂时还没有找到定期船的下落。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '发生什么事情了……\n',
            '看来今天没有欣赏女孩子的份了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '拜托了，王国军。\n',
            '我可是付了税金给你们做事的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E4')

    def _loc_1584(): pass

    label('loc_1584')

    ChrTalk(
        0x000C,
        (
            '王国军正在搜索\n',
            '行踪不明的定期船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '而且，根据公社的消息，\n',
            '暂时还没有找到定期船的下落。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15E4(): pass

    label('loc_15E4')

    Jump('loc_2B05')

    def _loc_15E7(): pass

    label('loc_15E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 2, 0x262)),
            Expr.Return,
        ),
        'loc_1FBE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 3, 0x263)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F33',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(35650, 0, 32590, 0)
    OP_67(0, 7490, -10000, 0)
    CameraSetDistance(3120, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrPos(0x0101, 35850, 0, 33370, 0)
    SetChrPos(0x0102, 36660, 0, 32180, 0)
    SetChrPos(0x0103, 35060, 0, 31950, 0)
    ChrTurnDirection(0x000C, 0x0101, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#1030011153V真、真是对不起！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011154V定期船很快就会到的，\n',
            '麻烦您再稍等片刻吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011155V#004F#4P阿兰哥哥，是我们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011156V怎么，是艾丝蒂尔你们啊。\n',
            '哟，雪拉扎德小姐也在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011157V到底怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011158V#012F#4P你有没有看到过\n',
            '一位穿校服的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011159V穿校服的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011160V是哪所学校的校服呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011161V#002F#4P杰尼丝王立学院的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011162V啊啊！\n',
            '王立学院的校服真的很可爱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011163V清纯可爱的白色短裙，\n',
            '和蓝色的长筒袜形成鲜明的对比。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011164V嗯～真是太迷人了。\n',
            '不过，男生的校服我可不记得哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011165V#007F#4P我、我们问的不是这些啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011166V#027F这就是男人的天性啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011167V#027F听你的意思就是没见到\n',
            '有王立学院的女生来过吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011168V没有，\n',
            '这一个月来都没见到过呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011169V我一直在检查乘客的出入情况，\n',
            '至少可以肯定的是没来过飞艇坪这边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011170V#022F也就是说，那女孩没有乘坐飞艇，\n',
            '而是沿着大道走到洛连特来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011171V#022F呼，这下可麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020011172V#012F搜索范围一下子变大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011173V#012F仔细想想的话，她也许有同伙，\n',
            '而且可能潜伏在这附近什么地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1200)

    SetChrDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010011174V#004F啊，对了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011175V#023F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【拿出塞尔贝树叶】\n'),
            TXT(0x01, '【………………是什么呢？】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C12',
    )

    SetMessageWindowPos(72, 320, 56, 3)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔拿出在阁楼里发现的塞尔贝树叶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010011176V#006F我都忘了捡到这个了。\n',
            '说不定这是我们的线索呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D8D')

    def _loc_1C12(): pass

    label('loc_1C12')

    ChrTalk(
        0x0101,
        (
            '#0010011177V#008F………………是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020011178V#018F我说……\n',
            '艾丝蒂尔，你也认真一点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011179V#022F难道刚才\n',
            '在市长官邸里发现了什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011180V#001F啊，对对，就是那个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔拿出在阁楼里发现的塞尔贝树叶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010011181V#006F我都忘了捡到这个了。\n',
            '说不定这是我们的线索呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D8D(): pass

    label('loc_1D8D')

    ChrTalk(
        0x0102,
        (
            '#0020011182V#010F对啊……还有这个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011183V#010F雪拉姐姐，\n',
            '知道这附近哪里会有塞尔贝树吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011184V#026F塞尔贝树啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011185V#020F我记得是生长在\n',
            '洛连特南部的神秘森林里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011186V#010F神秘森林……\n',
            '那地方是在我们家正南方向吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011187V#006F嗯，看来我们有必要去一趟了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011188V#006F既然决定了，\n',
            '我们就赶快从南门出城吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1030011189V真有干劲呢。\n',
            '虽然不知道怎么回事，不过多加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x004C, 3, 0x263))
    OP_28(0x001B, 0x01, 0x0010)
    OP_28(0x001B, 0x01, 0x0020)
    OP_28(0x001B, 0x01, 0x0040)
    EventEnd(0x00)

    Jump('loc_1FBB')

    def _loc_1F33(): pass

    label('loc_1F33')

    ChrTalk(
        0x000C,
        (
            '杰尼丝王立学院吗……\n',
            '王立学院的校服真的很可爱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '清纯可爱的白色短裙，\n',
            '和蓝色的长筒袜形成鲜明的对比。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯～真是太迷人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1FBB(): pass

    label('loc_1FBB')

    Jump('loc_2B05')

    def _loc_1FBE(): pass

    label('loc_1FBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_20DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2085',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '从柏斯起飞的定期船\n',
            '到现在还没来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '就因为这个， \n',
            '让我不能欣赏女孩子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊啊，那可是我唯一的乐趣……\n',
            '真是闷得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F真是的，这个人啊……\n',
            '还是老样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D8')

    def _loc_2085(): pass

    label('loc_2085')

    ChrTalk(
        0x000C,
        (
            '从柏斯起飞的\n',
            '定期船到现在还没来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '就因为这个， \n',
            '让我不能欣赏女孩子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20D8(): pass

    label('loc_20D8')

    Jump('loc_2B05')

    def _loc_20DB(): pass

    label('loc_20DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_229D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2231',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '听说最近柏斯地区\n',
            '有一伙驾驶飞艇进行抢劫的空贼\n',
            '在到处作案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '对乘客的安检\n',
            '必须要再严格些才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '要是有罪犯混进来，\n',
            '那可就糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F咦，难得听到阿兰哥哥\n',
            '说这么正经的话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '因为要是女孩们遇到危险的话\n',
            '我会很伤心的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '而且顺便也能给可爱的女孩作安检，\n',
            '一石二鸟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F……真是白夸他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_229A')

    def _loc_2231(): pass

    label('loc_2231')

    ChrTalk(
        0x000C,
        (
            '听说最近柏斯地区\n',
            '有一伙驾驶飞艇进行抢劫的空贼\n',
            '在到处作案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '对乘客的安检\n',
            '必须要再严格些才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_229A(): pass

    label('loc_229A')

    Jump('loc_2B05')

    def _loc_229D(): pass

    label('loc_229D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_240A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_239F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '女王诞辰庆典前后\n',
            '是定期船最繁忙拥挤的时期。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我要是有个女朋友的话，\n',
            '也想和她一起去王都游览啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '在各国皇帝与众将大臣面前\n',
            '寸步不让的女王陛下，\n',
            '无论如何我都想见上一面啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '当然，\n',
            '也一定要见见科洛蒂娅公主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '……唔唔㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2407')

    def _loc_239F(): pass

    label('loc_239F')

    ChrTalk(
        0x000C,
        (
            '女王诞辰庆典前后\n',
            '是定期船最繁忙拥挤的时期。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我要是有个女朋友的话，\n',
            '也想和她一起去王都游览啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2407(): pass

    label('loc_2407')

    Jump('loc_2B05')

    def _loc_240A(): pass

    label('loc_240A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_2549',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24EC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '虽然纯朴的姑娘很不错，\n',
            '不过还是王都、柏斯这些地方的美女\n',
            '更具有成熟魅力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '说起王都，\n',
            '艾莉茜雅女王的孙女\n',
            '科洛蒂娅公主也在那里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '传言说她清秀文雅楚楚动人，\n',
            '真想一睹这位传说中的公主的风采。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2546')

    def _loc_24EC(): pass

    label('loc_24EC')

    ChrTalk(
        0x000C,
        (
            '虽然王都、柏斯这些地方的美女\n',
            '更具有成熟魅力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '但纯朴的姑娘\n',
            '也实在难以割舍啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2546(): pass

    label('loc_2546')

    Jump('loc_2B05')

    def _loc_2549(): pass

    label('loc_2549')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_25AC',
    )

    ChrTalk(
        0x000C,
        (
            '嗯……\n',
            '今天开了个好头啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '从目前的情况来看，\n',
            '平均能打８３分吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B05')

    def _loc_25AC(): pass

    label('loc_25AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_26B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_265A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '真没劲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '今天的乘客里\n',
            '连一个我喜欢的类型都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '昨天柏斯来的定期船里\n',
            '倒是出现了一个\n',
            '外地口音的大美女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不知道她现在还在洛连特吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26B6')

    def _loc_265A(): pass

    label('loc_265A')

    ChrTalk(
        0x000C,
        (
            '昨天柏斯来的定期船里\n',
            '倒是出现了一个\n',
            '外地口音的大美女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不知道她现在还在洛连特吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26B6(): pass

    label('loc_26B6')

    Jump('loc_2B05')

    def _loc_26B9(): pass

    label('loc_26B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_28A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2853',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '古铜色的肌肤，红宝石似的双眸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '雪拉扎德小姐的确是一位\n',
            '充满异国色彩的美女啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '她有着利贝尔人\n',
            '所没有的奇特魅力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F又来了，\n',
            '阿兰哥哥的嗜好又要开始发作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '其实我以前还和雪拉扎德小姐\n',
            '一起去喝过酒呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过奇怪的是\n',
            '我完全记不起当时的情形了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哈～哈～哈，\n',
            '下次再邀请她一起去喝酒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(500)

    Jump('loc_28A6')

    def _loc_2853(): pass

    label('loc_2853')

    ChrTalk(
        0x000C,
        (
            '整个上午，\n',
            '连一个可爱的女孩子都没有出现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '唯有看下午的班次会不会有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28A6(): pass

    label('loc_28A6')

    Jump('loc_2B05')

    def _loc_28A9(): pass

    label('loc_28A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AC1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000C,
        (
            '今天又有许多人\n',
            '从这里踏上他们各自的旅途了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '同时也有许多人\n',
            '来到洛连特这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '最重要的是有许多的女孩子\n',
            '也会经过这里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '从远处这样看着她们来来往往，\n',
            '我感觉到了一种很单纯的快乐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '你明白这感觉吗，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#010F哦，也许吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F阿兰哥哥，\n',
            '你还真是一副老样子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#501F就因为你老说这个，\n',
            '才会没有女朋友的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '你真是会揭人伤疤啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过就是有这份乐趣在，\n',
            '工作起来才觉得很有意思嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哈哈哈～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F真是无药可救了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B05')

    def _loc_2AC1(): pass

    label('loc_2AC1')

    ChrTalk(
        0x000C,
        (
            '看着各种各样的女孩子\n',
            '从这里经过，\n',
            '我感觉到了一种很单纯的快乐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B05(): pass

    label('loc_2B05')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x2B09
@scena.Code('func_0B_2B09')
def func_0B_2B09():
    PlayBGM(88)
    OP_71(0x000A, 0x0004)
    OP_71(0x000A, 0x0002)
    OP_72(0x000B, 0x0004)
    OP_72(0x000C, 0x0004)
    OP_72(0x000D, 0x0004)
    OP_6F(0x000B, 0)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    EventBegin(0x00)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    CreateThread(0x0101, 0x00, 0x00, 0x000C)
    CreateThread(0x0102, 0x00, 0x00, 0x000D)
    CreateThread(0x000A, 0x00, 0x00, 0x000F)
    CreateThread(0x000B, 0x00, 0x00, 0x000E)
    CreateThread(0x000B, 0x01, 0x00, 0x0010)
    OP_67(0, 4500, -10000, 0)
    CameraSetDistance(6000, 0)

    @scena.Lambda('lambda_2B87')
    def lambda_2B87():
        OP_67(0, 9500, -10000, 14000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_2B87)

    @scena.Lambda('lambda_2B9F')
    def lambda_2B9F():
        CameraSetDistance(2800, 14000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_2B9F)

    PlaySE(117, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    CameraMove(42820, 4000, 32330, 14000)
    OP_A5(0x0004)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0160001263V#080F好了……差不多到时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001264V#080F艾丝蒂尔，我不在的时候，\n',
            '你可不要给约修亚添麻烦哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001265V#007F#3P老说这个，耳朵都听出茧来了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001266V#000F爸爸也是，不要老是逞强哦。\n',
            '年纪都一大把了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0160001267V#085F哼哼，\n',
            '我才不会输给年轻人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '#0160001268V#080F雪拉，突然把工作都交给你，\n',
            '真是不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030001269V#027F哪里，请别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030001270V#027F我还有点担心\n',
            '自己无法代替老师完成任务呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0160001271V#080F你太谦虚了，银闪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001272V#080F我不在的这段时间，\n',
            '这两个孩子就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030001273V#021F呵呵，老师请放心吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030001274V#021F毫不纵容地\n',
            '对他们严加管教就行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0160001275V#081F你果然明白我的想法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010001276V#009F#3P什么呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001277V#019F#3P呵呵，真是心灵相通的俩师徒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(166, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('女性的声音')

    Talk(
        (
            '#0880001278V',
            (TxtCtl.SetColor, 0x5),
            '开往王都的定期船\n',
            '『林德号』马上就要起飞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0880001279V请尚未登机的乘客尽快登机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrDirection(0x000B, 0, 400)
    SetChrDirection(0x000B, 45, 400)

    ChrTalk(
        0x000B,
        (
            '#0160001280V#084F哦，要出发了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2F6C')
    def lambda_2F6C():
        OP_67(0, 4370, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_2F6C)

    @scena.Lambda('lambda_2F84')
    def lambda_2F84():
        OP_6E(365, 6000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_2F84)

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_A5(0x0002)
    OP_A5(0x0004)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020001281V#010F爸爸，一路顺风。\n',
            '我们的事情您就放心好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        32,
        0,
        (
            TXT(0x00, '『要早点回来哦』\n'),
            TXT(0x01, '『别忘记带礼物回来哦』\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_304D'),
        (0x00000001, 'loc_3108'),
        (-1, 'loc_3200'),
    )

    def _loc_304D(): pass

    label('loc_304D')

    ChrTalk(
        0x0101,
        (
            '#0010001282V#006F工作结束之后不要到处闲逛，\n',
            '要早点回来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0160001283V#083F你就不能说点好听的话吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001284V#080F算了……\n',
            '总之我会尽早回来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001285V#080F那我走了，你们两个多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3200')

    def _loc_3108(): pass

    label('loc_3108')

    ChrTalk(
        0x0101,
        (
            '#0010001286V#501F虽然不知道你要去哪里，\n',
            '不过别忘记带礼物回来哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001287V#001F随便买些好玩的东西就行了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0160001288V#083F喂喂，\n',
            '我又不是去游山玩水。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001289V#080F不过钱包还有余裕的话，\n',
            '倒是可以考虑一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001290V#080F那我走了，你们两个多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3200')

    def _loc_3200(): pass

    label('loc_3200')

    Sleep(500)

    SetChrDirection(0x0000, 90, 0)
    SetChrDirection(0x0001, 90, 0)

    @scena.Lambda('lambda_3219')
    def lambda_3219():
        OP_67(0, 7390, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_3219)

    @scena.Lambda('lambda_3231')
    def lambda_3231():
        OP_6C(90000, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_3231)

    PlaySE(120, 0x00, 0x64)
    OP_70(0x000D, 280)
    Sleep(3000)

    OP_6F(0x000B, 2)
    OP_70(0x000B, 280)
    Sleep(700)

    PlaySE(118, 0x00, 0x64)
    OP_73(0x000B)
    WaitForThreadExit(0x0001, 0x0003)
    Fade(1500)
    CameraMove(54360, -3070, 41690, 0)
    OP_67(0, 40540, -45000, 0)
    CameraSetDistance(740, 0)
    OP_6C(208000, 0)
    OP_6E(510, 0)
    SetChrDirection(0x0000, 45, 0)
    SetChrDirection(0x0001, 45, 0)
    SetChrDirection(0x000A, 45, 0)
    SetChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_32CE')
    def lambda_32CE():
        OP_6C(223000, 13000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_32CE)

    LoadEffect(0x00, 'map\\\\mp028_00.eff')
    Play3DEffect(0x00, 0x00, 0x0B, 'Frame1_E0000_ground_Layer1', 0xFFFFE7C8, 0x000008FC, 0x00002567, 0x0000, 0x0000, 0x0000, 0x000005DC, 0x000005DC, 0x000005DC, 0x00000000)
    Play3DEffect(0x00, 0x01, 0x0B, 'Frame1_E0000_ground_Layer1', 0x00001838, 0x000008FC, 0x00002567, 0x0000, 0x0000, 0x0000, 0x000005DC, 0x000005DC, 0x000005DC, 0x00000000)
    PlaySE(119, 0x00, 0x64)
    OP_6F(0x000B, 200)
    OP_6F(0x000C, 200)
    OP_70(0x000B, 545)
    OP_70(0x000C, 545)
    OP_73(0x000B)

    @scena.Lambda('lambda_3398')
    def lambda_3398():
        CameraMove(54360, 1000, 41690, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3398)

    OP_6F(0x000B, 546)
    OP_6F(0x000C, 546)
    OP_70(0x000B, 800)
    OP_70(0x000C, 800)
    OP_73(0x000B)

    @scena.Lambda('lambda_33CF')
    def lambda_33CF():
        OP_67(0, 39850, -45000, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_33CF)

    @scena.Lambda('lambda_33E7')
    def lambda_33E7():
        OP_6C(314000, 12000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_33E7)

    OP_6F(0x000B, 800)
    OP_6F(0x000C, 800)
    OP_70(0x000B, 900)
    OP_70(0x000C, 900)
    OP_73(0x000B)
    OP_B0(0x000B, 0x28)
    OP_B0(0x000C, 0x28)
    OP_6F(0x000B, 901)
    OP_6F(0x000C, 901)
    OP_70(0x000B, 950)
    OP_70(0x000C, 950)
    OP_73(0x000B)
    OP_B0(0x000B, 0x32)
    OP_B0(0x000C, 0x32)
    OP_6F(0x000B, 951)
    OP_6F(0x000C, 951)
    OP_70(0x000B, 1000)
    OP_70(0x000C, 1000)
    OP_73(0x000B)
    OP_B0(0x000B, 0x3C)
    OP_B0(0x000C, 0x3C)
    OP_6F(0x000B, 1001)
    OP_6F(0x000C, 1001)
    OP_70(0x000B, 1050)
    OP_70(0x000C, 1050)
    OP_73(0x000B)
    OP_B0(0x000B, 0x46)
    OP_B0(0x000C, 0x46)
    OP_6F(0x000B, 1051)
    OP_6F(0x000C, 1051)
    OP_70(0x000B, 1100)
    OP_70(0x000C, 1100)
    OP_73(0x000B)
    OP_B0(0x000B, 0x50)
    OP_B0(0x000C, 0x50)
    OP_6F(0x000B, 1101)
    OP_6F(0x000C, 1101)
    OP_70(0x000B, 1150)
    OP_70(0x000C, 1150)
    OP_73(0x000B)
    OP_B0(0x000B, 0x5A)
    OP_B0(0x000C, 0x5A)
    OP_6F(0x000B, 1151)
    OP_6F(0x000C, 1151)
    OP_70(0x000B, 1200)
    OP_70(0x000C, 1200)
    OP_73(0x000B)
    OP_B0(0x000B, 0x64)
    OP_B0(0x000C, 0x64)
    OP_6F(0x000B, 1201)
    OP_6F(0x000C, 1201)
    OP_70(0x000B, 1250)
    OP_70(0x000C, 1250)
    OP_73(0x000B)
    OP_B0(0x000B, 0x6E)
    OP_B0(0x000C, 0x6E)
    OP_6F(0x000B, 1251)
    OP_6F(0x000C, 1251)
    OP_70(0x000B, 1300)
    OP_70(0x000C, 1300)
    OP_73(0x000B)
    OP_B0(0x000B, 0x78)
    OP_B0(0x000C, 0x78)
    OP_6F(0x000B, 1301)
    OP_6F(0x000C, 1301)
    OP_70(0x000B, 1350)
    OP_70(0x000C, 1350)
    OP_73(0x000B)
    OP_B0(0x000B, 0x82)
    OP_B0(0x000C, 0x82)
    OP_6F(0x000B, 1351)
    OP_6F(0x000C, 1351)
    OP_70(0x000B, 1400)
    OP_70(0x000C, 1400)
    OP_73(0x000B)
    OP_B0(0x000B, 0x96)
    OP_B0(0x000C, 0x96)
    OP_6F(0x000B, 1401)
    OP_6F(0x000C, 1401)
    OP_70(0x000B, 2000)
    OP_70(0x000C, 2000)
    FadeOut(2000, 0, -1)
    Sleep(1500)

    OP_24(0x0075, 0x5A)
    OP_24(0x0077, 0x5A)
    Sleep(100)

    OP_24(0x0075, 0x50)
    OP_24(0x0077, 0x50)
    Sleep(100)

    OP_24(0x0075, 0x46)
    OP_24(0x0077, 0x46)
    Sleep(100)

    OP_24(0x0075, 0x3C)
    OP_24(0x0077, 0x3C)
    Sleep(100)

    OP_24(0x0075, 0x32)
    OP_24(0x0077, 0x32)
    Sleep(100)

    OP_24(0x0075, 0x28)
    OP_24(0x0077, 0x28)
    Sleep(100)

    OP_24(0x0075, 0x1E)
    OP_24(0x0077, 0x1E)
    Sleep(100)

    OP_24(0x0075, 0x14)
    OP_24(0x0077, 0x14)
    Sleep(100)

    OP_24(0x0075, 0x0A)
    OP_24(0x0077, 0x0A)
    Sleep(100)

    OP_23(0x0075)
    OP_23(0x0077)
    Sleep(1000)

    OP_0D()
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    SetChrPos(0x0101, 41807, 4000, 39449, 170)
    SetChrPos(0x0102, 42334, 4000, 37937, 315)
    SetChrPos(0x000A, 40186, 4000, 39987, 158)
    OP_67(0, 8000, -10000, 0)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    CameraMove(41380, 5450, 39120, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3280, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    ClearChrFlags(0x0008, 0x0080)
    OP_72(0x000A, 0x0004)
    OP_72(0x000A, 0x0002)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020001291V#010F开走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001292V#003F#1P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030001293V#020F别一脸寂寞的样子嘛。\n',
            '反正老师很快就会回来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030001294V#020F虽然不知道要调查什么，\n',
            '不过对老师来说肯定是小菜一碟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001295V#009F#1P我、我才不觉得寂寞呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001296V#009F反正老爸不在家是常有的事。\n',
            '我又不是不习惯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030001297V#021F是是。\n',
            '随你怎么说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030001298V#020F好了，我也要去处理\n',
            '老师留给我的工作了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030001299V#020F如果工作上遇到什么困难，\n',
            '尽管来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001300V#006F#1P嗯，不过刚开始的时候\n',
            '还是要靠自己努力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001301V#006F起码要试试能做到什么程度吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030001302V#020F呵呵，听起来挺有自信的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030001303V#020F不过有约修亚在，\n',
            '我也用不着太过担心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030001304V#020F你们两人要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001305V#006F#1P嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001306V#010F我们会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_A5(0x0003)
    SetChrFlags(0x000A, 0x0080)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001307V#010F接下来……要做什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001308V#010F先到协会去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001309V#000F#1P嗯，问一下爱娜姐姐\n',
            '看看我们可以做些什么工作吧。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001310V#001F好的～我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    OP_20(0x000005DC)
    EventEnd(0x00)
    ClearMapFlags(0x00400000)
    SetScenaFlags(ScenaFlag(0x0042, 3, 0x213))
    OP_21()
    OP_1E()

    Return()

# id: 0x000C offset: 0x3ABB
@scena.Code('func_0C_3ABB')
def func_0C_3ABB():
    OP_A6(0x0000)
    OP_92(0x00FE, 0x0000, 0, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x000D offset: 0x3AD0
@scena.Code('func_0D_3AD0')
def func_0D_3AD0():
    OP_A6(0x0001)
    OP_92(0x00FE, 0x0000, 0, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x000E offset: 0x3AE5
@scena.Code('func_0E_3AE5')
def func_0E_3AE5():
    OP_A6(0x0002)
    ChrWalkTo(0x00FE, 46013, 4200, 31046, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 53013, 4200, 31046, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x000F offset: 0x3B20
@scena.Code('func_0F_3B20')
def func_0F_3B20():
    OP_A6(0x0003)
    def _loc_3B23(): pass

    label('loc_3B23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3B35',
    )

    ChrTurnDirection(0x00FE, 0x000B, 0)
    Yield()

    Jump('loc_3B23')

    def _loc_3B35(): pass

    label('loc_3B35')

    OP_A6(0x0003)
    ChrWalkTo(0x00FE, 38628, 4000, 39053, 2000, 0x00)
    ChrWalkTo(0x00FE, 33196, 2000, 39053, 2000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x0010 offset: 0x3B64
@scena.Code('func_10_3B64')
def func_10_3B64():
    OP_A6(0x0004)
    OP_6C(72000, 14000)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_A6(0x0004)
    CameraMove(48784, 4000, 31814, 6000)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_A6(0x0004)
    CameraMove(55314, 1821, 30831, 4000)
    CameraMove(55314, 6821, 30831, 4000)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

# id: 0x0011 offset: 0x3BB3
@scena.Code('func_11_3BB3')
def func_11_3BB3():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3C2C',
    )

    ChrTurnDirection(0x00FE, 0x0000, 0)

    ChrTalk(
        0x00FE,
        (
            '怎么了？\n',
            '还有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，\n',
            '我现在正在忙着准备交易的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请不要打扰我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 0, 0)

    Jump('loc_4E38')

    def _loc_3C2C(): pass

    label('loc_3C2C')

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_3C68',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在柏斯的交易\n',
            '无论如何也要成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E38')

    def _loc_3C68(): pass

    label('loc_3C68')

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x01, 0x0002)"),
            (Expr.Eval, "OP_40(0x0384)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4631',
    )

    OP_28(0x0005, 0x04, 0x10)
    OP_28(0x0005, 0x01, 0x0004)
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    Fade(1000)
    EventBegin(0x00)
    SetChrPos(0x0101, 38840, 0, 27320, 315)
    SetChrPos(0x0102, 37840, 0, 26710, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3CDF',
    )

    SetChrPos(0x0002, 38840, 0, 25820, 0)
    SetChrPos(0x0003, 37840, 0, 25210, 0)

    def _loc_3CDF(): pass

    label('loc_3CDF')

    CameraMove(37930, 0, 27910, 0)
    OP_6C(135000, 0)
    CameraSetDistance(2800, 0)
    OP_6E(280, 0)
    OP_4A(0x000D, 255)
    SetChrDirection(0x000D, 180, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1070150221V怎么了？\n',
            '找到蘑菇了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 0)

    ChrTalk(
        0x0101,
        (
            '#0010150222V#002F找是找到了没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150223V噢，太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150224V#505F不过呢，\n',
            '情况和你所说的有所不同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150225V#505F这个蘑菇……\n',
            '可是会吸引魔兽的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150226V呜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000D, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150227V#012F奥维德先生在委托我们时\n',
            '就知道会发生这样的情况吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0102, 400)
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1070150228V这、这样的事，\n',
            '我怎么会知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150229V况且你们不是游击士吗，\n',
            '处理危险情况本来就是你们的工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    OP_94(0x01, 0x0101, 0x0000, 0x000001F4, 0x00001770, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010150230V#005F那也得先让我们有所准备啊！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpTo(0x000D, 38000, 0, 28910, 600, 10000)
    ChrJumpTo(0x000D, 37500, 0, 29470, 200, 10000)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020150231V#012F我们的事情就算了，\n',
            '问题是奥维德先生你的目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150232V这个蘑菇，\n',
            '是要用来做什么的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150233V#009F对～呀～\n',
            '看起来也不像是用来做武器的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150234V老实交代，\n',
            '是不是打算用来做坏事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000D, 38020, 0, 28750, 2000, 0x00)
    ChrTurnDirection(0x000D, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150235V是用来做什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150236V当然是用作料理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150237V#004F啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150238V#014F…………料理？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150239V#004F那种危险的蘑菇\n',
            '居然可以拿来吃？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)
    OP_62(0x000D, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1070150240V……所以说嘛，\n',
            '你们乡下人就是不懂这些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150241V如果经过优秀厨师的精心烹制，\n',
            '特别的食材可以产生出无与伦比的美味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150242V在我看来，\n',
            '『荧光菇』就是这样特别的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150243V毫无疑问可以烹制出究极的菜品！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4269',
    )

    OP_62(0x0002, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0003, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_4269(): pass

    label('loc_4269')

    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020150244V#017F………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010150245V#509F那你就慢慢品尝\n',
            '自己所说的稀奇古怪的东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150246V吃不到葡萄就说葡萄酸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150247V唉，像你们这种平民百姓，\n',
            '一生都不会有机会品尝到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150248V#007F……随便你怎么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150249V我肯定一生都不会\n',
            '去吃那种绿色的蘑菇的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150250V#018F（确实是不太好吃的样子……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150251V好了好了，\n',
            '我要准备待会儿的交易了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150252V快，\n',
            '乖乖地把蘑菇交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150253V#007F好～好～\n',
            '早就想快点给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x000D, 500, 2000, 0x00)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '荧光菇',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0384, 1)
    OP_94(0x01, 0x0101, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

    ChrTalk(
        0x00FE,
        (
            '#1070150254V嗯，好了。看在蘑菇的份上，\n',
            '我就当作没看到你们的无理好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150255V报酬依然会按照约定的数额支付，\n',
            '就算是我一丁点儿的感谢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150256V#009F哼，\n',
            '那个蘑菇是绝对卖不出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150257V#009F我们走，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150258V#017F告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150259V嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【采蘑菇】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrDirection(0x00FE, 0, 0)
    SetChrFlags(0x000D, 0x0010)
    Fade(1000)
    CameraSetDistance(3300, 0)
    OP_6E(262, 0)
    OP_4B(0x000D, 255)
    EventEnd(0x00)
    TalkEnd(0x000D)

    Jump('loc_4E38')

    def _loc_4631(): pass

    label('loc_4631')

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_48A1',
    )

    ChrTalk(
        0x00FE,
        (
            '#1070150132V有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4656(): pass

    label('loc_4656')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4894',
    )

    FadeOut(300, 0, 100)

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【确认蘑菇的特征】\n'),
            TXT(0x01, '【没什么事】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_46B6'),
        (0x00000001, 'loc_4855'),
        (-1, 'loc_4855'),
    )

    def _loc_46B6(): pass

    label('loc_46B6')

    ChrTalk(
        0x00FE,
        (
            '#1070150133V『荧光菇』据说只生长在\n',
            '富含七耀石成份的土壤里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150134V而且通常会生长在\n',
            '茂密的草丛里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150135V但是，由于埋在土里的缘故，\n',
            '不仔细注意是很不容易发现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150136V如果还要说有什么其他特征，\n',
            '就是会发出和其名字相符的淡绿色光芒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150137V……嗯，大概就这么多了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150138V#000F总的说来就是去玛鲁加山道的草丛中\n',
            '寻找发光的蘑菇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150139V那么，希望你们能够尽快找到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_4891')

    def _loc_4855(): pass

    label('loc_4855')

    ChrTalk(
        0x00FE,
        (
            '#1070150139V那么，希望你们能够尽快找到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_5F(0x0000)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_4891')

    def _loc_4891(): pass

    label('loc_4891')

    Jump('loc_4656')

    def _loc_4894(): pass

    label('loc_4894')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4E38')

    def _loc_48A1(): pass

    label('loc_48A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_4E38',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_4DC3',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_4A67',
    )

    ClearChrFlags(0x000D, 0x0010)
    ChrTurnDirection(0x000D, 0x0000, 0)

    ChrTalk(
        0x00FE,
        (
            '#1070150141V哦哦，现在有空吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150142V因为这件事情很急，\n',
            '所以现在就谈谈行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_491C(): pass

    label('loc_491C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4A5A',
    )

    FadeOut(300, 0, 100)

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【听他说】\n'),
            TXT(0x01, '【不听】\n'),
        ),
    )

    MenuEnd(0x0001)
    OP_5F(0x0000)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_4970'),
        (0x00000001, 'loc_49A0'),
        (-1, 'loc_4A57'),
    )

    def _loc_4970(): pass

    label('loc_4970')

    ChrTalk(
        0x0101,
        (
            '#0010150127V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    Call(0, 0x0012)

    Jump('loc_4A57')

    def _loc_49A0(): pass

    label('loc_49A0')

    ChrTalk(
        0x0101,
        (
            '#0010150122V#505F嗯～抱歉哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150145V现在还不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150146V唉，真是没办法啊。\n',
            '我会在这儿等着的，\n',
            '等你们有空再过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150126V总之是越快越好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0005, 0x01, 0x8000)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    SetChrDirection(0x000D, 0, 0)
    TalkEnd(0x000D)

    Jump('loc_4A57')

    def _loc_4A57(): pass

    label('loc_4A57')

    Jump('loc_491C')

    def _loc_4A5A(): pass

    label('loc_4A5A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4DC0')

    def _loc_4A67(): pass

    label('loc_4A67')

    ClearChrFlags(0x000D, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '#1070150116V可恶，那些游击士。\n',
            '到底还要我再等多久啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150117V再不快一点，\n',
            '我就要赶不上定期船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150118V果然是乡下的地方…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(400)

    ChrTurnDirection(0x000D, 0x0000, 0)

    ChrTalk(
        0x00FE,
        (
            '#1070150119V…………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150120V哦！\n',
            '那不是游击士徽章吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150121V让我等好久了。\n',
            '因为这件事情很急，\n',
            '所以现在就谈谈行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 0)
    def _loc_4BA5(): pass

    label('loc_4BA5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4DB6',
    )

    FadeOut(300, 0, 100)

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【听他说】\n'),
            TXT(0x01, '【不听】\n'),
        ),
    )

    MenuEnd(0x0001)
    OP_5F(0x0000)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_4BF9'),
        (0x00000001, 'loc_4CDA'),
        (-1, 'loc_4DB3'),
    )

    def _loc_4BF9(): pass

    label('loc_4BF9')

    ChrTalk(
        0x0101,
        (
            '#0010150127V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150128V哦哦，太好了。\n',
            '真是帮了我大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150129V那我就立刻说明\n',
            '委托的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4CC1',
    )

    ChrTurnDirection(0x010F, 0x000D, 400)

    ChrTalk(
        0x010F,
        (
            '#0270150130V#0142F………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270150131V……我说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CC1(): pass

    label('loc_4CC1')

    Sleep(400)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    Call(0, 0x0012)

    Jump('loc_4DB3')

    def _loc_4CDA(): pass

    label('loc_4CDA')

    ChrTalk(
        0x0101,
        (
            '#0010150122V#505F嗯～抱歉哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150123V现在还不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150124V什么？没空吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150125V唉，真是没办法啊。\n',
            '我会在这儿等着的，\n',
            '等你们有空再过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150126V总之是越快越好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0005, 0x01, 0x8000)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    SetChrDirection(0x000D, 0, 0)
    TalkEnd(0x000D)

    Jump('loc_4DB3')

    def _loc_4DB3(): pass

    label('loc_4DB3')

    Jump('loc_4BA5')

    def _loc_4DB6(): pass

    label('loc_4DB6')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4DC0(): pass

    label('loc_4DC0')

    Jump('loc_4E38')

    def _loc_4DC3(): pass

    label('loc_4DC3')

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '要让我等到什么时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再不快一点，\n',
            '我就要赶不上定期船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，\n',
            '就因为这样我才讨厌乡下地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E38(): pass

    label('loc_4E38')

    TalkEnd(0x000D)

    Return()

# id: 0x0012 offset: 0x4E3C
@scena.Code('func_12_4E3C')
def func_12_4E3C():
    Fade(1000)
    EventBegin(0x00)
    SetChrPos(0x0101, 38840, 0, 27320, 315)
    SetChrPos(0x0102, 37840, 0, 26710, 0)
    SetChrPos(0x0002, 38840, 0, 25820, 0)
    SetChrPos(0x0003, 37840, 0, 25210, 0)
    CameraMove(37930, 0, 27910, 0)
    OP_6C(135000, 0)
    CameraSetDistance(2800, 0)
    OP_6E(280, 0)
    OP_4A(0x000D, 255)
    SetChrDirection(0x000D, 180, 0)
    OP_0D()
    OP_28(0x0005, 0x04, 0x04)
    OP_28(0x0005, 0x04, 0x08)
    OP_28(0x0005, 0x01, 0x0001)

    ChrTalk(
        0x00FE,
        (
            '#1070150148V先自我介绍一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150149V我叫奥维德，\n',
            '是奥维德商会的代表。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150150V#000F我叫艾丝蒂尔，\n',
            '旁边的这位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000D, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150151V#010F我叫约修亚，请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150152V是艾丝蒂尔和约修亚啊。\n',
            '两个人都很年轻嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150153V#506F嘿嘿，\n',
            '因为我们都还是游击士的新人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150154V新人……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150155V……唔，倒也无所谓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150156V#501F什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150157V咳咳……没、没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150158V我现在就告诉你们委托的内容，\n',
            '再不快点可能就会来不及的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150159V#006F好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150160V我正在寻找一种叫做\n',
            '『荧光菇』的稀有蘑菇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150161V据说这种蘑菇只生长在\n',
            '富含七耀石成份的土壤里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150162V洛连特这里有过采集记录，\n',
            '但我找遍了所有商店都没有买到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150163V无论如何\n',
            '我都想得到这种蘑菇，\n',
            '因此就只能拜托游击士协会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150164V#013F这周围能采集到耀晶片的地方\n',
            '就只有玛鲁加山道附近了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150165V#010F这种蘑菇还有什么其他的特征吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150166V据说它通常会生长在\n',
            '茂密的草丛里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150167V但是，由于埋在土里的缘故，\n',
            '如果不仔细寻找，\n',
            '就很不容易发现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150168V#002F唉，这岂不是很麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150169V不过一旦挖出来的话，\n',
            '很简单就可以辨认出\n',
            '是不是荧光菇了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150170V因为那种蘑菇会\n',
            '发出淡绿色的光芒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150171V#014F这就是得名『荧光菇』的原因吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150172V#000F啊，原来是这样啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150173V我的说明够清楚了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150174V#006F嗯，总之就是到玛鲁加山道的草丛中\n',
            '寻找发光的蘑菇对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150175V#010F嗯，就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150176V如果真的是生长在土壤下面的话，\n',
            '找起来就没那么简单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_54CD')
    def lambda_54CD():
        ChrTurnDirection(0x000D, 0x0000, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_54CD)

    Sleep(200)

    ChrTurnDirection(0x0102, 0x000D, 400)

    ChrTalk(
        0x00FE,
        (
            '#1070150177V嗯，如果还有什么问题\n',
            '就再到这儿来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1070150139V那么，希望你们能够尽快找到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    CameraSetDistance(3300, 0)
    OP_6E(262, 0)
    OP_4B(0x000D, 255)
    EventEnd(0x00)
    TalkEnd(0x000D)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
