import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1220_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1220   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1220.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '埃米尔',
            x                   = -1600,
            z                   = -1000,
            y                   = 7600,
            direction           = 135,
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
            triggerX            = -670,
            triggerZ            = -1000,
            triggerY            = 6680,
            triggerRange        = 400,
            actorX              = -1600,
            actorZ              = 500,
            actorY              = 7600,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xF6
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xF7
@scena.Code('func_01_F7')
def func_01_F7():
    Return()

# id: 0x0002 offset: 0xF8
@scena.Code('func_02_F8')
def func_02_F8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_10D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_F8')

    def _loc_10D(): pass

    label('loc_10D')

    Return()

# id: 0x0003 offset: 0x10E
@scena.Code('func_03_10E')
def func_03_10E():
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
        'loc_16C',
    )

    OP_0D()
    OP_A9(0x0E)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_16C(): pass

    label('loc_16C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17D',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_17D(): pass

    label('loc_17D')

    Call(0, 0x0004)
    ChrSetDirection(0x0008, 135, 0)

    Return()

# id: 0x0004 offset: 0x189
@scena.Code('func_04_189')
def func_04_189():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1E0',
    )

    ChrTalk(
        0x0008,
        (
            '现在，在果树园工作的人\n',
            '都聚集在村长的家里，\n',
            '好像在一起商量什么事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B8')

    def _loc_1E0(): pass

    label('loc_1E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_32E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '这个村子里，\n',
            '除了库赖爷爷和贝斯卡经常吵架，\n',
            '其他时间都十分安静和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '帝国军到来之前，\n',
            '这个村子就和现在一样\n',
            '又平静又祥和…… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '所以，\n',
            '我有时候会觉得现在的这种和平\n',
            '总有一天会被打破。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32B')

    def _loc_2B8(): pass

    label('loc_2B8')

    ChrTalk(
        0x0008,
        (
            '就在帝国军来之前不多久，\n',
            '村子曾经非常和平安稳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '所以，\n',
            '我有时候会觉得现在的这种和平\n',
            '总有一天会被打破。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32B(): pass

    label('loc_32B')

    Jump('loc_5B8')

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_3DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '王国军的人到这里来过，\n',
            '是不是发生什么事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我听说之前来调查的时候，\n',
            '也没有找到什么东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DC')

    def _loc_3A9(): pass

    label('loc_3A9')

    ChrTalk(
        0x0008,
        (
            '穿军服的人进进出出，\n',
            '我总觉得有些莫名的不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DC(): pass

    label('loc_3DC')

    Jump('loc_5B8')

    def _loc_3DF(): pass

    label('loc_3DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_4A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_464',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '我也想在柏斯超市里\n',
            '开一家小店啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过还是故乡最适合定居。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这里商品的进货不太方便，\n',
            '非常辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A3')

    def _loc_464(): pass

    label('loc_464')

    ChrTalk(
        0x0008,
        (
            '在青空市场时代我学到了很多东西，\n',
            '现在想想真是非常有用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A3(): pass

    label('loc_4A3')

    Jump('loc_5B8')

    def _loc_4A6(): pass

    label('loc_4A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_4FF',
    )

    ChrTalk(
        0x0008,
        (
            '百日战争的时候，\n',
            '连幼小的孩童都难以生还。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在想起来心里还是很难过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B8')

    def _loc_4FF(): pass

    label('loc_4FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_57F',
    )

    ChrTalk(
        0x0008,
        (
            '这个村子和帝国邻近，\n',
            '所以战争的时候最先被占领。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '有很多人在战争中牺牲了，\n',
            '直到如今，村子的伤疤仍然没有痊愈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B8')

    def _loc_57F(): pass

    label('loc_57F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_5B8',
    )

    ChrTalk(
        0x0008,
        (
            '哟，我没见过你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '欢迎来到拉文努村！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B8(): pass

    label('loc_5B8')

    OP_56(0x00)
    TalkEnd(0x0008)
    Sleep(300)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
