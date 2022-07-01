import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0121_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0121_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0121_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x8B70
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B9',
    )

    OP_2A(0x00B7, 0x00B8, 0xFFFF)

    Jump('loc_155')

    def _loc_B9(): pass

    label('loc_B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_DA',
    )

    OP_2A(0x0072, 0x0073, 0x00AD, 0x00AE, 0x0074, 0x0075, 0x0076, 0x0077, 0x00AF, 0x00B0, 0xFFFF)

    Jump('loc_155')

    def _loc_DA(): pass

    label('loc_DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Return,
        ),
        'loc_F5',
    )

    OP_2A(0x0072, 0x0073, 0x00AD, 0x00AE, 0x0074, 0x00AF, 0x00B0, 0xFFFF)

    Jump('loc_155')

    def _loc_F5(): pass

    label('loc_F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_10C',
    )

    OP_2A(0x0072, 0x0073, 0x00AD, 0x00AE, 0x0074, 0xFFFF)

    Jump('loc_155')

    def _loc_10C(): pass

    label('loc_10C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_121',
    )

    OP_2A(0x0072, 0x0073, 0x00AD, 0x00AE, 0xFFFF)

    Jump('loc_155')

    def _loc_121(): pass

    label('loc_121')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '没发出什么委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_155(): pass

    label('loc_155')

    TalkEnd(0x00FF)

    Return()

# id: 0x0001 offset: 0x159
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 46210, 0, -1330, 90)
    SetChrPos(0x0103, 45510, 0, -550, 90)
    SetChrPos(0x00F8, 45070, 0, -1770, 90)
    SetChrPos(0x00F9, 44550, 0, -830, 90)
    OP_8C(0x00FE, 270, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DA',
    )

    SetChrPos(0x00F9, 45070, 0, -1770, 90)
    SetChrPos(0x00F8, 44550, 0, -830, 90)

    def _loc_1DA(): pass

    label('loc_1DA')

    OP_6D(47260, 0, -210, 0)
    OP_67(0, 5030, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010370608V#1011F#1P请问，能麻烦婆婆点事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470240V#2P什么事，艾丝蒂尔。\n',
            '想让我做什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470241V#1015F#1P嗯，有点小事\n',
            '想问您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '诉说了在寻找拉欧老人\n',
            '所说的炖煮料理食谱的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#3570470242V#2P原来是关于\n',
            '香辣炖煮的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470243V#2P以前，在这地方\n',
            '是一道经常吃的传统菜哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E8',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_426')

    def _loc_3E8(): pass

    label('loc_3E8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40F',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_426')

    def _loc_40F(): pass

    label('loc_40F')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_426(): pass

    label('loc_426')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44D',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_48B')

    def _loc_44D(): pass

    label('loc_44D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_474',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_48B')

    def _loc_474(): pass

    label('loc_474')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_48B(): pass

    label('loc_48B')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010470244V#1004F#1P啊……！？',
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
        'loc_4ED',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470245V#064F婆婆也知道？？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_586')

    def _loc_4ED(): pass

    label('loc_4ED')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_521',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470246V#044F真的知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_586')

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_555',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470247V#033F或许会知道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_586')

    def _loc_555(): pass

    label('loc_555')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_586',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470248V#073F难道会知道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_586(): pass

    label('loc_586')

    ChrTalk(
        0x00FE,
        (
            '#3570470249V#2P当然知道啦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470250V#2P那在以前可是家家都会做的\n',
            '一道著名菜式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470251V#1011F#1P啊，德瑟鲁大叔他也\n',
            '这么说过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470252V#1001F嗯嗯，一定就是这个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470253V#020F#1P找的就是这个食谱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470254V能不能\n',
            '教我怎么做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470255V#2P啊啊，教吗？\n',
            '当然是可以，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470256V#2P我所知道的食谱\n',
            '大概与你要找的不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470257V#2P这一点\n',
            '你们最好先了解清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470258V#1011F#1P咦，难道不同么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470259V……不是一样的菜吗？',
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
        'loc_7B9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470260V#555F这到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_864')

    def _loc_7B9(): pass

    label('loc_7B9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7F7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470261V#070F嗯，到底是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_864')

    def _loc_7F7(): pass

    label('loc_7F7')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_829',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470262V#033F怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_864')

    def _loc_829(): pass

    label('loc_829')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_864',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470263V#044F那，那到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_864(): pass

    label('loc_864')

    ChrTalk(
        0x00FE,
        (
            '#3570470264V#2P我的食谱呢～\n',
            '是我们家一代一代传下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470265V#2P因此，肯定和最原始的料理\n',
            '味道也有所改变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470266V#2P如果你认为这没有什么关系，\n',
            '我就教，如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470267V#1002F#1P也就是说……\n',
            '经过了改良？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470268V#1003F嗯，虽然还是最想\n',
            '要原始版，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470269V#027F#1P还是先\n',
            '请您教我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470270V总不能空手回去，\n',
            '白来一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A42',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470271V#030F雪拉说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470272V我们不能辜负了\n',
            '老人的一番厚意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6E')

    def _loc_A42(): pass

    label('loc_A42')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470273V#070F哈哈，你说的没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080470274V自然是不忍心\n',
            '拒绝老人的好意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6E')

    def _loc_AA7(): pass

    label('loc_AA7')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B0C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470275V#040F嗯嗯，是的是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060470276V无视老人的好意\n',
            '是件失礼的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6E')

    def _loc_B0C(): pass

    label('loc_B0C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B6E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470277V#051F雪拉扎德说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470278V一定要学的。\n',
            '那就安静地听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B6E(): pass

    label('loc_B6E')

    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470279V#1006F#1P嗯……是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470280V……那就这么决定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470281V那就你们等我去拿\n',
            '料理手册。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470282V#020F#1P好，那就麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x00FE, 44800, 0, 2410, 0)
    CreateThread(0x00FE, 0x00, 0x01, 0x0002)
    SetChrPos(0x0101, 44360, 0, -280, 0)
    SetChrPos(0x0103, 43020, 0, 160, 45)
    SetChrPos(0x00F8, 45040, 0, -1020, 0)
    SetChrPos(0x00F9, 46250, 0, -820, 315)
    OP_6D(45660, 0, 1500, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(3000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010470283V#1015F（…………………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470284V（找了好久，\n',
            '  这么长时间……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470285V#026F（不要那么着急。\n',
            '  再稍微等等吧。）',
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
        'loc_DED',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470286V#051F（就算是相当熟悉，\n',
            '  毕竟是老婆婆，再等等的。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470287V(找东西花费些时间\n',
            '  也是没有办法的。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F72')

    def _loc_DED(): pass

    label('loc_DED')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E6C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470288V#070F（虽说身体还比较健壮，\n',
            '  不过年纪确实是大了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080470289V(就请在这里耐心地等候吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F72')

    def _loc_E6C(): pass

    label('loc_E6C')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EF6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470290V#031F（虽说很熟悉，\n',
            '  不过年纪大了是无法否认的事实。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470291V（我们还是在这里耐心地\n',
            '  等候吧。 ）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F72')

    def _loc_EF6(): pass

    label('loc_EF6')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F72',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470292V#040F（虽说十分精神，\n',
            '不过也已经是这个岁数了。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060470293V（还是在这里慢慢地\n',
            '  等候吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F72(): pass

    label('loc_F72')

    OP_4A(0x00FE, 255)
    OP_8C(0x00FE, 0, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#3570470294V哎呀……那么说来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470295V……是的是的，应该没错了。\n',
            '有些事情是无法用理论来解释的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x00FE, 44800, 0, 2410, 1000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#3570470296V……让你们久等了，\n',
            '不好意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470297V我是不是太慢了？\n',
            '你们都着急了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470298V#1016F哪、哪里……\n',
            '没有那回事啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470299V#1011F那……\n',
            '找到食谱了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470300V哎呀，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470301V其实……很早以前\n',
            '好像送给谁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010470302V#1020F啊！？',
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
        'loc_11A5',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470303V#561F这，这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1250')

    def _loc_11A5(): pass

    label('loc_11A5')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11DB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470304V#043F这下糟糕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1250')

    def _loc_11DB(): pass

    label('loc_11DB')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1219',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470305V#055F喂喂……没有这样的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1250')

    def _loc_1219(): pass

    label('loc_1219')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1250',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470306V#074F呼、真是败给您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1250(): pass

    label('loc_1250')

    ChrTalk(
        0x00FE,
        (
            '#3570470307V抱歉……\n',
            '忽然想起来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470308V有个喜欢收集古书的人\n',
            '无论如何也想要那本书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470309V我想也已经没有用了，\n',
            '就很爽快地送给他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470310V咳，看来做人\n',
            '也不能太慷慨呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470311V#1007F啊，您还叹什么气啊～\n',
            '即使要叹，也是我们叹气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470312V真是的，不知道是哪个家伙\n',
            '给我们添的麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470313V#027F已经发生的事\n',
            '多说也无济于事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470314V接下来该怎样做……\n',
            '才是我们现在应该考虑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1416')
    def lambda_1416():
        ChrTurnDirection(0x00F8, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1416)

    Sleep(150)

    ChrTurnDirection(0x00F9, 0x0103, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1493',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470315V#042F嗯，说得没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060470316V只要能够找到拿着食谱的人\n',
            '就行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C9')

    def _loc_1493(): pass

    label('loc_1493')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14F6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470317V#035F嗯，我也这么想的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470318V首先要断定是谁\n',
            '拿走了食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C9')

    def _loc_14F6(): pass

    label('loc_14F6')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1569',
    )

    ChrTalk(
        0x0108,
        (
            '#0080280451V#070F啊啊，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080470320V如果能够找到拿到食谱的人，\n',
            '一切都可以迎刃而解……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C9')

    def _loc_1569(): pass

    label('loc_1569')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15C9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470321V#050F是，同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470322V只要找到拿到食谱的家伙\n',
            '那就行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15C9(): pass

    label('loc_15C9')

    ChrTalk(
        0x0101,
        (
            '#0010470323V#1015F看来只好重整旗鼓、\n',
            '继续调查了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470324V婆婆说了，\n',
            '是个有古书收集爱好的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470325V#020F如果你感觉可能会是哪些人，\n',
            '就从这些人身上开始调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3570470326V真是抱歉呢。\n',
            '让你们这么期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_16B4')
    def lambda_16B4():
        ChrTurnDirection(0x00F8, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_16B4)

    Sleep(150)

    @scena.Lambda('lambda_16C7')
    def lambda_16C7():
        ChrTurnDirection(0x00F9, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_16C7)

    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470327V#1006F嗯，没有关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470328V总之还是得到了一些线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x00FE, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470329V#020F嗯，谢谢您提供的帮助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470330V那么，我们就继续\n',
            '进行调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)
    OP_28(0x0075, 0x01, 0x0200)
    EventEnd(0x00)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0002 offset: 0x1798
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_17E4',
    )

    OP_8E(0x00FE, 44800, 0, 2410, 1000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(1500)

    OP_8E(0x00FE, 45830, 0, 2410, 1000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(1500)

    Jump('ReInit')

    def _loc_17E4(): pass

    label('loc_17E4')

    Return()

# id: 0x0003 offset: 0x17E5
@scena.Code('func_03_17E5')
def func_03_17E5():
    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_197D',
    )

    EventBegin(0x01)
    OP_6D(13410, 0, 139810, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeOut(300, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择２名固定成员\n',
            '以外的同行者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x01,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0004,
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

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1905',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 8)
    SetChrPos(0x000A, -790, 200, 69820, 360)

    def _loc_1905(): pass

    label('loc_1905')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1928',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -1940, 0, 74490, 360)

    def _loc_1928(): pass

    label('loc_1928')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_194B',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -4290, 0, 73800, 360)

    def _loc_194B(): pass

    label('loc_194B')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1978',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0004)
    SetChrChipByIndex(0x000E, 10)
    SetChrPos(0x000E, 140, 200, 71510, 180)

    def _loc_1978(): pass

    label('loc_1978')

    Sleep(300)

    def _loc_197D(): pass

    label('loc_197D')

    FadeOut(0, 0, -1)
    EventBegin(0x00)
    SetChrPos(0x0101, 1200, 0, 116170, 0)
    SetChrPos(0x00F7, 370, 0, 115520, 0)
    SetChrPos(0x00F8, 1850, 0, 114800, 0)
    SetChrPos(0x00F9, 910, 0, 114140, 0)
    OP_6D(750, 0, 117600, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4A(0x0008, 255)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0350470981V#741F#2P好久没有像今天一样痛快地喝上一杯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470982V事情的原由先不提了，\n',
            '还是要对你们表示感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470983V#1016F#4P这、这、这样虽好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470984V#1015F对了，奥利维尔那家伙\n',
            '后来怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350470985V#740F#2P嗯，教区长对他进行\n',
            '了治疗。\n',
            '现在正在协会的２楼休息着呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470986V好象有点筋疲力尽的样子，不过\n',
            '据说身体已经没有大碍了。\n',
            '不要有什么顾虑，带走他就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x1BBA
@scena.Code('func_04_1BBA')
def func_04_1BBA():
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
        'loc_1BCD',
    )

    Call(0, 0x0027)

    def _loc_1BCD(): pass

    label('loc_1BCD')

    OP_4A(0x0008, 255)
    OP_6D(1310, 0, 112280, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['阿加特'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xF9, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFC, 0xFF)
    SetChrPos(0x0101, 540, 0, 116590, 0)
    SetChrPos(0x0103, 1740, 0, 116600, 0)
    SetChrPos(0x0108, -60, 0, 114490, 0)
    SetChrPos(0x0104, 3390, 0, 114890, 0)
    SetChrPos(0x0106, 2040, 0, 115240, 0)
    SetChrPos(0x0107, 1100, 0, 115100, 0)
    SetChrPos(0x0105, 110, 0, 115560, 0)

    @scena.Lambda('lambda_1CA3')
    def lambda_1CA3():
        OP_6D(80, -200, 117460, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CA3)

    @scena.Lambda('lambda_1CBB')
    def lambda_1CBB():
        OP_67(0, 6590, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1CBB)

    FadeIn(1500, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0350280712V#741F呵呵，没想到这个时候\n',
            '你们会来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280713V#740F记得\n',
            '本来是要去柏斯支部的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280714V#025F#6P嗯嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280715V#524F不失时机地\n',
            '被这事情耽搁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280716V#741F不过因此\n',
            '倒是帮了我们大忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280717V#740F话说回来……\n',
            '艾丝蒂尔去了训练场以后\n',
            '就没再见过了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280718V工作用的新衣服\n',
            '也很合身嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280719V#1025F#6P是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280720V#740F和金先生、科洛蒂娅殿下、\n',
            '还有小提妲初次见面吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280721V我是负责洛连特支部\n',
            '接待的爱娜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280722V请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060280723V#048F#6P是，请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070280724V#560F#6P那个那个……\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280725V#071F哈哈，你的事迹\n',
            '听过不少哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280726V#743F哎呀……是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0104, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0350280727V#740F对了奥利维尔先生。\n',
            '你在那儿干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    OP_91(0x0104, -300, 0, 0, 1000, 0x00)

    ChrTalk(
        0x0104,
        (
            '#0040280728V#031F#6P哈哈哈……\n',
            '别，别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280729V一定是回想\n',
            '起了那晚的事了。\n',
            '是这样没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280730V#743F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280731V#021F#6P呵呵……\n',
            '别提了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280732V#020F说起来阿加特\n',
            '认识爱娜的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 400)

    ChrTalk(
        0x0106,
        (
            '#0050280733V#051F算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280734V只不过很少来洛连特，\n',
            '才见过几面而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280735V#741F呵呵，这次就麻烦你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280736V#742F寒暄就到此为止。\n',
            '赶快听我说明状况吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280737V#022F#6P嗯嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280738V#742F……起雾是在\n',
            '今天清晨左右。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280739V一开始只是\n',
            '薄薄的雾霭……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280740V但是慢慢就浓了起来，\n',
            '开始遮挡住视线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060280741V#043F#6P起雾的原因\n',
            '现在还不清楚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280742V#742F嗯嗯，现在是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280743V可以确定已经覆盖了\n',
            '洛连特市内整片区域……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280744V#074F雾也分很多种类的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280745V有的在海上产生，\n',
            '并慢慢飘到岸上，\n',
            '也有在盆地直接产生的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040280746V#030F#6P唔……从王国地图上看，\n',
            '洛连特好像在盆地里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280747V#740F嗯嗯，算是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280748V所以也很有可能\n',
            '只是单纯的自然现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280749V#026F#6P无论如何……\n',
            '最好还是警戒一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280750V#020F柏斯行中断，\n',
            '暂时留在在洛连特地区\n',
            '看看情况比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280751V#051F看来是这样比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280752V况且在雾散之前，\n',
            '定期船也无法启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280753V#1003F#6P啊……那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050280754V#052F什么，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010280755V#1025F#5P嗯，想问问\n',
            '那个空贼事件怎样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280756V#050F那个事件\n',
            '是因为暂时没有别的事情\n',
            '才打算调查看看的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280757V但调查现在也由王国军在做了，\n',
            '所以我们也没必要勉强帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280758V#1026F#5P但，但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280759V#555F怎么……\n',
            '什么地方值得注意吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280760V#1003F#5P啊，不是……\n',
            '倒不是这个意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280761V但是……我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(50)

    ChrTurnDirection(0x0105, 0x0101, 400)
    Sleep(50)

    ChrTurnDirection(0x0104, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030280762V#026F……艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280763V#020F虽然不知道\n',
            '你在想什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280764V但稍微冷静点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211050V#1004F#5P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280766V#020F空贼艇抢夺事件，\n',
            '在某种程度上是已经结束了的事件哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280767V若是有人质被抓走也就罢了，\n',
            '但还没有到需要协会出动那地步。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280768V再说空贼在柏斯周边地区\n',
            '停留的可能性也很小了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280769V#1026F#5P这、这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280770V#026F另一方面这边的异常现象\n',
            '引起的事件现在还层出不穷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280771V而且很可能会是\n',
            '『结社』干的好事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280772V#022F那么……\n',
            '如何取舍才是对的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280773V#1003F#5P………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060280774V#043F#6P……艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070280775V#065F#6P那，那个，雪拉姐！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280776V我想姐姐大概\n',
            '也有自己的原因！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280777V所以，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280778V#1003F#5P……不，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280779V#1007F雪拉姐说得对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070280780V#063F#6P姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280781V#1025F#5P对不起，雪拉姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280782V看来我还\n',
            '没搞清楚状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280783V#524F不用道歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280784V搞不清楚状况\n',
            '的时候谁都会有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280785V#021F连我也会这样的，\n',
            '特别是那边的阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0103, 400)

    ChrTalk(
        0x0106,
        (
            '#0050280786V#055F你说啥？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280787V#026F但是，不迷失自我、\n',
            '不断摸索最好的道路，\n',
            '对游击士来说也是必要的思想准备哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280788V#525F说起来容易，\n',
            '做起来难倒是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280789V#070F关于这方面，\n',
            '我也还在学着呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280790V比起大人我们还差得远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010280791V#1004F#2P是，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280792V#074F在任何逆境中都不会迷失自我……\n',
            '那诙谐幽默而坚强的心灵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280793V#070F以前、大人来卡尔瓦德时，\n',
            '好几次把我从危机中救出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280794V#1025F#2P是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050280795V#051F不过，那大叔的境界\n',
            '可没那么简单就能达到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280796V我们就以自己的步调\n',
            '一步步前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010280797V#1006F#5P嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280798V#1007F#6P爱娜姐，对不起。\n',
            '跑题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E4D')
    def lambda_2E4D():
        OP_8C(0x0103, 0, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2E4D)

    Sleep(50)

    @scena.Lambda('lambda_2E60')
    def lambda_2E60():
        OP_8C(0x0108, 0, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2E60)

    Sleep(50)

    @scena.Lambda('lambda_2E73')
    def lambda_2E73():
        OP_8C(0x0104, 0, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_2E73)

    Sleep(50)

    @scena.Lambda('lambda_2E86')
    def lambda_2E86():
        OP_8C(0x0106, 0, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2E86)

    Sleep(50)

    @scena.Lambda('lambda_2E99')
    def lambda_2E99():
        OP_8C(0x0107, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2E99)

    Sleep(50)

    @scena.Lambda('lambda_2EAC')
    def lambda_2EAC():
        OP_8C(0x0105, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2EAC)

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0350280799V#741F呵呵，没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280800V#740F那么我就\n',
            '继续往下说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280801V此时此刻没有什么\n',
            '特别的工作要委托你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280802V只是以防万一，\n',
            '在这里待命就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280803V回家里等也可以哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280804V#1011F#6P啊，嗯。\n',
            '我是打算回家一趟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280805V除此以外，\n',
            '还有没有需要注意的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280806V#744F嗯……是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280807V#742F一定要说的话，就希望你们\n',
            '调查一下各街道的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280808V#1004F#6P调查街道的情况？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280809V#742F刚才也说过了，\n',
            '雾覆盖了\n',
            '洛连特市整个地区……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280810V而且似乎在城外\n',
            '也扩展得相当快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280811V考虑到今后的事，\n',
            '还是视察清楚\n',
            '具体起雾的范围比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040280812V#030F#6P嗯，像这样\n',
            '定期船持续无法启动的话，\n',
            '就需要确保陆路的安全了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350280813V#740F嗯嗯，正是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280814V南边的艾利兹街道，\n',
            '西边的米尔西街道，北边的玛鲁加山道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280815V希望你们去确认这三条街道的状态，\n',
            '看看雾到底蔓延到哪里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280816V#1006F#6P明白。\n',
            '这点工作小事一桩啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030280817V#027F那么，既然如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280818V这次我和艾丝蒂尔\n',
            '来当向导比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010280819V#1006F#5P嗯，是啊。\n',
            '洛连特地区大致上我们都很熟悉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280820V#051F没办法了……\n',
            '赶快选择同行者吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, -1)
    OP_0D()
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    OP_6D(16980, 0, 120650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
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

    FadeIn(300, 0)
    OP_0D()
    OP_A2(0x180C)
    OP_A2(0x10F0)
    ClearMapFlags(0x02000000)
    NewScene('ED6_DT21/T0100._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x3446
@scena.Code('func_05_3446')
def func_05_3446():
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
        'loc_3466',
    )

    Call(0, 0x0027)
    FadeIn(0, 0)
    Call(0, 0x0028)

    def _loc_3466(): pass

    label('loc_3466')

    Call(0, 0x0025)
    OP_4A(0x0008, 255)
    OP_6D(210, -100, 117420, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(279, 0)
    SetChrPos(0x0101, 510, 0, 116600, 0)
    SetChrPos(0x0103, 1570, 0, 116600, 0)
    SetChrPos(0x0105, -230, 0, 115790, 0)
    SetChrPos(0x0106, 2320, 0, 115270, 0)
    SetChrPos(0x0108, 250, 0, 114280, 0)
    SetChrPos(0x0104, 1850, 0, 114310, 0)
    SetChrPos(0x0107, 1070, 0, 115580, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0350281309V#740F大家都辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281310V首先请让我\n',
            '支付报酬吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008F, 0x04, 0x10)
    OP_AF(0x03, 0x008F)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0350281311V#744F不过，本以为\n',
            '报告不会太清晰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281312V没想到雾扩散的界线，\n',
            '调查的这么清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281313V#022F#6P嗯嗯……\n',
            '说起来是有点不自然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281314V#1015F#6P实际在地图上\n',
            '雾是怎样蔓延的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350281315V#742F……稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_C5(0x00, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS135._CH')
    OP_C5(0x01, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS220._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(1500)

    SetChrName('爱娜')
    SetMessageWindowPos(250, 50, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0350281316V#744F艾利兹街道方向是６０塞尔矩，\n',
            '米尔西街道方向８０塞尔矩，\n',
            '玛鲁加山道方向１４０塞尔矩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281317V#740F……这样可以了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x03, -1, 500, 0)
    Sleep(1000)

    OP_61(0x0101)
    SetMessageWindowPos(50, 80, -1, -1)

    Talk(
        (
            '#0010281318V#1007F嗯、只是这样的话\n',
            '还是很不清楚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 180, -1, -1)
    OP_61(0x0105)

    Talk(
        (
            '#0060281319V#043F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060281320V雾的蔓延形式，似乎根据\n',
            '产生原因和风向流动而变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 1000, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)

    ChrTalk(
        0x0106,
        (
            '#0050281321V#555F说回来，这情况\n',
            '还真是不清不楚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050281322V还是只能在这里待命\n',
            '以备不时之需吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350281323V#745F嗯～只能这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281324V单凭现状，王国军\n',
            '好象也难以决定是否出动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281325V#1004F#6P啊，这么说来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010281326V#1018F#5P对了，提妲！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281327V『除雾装置』之类的新发明，\n',
            '博士不是做出来了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3A46')
    def lambda_3A46():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3A46')

    DispatchAsync2(0x0107, 0x0003, lambda_3A46)

    @scena.Lambda('lambda_3A57')
    def lambda_3A57():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3A57')

    DispatchAsync2(0x0103, 0x0003, lambda_3A57)

    @scena.Lambda('lambda_3A68')
    def lambda_3A68():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3A68')

    DispatchAsync2(0x0106, 0x0003, lambda_3A68)

    @scena.Lambda('lambda_3A79')
    def lambda_3A79():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3A79')

    DispatchAsync2(0x0104, 0x0003, lambda_3A79)

    @scena.Lambda('lambda_3A8A')
    def lambda_3A8A():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3A8A')

    DispatchAsync2(0x0105, 0x0003, lambda_3A8A)

    @scena.Lambda('lambda_3A9B')
    def lambda_3A9B():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3A9B')

    DispatchAsync2(0x0108, 0x0003, lambda_3A9B)

    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070281328V#064F#6P啊啊……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070281329V#063F嗯～唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070281330V之前爷爷是\n',
            '发明过『除湿机』\n',
            '之类的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281331V#1006F#5P『除湿器』──从名称来看，\n',
            '就是除去湿气的装置吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281332V那个能用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070281333V#561F#6P嗯～应该不行哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070281334V#063F要处理室外的空气\n',
            '会需要几百台才行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070281335V就算准备除湿机，\n',
            '也只能暂时起些作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281336V#1007F#5P唉……\n',
            '没那么简单啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080281337V#074F要是有和『结社』\n',
            '扯上关系的证据就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281338V但现在要硬说是他们干的\n',
            '又看起来不大像。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010281339V#1004F#5P这话怎么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080281340V#072F像之前的事件，\n',
            '他们使用『福音』后\n',
            '就发生了『不可能的现象』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281341V但是，这次的雾\n',
            '看起来并没有那么夸张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281342V#1002F#5P这倒是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040281343V#035F#6P呼，还有一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040281344V#030F他们每次都会以\n',
            '某种形式发送『暗示』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040281345V可是，这次看来还\n',
            '没收到类似的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010281346V#1004F#5P暗示？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040281347V#035F#6P亡灵骚乱、戴墨镜的男子、\n',
            '还有送到各处的恐吓信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040281348V#030F就是说让我们感到\n',
            '『可疑』的挑衅性标志。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281349V#1015F#5P原，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350281350V#742F唔……\n',
            '确实给一种疑惑的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281351V#522F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350281352V#743F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281353V怎么了，雪拉扎德？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281354V#026F#6P……刚刚说的暗示。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281355V#022F搞不好已经\n',
            '收到了也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350281356V#742F喔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010281357V#1020F#5P怎、怎么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000BB8)
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    SetChrPos(0x000F, 4170, 0, 108710, 0)

    NpcTalk(
        0x000F,
        '老人的声音',
        (
            '#0340281358V#2P#3S不、不好啦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_415E')
    def lambda_415E():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_415E')

    DispatchAsync2(0x0101, 0x0003, lambda_415E)

    @scena.Lambda('lambda_416F')
    def lambda_416F():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_416F')

    DispatchAsync2(0x0103, 0x0003, lambda_416F)

    @scena.Lambda('lambda_4180')
    def lambda_4180():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_4180')

    DispatchAsync2(0x0106, 0x0003, lambda_4180)

    @scena.Lambda('lambda_4191')
    def lambda_4191():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_4191')

    DispatchAsync2(0x0104, 0x0003, lambda_4191)

    @scena.Lambda('lambda_41A2')
    def lambda_41A2():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_41A2')

    DispatchAsync2(0x0105, 0x0003, lambda_41A2)

    @scena.Lambda('lambda_41B3')
    def lambda_41B3():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_41B3')

    DispatchAsync2(0x0107, 0x0003, lambda_41B3)

    @scena.Lambda('lambda_41C4')
    def lambda_41C4():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_41C4')

    DispatchAsync2(0x0108, 0x0003, lambda_41C4)

    @scena.Lambda('lambda_41D5')
    def lambda_41D5():
        OP_6D(2380, 0, 113020, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_41D5)

    Sleep(1000)

    CreateThread(0x000F, 0x00, 0x01, 0x0006)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_41FE')
    def lambda_41FE():
        OP_6D(-420, 200, 116820, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_41FE)

    @scena.Lambda('lambda_4216')
    def lambda_4216():
        OP_6B(2720, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4216)

    @scena.Lambda('lambda_4226')
    def lambda_4226():
        OP_8F(0x00FE, -960, 0, 115060, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0000, lambda_4226)

    Sleep(100)

    @scena.Lambda('lambda_4246')
    def lambda_4246():
        OP_8F(0x00FE, 2060, 0, 114310, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0000, lambda_4246)

    WaitForThreadExit(0x000F, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0103, 0x03)
    TerminateThread(0x0106, 0x03)
    TerminateThread(0x0104, 0x03)
    TerminateThread(0x0105, 0x03)
    TerminateThread(0x0107, 0x03)
    TerminateThread(0x0108, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010281359V#1026F#2P市、市长爷爷！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4349',
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
            TXT(0x00, '【◇不与克劳斯市长重逢】\n'),
            TXT(0x01, '【◇与克劳斯市长重逢】\n'),
            TXT(0x02, '【◇不变更】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_433D'),
        (0x00000001, 'loc_4343'),
        (-1, 'loc_4349'),
    )

    def _loc_433D(): pass

    label('loc_433D')

    OP_A3(0x1881)

    Jump('loc_4349')

    def _loc_4343(): pass

    label('loc_4343')

    OP_A2(0x1881)

    Jump('loc_4349')

    def _loc_4349(): pass

    label('loc_4349')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 1, 0x1881)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4447',
    )

    ChrTalk(
        0x000F,
        (
            '#0340281360V#603F呼呼、啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281361V#604F哦、哦哦、艾丝蒂尔……\n',
            '真是好久不见了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281362V#1025F#2P啊、嗯。\n',
            '好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281363V不过，您怎么了？\n',
            '这么惊慌……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281364V#1015F……唔，好象和上次\n',
            '事件时候一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4509')

    def _loc_4447(): pass

    label('loc_4447')

    ChrTalk(
        0x000F,
        (
            '#0340281365V#603F呼呼、啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281366V#604F太、太好了……\n',
            '正好大家都在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281367V#1025F#2P您怎、怎么了？\n',
            '这么惊慌……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281364V#1015F……唔，好象和上次\n',
            '事件时候一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4509(): pass

    label('loc_4509')

    ChrTalk(
        0x0103,
        (
            '#0030281369V#022F#2P市长先生。\n',
            '请先冷静下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281370V发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0340281371V#604F发、发生什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281372V#602F唔，你们都\n',
            '没事吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281373V#023F#2P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350281374V#743F请问，是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_1D(0x51)
    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#0340281375V#602F……刚才，我家的玲达\n',
            '突然昏倒了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281376V而且，好像还有其它市民\n',
            '也和她一样昏倒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270984V#1020F#2P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350281378V#742F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0026)
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0101._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x46CC
@scena.Code('func_06_46CC')
def func_06_46CC():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_46E7')
    def lambda_46E7():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_46E7)

    OP_8E(0x00FE, 3940, 0, 110620, 3000, 0x00)
    OP_8E(0x00FE, 850, 0, 113120, 3000, 0x00)
    OP_8E(0x00FE, 670, 0, 114040, 3000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0007 offset: 0x4737
@scena.Code('func_07_4737')
def func_07_4737():
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
        'loc_474E',
    )

    Call(0, 0x0027)
    Call(1, 0x0013)

    def _loc_474E(): pass

    label('loc_474E')

    OP_4A(0x0008, 255)
    SetChrFlags(0x0011, 0x0080)
    OP_6D(340, 0, 118500, 0)
    OP_67(0, 8029, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(315000, 0)
    OP_6E(292, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0350350381V#743F#2P哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrPos(0x0101, 3810, 0, 110590, 315)
    SetChrPos(0x0102, 3810, 0, 110590, 315)
    SetChrPos(0x00F8, 3810, 0, 110590, 315)
    SetChrPos(0x00F9, 3810, 0, 110590, 315)

    @scena.Lambda('lambda_4830')
    def lambda_4830():
        OP_6D(90, 0, 117790, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4830)

    @scena.Lambda('lambda_4848')
    def lambda_4848():
        OP_67(0, 6910, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4848)

    @scena.Lambda('lambda_4860')
    def lambda_4860():
        OP_6B(2600, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_4860)

    @scena.Lambda('lambda_4870')
    def lambda_4870():
        OP_6E(294, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_4870)

    CreateThread(0x0101, 0x01, 0x01, 0x0008)
    Sleep(400)

    CreateThread(0x0102, 0x01, 0x01, 0x0009)
    Sleep(600)

    CreateThread(0x00F8, 0x01, 0x01, 0x000A)
    Sleep(400)

    CreateThread(0x00F9, 0x01, 0x01, 0x000B)
    WaitForThreadExit(0x00F9, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B10',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350382V#021F#6P嗨，爱娜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350383V#1006F#6P我们来了呀，爱娜姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350384V#1035F#6P……好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350385V#743F#2P雪拉扎德……\n',
            '啊，还有艾丝蒂尔，约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350386V#741F真好……看来是平安无事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350387V你们去『塔』的时候\n',
            '发生了突变，我很担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030350388V#025F#6P的确是十分危险的地方，\n',
            '不过总算是安然无恙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350389V#524F你这边\n',
            '才真得很严重吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350390V#745F#2P是的……\n',
            '确实是发生了些骚乱，不过\n',
            '还好没有导致什么严重的后果。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350391V#740F克劳斯市长和迪拜恩教区长\n',
            '控制了混乱的局面，功劳不小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350392V#1025F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D04')

    def _loc_4B10(): pass

    label('loc_4B10')

    ChrTalk(
        0x0101,
        (
            '#0010350393V#1006F#6P让你担心了，爱娜姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350384V#1035F#6P……好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350395V#741F#2P太好了……你们平安无事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350396V#740F你们去『塔』的时候\n',
            '发生了异变，我很担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350397V#1016F嗯，确实十分危险。\n',
            '不过总算是安然无恙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350398V#1025F你这边\n',
            '才真的很严重吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350390V#745F#2P是的……\n',
            '确实是发生了些骚乱，不过\n',
            '还好没有导致什么严重的后果。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350391V#740F克劳斯市长和迪拜恩教区长\n',
            '控制了混乱的局面，功劳不小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350401V#1025F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D04(): pass

    label('loc_4D04')

    ChrTalk(
        0x0008,
        (
            '#0350350402V#740F#2P不管怎样，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350403V#741F你平安回来就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350404V#1035F#6P是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350405V#1043F让大家替我担心。\n',
            '对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350406V#744F#2P哈哈，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350407V#740F对于我们协会的接待员来说，\n',
            '某种意义上，游击士就像孩子一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350408V更不用说你们的游击士手册\n',
            '可是我亲手交给你们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350409V#741F能够平安回来，真是太好啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350410V#1040F#6P爱娜小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F18',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350411V#027F#6P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010350412V#1008F#4P哈哈哈……\n',
            '真好啊，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F55')

    def _loc_4F18(): pass

    label('loc_4F18')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010350412V#1008F#4P哈哈哈……\n',
            '真好啊，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F55(): pass

    label('loc_4F55')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010350414V#1004F#6P对了，爱娜姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350415V#1002F其实有很多很多的话\n',
            '想和你说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350416V#744F#2P嗯……关于那浮游岛吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350417V#742F如果知道什么详情\n',
            '能告诉我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350418V#1042F#6P是，情况是这样的──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人向爱娜说明了\n',
            '『浮游都市』出现了的缘由以及\n',
            '关于『零力场发生器』的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0350350419V#744F#2P是吗……那就是『辉之环』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350420V与想象中的情形\n',
            '有相当大的差异……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350421V#742F但是不管怎么说，目前我们\n',
            '还是没有能力和对方抗衡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5200',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350422V#025F#6P嗯……虽然这件事令人十分懊丧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350423V#022F但看来首先必须先重新调整我们的状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5309')

    def _loc_5200(): pass

    label('loc_5200')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5281',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350424V#053F#6P啊啊……\n',
            '真是让人生气的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350425V#555F但首先还是必须先重新调整好我们的状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5309')

    def _loc_5281(): pass

    label('loc_5281')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5309',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350426V#074F#6P啊啊……\n',
            '虽然很着急，但是是没有办法的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350427V#070F自然是只有先调整好我们的状态才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5309(): pass

    label('loc_5309')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_53B1',
    )

    ChrTalk(
        0x0008,
        (
            '#0350350428V#744F嗯，也就是说，如果可以能使用通讯器\n',
            '那肯定对我们有所帮助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350429V#740F那就赶快将『零力场发生器』\n',
            '设置好，如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5421')

    def _loc_53B1(): pass

    label('loc_53B1')

    ChrTalk(
        0x0008,
        (
            '#0350350430V#744F嗯，也就是说，如果可以使用通讯器，\n',
            '那就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350431V#740F尽快将此装置\n',
            '设置好如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5421(): pass

    label('loc_5421')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5544',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350432V#560F#6P是！\n',
            '请稍等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(1, 0x0014)
    SetChrPos(0x0107, -560, 0, 119000, 0)
    ChrTurnDirection(0x0008, 0x0107, 0)
    OP_6D(-810, 0, 119530, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(314000, 0)
    OP_6E(309, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070350433V#061F#5P……嗯，ＯＫ了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲打开了通讯器的开关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_565F')

    def _loc_5544(): pass

    label('loc_5544')

    ChrTalk(
        0x0102,
        (
            '#0020350434V#1040F#6P啊啊，那么开始……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(1, 0x0014)
    SetChrPos(0x0102, -560, 0, 119000, 0)
    ChrTurnDirection(0x0008, 0x0102, 0)
    OP_6D(-810, 0, 119530, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(314000, 0)
    OP_6E(309, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020350435V#1035F#5P……这下应该好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚打开了通讯器的开关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_565F(): pass

    label('loc_565F')

    Sleep(500)

    OP_22(0x009D, 0x00, 0x64)
    Sleep(1000)

    OP_22(0x0083, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0350350436V#743F启动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x01, 0x00)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5780',
    )

    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070350437V#560F#5P这下，通讯器\n',
            '应该能够使用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350438V不过，如果对方的通讯器没修好\n',
            '还是不能发送的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5800')

    def _loc_5780(): pass

    label('loc_5780')

    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020350439V#1040F#5P这下，通讯器\n',
            '能够使用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350440V但这必须是在对方的通讯器\n',
            '也已经修好，可以使用的前提下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5800(): pass

    label('loc_5800')

    ChrTalk(
        0x0008,
        (
            '#0350350441V#744F这下可真帮了大忙了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    @scena.Lambda('lambda_5838')
    def lambda_5838():
        OP_6D(-150, 0, 118340, 1100)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5838)

    OP_8C(0x0008, 180, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0350350442V#740F#2P感谢大家。\n',
            '这份人情一定会还的。',
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
        'loc_58A7',
    )

    OP_8C(0x0107, 135, 400)

    Jump('loc_58AE')

    def _loc_58A7(): pass

    label('loc_58A7')

    OP_8C(0x0102, 135, 400)

    def _loc_58AE(): pass

    label('loc_58AE')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5958',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350443V#021F#6P嗯，那就下次\n',
            '请大家吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350444V#741F#2P嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350445V#1052F这两个人还是老样子，一点都没有改变……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_59D5')

    def _loc_5958(): pass

    label('loc_5958')

    ChrTalk(
        0x0101,
        (
            '#0010350446V#1016F#6P好了，爱娜姐\n',
            '就别再说那些见外的话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350447V#1040F这也是和我们的工作\n',
            '息息相关的事情哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_59D5(): pass

    label('loc_59D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A73',
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
            TXT(0x00, '【◇恢复全部的通讯器】\n'),
            TXT(0x01, '【◇只恢复这里的通讯器】\n'),
            TXT(0x02, '【◇不变更】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5A61'),
        (0x00000001, 'loc_5A6A'),
        (-1, 'loc_5A73'),
    )

    def _loc_5A61(): pass

    label('loc_5A61')

    OP_A2(0x2001)
    OP_A2(0x2005)

    Jump('loc_5A73')

    def _loc_5A6A(): pass

    label('loc_5A6A')

    OP_A3(0x2001)
    OP_A3(0x2005)

    Jump('loc_5A73')

    def _loc_5A73(): pass

    label('loc_5A73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5DBF',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5B0A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350448V#070F好了，这下子\n',
            '地方支部所有的通讯器都修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350449V那么，配合各地的状况\n',
            '进行执行任务的报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C25')

    def _loc_5B0A(): pass

    label('loc_5B0A')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5B9A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350450V#020F好了，这下子\n',
            '地方支部所有的通讯器都修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350451V那么，结合各地的状况\n',
            '一起进行一下任务的报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C25')

    def _loc_5B9A(): pass

    label('loc_5B9A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5C25',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350452V#051F好了，这下子\n',
            '地方支部所有的通讯器都修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350453V那么，结合各地的状况，\n',
            '开始进行任务的汇报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C25(): pass

    label('loc_5C25')

    OP_59()
    OP_28(0x009B, 0x04, 0x10)
    OP_AF(0x67, 0x009B)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_28(0x009B, 0x01, 0x0100)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5CA3',
    )

    ChrTalk(
        0x0008,
        (
            '#0350350454V#741F#2P真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350455V这下子，就可以\n',
            '迅速应对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CFB')

    def _loc_5CA3(): pass

    label('loc_5CA3')

    ChrTalk(
        0x0008,
        (
            '#0350350456V#741F#2P大伙们，\n',
            '真的辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350457V这下子，就可以\n',
            '迅速应对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5CFB(): pass

    label('loc_5CFB')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D3D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350458V#070F还有其它什么事要帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DBC')

    def _loc_5D3D(): pass

    label('loc_5D3D')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D83',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350459V#020F是否还有其它什么事要帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DBC')

    def _loc_5D83(): pass

    label('loc_5D83')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5DBC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350460V#051F还有什么要帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5DBC(): pass

    label('loc_5DBC')

    Jump('loc_5F79')

    def _loc_5DBF(): pass

    label('loc_5DBF')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5E52',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350461V#070F#6P嗯，准备照这个样子，\n',
            '把其他几个协会的通讯器也\n',
            '给修理好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350462V不过，这里还有其他事情要帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F79')

    def _loc_5E52(): pass

    label('loc_5E52')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5EE9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350463V#051F#6P嗯，准备照这个样子，\n',
            '把其他几个协会的通讯器也\n',
            '给修理好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350464V不过，这里没有其他要帮忙的事情了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F79')

    def _loc_5EE9(): pass

    label('loc_5EE9')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F79',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350465V#020F#6P嗯，准备照这个样子，\n',
            '把其他几个协会的通讯器也\n',
            '给修理好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350466V不过，这里还有什么需要帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F79(): pass

    label('loc_5F79')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6069',
    )

    ChrTalk(
        0x0008,
        (
            '#0350350467V#744F#2P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350468V#740F可以的话，就去\n',
            '查看一下留言板上的工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350469V另外，希望你们去确认\n',
            '一下洛连特的近郊是否\n',
            '有什么情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350470V特别是利吉去的\n',
            '玛鲁加矿山，我总是放心不下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6148')

    def _loc_6069(): pass

    label('loc_6069')

    ChrTalk(
        0x0008,
        (
            '#0350350471V#744F#2P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350472V#740F可以的话，就去\n',
            '查看一下留言板上的工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350473V另外，希望你们去确认\n',
            '一下洛连特的近郊是否\n',
            '有什么情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350474V特别是利吉去的\n',
            '玛鲁加矿山，我总是放心不下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6148(): pass

    label('loc_6148')

    ChrTalk(
        0x0101,
        (
            '#0010350475V#1004F#6P啊？矿山出了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350476V#740F#2P不，只是警备的工作而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350477V还记得吧？在以前的塌方事故时，\n',
            '部分坑道与魔兽的巢穴是相连的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350478V就在数日前，当正要进行\n',
            '正式的封锁工程的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350479V#1043F#5P就是在那时候\n',
            '发生的那起非常事件吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350480V……确实很令人在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350481V#740F#2P嗯，如果有时间的话\n',
            '无论如何一定去观察一下情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350482V#1006F#6P嗯，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350483V缇欧的家啦、矿山啦，\n',
            '觉得有人去的地方都会试着去看一下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020350484V#1040F#5P是啊……\n',
            '总之，小心行事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350485V#741F#2P那就拜托啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※因为通讯器已经修好了，可以呼叫在其他支部待命的同伴，\n',
            '  将他们召集来洛连特支部。\n',
            '　想呼叫的时候请在接待处选择『呼叫同伴』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    OP_4B(0x0008, 255)
    OP_A2(0x2003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_645E',
    )

    OP_A2(0x2091)

    Jump('loc_6461')

    def _loc_645E(): pass

    label('loc_645E')

    OP_A3(0x2091)

    def _loc_6461(): pass

    label('loc_6461')

    OP_28(0x009B, 0x02, 0x0040)
    OP_28(0x009B, 0x01, 0x0080)
    OP_6D(520, 0, 114520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 520, 0, 114520, 135)
    SetChrPos(0x0001, 520, 0, 114520, 135)
    SetChrPos(0x0002, 520, 0, 114520, 135)
    SetChrPos(0x0003, 520, 0, 114520, 135)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x64FF
@scena.Code('func_08_64FF')
def func_08_64FF():
    OP_8E(0x00FE, 2370, 0, 112600, 2500, 0x00)
    OP_8E(0x00FE, 1500, 0, 116440, 2500, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0009 offset: 0x652F
@scena.Code('func_09_652F')
def func_09_652F():
    OP_8E(0x00FE, 1280, 0, 112650, 2500, 0x00)
    OP_8E(0x00FE, 400, 0, 116440, 2500, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000A offset: 0x655F
@scena.Code('func_0A_655F')
def func_0A_655F():
    OP_8E(0x00FE, 2370, 0, 112600, 2500, 0x00)
    OP_8E(0x00FE, 1500, 0, 115300, 2500, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000B offset: 0x658F
@scena.Code('func_0B_658F')
def func_0B_658F():
    OP_8E(0x00FE, 1280, 0, 112650, 2500, 0x00)
    OP_8E(0x00FE, 400, 0, 115300, 2500, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000C offset: 0x65BF
@scena.Code('func_0C_65BF')
def func_0C_65BF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 2, 0x2002)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 4, 0x2004)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 6, 0x2006)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_65D9',
    )

    Return()

    def _loc_65D9(): pass

    label('loc_65D9')

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
        'loc_65F9',
    )

    Call(0, 0x0027)
    Call(1, 0x0013)
    FadeIn(0, 0)

    def _loc_65F9(): pass

    label('loc_65F9')

    OP_22(0x00C3, 0x01, 0x64)
    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_4A(0x0008, 255)

    ChrTalk(
        0x0101,
        (
            '#0010260612V#1004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6683')
    def lambda_6683():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6683)

    @scena.Lambda('lambda_6691')
    def lambda_6691():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_6691)

    Sleep(100)

    @scena.Lambda('lambda_66A4')
    def lambda_66A4():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_66A4)

    OP_8C(0x0003, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0350350487V#743F#6P啊，刚修好\n',
            '就有联络来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(-1130, 0, 119950, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(268, 0)
    SetChrPos(0x0101, 3810, 0, 110590, 0)
    SetChrPos(0x0102, 3810, 0, 110590, 0)
    SetChrPos(0x00F8, 3810, 0, 110590, 0)
    SetChrPos(0x00F9, 3810, 0, 110590, 0)
    OP_8C(0x0008, 315, 0)
    OP_8E(0x0008, -560, 0, 119000, 2000, 0x00)
    OP_8C(0x0008, 0, 400)
    Sleep(700)

    OP_23(0x00C3)
    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x00, 0x00)
    PlayEffect(0x01, 0x01, 0x00FF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0101, 0x0001)
    CreateThread(0x0101, 0x00, 0x01, 0x000D)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0350350488V#742F#6P这里是游击士协会，\n',
            '这里是洛连特支部……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350489V#743F……啊啊！\n',
            '那边也是修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350490V#741F嗯，这边也是\n',
            '刚刚才弄好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350491V#740F……她们吗？\n',
            '嗯，现在就在这里呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_68C9')
    def lambda_68C9():
        OP_6D(-730, 0, 118880, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_68C9)

    @scena.Lambda('lambda_68E1')
    def lambda_68E1():
        OP_67(0, 5820, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_68E1)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010350492V#1004F#6P（找我们的……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350493V#1044F#6P（好像有话要说。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350494V#744F#6P……是……是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350495V………………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350496V#740F……知道了。\n',
            '我会向转达给他们本人的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350497V关于这边的状况\n',
            '过一会儿再和你联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350498V#741F……是呀。\n',
            '大家一起加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x01, 0x00)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6A93',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350499V#023F#6P爱娜。\n',
            '是哪里来的联络？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6AC7')

    def _loc_6A93(): pass

    label('loc_6A93')

    ChrTalk(
        0x0101,
        (
            '#0010350500V#1015F#6P爱娜姐。\n',
            '是哪里来的联络？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6AC7(): pass

    label('loc_6AC7')

    OP_8E(0x0008, 750, 0, 118600, 2000, 0x00)
    OP_8C(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0350350501V#740F#2P是王都支部的艾南先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350502V艾莉茜雅女王陛下\n',
            '好象有话要对你们说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350503V如果去格兰赛尔附近的话，\n',
            '希望能顺便去王城一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350504V#1004F#6P女王陛下！？',
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
        'loc_6BF9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350505V#052F#6P真是让人吃惊啊……\n',
            '到底有什么事呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C98')

    def _loc_6BF9(): pass

    label('loc_6BF9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6C4B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350506V#073F#6P那真是让人吃惊啊。\n',
            '究竟有什么事情呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C98')

    def _loc_6C4B(): pass

    label('loc_6C4B')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6C98',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350507V#023F#6P这真让人惊讶……\n',
            '究竟有什么事情呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C98(): pass

    label('loc_6C98')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_6D18',
    )

    ChrTalk(
        0x0008,
        (
            '#0350350508V#744F#2P这就没有详细问了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350509V#742F好像是不大适合在\n',
            '通讯器中传达的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D8A')

    def _loc_6D18(): pass

    label('loc_6D18')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6D8A',
    )

    ChrTalk(
        0x0008,
        (
            '#0350350510V#744F#2P具体就没有细问了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350511V#742F好像是不大适合在\n',
            '通讯器中传达的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D8A(): pass

    label('loc_6D8A')

    ChrTalk(
        0x0101,
        (
            '#0010350512V#1015F#6P不能在通讯中传达……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350513V#1026F是吗，导力通讯\n',
            '存在被人监听的危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350514V#1042F#6P看来是\n',
            '比较机密的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350350515V#740F#2P不过，也没有让\n',
            '你们马上就去的意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350516V要是以后路过王都附近的话，\n',
            '就顺便去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350517V#1006F#6P这样的啊……知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6F04',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350518V#021F#6P赶快过去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F2F')

    def _loc_6F04(): pass

    label('loc_6F04')

    ChrTalk(
        0x0102,
        (
            '#0020350519V#1040F#6P赶快过去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F2F(): pass

    label('loc_6F2F')

    OP_A2(0x2004)
    OP_28(0x009B, 0x01, 0x0100)
    OP_28(0x009B, 0x01, 0x0200)
    OP_28(0x009B, 0x01, 0x0400)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_4B(0x0008, 255)
    OP_6D(520, 0, 114520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 520, 0, 114520, 135)
    SetChrPos(0x0001, 520, 0, 114520, 135)
    SetChrPos(0x0002, 520, 0, 114520, 135)
    SetChrPos(0x0003, 520, 0, 114520, 135)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x6FEC
@scena.Code('func_0D_6FEC')
def func_0D_6FEC():
    CreateThread(0x0101, 0x01, 0x01, 0x0008)
    Sleep(400)

    CreateThread(0x0102, 0x01, 0x01, 0x0009)
    Sleep(600)

    CreateThread(0x00F8, 0x01, 0x01, 0x000A)
    Sleep(400)

    CreateThread(0x00F9, 0x01, 0x01, 0x000B)
    WaitForThreadExit(0x00F8, 0x0001)

    Return()

# id: 0x000E offset: 0x701D
@scena.Code('func_0E_701D')
def func_0E_701D():
    OP_8E(0x00FE, 740, 0, 112990, 2000, 0x00)
    OP_8E(0x00FE, 440, 0, 116590, 2000, 0x00)

    @scena.Lambda('lambda_704B')
    def lambda_704B():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_704B')

    DispatchAsync2(0x00FE, 0x0002, lambda_704B)

    Return()

# id: 0x000F offset: 0x7057
@scena.Code('func_0F_7057')
def func_0F_7057():
    OP_8E(0x00FE, 2050, 0, 112970, 2000, 0x00)
    OP_8E(0x00FE, 1170, 0, 116600, 2000, 0x00)

    @scena.Lambda('lambda_7085')
    def lambda_7085():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_7085')

    DispatchAsync2(0x00FE, 0x0002, lambda_7085)

    Return()

# id: 0x0010 offset: 0x7091
@scena.Code('func_10_7091')
def func_10_7091():
    OP_8E(0x00FE, 740, 0, 112990, 2000, 0x00)
    OP_8E(0x00FE, -220, 0, 116080, 2000, 0x00)

    @scena.Lambda('lambda_70BF')
    def lambda_70BF():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_70BF')

    DispatchAsync2(0x00FE, 0x0002, lambda_70BF)

    Return()

# id: 0x0011 offset: 0x70CB
@scena.Code('func_11_70CB')
def func_11_70CB():
    OP_8E(0x00FE, 2050, 0, 112970, 2000, 0x00)
    OP_8E(0x00FE, 1930, 0, 116400, 2000, 0x00)

    @scena.Lambda('lambda_70F9')
    def lambda_70F9():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_70F9')

    DispatchAsync2(0x00FE, 0x0002, lambda_70F9)

    Return()

# id: 0x0012 offset: 0x7105
@scena.Code('func_12_7105')
def func_12_7105():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    OP_6D(-1470, 0, 125030, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4A(0x0008, 255)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, 300, 0, 116600, 135)
    SetChrPos(0x0101, 1840, 0, 115000, 0)
    SetChrPos(0x0102, 710, 0, 115000, 0)
    SetChrPos(0x00F8, 1840, 0, 113800, 0)
    SetChrPos(0x00F9, 740, 0, 113800, 0)
    Sleep(1000)

    @scena.Lambda('lambda_71B7')
    def lambda_71B7():
        OP_6D(250, 0, 116610, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_71B7)

    @scena.Lambda('lambda_71CF')
    def lambda_71CF():
        OP_67(0, 6910, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_71CF)

    @scena.Lambda('lambda_71E7')
    def lambda_71E7():
        OP_6B(2600, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_71E7)

    @scena.Lambda('lambda_71F7')
    def lambda_71F7():
        OP_6E(294, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_71F7)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0102, 0x0003)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0350351067V#745F──原来如此，事情是那样吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351068V要是再迟一步的话，\n',
            '结果真是不堪设想啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351069V#1P啊啊，多亏这位小姐和她的朋友\n',
            '我们才能得救。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351070V#1P上次被你搭救的时候\n',
            '还觉得提心吊胆的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351071V#1P但今天感觉却完全不同，\n',
            '简直像换了个人一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0015, 400)

    ChrTalk(
        0x0101,
        (
            '#0010351072V#1008F#4P哎呀？真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351073V可、可是我倒没觉得\n',
            '自己有什么变化啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351074V#1P不用谦虚啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351075V#1P这可是我的\n',
            '真心感想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020351076V#1048F#1P谦虚吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020351077V#1035F如果是艾丝蒂尔的话，\n',
            '大概是真的没发觉吧。',
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
        'loc_748C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070351078V#560F嘿嘿嘿，也说不定哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_748C(): pass

    label('loc_748C')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_74C1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351079V#021F呵呵，有可能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_74C1(): pass

    label('loc_74C1')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7507',
    )

    ChrTalk(
        0x0106,
        (
            '#0050351080V#051F错不了，\n',
            '这家伙本来就是少根筋嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7507(): pass

    label('loc_7507')

    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    OP_8C(0x0101, 180, 400)
    Sleep(600)

    ChrTalk(
        0x0101,
        (
            '#0010351081V#1019F#4P呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351082V明明是在被赞扬，\n',
            '但为什么一点都高兴不起来呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350351083V#741F不管是谁，想要发觉\n',
            '自己的变化也是很难的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351084V因为毕竟是一点一点\n',
            '逐渐变化的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351085V#1P嗯，我是因为好久没有见到你们，\n',
            '所以感觉才会这样强烈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351086V#1P不管怎么说，你们真的已经是\n',
            '很出色的游击士了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_773E',
    )

    ChrTalk(
        0x0008,
        (
            '#0350351087V#740F艾丝蒂尔、约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351088V还有阿加特和\n',
            '雪拉扎德……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351089V做的真是很好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351090V我身为协会的一员，\n',
            '也替你们感到骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AC6')

    def _loc_773E(): pass

    label('loc_773E')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_77FD',
    )

    ChrTalk(
        0x0008,
        (
            '#0350351087V#740F艾丝蒂尔、约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351092V还有金先生和\n',
            '雪拉扎德……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351089V做的真是很好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351090V我身为协会的一员，\n',
            '也替你们感到骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AC6')

    def _loc_77FD(): pass

    label('loc_77FD')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_78BA',
    )

    ChrTalk(
        0x0008,
        (
            '#0350351087V#740F艾丝蒂尔、约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351096V还有雪拉扎德和\n',
            '提妲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351089V做的真是很好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351090V我身为协会的一员，\n',
            '也替你们感到骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AC6')

    def _loc_78BA(): pass

    label('loc_78BA')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7965',
    )

    ChrTalk(
        0x0008,
        (
            '#0350351099V#740F艾丝蒂尔和约修亚。\n',
            '还有金先生和阿加特…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351089V做的真是很好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351090V我身为协会的一员，\n',
            '也替你们感到骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AC6')

    def _loc_7965(): pass

    label('loc_7965')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7A20',
    )

    ChrTalk(
        0x0008,
        (
            '#0350351087V#740F艾丝蒂尔、约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351103V还有阿加特和\n',
            '提妲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351089V做的真是很好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351090V我身为协会的一员，\n',
            '也替你们感到骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AC6')

    def _loc_7A20(): pass

    label('loc_7A20')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7AC6',
    )

    ChrTalk(
        0x0008,
        (
            '#0350351106V#740F艾丝蒂尔和约修亚。\n',
            '还有金先生和提妲，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351089V做的真是很好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351090V我身为协会的一员，\n',
            '也替你们感到骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7AC6(): pass

    label('loc_7AC6')

    @scena.Lambda('lambda_7ACC')
    def lambda_7ACC():
        OP_8C(0x0102, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7ACC)

    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010351109V#1017F#4P嗯，哪里哪里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351110V#1041F#1P今后也\n',
            '请多关照。',
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
        'loc_7B5F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070260805V#067F嘿嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7B5F(): pass

    label('loc_7B5F')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7B9C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080351112V#070F好了，任务也算是完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7B9C(): pass

    label('loc_7B9C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7BD1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050351113V#051F嘿，这是当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7BD1(): pass

    label('loc_7BD1')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7D17',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351114V#021F这样的话～爱娜啊～\n',
            '这次不如请我们喝一杯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350351115V#741F哎呀，一杯就够了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030351116V#525F呵呵，这嘛…\n',
            '用超大号杯也就差不多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010351117V#1007F#4P又、又扯到喝酒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351118V#1048F#1P不管是什么话题，\n',
            '她们也都能转移到喝酒上去…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D17(): pass

    label('loc_7D17')

    ChrTalk(
        0x0015,
        (
            '#0940351119V#1P不好意思，我也没有什么\n',
            '礼物送大家表示感谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351120V#1P这就要回\n',
            '矿山去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351121V#1P虽然事故刚刚结束，\n',
            '但工作还是不能耽误了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#0010351122V#1004F#4P嗯，说的也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351123V#1P上层的坑道也有\n',
            '不少要做的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351124V#1P请大家替我向那位\n',
            '警备的兄弟问声好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x0008, 400)

    ChrTalk(
        0x0015,
        (
            '#0940351125V#1P他已经没事了吧？\n',
            '那时伤得好像很厉害…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350351126V#740F嗯，伤得确实不轻，\n',
            '不过对游击士来说也没什么大不了的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351127V现在已经恢复意识了，\n',
            '正在旅店里面休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351128V#1P是吗……\n',
            '那我也就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0015, 135, 400)

    ChrTalk(
        0x0015,
        (
            '#0940351129V#1P好了，那我这就告辞了。\n',
            '今天实在是谢谢大家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010351130V#1006F#4P您也要小心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351131V#1040F#1P工作请加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0940351132V#1P噢！再见啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_800F')
    def lambda_800F():
        OP_6D(-30, 0, 115770, 2500)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_800F)

    @scena.Lambda('lambda_8027')
    def lambda_8027():
        ChrTurnDirection(0x00FE, 0x0015, 400)
        Yield()

        Jump('lambda_8027')

    DispatchAsync2(0x0008, 0x0001, lambda_8027)

    @scena.Lambda('lambda_8038')
    def lambda_8038():
        ChrTurnDirection(0x00FE, 0x0015, 400)
        Yield()

        Jump('lambda_8038')

    DispatchAsync2(0x0101, 0x0001, lambda_8038)

    @scena.Lambda('lambda_8049')
    def lambda_8049():
        ChrTurnDirection(0x00FE, 0x0015, 400)
        Yield()

        Jump('lambda_8049')

    DispatchAsync2(0x0102, 0x0001, lambda_8049)

    @scena.Lambda('lambda_805A')
    def lambda_805A():
        ChrTurnDirection(0x00FE, 0x0015, 400)
        Yield()

        Jump('lambda_805A')

    DispatchAsync2(0x00F8, 0x0001, lambda_805A)

    @scena.Lambda('lambda_806B')
    def lambda_806B():
        ChrTurnDirection(0x00FE, 0x0015, 400)
        Yield()

        Jump('lambda_806B')

    DispatchAsync2(0x00F9, 0x0001, lambda_806B)

    SetChrFlags(0x0015, 0x0040)
    OP_8E(0x0015, -330, 0, 113500, 2000, 0x00)
    OP_8E(0x0015, 4170, 0, 110120, 2000, 0x00)
    OP_8C(0x0015, 180, 400)
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_80BA')
    def lambda_80BA():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0015, 0x0000, lambda_80BA)

    OP_8E(0x0015, 4210, 0, 108510, 2000, 0x00)
    WaitForThreadExit(0x0015, 0x0000)
    SetChrFlags(0x0015, 0x0080)
    OP_22(0x0007, 0x00, 0x64)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0008, 0x01)
    OP_8C(0x0008, 180, 400)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)

    @scena.Lambda('lambda_810E')
    def lambda_810E():
        OP_6D(90, 0, 117790, 1500)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_810E)

    Sleep(800)

    @scena.Lambda('lambda_812B')
    def lambda_812B():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_812B)

    Sleep(100)

    @scena.Lambda('lambda_813E')
    def lambda_813E():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_813E)

    Sleep(200)

    @scena.Lambda('lambda_8151')
    def lambda_8151():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_8151)

    @scena.Lambda('lambda_815F')
    def lambda_815F():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_815F)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_8172')
    def lambda_8172():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8172)

    Sleep(160)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_8192')
    def lambda_8192():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8192)

    Sleep(150)

    WaitForThreadExit(0x00F8, 0x0001)

    @scena.Lambda('lambda_81B2')
    def lambda_81B2():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_81B2)

    Sleep(140)

    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_81D2')
    def lambda_81D2():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_81D2)

    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0350351133V#740F好了，这下算是完成任务了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351134V利吉和你们今天\n',
            '都辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350525V以后也请保持这个状态\n',
            '继续活跃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351136V#1040F#1P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350351137V#740F这次的事件，\n',
            '我也已经评定完毕了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350351138V要想收取报酬的话，\n',
            '只要另外再向我报告就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010351139V#1001F#4P嗯!了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0017, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【营救矿工】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x0015, 0x0040)
    OP_4B(0x0008, 255)
    OP_A2(0x000B)
    OP_A2(0x2085)
    OP_28(0x00BF, 0x04, 0x10)
    OP_28(0x00BF, 0x01, 0x0200)
    OP_28(0x00BF, 0x01, 0x0400)
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x8395
@scena.Code('func_13_8395')
def func_13_8395():
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

# id: 0x0014 offset: 0x83EE
@scena.Code('func_14_83EE')
def func_14_83EE():
    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0151, 0x01)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_840F',
    )

    RemoveItem(ItemTable['零力场发生器'], 1)

    Jump('loc_8927')

    def _loc_840F(): pass

    label('loc_840F')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0xFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8927',
    )

    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择取下零力场发生器的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x0, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_8478',
    )

    Call(1, 0x0015)

    Jump('loc_847C')

    def _loc_8478(): pass

    label('loc_8478')

    Call(1, 0x0016)

    def _loc_847C(): pass

    label('loc_847C')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x1, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x1, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_84A3',
    )

    Call(1, 0x0015)

    Jump('loc_84A7')

    def _loc_84A3(): pass

    label('loc_84A3')

    Call(1, 0x0016)

    def _loc_84A7(): pass

    label('loc_84A7')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x2, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x2, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_84CE',
    )

    Call(1, 0x0015)

    Jump('loc_84D2')

    def _loc_84CE(): pass

    label('loc_84CE')

    Call(1, 0x0016)

    def _loc_84D2(): pass

    label('loc_84D2')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x3, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x3, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_84F9',
    )

    Call(1, 0x0015)

    Jump('loc_84FD')

    def _loc_84F9(): pass

    label('loc_84F9')

    Call(1, 0x0016)

    def _loc_84FD(): pass

    label('loc_84FD')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(72, 320, 56, 3)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_8544'),
        (0x00000001, 'loc_858A'),
        (0x00000002, 'loc_85D0'),
        (0x00000003, 'loc_8616'),
        (-1, 'loc_865C'),
    )

    def _loc_8544(): pass

    label('loc_8544')

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8567',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8587')

    def _loc_8567(): pass

    label('loc_8567')

    If(
        (
            (Expr.GetChrWork, 0x0, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8587',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8587(): pass

    label('loc_8587')

    Jump('loc_865C')

    def _loc_858A(): pass

    label('loc_858A')

    If(
        (
            (Expr.GetChrWork, 0x1, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_85AD',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_85CD')

    def _loc_85AD(): pass

    label('loc_85AD')

    If(
        (
            (Expr.GetChrWork, 0x1, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_85CD',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_85CD(): pass

    label('loc_85CD')

    Jump('loc_865C')

    def _loc_85D0(): pass

    label('loc_85D0')

    If(
        (
            (Expr.GetChrWork, 0x2, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_85F3',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8613')

    def _loc_85F3(): pass

    label('loc_85F3')

    If(
        (
            (Expr.GetChrWork, 0x2, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8613',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8613(): pass

    label('loc_8613')

    Jump('loc_865C')

    def _loc_8616(): pass

    label('loc_8616')

    If(
        (
            (Expr.GetChrWork, 0x3, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8639',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8659')

    def _loc_8639(): pass

    label('loc_8639')

    If(
        (
            (Expr.GetChrWork, 0x3, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8659',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushValueByIndex, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8659(): pass

    label('loc_8659')

    Jump('loc_865C')

    def _loc_865C(): pass

    label('loc_865C')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0xFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8685',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '未装备零力场发生器。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8918')

    def _loc_8685(): pass

    label('loc_8685')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_86CD',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8918')

    def _loc_86CD(): pass

    label('loc_86CD')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8713',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8918')

    def _loc_8713(): pass

    label('loc_8713')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_875B',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8918')

    def _loc_875B(): pass

    label('loc_875B')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_87A3',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '奥利维尔已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8918')

    def _loc_87A3(): pass

    label('loc_87A3')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_87E9',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '科洛丝已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8918')

    def _loc_87E9(): pass

    label('loc_87E9')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_882F',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '阿加特已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8918')

    def _loc_882F(): pass

    label('loc_882F')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8899',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲已取下零力场发生器，\n',
            '无法使用魔法，战技，普通攻击。\n',
            '但S战技『炮射冲击』仍可使用。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8918')

    def _loc_8899(): pass

    label('loc_8899')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88D9',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '金已取下零力场发生器\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8918')

    def _loc_88D9(): pass

    label('loc_88D9')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8918',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '凯文已取下零力场发生器\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    def _loc_8918(): pass

    label('loc_8918')

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_840F')

    def _loc_8927(): pass

    label('loc_8927')

    Return()

# id: 0x0015 offset: 0x8928
@scena.Code('func_15_8928')
def func_15_8928():
    Switch(
        (
            (Expr.PushReg, 0x4),
            Expr.Return,
        ),
        (0x00000000, 'loc_8955'),
        (0x00000001, 'loc_8970'),
        (0x00000002, 'loc_8989'),
        (0x00000003, 'loc_89A4'),
        (0x00000004, 'loc_89BF'),
        (0x00000005, 'loc_89D8'),
        (0x00000006, 'loc_89F1'),
        (0x00000007, 'loc_8A08'),
        (0x00000008, 'loc_8A1D'),
        (-1, 'loc_8A34'),
    )

    def _loc_8955(): pass

    label('loc_8955')

    OP_CC(0x01, 0x00, '【艾丝蒂尔　装备中】')

    Jump('loc_8A34')

    def _loc_8970(): pass

    label('loc_8970')

    OP_CC(0x01, 0x00, '【约修亚　装备中】')

    Jump('loc_8A34')

    def _loc_8989(): pass

    label('loc_8989')

    OP_CC(0x01, 0x00, '【雪拉扎德　装备中】')

    Jump('loc_8A34')

    def _loc_89A4(): pass

    label('loc_89A4')

    OP_CC(0x01, 0x00, '【奥利维尔　装备中】')

    Jump('loc_8A34')

    def _loc_89BF(): pass

    label('loc_89BF')

    OP_CC(0x01, 0x00, '【科洛丝　装备中】')

    Jump('loc_8A34')

    def _loc_89D8(): pass

    label('loc_89D8')

    OP_CC(0x01, 0x00, '【阿加特　装备中】')

    Jump('loc_8A34')

    def _loc_89F1(): pass

    label('loc_89F1')

    OP_CC(0x01, 0x00, '【提妲　装备中】')

    Jump('loc_8A34')

    def _loc_8A08(): pass

    label('loc_8A08')

    OP_CC(0x01, 0x00, '【金　装备中】')

    Jump('loc_8A34')

    def _loc_8A1D(): pass

    label('loc_8A1D')

    OP_CC(0x01, 0x00, '【凯文　装备中】')

    Jump('loc_8A34')

    def _loc_8A34(): pass

    label('loc_8A34')

    Return()

# id: 0x0016 offset: 0x8A35
@scena.Code('func_16_8A35')
def func_16_8A35():
    Switch(
        (
            (Expr.PushReg, 0x4),
            Expr.Return,
        ),
        (0x00000000, 'loc_8A62'),
        (0x00000001, 'loc_8A7D'),
        (0x00000002, 'loc_8A96'),
        (0x00000003, 'loc_8AB1'),
        (0x00000004, 'loc_8ACC'),
        (0x00000005, 'loc_8AE5'),
        (0x00000006, 'loc_8AFE'),
        (0x00000007, 'loc_8B15'),
        (0x00000008, 'loc_8B2A'),
        (-1, 'loc_8B41'),
    )

    def _loc_8A62(): pass

    label('loc_8A62')

    OP_CC(0x01, 0x00, '【艾丝蒂尔　未装备】')

    Jump('loc_8B41')

    def _loc_8A7D(): pass

    label('loc_8A7D')

    OP_CC(0x01, 0x00, '【约修亚　未装备】')

    Jump('loc_8B41')

    def _loc_8A96(): pass

    label('loc_8A96')

    OP_CC(0x01, 0x00, '【雪拉扎德　未装备】')

    Jump('loc_8B41')

    def _loc_8AB1(): pass

    label('loc_8AB1')

    OP_CC(0x01, 0x00, '【奥利维尔　未装备】')

    Jump('loc_8B41')

    def _loc_8ACC(): pass

    label('loc_8ACC')

    OP_CC(0x01, 0x00, '【科洛丝　未装备】')

    Jump('loc_8B41')

    def _loc_8AE5(): pass

    label('loc_8AE5')

    OP_CC(0x01, 0x00, '【阿加特　未装备】')

    Jump('loc_8B41')

    def _loc_8AFE(): pass

    label('loc_8AFE')

    OP_CC(0x01, 0x00, '【提妲　未装备】')

    Jump('loc_8B41')

    def _loc_8B15(): pass

    label('loc_8B15')

    OP_CC(0x01, 0x00, '【金　未装备】')

    Jump('loc_8B41')

    def _loc_8B2A(): pass

    label('loc_8B2A')

    OP_CC(0x01, 0x00, '【凯文　未装备】')

    Jump('loc_8B41')

    def _loc_8B41(): pass

    label('loc_8B41')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
