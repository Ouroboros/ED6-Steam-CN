import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2321_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2321   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2321.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '珂蕾妲婆婆',
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

# id: 0x10002 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xD2
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
@scena.Code('Init')
def Init():
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
@scena.Code('func_01_14E')
def func_01_14E():
    Return()

# id: 0x0002 offset: 0x14F
@scena.Code('func_02_14F')
def func_02_14F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_164',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_14F')

    def _loc_164(): pass

    label('loc_164')

    Return()

# id: 0x0003 offset: 0x165
@scena.Code('func_03_165')
def func_03_165():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x16A
@scena.Code('func_04_16A')
def func_04_16A():
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
        'loc_1C8',
    )

    OP_0D()
    OP_A9(0x28)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_1C8(): pass

    label('loc_1C8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D9',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_1D9(): pass

    label('loc_1D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_24B',
    )

    ChrTalk(
        0x0008,
        (
            '听说这次事件的犯人\n',
            '被关在风车小屋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他们在被交给游击士协会之前，\n',
            '真想用石头狠狠砸那些纵火犯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_726')

    def _loc_24B(): pass

    label('loc_24B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_2C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '商店也要关门了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我想，\n',
            '至少要给孩子送点慰问品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C6')

    def _loc_29F(): pass

    label('loc_29F')

    ChrTalk(
        0x0008,
        (
            '我想，\n',
            '至少要给孩子送点慰问品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C6(): pass

    label('loc_2C6')

    Jump('loc_726')

    def _loc_2C9(): pass

    label('loc_2C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_3A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_351',
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

    Jump('loc_39D')

    def _loc_351(): pass

    label('loc_351')

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

    def _loc_39D(): pass

    label('loc_39D')

    Jump('loc_726')

    def _loc_3A0(): pass

    label('loc_3A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_3F8',
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

    Jump('loc_726')

    def _loc_3F8(): pass

    label('loc_3F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_43F',
    )

    ChrTalk(
        0x0008,
        (
            '是不是我心理作用呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总觉得村里\n',
            '好像吵吵闹闹的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_726')

    def _loc_43F(): pass

    label('loc_43F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_514',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C4',
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

    Jump('loc_511')

    def _loc_4C4(): pass

    label('loc_4C4')

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

    def _loc_511(): pass

    label('loc_511')

    Jump('loc_726')

    def _loc_514(): pass

    label('loc_514')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_60A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B5',
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

    Jump('loc_607')

    def _loc_5B5(): pass

    label('loc_5B5')

    ChrTalk(
        0x0008,
        (
            '玛诺利亚村很萧条，\n',
            '为此遗憾的人也很多，\n',
            '不过我认为能安静地生活才是最重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_607(): pass

    label('loc_607')

    Jump('loc_726')

    def _loc_60A(): pass

    label('loc_60A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_65F',
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

    Jump('loc_726')

    def _loc_65F(): pass

    label('loc_65F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_726',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E9',
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

    Jump('loc_726')

    def _loc_6E9(): pass

    label('loc_6E9')

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

    def _loc_726(): pass

    label('loc_726')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
