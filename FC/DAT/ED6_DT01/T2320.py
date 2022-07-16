import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2320_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2320   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '珂蕾妲婆婆'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2320.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x8AC
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
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -4000,
            z                   = 500,
            y                   = 8800,
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
    )

# id: 0x10003 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -4040,
            triggerZ            = 500,
            triggerY            = 7530,
            triggerRange        = 400,
            actorX              = -4000,
            actorZ              = 2000,
            actorY              = 8800,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xF6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_100',
    )

    Jump('loc_14D')

    def _loc_100(): pass

    label('loc_100')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_10A',
    )

    Jump('loc_14D')

    def _loc_10A(): pass

    label('loc_10A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_114',
    )

    Jump('loc_14D')

    def _loc_114(): pass

    label('loc_114')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_11E',
    )

    Jump('loc_14D')

    def _loc_11E(): pass

    label('loc_11E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_128',
    )

    Jump('loc_14D')

    def _loc_128(): pass

    label('loc_128')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_132',
    )

    Jump('loc_14D')

    def _loc_132(): pass

    label('loc_132')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_13C',
    )

    Jump('loc_14D')

    def _loc_13C(): pass

    label('loc_13C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_146',
    )

    Jump('loc_14D')

    def _loc_146(): pass

    label('loc_146')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_14D',
    )

    def _loc_14D(): pass

    label('loc_14D')

    Return()

# id: 0x0001 offset: 0x14E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_166',
    )

    OP_B1('t2320_y')

    Jump('loc_16F')

    def _loc_166(): pass

    label('loc_166')

    OP_B1('t2320_n')

    def _loc_16F(): pass

    label('loc_16F')

    Return()

# id: 0x0002 offset: 0x170
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_185',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_185(): pass

    label('loc_185')

    Return()

# id: 0x0003 offset: 0x186
@scena.Code('func_03_186')
def func_03_186():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x18B
@scena.Code('func_04_18B')
def func_04_18B():
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
        'loc_1E9',
    )

    OP_0D()
    OP_A9(0x28)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_1E9(): pass

    label('loc_1E9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FA',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_1FA(): pass

    label('loc_1FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_25E',
    )

    ChrTalk(
        0x0008,
        (
            '只要孩子们一来，\n',
            '我的腰痛就不犯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说不定是孩子们\n',
            '把他们的精神劲头分给我了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89E')

    def _loc_25E(): pass

    label('loc_25E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_350',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2ED',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '听说这次事件的\n',
            '犯人被关在风车小屋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他们在被交给游击士协会之前，\n',
            '应该先向孩子们道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们也是这么想的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34D')

    def _loc_2ED(): pass

    label('loc_2ED')

    ChrTalk(
        0x0008,
        (
            '听说这次事件的\n',
            '犯人被关在风车小屋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他们在被交给游击士协会之前，\n',
            '应该先向孩子们道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34D(): pass

    label('loc_34D')

    Jump('loc_89E')

    def _loc_350(): pass

    label('loc_350')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_409',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '那些孩子们\n',
            '本来就已经沦落天涯，\n',
            '竟然还遇到这样的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '空之女神大人\n',
            '到底在做什么啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_406')

    def _loc_3C8(): pass

    label('loc_3C8')

    ChrTalk(
        0x0008,
        (
            '那些孩子们\n',
            '本来就已经沦落天涯，\n',
            '竟然还遇到这样的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_406(): pass

    label('loc_406')

    Jump('loc_89E')

    def _loc_409(): pass

    label('loc_409')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_4E0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_491',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '孤儿院的孩子们\n',
            '经常到这里来玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就好像一下子\n',
            '多了许多孙子一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然我喜欢安静，\n',
            '但是这样也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DD')

    def _loc_491(): pass

    label('loc_491')

    ChrTalk(
        0x0008,
        (
            '孤儿院的孩子们\n',
            '经常到这里来玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就好像一下子\n',
            '多了许多孙子一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DD(): pass

    label('loc_4DD')

    Jump('loc_89E')

    def _loc_4E0(): pass

    label('loc_4E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_55C',
    )

    ChrTalk(
        0x0008,
        (
            '竟然放火烧孤儿院，\n',
            '那些家伙真是不像话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '人，\n',
            '也有绝对不能做的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我无法原谅做了这种事的犯人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89E')

    def _loc_55C(): pass

    label('loc_55C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_5A5',
    )

    ChrTalk(
        0x0008,
        (
            '总觉得村里气氛\n',
            '好像有一些慌乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '发生什么事情了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89E')

    def _loc_5A5(): pass

    label('loc_5A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_67A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_62A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '这个村子\n',
            '景色和花都很漂亮吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然在像卢安那样的城市里\n',
            '生活很便利……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过还是这里更合我心意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_677')

    def _loc_62A(): pass

    label('loc_62A')

    ChrTalk(
        0x0008,
        (
            '虽然在像卢安那样的城市里\n',
            '生活很便利……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过还是这里更合我心意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_677(): pass

    label('loc_677')

    Jump('loc_89E')

    def _loc_67A(): pass

    label('loc_67A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_76C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_71B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '很多人都在感叹\n',
            '定期船的开航\n',
            '让这里变得很冷清……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我倒是觉得，\n',
            '这样也挺不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '上了年纪之后，\n',
            '就希望自己能够过上安静的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_769')

    def _loc_71B(): pass

    label('loc_71B')

    ChrTalk(
        0x0008,
        (
            '虽然定期船的开航\n',
            '让这里变得很冷清……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我倒是觉得，\n',
            '这样也挺不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_769(): pass

    label('loc_769')

    Jump('loc_89E')

    def _loc_76C(): pass

    label('loc_76C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_7C1',
    )

    ChrTalk(
        0x0008,
        (
            '一个戴着帽子的男孩？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他没有到这家店来哦。\n',
            '你们问问门外的萨蒂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89E')

    def _loc_7C1(): pass

    label('loc_7C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_89E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_861',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '我的孙女萨蒂\n',
            '是个非常温柔的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那孩子的父母\n',
            '因为工作而到外地去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为了照顾我，\n',
            '萨蒂留在了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真是难能可贵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89E')

    def _loc_861(): pass

    label('loc_861')

    ChrTalk(
        0x0008,
        (
            '我的孙女萨蒂\n',
            '是个非常温柔的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真是难能可贵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_89E(): pass

    label('loc_89E')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
