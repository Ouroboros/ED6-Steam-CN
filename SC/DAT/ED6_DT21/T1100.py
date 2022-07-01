import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '马尔科'),
    TXT(0x02, '蒙提'),
    TXT(0x03, '法娜'),
    TXT(0x04, '阿尔贝尔'),
    TXT(0x05, '西蒙'),
    TXT(0x06, '王国军士兵'),
    TXT(0x07, '莉咏'),
    TXT(0x08, '莫德娜'),
    TXT(0x09, '安赛尔新街方向'),
    TXT(0x0A, '柏斯市·北街区'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1100.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0001
    header.entryFunction  = 0x0001
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1635
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
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 50000,
            z                   = -3000,
            y                   = 31800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = -3000,
            y                   = 30480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 51870,
            z                   = -3000,
            y                   = 30650,
            direction           = 43,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 52830,
            z                   = -3000,
            y                   = 32950,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 51780,
            z                   = -3000,
            y                   = 32900,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 44410,
            z                   = -3000,
            y                   = 20760,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 44380,
            z                   = -3000,
            y                   = 29520,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 43530,
            z                   = -3000,
            y                   = 30940,
            direction           = 122,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = 47970,
            z                   = -3000,
            y                   = 4220,
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
            x                   = 48070,
            z                   = 0,
            y                   = 48590,
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

# id: 0x10003 offset: 0x232
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 53090,
            y           = -3000,
            z           = 20940,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = 55320,
            y           = -3000,
            z           = 33040,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000D,
        ),
    )

# id: 0x10005 offset: 0x272
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 65140,
            triggerZ            = 3000,
            triggerY            = 36680,
            triggerRange        = 1000,
            actorX              = 65280,
            actorZ              = 5000,
            actorY              = 36680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x296
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2C0',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2BD',
    )

    ClearChrFlags(0x000A, 0x0080)

    def _loc_2BD(): pass

    label('loc_2BD')

    Jump('loc_325')

    def _loc_2C0(): pass

    label('loc_2C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2DE',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)

    Jump('loc_325')

    def _loc_2DE(): pass

    label('loc_2DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2ED',
    )

    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_325')

    def _loc_2ED(): pass

    label('loc_2ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2FC',
    )

    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_325')

    def _loc_2FC(): pass

    label('loc_2FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_325',
    )

    SetChrPos(0x0008, 50940, -3000, 31530, 0)
    SetChrPos(0x0009, 49760, -3000, 30480, 0)

    def _loc_325(): pass

    label('loc_325')

    Return()

# id: 0x0001 offset: 0x326
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFEC780, 0xFFFE7960, 0x00230040)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_342',
    )

    Jump('loc_35B')

    def _loc_342(): pass

    label('loc_342')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_35B',
    )

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x00)
    OP_10(0x02, 0x00)
    OP_10(0x0F, 0x01)
    OP_10(0x10, 0x01)
    OP_10(0x11, 0x01)

    def _loc_35B(): pass

    label('loc_35B')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0078, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_37E',
    )

    OP_65(0x00, 0x0001)

    def _loc_37E(): pass

    label('loc_37E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_38F',
    )

    OP_1B(0x0D, 0x00, 0x000B)

    def _loc_38F(): pass

    label('loc_38F')

    OP_71(0x0012, 0x0002)

    Return()

# id: 0x0002 offset: 0x395
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_3F2',
    )

    ChrTalk(
        0x00FE,
        (
            '博尔德先生的太太\n',
            '好像去了超市了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总算是重新\n',
            '开始营业了，\n',
            '去买些东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F2(): pass

    label('loc_3F2')

    TalkEnd(0x000F)

    Return()

# id: 0x0003 offset: 0x3F6
@scena.Code('func_03_3F6')
def func_03_3F6():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_47F',
    )

    ChrTalk(
        0x00FE,
        (
            '平静的日子\n',
            '终于回来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船也恢复航行了，\n',
            '商业上的竞争现在才要开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '买、买东西的时候\n',
            '本应该忘记那些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47F(): pass

    label('loc_47F')

    TalkEnd(0x000E)

    Return()

# id: 0x0004 offset: 0x483
@scena.Code('func_04_483')
def func_04_483():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_503',
    )

    ChrTalk(
        0x00FE,
        (
            '不过、听说飞行舰队\n',
            '没有抓到那条龙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然会失败，\n',
            '真是有点失望啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '警备市街区的我们\n',
            '也觉得不好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_55A')

    def _loc_503(): pass

    label('loc_503')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_55A',
    )

    ChrTalk(
        0x00FE,
        (
            '听说这次龙的骚乱事件\n',
            '给军队高层带来了很大冲击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连飞行舰队\n',
            '都出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_55A(): pass

    label('loc_55A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x55E
@scena.Code('func_05_55E')
def func_05_55E():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_67C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_5CE',
    )

    ChrTalk(
        0x00FE,
        (
            '商人对交易要慎重，\n',
            '到现在也没签署协议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也知道在飞船停航的\n',
            '情况下什么也做不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_679')

    def _loc_5CE(): pass

    label('loc_5CE')

    ChrTalk(
        0x00FE,
        (
            '虽然要\n',
            '签署协定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但这种事总要慎重些。\n',
            '到现在也没签署协议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也知道在飞船停航的\n',
            '情况下什么也做不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果商谈不成功的话，\n',
            '来王国也就没有意义了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_679(): pass

    label('loc_679')

    Jump('loc_869')

    def _loc_67C(): pass

    label('loc_67C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_6F8',
    )

    ChrTalk(
        0x00FE,
        (
            '超市被袭事件之后，\n',
            '王国军也开始行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是这一带\n',
            '距离我们帝国的国境线很近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望不要出什么乱子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_869')

    def _loc_6F8(): pass

    label('loc_6F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_786',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_72E',
    )

    ChrTalk(
        0x00FE,
        (
            '北街区的超市似乎\n',
            '有什么骚动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_783')

    def _loc_72E(): pass

    label('loc_72E')

    ChrTalk(
        0x00FE,
        (
            '北街区的超市似乎\n',
            '有什么骚动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真糟糕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我才正打算\n',
            '出去商谈…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_783(): pass

    label('loc_783')

    Jump('loc_869')

    def _loc_786(): pass

    label('loc_786')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_869',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7E7',
    )

    ChrTalk(
        0x00FE,
        (
            '第一次来这里的时候\n',
            '我也迷路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经过了多次的来往，\n',
            '也完全熟悉了柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_869')

    def _loc_7E7(): pass

    label('loc_7E7')

    ChrTalk(
        0x00FE,
        (
            '我第一次从帝国来的时候\n',
            '也迷路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经过了多次的来往，\n',
            '也完全熟悉了柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，先在南街区转转，\n',
            '然后再去超市吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_869(): pass

    label('loc_869')

    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x86D
@scena.Code('func_06_86D')
def func_06_86D():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_8F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_8A2',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的。\n',
            '商谈还是没有进展。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8ED')

    def _loc_8A2(): pass

    label('loc_8A2')

    ChrTalk(
        0x00FE,
        (
            '呼，真是的。\n',
            '商谈还是没有进展。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来的不是时候，\n',
            '也只有放弃了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_8ED(): pass

    label('loc_8ED')

    Jump('loc_B4C')

    def _loc_8F0(): pass

    label('loc_8F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_9DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_95B',
    )

    ChrTalk(
        0x00FE,
        (
            '帝国军的导力战车\n',
            '定货量明显减少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '仔细想想，\n',
            '也许是因为互不侵犯条约的影响吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DA')

    def _loc_95B(): pass

    label('loc_95B')

    ChrTalk(
        0x00FE,
        (
            '帝国军的导力战车\n',
            '定货量明显减少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '仔细想想，\n',
            '也许是因为互不侵犯条约的影响吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为商人，想法还是很复杂的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_9DA(): pass

    label('loc_9DA')

    Jump('loc_B4C')

    def _loc_9DD(): pass

    label('loc_9DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_A28',
    )

    ChrTalk(
        0x00FE,
        (
            '超市的被袭事件吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '商谈似乎无法继续了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4C')

    def _loc_A28(): pass

    label('loc_A28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_B4C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A91',
    )

    ChrTalk(
        0x00FE,
        (
            '即使如此，这里真的是\n',
            '比我想象中得还发达呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们帝国的都市\n',
            '也未必有这么繁荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4C')

    def _loc_A91(): pass

    label('loc_A91')

    ChrTalk(
        0x00FE,
        (
            '我身为帝国的商人，\n',
            '也想拓展一下海外的市场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以这次才下定决心\n',
            '来王国进行商谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏前辈马尔科的帮忙，\n',
            '我才能和这里的商人们联系上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来就希望\n',
            '商谈能早些达成吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_B4C(): pass

    label('loc_B4C')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0xB50
@scena.Code('func_07_B50')
def func_07_B50():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BEE',
    )

    ChrTalk(
        0x00FE,
        (
            '这个店一定\n',
            '希望有个帮手吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果和店主商量商量，\n',
            '一定会被采纳的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，太混乱了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，总之要有\n',
            '长期作战的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_C28')

    def _loc_BEE(): pass

    label('loc_BEE')

    ChrTalk(
        0x00FE,
        (
            '工房来了\n',
            '很多客人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们应该\n',
            '人手不足了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C28(): pass

    label('loc_C28')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0xC2C
@scena.Code('func_08_C2C')
def func_08_C2C():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_C84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C45',
    )

    Call(0, 0x000A)

    Jump('loc_C81')

    def _loc_C45(): pass

    label('loc_C45')

    ChrTalk(
        0x00FE,
        (
            '前面的客人\n',
            '是怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '进了店以后\n',
            '这么久也没出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C81(): pass

    label('loc_C81')

    Jump('loc_CDE')

    def _loc_C84(): pass

    label('loc_C84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_CDE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CA4',
    )

    Call(0, 0x000A)
    ClearChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x000C, 0x0010)

    Jump('loc_CDE')

    def _loc_CA4(): pass

    label('loc_CA4')

    ChrTalk(
        0x00FE,
        (
            '昨天晚上我家\n',
            '非常恐慌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工房好像也\n',
            '非常混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CDE(): pass

    label('loc_CDE')

    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0xCE2
@scena.Code('func_09_CE2')
def func_09_CE2():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_D44',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CFB',
    )

    Call(0, 0x000A)

    Jump('loc_D41')

    def _loc_CFB(): pass

    label('loc_CFB')

    ChrTalk(
        0x00FE,
        (
            '接下来就去看看\n',
            '店里的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前边的客人\n',
            '应该已经办完事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D41(): pass

    label('loc_D41')

    Jump('loc_DB6')

    def _loc_D44(): pass

    label('loc_D44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_DB6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D64',
    )

    Call(0, 0x000A)
    ClearChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x000C, 0x0010)

    Jump('loc_DB6')

    def _loc_D64(): pass

    label('loc_D64')

    ChrTalk(
        0x00FE,
        (
            '现在一到晚上，\n',
            '我家里就很麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特里诺家也在找油灯，\n',
            '把家里都翻了个遍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DB6(): pass

    label('loc_DB6')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0xDBA
@scena.Code('func_0A_DBA')
def func_0A_DBA():
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_E9E',
    )

    ChrTalk(
        0x000C,
        (
            '对了，阿尔贝尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '你好像是准备\n',
            '考进王立学院吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '嗯，为了准备考试\n',
            '一直在拼命学习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '就算是现在这种状况，\n',
            '也只有努力克服了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '确实如此呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '导力器全都瘫痪了，\n',
            '日常生活也受到很大影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F24')

    def _loc_E9E(): pass

    label('loc_E9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_F24',
    )

    ChrTalk(
        0x000B,
        (
            '啊，西蒙…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你也有事\n',
            '要到工房吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯，是米拉诺\n',
            '让我来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我的父亲也吩咐过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '任何一家\n',
            '似乎都很头疼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F24(): pass

    label('loc_F24')

    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)
    OP_A2(0x0003)
    OP_A2(0x0004)

    Return()

# id: 0x000B offset: 0xF33
@scena.Code('func_0B_F33')
def func_0B_F33():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10A6',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FB4',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300975V#074F现在已经\n',
            '没空乱逛了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300976V#070F在街上买过东西之后\n',
            '就去国际空港吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1032')

    def _loc_FB4(): pass

    label('loc_FB4')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FCA',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_FD1')

    def _loc_FCA(): pass

    label('loc_FCA')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_FD1(): pass

    label('loc_FD1')

    ChrTalk(
        0x0103,
        (
            '#0030300977V#020F现在已经\n',
            '没时间闲逛了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300978V在街上买完东西以后\n',
            '就去国际空港吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1032(): pass

    label('loc_1032')

    Fade(1000)
    OP_59()
    SetChrPos(0x0101, 47790, -3000, 17080, 0)
    SetChrPos(0x0103, 47790, -3000, 17080, 0)
    SetChrPos(0x0108, 47790, -3000, 17080, 0)
    SetChrPos(0x0105, 47790, -3000, 17080, 0)
    SetChrPos(0x0104, 47790, -3000, 17080, 0)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    OP_8C(0x0000, 0, 0)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1610')

    def _loc_10A6(): pass

    label('loc_10A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 6, 0x1A16)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1353',
    )

    EventBegin(0x02)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_10D4'),
        (0x00000002, 'loc_112A'),
        (0x00000004, 'loc_1188'),
        (0x00000003, 'loc_11E2'),
        (0x00000006, 'loc_1240'),
        (0x00000007, 'loc_12A0'),
        (-1, 'loc_12F7'),
    )

    def _loc_10D4(): pass

    label('loc_10D4')

    ChrTalk(
        0x0101,
        (
            '#0010300979V#1002F不是这条路啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300980V准备完毕之后\n',
            '马上回拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F7')

    def _loc_112A(): pass

    label('loc_112A')

    ChrTalk(
        0x0103,
        (
            '#0030300981V#022F现在没时间\n',
            '绕远路了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300982V准备结束之后\n',
            '就赶快回拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F7')

    def _loc_1188(): pass

    label('loc_1188')

    ChrTalk(
        0x0105,
        (
            '#0060300983V#042F现在没空\n',
            '绕远路了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300984V准备结束之后\n',
            '赶快回拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F7')

    def _loc_11E2(): pass

    label('loc_11E2')

    ChrTalk(
        0x0104,
        (
            '#0040300985V#032F现在不是闲逛\n',
            '的时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300986V准备完毕之后\n',
            '赶快回拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F7')

    def _loc_1240(): pass

    label('loc_1240')

    ChrTalk(
        0x0107,
        (
            '#0070300987V#062F……别再\n',
            '磨磨蹭蹭的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300988V准备好之后\n',
            '赶快追上阿加特哥哥吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F7')

    def _loc_12A0(): pass

    label('loc_12A0')

    ChrTalk(
        0x0108,
        (
            '#0080300989V#072F已经没时间乱逛了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300990V准备好之后\n',
            '赶快回拉文努村吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F7')

    def _loc_12F7(): pass

    label('loc_12F7')

    Fade(1000)
    OP_59()
    SetChrPos(0x0000, 47790, -3000, 17080, 0)
    SetChrPos(0x0001, 47790, -3000, 17080, 0)
    SetChrPos(0x0002, 47790, -3000, 17080, 0)
    SetChrPos(0x0003, 47790, -3000, 17080, 0)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1610')

    def _loc_1353(): pass

    label('loc_1353')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1610',
    )

    EventBegin(0x02)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_1381'),
        (0x00000002, 'loc_13D9'),
        (0x00000004, 'loc_1432'),
        (0x00000003, 'loc_148B'),
        (0x00000006, 'loc_14E0'),
        (0x00000007, 'loc_1564'),
        (-1, 'loc_15B7'),
    )

    def _loc_1381(): pass

    label('loc_1381')

    ChrTalk(
        0x0101,
        (
            '#0010300991V#1002F现在必须要\n',
            '赶快到拉文努村…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300992V从西边的出口出去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15B7')

    def _loc_13D9(): pass

    label('loc_13D9')

    ChrTalk(
        0x0103,
        (
            '#0030300993V#022F要去拉文努村的话，\n',
            '得从西边的出口出去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300994V快一点吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15B7')

    def _loc_1432(): pass

    label('loc_1432')

    ChrTalk(
        0x0105,
        (
            '#0060300995V#042F拉文努村\n',
            '位于柏斯的西北方向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300996V从西边的出口出去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15B7')

    def _loc_148B(): pass

    label('loc_148B')

    ChrTalk(
        0x0104,
        (
            '#0040300997V#032F拉文努村\n',
            '是在西北方向呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300998V从西边的出口出去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15B7')

    def _loc_14E0(): pass

    label('loc_14E0')

    ChrTalk(
        0x0107,
        (
            '#0070300999V#065F啊啊……\n',
            '要去拉文努村的话，\n',
            '应该从西边的出口出去啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301000V#062F我们必须要早点\n',
            '追上阿加特哥哥……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15B7')

    def _loc_1564(): pass

    label('loc_1564')

    ChrTalk(
        0x0108,
        (
            '#0080301001V#072F去拉文努村的话、\n',
            '要从西边出去，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080301002V赶快行动吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15B7')

    def _loc_15B7(): pass

    label('loc_15B7')

    Fade(1000)
    OP_59()
    SetChrPos(0x0000, 47790, -3000, 17080, 0)
    SetChrPos(0x0001, 47790, -3000, 17080, 0)
    SetChrPos(0x0002, 47790, -3000, 17080, 0)
    SetChrPos(0x0003, 47790, -3000, 17080, 0)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    Sleep(50)

    EventEnd(0x04)

    def _loc_1610(): pass

    label('loc_1610')

    Return()

# id: 0x000C offset: 0x1611
@scena.Code('func_0C_1611')
def func_0C_1611():
    SetPlaceName(0x0022)

    Return()

# id: 0x000D offset: 0x1615
@scena.Code('func_0D_1615')
def func_0D_1615():
    SetPlaceName(0x0024)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
